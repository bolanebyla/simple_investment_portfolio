from uuid import UUID

from investment_portfolio.application.dto import SendEmailDto
from investment_portfolio.application.interfaces import EmailSender


class SendFirstUserPortfolioCreatedEmailUseCase:
    def __init__(
        self,
        # sender_email: str,
        email_sender: EmailSender,
    ):
        self._sender_email = "sender_email"  # TODO:!!!!
        self._email_sender = email_sender

    def execute(self, investment_portfolio_id: UUID) -> None:
        user_id = 0

        send_email_dto = SendEmailDto(
            sender_email=self._sender_email,
            recipients_emails=["test@test.com"],
            title=f"test: {user_id}",
            body="Test test test.",
        )
        self._email_sender.send_email(send_email_dto=send_email_dto)
