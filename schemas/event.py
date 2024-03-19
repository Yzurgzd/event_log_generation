class Event:
    """
    Класс для представления события.

    Attributes:
        user_id (int): Идентификатор пользователя, к которому относится событие.
        event_type (int): Тип события (число от 1 до 4).
        timestamp (str): Временная метка события в формате '%Y-%m-%d %H:%M:%S'.
        source (str): Источник события (например, 'Яндекс', 'Гугл' и т.д.).
        browser (str): Тип браузера (например, 'Мобильный', 'Планшет', 'Десктоп').
        amount (int): Сумма заказа (от 10 000 до 1 000 000 руб.).
        pages_viewed (int): Количество просмотренных страниц (от 1 до 100).
        call_successful (int): Флаг успешного звонка (0 или 1).
    """

    def __init__(
        self,
        user_id: int,
        event_type: int,
        timestamp: str,
        source: str = None,
        browser: str = None,
        amount: float = None,
        pages_viewed: int = None,
        call_successful: int = None,
    ):
        """
        Инициализация события.

        Args:
            user_id (int): Идентификатор пользователя.
            event_type (int): Тип события (число от 1 до 4).
            timestamp (str): Временная метка события в формате '%Y-%m-%d %H:%M:%S'.
            source (str, optional): Источник события. По умолчанию None.
            browser (str, optional): Тип браузера. По умолчанию None.
            amount (float, optional): Сумма заказа. По умолчанию None.
            pages_viewed (int, optional): Количество просмотренных страниц. По умолчанию None.
            call_successful (int, optional): Флаг успешного звонка. По умолчанию None.
        """
        self.user_id = user_id
        self.event_type = event_type
        self.timestamp = timestamp
        self.source = source
        self.browser = browser
        self.amount = amount
        self.pages_viewed = pages_viewed
        self.call_successful = call_successful
