import base64
from datetime import date
import datetime
import hashlib
import hmac
import json
from uuid import uuid4

from django.shortcuts import redirect, render
import requests


def payment_page(request):
    return render(request, "pages/payment/payment.html")


def generate_signature(msg):
    message = msg.encode("utf-8")
    hmac_sha256 = hmac.new("8gBm/:&EnhH.1/q".encode("utf-8"), message, hashlib.sha256)
    digest = hmac_sha256.digest()
    signature = base64.b64encode(digest).decode("utf-8")

    return signature


def pay_with_esewa(request):
    if request.method == "POST":
        target_url = "https://rc-epay.esewa.com.np/api/epay/main/v2/form"

        total_amount = "1010"
        transaction_uuid = uuid4()
        product_code = "EPAYTEST"

        msg = f"total_amount={total_amount},transaction_uuid={transaction_uuid},product_code={product_code}"
        signature = generate_signature(msg)

        payload = {
            "amount": "1000",
            "tax_amount": "10",
            "product_service_charge": "0",
            "product_delivery_charge": "0",
            "product_code": f"{product_code}",
            "total_amount": f"{total_amount}",
            "transaction_uuid": f"{transaction_uuid}",
            "success_url": "http://localhost:8000/",
            "failure_url": "http://localhost:8000/",
            "signed_field_names": "total_amount,transaction_uuid,product_code",
            "signature": f"{signature}",
        }

        response = requests.post(target_url, data=payload)
        if response.status_code == 200:
            return redirect(response.url)
        else:
            return render(request, "500.html")


def pay_with_khalti(request):
    url = "https://dev.khalti.com/api/v2/epayment/initiate/"
    payload = json.dumps(
        {
            "return_url": "http://localhost:8000/",
            "website_url": "http://localhost:8000",
            "amount": 10 * 100,
            "purchase_order_id": 1,
            "purchase_order_name": "TESTKHALTI",
            "customer_info": {
                "name": request.user.full_name(),
                "email": request.user.email,
                "phone": request.user.phone_number,
            },
            "amount_breakdown": [
                {"label": "Mark Price", "amount": 10 * 100},
                {"label": "VAT", "amount": 0},
            ],
        }
    )

    headers = {
        "Authorization": "Key dcb5a1bfaa9248cca4068fb95ffa0438",
        "Content-Type": "application/json",
    }
    response = requests.post(url, headers=headers, data=payload)
    print(response.content)

    if response.status_code == 200:
        return redirect(response.json()["payment_url"])
    else:
        return render(request, "500.html")
