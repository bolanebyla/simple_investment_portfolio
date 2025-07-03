from rest_framework import serializers

from investment_portfolio.application.use_cases import (
    AddAssetToInvestmentPortfolioDto,
    CreateUserInvestmentPortfolioDto,
)


class CreateUserInvestmentPortfolioSerializer(serializers.Serializer):
    # user = serializers.HiddenField(
    #     default=serializers.CurrentUserDefault()
    # )
    title = serializers.CharField()

    def create(self, validated_data: dict) -> CreateUserInvestmentPortfolioDto:
        # user: User = validated_data.pop("user")

        return CreateUserInvestmentPortfolioDto(
            **validated_data,
            user_id=1,  # TODO:
        )


class AddAssetToInvestmentPortfolioSerializer(serializers.Serializer):
    # user = serializers.HiddenField(
    #     default=serializers.CurrentUserDefault()
    # )

    investment_portfolio_id = serializers.UUIDField()
    asset_ticket = serializers.CharField()

    def create(self, validated_data: dict) -> AddAssetToInvestmentPortfolioDto:
        # user: User = validated_data.pop("user")

        return AddAssetToInvestmentPortfolioDto(
            **validated_data,
            user_id=1,  # TODO:
        )
