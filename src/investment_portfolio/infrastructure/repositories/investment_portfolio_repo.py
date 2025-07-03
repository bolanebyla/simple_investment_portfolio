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


class InvestmentPortfolioRepoImpl(InvestmentPortfolioRepo):
    def add(self, investment_portfolio: InvestmentPortfolio) -> None:
        # Создаем или обновляем портфель
        db_investment_portfolio, created = (
            InvestmentPortfolioModel.objects.update_or_create(
                id=investment_portfolio.id,
                defaults={
                    "title": investment_portfolio.title,
                    "user_id": investment_portfolio.user_id,
                },
            )
        )

        # Сохраняем вложенные активы
        for asset in investment_portfolio.assets:
            InvestmentAssetModel.objects.update_or_create(
                id=asset.id,
                defaults={
                    "ticket": asset.ticket,
                    "name": asset.name,
                    "investment_portfolio": db_investment_portfolio,
                },
            )

        # Удаляем активы, которые больше не находятся в портфеле
        current_asset_ids = {asset.id for asset in investment_portfolio.assets}
        InvestmentAssetModel.objects.filter(
            investment_portfolio=db_investment_portfolio
        ).exclude(id__in=current_asset_ids).delete()

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

        # Загружаем связанные активы
        db_assets = InvestmentAssetModel.objects.filter(
            investment_portfolio=db_investment_portfolio
        )

        # TODO: вынести в маппер
        # Создаем доменные объекты активов
        assets = []
        for db_asset in db_assets:
            asset = InvestmentAsset(
                id=db_asset.id,
                ticket=db_asset.ticket,
                name=db_asset.name,
            )
            assets.append(asset)

        # TODO: вынести в маппер
        return InvestmentPortfolio(
            id=db_investment_portfolio.id,
            title=db_investment_portfolio.title,
            user_id=db_investment_portfolio.user_id,
            assets=assets,
        )
