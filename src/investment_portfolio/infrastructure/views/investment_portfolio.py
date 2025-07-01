from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from framework.api import ValidationErrorSerializer, validation_error_response
from framework.di import DiRequest
from investment_portfolio.application.use_cases import (
    CreateUserInvestmentPortfolioUseCase,
)
from investment_portfolio.infrastructure.views.serializers import (
    CreateUserInvestmentPortfolioSerializer,
)


class InvestmentPortfolioView(APIView):
    @swagger_auto_schema(
        request_body=CreateUserInvestmentPortfolioSerializer,
        responses={
            200: None,
            400: ValidationErrorSerializer(),
        },
    )
    def post(self, request: DiRequest):
        create_serializer = CreateUserInvestmentPortfolioSerializer(
            data=request.data,
        )
        if create_serializer.is_valid():
            use_case = request.container.get(
                CreateUserInvestmentPortfolioUseCase
            )
            create_dto = create_serializer.save()
            use_case.execute(create_dto=create_dto)
            return Response()

        return validation_error_response(errors=create_serializer.errors)
