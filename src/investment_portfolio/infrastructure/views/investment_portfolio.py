from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from framework.api import ValidationErrorSerializer, validation_error_response
from framework.di import DiRequest
from investment_portfolio.application.use_cases import (
    AddAssetToInvestmentPortfolioUseCase,
    CreateUserInvestmentPortfolioUseCase,
)
from investment_portfolio.infrastructure.views.serializers import (
    AddAssetToInvestmentPortfolioSerializer,
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
        serializer = CreateUserInvestmentPortfolioSerializer(
            data=request.data,
        )
        if serializer.is_valid():
            use_case = request.container.get(
                CreateUserInvestmentPortfolioUseCase
            )
            dto = serializer.save()
            use_case.execute(create_dto=dto)
            return Response()

        return validation_error_response(errors=serializer.errors)


class AddAssetToInvestmentPortfolioView(APIView):
    @swagger_auto_schema(
        request_body=AddAssetToInvestmentPortfolioSerializer,
        responses={
            200: None,
            400: ValidationErrorSerializer(),
        },
    )
    def post(self, request: DiRequest):
        serializer = AddAssetToInvestmentPortfolioSerializer(
            data=request.data,
        )
        if serializer.is_valid():
            use_case = request.container.get(
                AddAssetToInvestmentPortfolioUseCase
            )
            dto = serializer.save()
            use_case.execute(add_dto=dto)
            return Response()

        return validation_error_response(errors=serializer.errors)
