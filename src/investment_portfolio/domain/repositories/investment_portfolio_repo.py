from abc import abstractmethod
from typing import Protocol

from investment_portfolio.domain import InvestmentPortfolio


class InvestmentPortfolioRepo(Protocol):
    @abstractmethod
    def add(self, investment_portfolio: InvestmentPortfolio) -> None: ...
