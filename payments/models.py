from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import CustomUser


class PaymentHistory(models.Model):
    class PaymentMethod(models.TextChoices):
        KHALTI = "khalti", _("Khalti")
        ESEWA = "esewa", _("Esewa")
        BANK = "bank", _("Bank Transfer")
        CARD = "card", _("Credit Card")

    transaction_id = models.CharField(
        _("transaction ID"), max_length=500, unique=True, db_index=True
    )
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="payment_histories"
    )
    total_payment = models.DecimalField(
        _("total amount"), max_digits=10, decimal_places=2, default=0
    )
    payment_via = models.CharField(
        _("payment method"), max_length=20, choices=PaymentMethod.choices
    )
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    class Meta:
        verbose_name = _("Payment History")
        verbose_name_plural = _("Payment Histories")
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.transaction_id} - {self.user.email} ({self.total_payment})"
