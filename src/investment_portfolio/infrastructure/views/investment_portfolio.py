from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from investment_portfolio.application.use_cases import (
    CreateUserInvestmentPortfolioUseCase,
)
from investment_portfolio.infrastructure.repositories import (
    InvestmentPortfolioRepoImpl,
)


class InvestmentPortfolioView(APIView):
    def post(self, request: Request):
        investment_portfolio_repo = InvestmentPortfolioRepoImpl()
        use_case = CreateUserInvestmentPortfolioUseCase(
            investment_portfolio_repo=investment_portfolio_repo,
        )
        use_case.execute()
        return Response()
