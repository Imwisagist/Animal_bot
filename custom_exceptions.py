class BadCodeStatus(Exception):
    """Статус-код ответа не равен 200."""
    pass


class InvalidArgument(Exception):
    """Не подходящий аргумент."""
    pass
