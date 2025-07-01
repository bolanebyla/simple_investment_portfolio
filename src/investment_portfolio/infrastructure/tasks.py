from uuid import UUID

from celery import shared_task
from dishka import FromDishka

from investment_portfolio.application.application_events import (
    FirstUserPortfolioCreatedEvent,
)
from investment_portfolio.application.use_cases import (
    SendFirstUserPortfolioCreatedEmailUseCase,
)


@shared_task
def send_first_user_portfolio_created_email(
    use_case: FromDishka[SendFirstUserPortfolioCreatedEmailUseCase],
    investment_portfolio_id: UUID,
) -> None:
    use_case.execute(investment_portfolio_id=investment_portfolio_id)
