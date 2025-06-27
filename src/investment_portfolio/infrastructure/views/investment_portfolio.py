from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from investment_portfolio.application.use_cases import (
    CreateUserInvestmentPortfolioUseCase,
)


class InvestmentPortfolioView(APIView):
    def post(self, request: Request):
        use_case = CreateUserInvestmentPortfolioUseCase()
        use_case.execute()
        return Response()
