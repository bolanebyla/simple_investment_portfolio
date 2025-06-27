from django.contrib import admin

from .models import InvestmentPortfolioModel


class InvestmentPortfolioModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at")


admin.site.register(InvestmentPortfolioModel, InvestmentPortfolioModelAdmin)
