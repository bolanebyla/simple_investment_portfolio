import uuid

from django.db import models

from ..app_label import app_label
from .investment_portfolio import InvestmentPortfolioModel


class InvestmentAssetModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    investment_portfolio = models.ForeignKey(
        InvestmentPortfolioModel,
        on_delete=models.CASCADE,
        related_name="assets",
    )

    ticket = models.CharField(max_length=20)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = f"{app_label}__investment_assets"
        db_table_comment = "Активы инвестиционного портфеля"
