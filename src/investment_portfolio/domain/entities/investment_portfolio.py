from dataclasses import dataclass
from uuid import UUID


@dataclass
class InvestmentPortfolio:
    """
    Инвестиционный портфель
    """

    id: UUID
    title: str
