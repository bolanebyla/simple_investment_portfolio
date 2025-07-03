from django.urls import path
from rest_framework import routers

from investment_portfolio.infrastructure.views import (
    InvestmentPortfolioView,
)
from investment_portfolio.infrastructure.views.investment_portfolio import (
    AddAssetToInvestmentPortfolioView,
)

investment_portfolio_api_router = routers.SimpleRouter()


investment_portfolio_api_urlpatterns = [
    path("investment_portfolio", InvestmentPortfolioView.as_view()),
    path(
        "investment_portfolio/add_asset_to_investment_portfolio",
        AddAssetToInvestmentPortfolioView.as_view(),
    ),
]

investment_portfolio_api_urlpatterns += investment_portfolio_api_router.urls
