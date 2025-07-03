# TODO: добавить коды к ошибкам


class AppError(Exception):
    pass


class InvestmentPortfolioNotFoundByIdAndUserId(AppError):
    pass


class InvestmentPortfolioAlreadyHasAssetWithTicket(AppError):
    pass
