from dataclasses import dataclass
from uuid import UUID

from investment_portfolio.application.interfaces import (
    InvestmentPortfolioReadRepo,
)


@dataclass(frozen=True)
class GetUserInvestmentPortfolioRequestDto:
    investment_portfolio_id: UUID
    user_id: int


@dataclass(frozen=True)
class GetUserInvestmentPortfolioResultDto:
    pass


class GetUserInvestmentPortfolioUseCase:
    def __init__(
        self,
        investment_portfolio_read_repo: InvestmentPortfolioReadRepo,
    ):
        self._investment_portfolio_read_repo = investment_portfolio_read_repo

    def execute(
        self,
        request_dto: GetUserInvestmentPortfolioRequestDto,
    ) -> GetUserInvestmentPortfolioResultDto:
        user_investment_portfolio_dto = (
            self._investment_portfolio_read_repo.get_user_investment_portfolio(
                investment_portfolio_id=request_dto.investment_portfolio_id,
                user_id=request_dto.user_id,
            )
        )

        # TODO:
        result_dto = GetUserInvestmentPortfolioResultDto()
        return result_dto
