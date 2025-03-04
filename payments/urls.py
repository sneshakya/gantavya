from django.urls import path

from payments import views


urlpatterns = [
    path("payment/", views.payment_page, name="payment_page"),
    path("esewa-payment/", views.pay_with_esewa, name="pay_with_esewa"),
    path("khalti-payment/", views.pay_with_khalti, name="pay_with_khalti"),
    path("verify-esewa/", views.verify_esewa, name="verify_esewa"),
    path("verify-khalti/", views.verify_khalti, name="verify_khalti"),
    path("payment-success/", views.payment_success, name="payment_success"),
    path("payment-failure/", views.payment_failure, name="payment_failure"),
]
