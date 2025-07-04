from typing import Any

from django.db.models import QuerySet

from investment_portfolio.domain import InvestmentPortfolio
from investment_portfolio.domain.entities import InvestmentAsset
from investment_portfolio.infrastructure.models import (
    InvestmentAssetModel,
    InvestmentPortfolioModel,
)


class InvestmentAssetModelMapper:
    def map_entity_to_model(
        self,
        entity: InvestmentAsset,
    ) -> InvestmentAssetModel:
        return InvestmentAssetModel(
            id=entity.id,
            ticket=entity.ticket,
            name=entity.name,
        )

    def map_entities_to_models(
        self, entities: list[InvestmentAsset]
    ) -> list[InvestmentAssetModel]:
        return [self.map_entity_to_model(entity=entity) for entity in entities]

    def map_model_to_entity(
        self, model: InvestmentAssetModel
    ) -> InvestmentAsset:
        return InvestmentAsset(
            id=model.id,
            ticket=model.ticket,
            name=model.name,
        )

    def map_models_to_entities(
        self, models: QuerySet[InvestmentAssetModel]
    ) -> list[InvestmentAsset]:
        assets = []
        for model in models:
            asset = self.map_model_to_entity(model=model)
            assets.append(asset)

        return assets


class InvestmentPortfolioModelMapper:
    def __init__(
        self,
        investment_asset_model_mapper: InvestmentAssetModelMapper,
    ):
        self._investment_asset_model_mapper = investment_asset_model_mapper

    def map_entity_to_model_defaults(
        self, entity: InvestmentPortfolio
    ) -> dict[str, Any]:
        return {
            "title": entity.title,
            "user_id": entity.user_id,
        }

    def map_model_to_entity(
        self, model: InvestmentPortfolioModel
    ) -> InvestmentPortfolio:
        assets = self._investment_asset_model_mapper.map_models_to_entities(
            models=model.assets.all(),
        )

        return InvestmentPortfolio(
            id=model.id,
            title=model.title,
            user_id=model.user.id,
            assets=assets,
        )
