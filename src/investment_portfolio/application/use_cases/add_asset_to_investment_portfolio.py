import uuid
from dataclasses import dataclass

from investment_portfolio.application.errors import (
    InvestmentPortfolioNotFoundByIdAndUserId,
)
from investment_portfolio.application.interfaces import EventDispatcher
from investment_portfolio.domain.entities import InvestmentAsset
from investment_portfolio.domain.repositories import InvestmentPortfolioRepo


@dataclass(frozen=True)
class AddAssetToInvestmentPortfolioDto:
    user_id: int
    investment_portfolio_id: uuid.UUID
    asset_ticket: str


class AddAssetToInvestmentPortfolioUseCase:
    def __init__(
        self,
        investment_portfolio_repo: InvestmentPortfolioRepo,
        event_dispatcher: EventDispatcher,
    ):
        self._investment_portfolio_repo = investment_portfolio_repo
        self._event_dispatcher = event_dispatcher

    def execute(
        self,
        add_dto: AddAssetToInvestmentPortfolioDto,
    ) -> None:
        investment_portfolio = (
            self._investment_portfolio_repo.get_by_id_and_user_id(
                id_=add_dto.investment_portfolio_id,
                user_id=add_dto.user_id,
            )
        )

        if investment_portfolio is None:
            raise InvestmentPortfolioNotFoundByIdAndUserId()

        asset = InvestmentAsset(
            id=uuid.uuid4(),
            ticket=add_dto.asset_ticket,
            name="test",  # TODO:
        )

        investment_portfolio.add_asset(asset=asset)

        self._investment_portfolio_repo.add(investment_portfolio)
