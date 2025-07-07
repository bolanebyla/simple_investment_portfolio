from uuid import UUID

from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from framework.api import ValidationErrorSerializer, validation_error_response
from framework.di import DiRequest
from investment_portfolio.application.use_cases import (
    AddAssetToInvestmentPortfolioUseCase,
    CreateUserInvestmentPortfolioUseCase,
    GetUserInvestmentPortfolioRequestDto,
    GetUserInvestmentPortfolioUseCase,
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

    def get(self, request: DiRequest):
        # TODO: вынести в серилизстор
        request_dto = GetUserInvestmentPortfolioRequestDto(
            investment_portfolio_id=UUID(
                "c1825398-1877-4813-90e2-d7ae823c89cf"
            ),
            user_id=1,
        )

        use_case = request.container.get(GetUserInvestmentPortfolioUseCase)
        # TODO: вынести в серилизстор
        result_dto = use_case.execute(request_dto=request_dto)
        return Response(str(result_dto))


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
