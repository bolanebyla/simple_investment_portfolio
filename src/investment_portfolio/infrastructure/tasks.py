from celery import shared_task


@shared_task
def send_first_user_portfolio_created_email() -> None:
    # TODO: вызывать сервис
    print("Hello, world!")
