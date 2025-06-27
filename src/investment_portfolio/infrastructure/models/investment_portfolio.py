import uuid

from django.db import models

from ..app_label import app_label

class InvestmentPortfolio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = f"{app_label}__investment_portfolios"
        db_table_comment = "Инвестиционные портфели"
