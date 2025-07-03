from dataclasses import dataclass

from .base import BaseEntity


@dataclass(kw_only=True)
class InvestmentAsset(BaseEntity):
    """
    Инвестиционный актив
    """

    ticket: str
    name: str
