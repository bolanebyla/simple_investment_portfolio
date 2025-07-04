from uuid import UUID

from investment_portfolio.domain import InvestmentPortfolio
from investment_portfolio.domain.entities.investment_asset import (
    InvestmentAsset,
)
from investment_portfolio.domain.repositories import InvestmentPortfolioRepo
from investment_portfolio.infrastructure.models import (
    InvestmentAssetModel,
    InvestmentPortfolioModel,
)
from investment_portfolio.infrastructure.repositories.mappers import (
    InvestmentAssetModelMapper,
    InvestmentPortfolioModelMapper,
)


class InvestmentPortfolioRepoImpl(InvestmentPortfolioRepo):
    def __init__(
        self,
        investment_portfolio_model_mapper: InvestmentPortfolioModelMapper,
        investment_asset_model_mapper: InvestmentAssetModelMapper,
    ):
        self._investment_portfolio_model_mapper = (
            investment_portfolio_model_mapper
        )
        self._investment_asset_model_mapper = investment_asset_model_mapper

    def add(self, investment_portfolio: InvestmentPortfolio) -> None:
        investment_portfolio_model_defaults = self._investment_portfolio_model_mapper.map_entity_to_model_defaults(
            entity=investment_portfolio,
        )

        # Создаем или обновляем портфель
        db_investment_portfolio, created = (
            InvestmentPortfolioModel.objects.update_or_create(
                id=investment_portfolio.id,
                defaults=investment_portfolio_model_defaults,
            )
        )

        if investment_portfolio.assets:
            asset_models = (
                self._investment_asset_model_mapper.map_entities_to_models(
                    entities=investment_portfolio.assets
                )
            )
            for asset_model in asset_models:
                asset_model.investment_portfolio = db_investment_portfolio

            InvestmentAssetModel.objects.bulk_create(
                asset_models,
                update_conflicts=True,
                unique_fields=["id"],
                update_fields=["ticket", "name"],  # TODO: ? вынести в маппер
            )

        current_asset_ids = {asset.id for asset in investment_portfolio.assets}
        db_investment_portfolio.assets.exclude(
            id__in=current_asset_ids
        ).delete()

    def get_by_id_and_user_id(
        self,
        id_: UUID,
        user_id: int,
    ) -> InvestmentPortfolio | None:
        try:
            db_investment_portfolio = InvestmentPortfolioModel.objects.get(
                id=id_,
                user_id=user_id,
            )
        except InvestmentPortfolioModel.DoesNotExist:
            return None

        return self._investment_portfolio_model_mapper.map_model_to_entity(
            model=db_investment_portfolio,
        )
