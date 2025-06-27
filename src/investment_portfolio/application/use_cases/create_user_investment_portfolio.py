import uuid

from investment_portfolio.domain import InvestmentPortfolio


class CreateUserInvestmentPortfolioUseCase:
    # TODO: async
    def execute(self) -> None:
        investment_portfolio = InvestmentPortfolio(
            id=uuid.uuid4(),
            title="test",
        )
        print(investment_portfolio)
