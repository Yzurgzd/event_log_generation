import random
from datetime import datetime, timedelta

from schemas.event import Event


class EventGenerator:
    """
    Класс для генерации случайных событий.

    Attributes:
        sources (list): Список возможных источников событий.
        browsers (list): Список возможных типов браузеров.
    """

    def __init__(self) -> None:
        """
        Инициализация объекта класса EventGenerator.
        """
        self.sources = ['Яндекс', 'Гугл', 'Фейсбук']
        self.browsers = ['Мобильный', 'Планшет', 'Десктоп']

    def random_date(
        self,
        start_date: datetime,
        end_date: datetime,
    ) -> datetime:
        """
        Генерирует случайную дату и время между двумя заданными датами.

        Args:
            start_date (datetime): Начальная дата и время.
            end_date (datetime): Конечная дата и время.

        Returns:
            datetime: Случайная дата и время между start_date и end_date.
        """
        delta = end_date - start_date
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = random.randrange(int_delta)
        return start_date + timedelta(seconds=random_second)

    def generate_event(self, user_id: int, event_type: int) -> Event:
        """
        Генерирует случайное событие для заданного пользователя.

        Args:
            user_id (int): Идентификатор пользователя.
            event_type (int): Тип события (число от 1 до 4).

        Returns:
            dict: Словарь с информацией о сгенерированном событии.
        """
        event_params = {
            1: {
                'source': random.choice(self.sources),
                'browser': random.choice(self.browsers),
            },
            2: {
                'source': random.choice(self.sources),
            },
            3: {
                'source': random.choice(self.sources),
                'amount': random.randint(10000, 1000000),
            },
            4: {}
        }
        event_metrics = {
            1: {'pages_viewed': random.randint(1, 100)},
            2: {'call_successful': random.randint(0, 1)},
            3: {},
            4: {}
        }
        event_param = event_params[event_type]
        event_metric = event_metrics[event_type]

        event_time = self.random_date(
            datetime(2024, 1, 1),
            datetime(2024, 1, 31),
        ).strftime('%Y-%m-%d %H:%M:%S')

        event = Event(
            user_id=user_id,
            event_type=event_type,
            timestamp=event_time,
            **event_param,
            **event_metric
        )
        return event
