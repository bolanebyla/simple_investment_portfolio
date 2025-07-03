import uuid

from django.contrib.auth.models import User
from django.db import models

from ..app_label import app_label


class InvestmentPortfolioModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField()
    user = models.ForeignKey(User, on_delete=models.RESTRICT)

    class Meta:
        db_table = f"{app_label}__investment_portfolios"
        db_table_comment = "Инвестиционные портфели"
