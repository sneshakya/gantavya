from django.urls import path

from payments import views


urlpatterns = [
    path("payment/", views.payment_page, name="payment_page"),
    path("esewa-payment/", views.pay_with_esewa, name="pay_with_esewa"),
    path("khalti-payment/", views.pay_with_khalti, name="pay_with_khalti"),
]
