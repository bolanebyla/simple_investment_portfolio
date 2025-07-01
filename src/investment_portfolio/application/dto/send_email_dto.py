from dataclasses import dataclass


@dataclass(frozen=True)
class SendEmailDto:
    sender_email: str
    recipients_emails: list[str]
    title: str
    body: str
