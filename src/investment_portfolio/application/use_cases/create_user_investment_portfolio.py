import uuid

from investment_portfolio.application.application_events import (
    FirstUserPortfolioCreatedEvent,
)
from investment_portfolio.application.interfaces import EventDispatcher
from investment_portfolio.domain import InvestmentPortfolio
from investment_portfolio.domain.repositories import InvestmentPortfolioRepo


class CreateUserInvestmentPortfolioUseCase:
    def __init__(
        self,
        investment_portfolio_repo: InvestmentPortfolioRepo,
        event_dispatcher: EventDispatcher,
    ):
        self._investment_portfolio_repo = investment_portfolio_repo
        self._event_dispatcher = event_dispatcher

    def execute(self) -> None:
        investment_portfolio = InvestmentPortfolio(
            id=uuid.uuid4(),
            title="test",
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
