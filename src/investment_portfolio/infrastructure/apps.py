from django.apps import AppConfig
from .app_label import app_label

class InvestmentPortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'investment_portfolio.infrastructure'
    label = app_label
