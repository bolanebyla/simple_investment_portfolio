from abc import abstractmethod
from typing import Protocol

from investment_portfolio.application.dto import SendEmailDto


class EmailSender(Protocol):
    @abstractmethod
    def send_email(self, send_email_dto: SendEmailDto) -> None: ...
