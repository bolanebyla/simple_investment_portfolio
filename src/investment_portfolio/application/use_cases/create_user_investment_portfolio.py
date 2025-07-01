import uuid
from dataclasses import dataclass

from investment_portfolio.application.application_events import (
    FirstUserPortfolioCreatedEvent,
)
from investment_portfolio.application.interfaces import EventDispatcher
from investment_portfolio.domain import InvestmentPortfolio
from investment_portfolio.domain.repositories import InvestmentPortfolioRepo


@dataclass(frozen=True)
class CreateUserInvestmentPortfolioDto:
    user_id: int
    title: str


class CreateUserInvestmentPortfolioUseCase:
    def __init__(
        self,
        investment_portfolio_repo: InvestmentPortfolioRepo,
        event_dispatcher: EventDispatcher,
    ):
        self._investment_portfolio_repo = investment_portfolio_repo
        self._event_dispatcher = event_dispatcher

    def execute(
        self,
        create_dto: CreateUserInvestmentPortfolioDto,
    ) -> None:
        investment_portfolio = InvestmentPortfolio(
            id=uuid.uuid4(),
            title=create_dto.title,
            user_id=create_dto.user_id,
        )
        self._investment_portfolio_repo.add(
            investment_portfolio=investment_portfolio
        )

        for domain_events in investment_portfolio.domain_events:
            self._event_dispatcher.dispatch(domain_events)

        first_user_portfolio_created_event = FirstUserPortfolioCreatedEvent(
            investment_portfolio_id=investment_portfolio.id,
        )
        self._event_dispatcher.dispatch(first_user_portfolio_created_event)
