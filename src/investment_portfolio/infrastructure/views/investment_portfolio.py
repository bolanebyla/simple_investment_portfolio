from rest_framework.response import Response
from rest_framework.views import APIView

from framework.di import DiRequest
from investment_portfolio.application.use_cases import (
    CreateUserInvestmentPortfolioUseCase,
)


class InvestmentPortfolioView(APIView):
    def post(self, request: DiRequest):
        use_case = request.container.get(CreateUserInvestmentPortfolioUseCase)

        use_case.execute()
        return Response()
