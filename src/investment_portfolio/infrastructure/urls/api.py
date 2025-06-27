from django.urls import path
from rest_framework import routers

from investment_portfolio.infrastructure.views import (
    InvestmentPortfolioView,
)

investment_portfolio_api_router = routers.SimpleRouter()


investment_portfolio_api_urlpatterns = [
    path("investment_portfolio", InvestmentPortfolioView.as_view()),
]

investment_portfolio_api_urlpatterns += investment_portfolio_api_router.urls
