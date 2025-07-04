from dishka import Provider, Scope, provide

from investment_portfolio.infrastructure.repositories.mappers import (
    InvestmentAssetModelMapper,
    InvestmentPortfolioModelMapper,
)


class DbModelMappersProvider(Provider):
    scope = Scope.REQUEST

    investment_asset_model_mapper = provide(
        InvestmentAssetModelMapper,
    )
    investment_portfolio_model_mapper = provide(
        InvestmentPortfolioModelMapper,
    )
