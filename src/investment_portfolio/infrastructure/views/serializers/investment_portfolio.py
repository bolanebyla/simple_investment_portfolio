from rest_framework import serializers

from investment_portfolio.application.use_cases import (
    CreateUserInvestmentPortfolioDto,
)


class CreateUserInvestmentPortfolioSerializer(serializers.Serializer):
    title = serializers.CharField()

    def create(self, validated_data: dict) -> CreateUserInvestmentPortfolioDto:
        return CreateUserInvestmentPortfolioDto(
            **validated_data,
            user_id=0,  # TODO:
        )
