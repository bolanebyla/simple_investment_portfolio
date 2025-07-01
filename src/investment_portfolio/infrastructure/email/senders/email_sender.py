from investment_portfolio.application.dto import SendEmailDto
from investment_portfolio.application.interfaces import EmailSender


class EmailSenderImpl(EmailSender):
    def send_email(self, send_email_dto: SendEmailDto) -> None:
        print("Sending email:", send_email_dto)
