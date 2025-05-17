import base64
import hashlib
import hmac
import json
import requests
from uuid import uuid1, uuid4
from datetime import datetime

from django.shortcuts import redirect, render
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt

from accounts.models import CustomUser
from payments.models import PaymentHistory
from trips.models import Hotel
from trips.views import add_booking


def payment_page(request):
    return render(request, "pages/payments/payment.html")


def payment_success(request):
    return render(request, "pages/payments/success.html")


def payment_failure(request):
    return render(request, "pages/payments/failure.html")


def generate_signature(msg):
    message = msg.encode("utf-8")
    hmac_sha256 = hmac.new("8gBm/:&EnhH.1/q".encode("utf-8"), message, hashlib.sha256)
    digest = hmac_sha256.digest()
    signature = base64.b64encode(digest).decode("utf-8")

    return signature


@csrf_exempt
def pay_with_esewa(request):
    if request.method == "POST":
        cache_data = cache.get("booking")
        if cache_data == None:
            return render(request, "500.html")

        product = cache_data["data"]

        target_url = "https://rc-epay.esewa.com.np/api/epay/main/v2/form"

        if isinstance(product, Hotel):
            start_date = cache_data["start_date"]
            to_date = cache_data["to_date"]

            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(to_date, "%Y-%m-%d")
            total_days = (end - start).days
            total_amount = product.price * total_days
        else:
            total_amount = str(round(product.price))

        transaction_uuid = uuid4()
        product_code = "EPAYTEST"

        msg = f"total_amount={total_amount},transaction_uuid={transaction_uuid},product_code={product_code}"
        signature = generate_signature(msg)

        payload = {
            "amount": f"{total_amount}",
            "tax_amount": "0",
            "product_service_charge": "0",
            "product_delivery_charge": "0",
            "product_code": f"{product_code}",
            "total_amount": f"{total_amount}",
            "transaction_uuid": f"{transaction_uuid}",
            "success_url": "http://localhost:8000/verify-esewa",
            "failure_url": "http://localhost:8000/payment-failure",
            "signed_field_names": "total_amount,transaction_uuid,product_code",
            "signature": f"{signature}",
        }

        response = requests.post(target_url, data=payload)
        if response.status_code == 200:
            return redirect(response.url)

    return render(request, "500.html")


@csrf_exempt
def pay_with_khalti(request):
    if request.method == "POST":
        cache_data = cache.get("booking")
        if cache_data == None:
            return render(request, "500.html")

        product = cache_data["data"]

        if isinstance(product, Hotel):
            start_date = cache_data["start_date"]
            to_date = cache_data["to_date"]

            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(to_date, "%Y-%m-%d")
            total_days = (end - start).days
            total_amount = product.price * total_days
        else:
            total_amount = round(product.price)

        purchase_id = uuid4().__str__()
        customer_info = {
            "name": request.user.full_name(),
            "email": request.user.email,
            "phone": request.user.phone_number,
        }

        raw_payload = {
            "return_url": "http://localhost:8000/verify-khalti",
            "website_url": "http://localhost:8000",
            "amount": round(total_amount * 100),
            "purchase_order_id": purchase_id,
            "purchase_order_name": product.name,
            "customer_info": customer_info,
            "amount_breakdown": [
                {"label": "Mark Price", "amount": round(total_amount * 100)},
                {"label": "VAT", "amount": 0},
            ],
        }

        print(raw_payload)

        url = "https://dev.khalti.com/api/v2/epayment/initiate/"
        payload = json.dumps(raw_payload)

        headers = {
            "Authorization": "Key dcb5a1bfaa9248cca4068fb95ffa0438",
            "Content-Type": "application/json",
        }
        response = requests.post(url, headers=headers, data=payload)
        print(response.content)

        if response.status_code == 200:
            return redirect(response.json()["payment_url"])

    return render(request, "500.html")


@csrf_exempt
def verify_esewa(request):
    if request.method == "GET":
        encoded_data = request.GET.get("data", None)

        if encoded_data:
            decoded_data = base64.b64decode(encoded_data)
            decoded_data = json.loads(decoded_data)

            if decoded_data["status"] == "COMPLETE":
                transaction_id = decoded_data["transaction_uuid"]
                total_amount = decoded_data["total_amount"].replace(",", "")

                cache_data = cache.get("booking")
                user = CustomUser.objects.get(id=cache_data.get("user_id"))

                # Save the transaction to the database
                payment_history = PaymentHistory(
                    transaction_id=transaction_id,
                    user=user,
                    total_payment=total_amount,
                    payment_via=PaymentHistory.PaymentMethod.ESEWA,
                )
                payment_history.save()

                add_booking(user, payment_history)

                return redirect("payment_success")

    return redirect("payment_failure")


@csrf_exempt
def verify_khalti(request):
    if request.method == "GET":
        status = request.GET.get("status", "Failed")

        if status == "Completed":
            pidx = request.GET.get("pidx")
            transaction_id = request.GET.get("transaction_id")
            amount = request.GET.get("amount")
            total_amount = request.GET.get("total_amount")
            purchase_order_id = request.GET.get("purchase_order_id")
            purchase_order_name = request.GET.get("purchase_order_name")

            cache_data = cache.get("booking")
            user = CustomUser.objects.get(id=cache_data.get("user_id"))

            # Save the transaction to the database
            payment_history = PaymentHistory(
                transaction_id=transaction_id,
                user=user,
                total_payment=total_amount,
                payment_via=PaymentHistory.PaymentMethod.KHALTI,
            )
            payment_history.save()

            add_booking(user, payment_history)

            return redirect("payment_success")

    return redirect("payment_failure")
