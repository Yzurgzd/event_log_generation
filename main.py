import os
import random

from const import EVENT_TYPES
from services.event import EventGenerator
from utils.database import EventDatabase
from utils.env import load_env

load_env()


class EventManager:
    """
    Класс для управления событиями.

    Attributes:
        event_generator (EventGenerator): Экземпляр класса EventGenerator для генерации событий.
        db (EventDatabase): Экземпляр класса EventDatabase для работы с базой данных.
    """

    def __init__(self) -> None:
        """
        Инициализация EventManager.
        """
        self.event_generator = EventGenerator()
        self.db = EventDatabase(os.getenv('DB_NAME'))

    def generate_user_events(self, user_id: int) -> None:
        """
        Генерирует события для пользователя.

        Args:
            user_id (int): Идентификатор пользователя.
        """
        user_events = self.db.get_user_events(user_id)
        if not user_events:
            min_event_type = min(EVENT_TYPES.keys())
            max_event_type = max(EVENT_TYPES.keys())
            event_type = random.randint(min_event_type, max_event_type)
            event = self.event_generator.generate_event(user_id, event_type)
            self.db.save_event(event.__dict__)
            user_events.append((event_type,))

            for i in range(1, event_type):
                if (i,) not in user_events:
                    event = self.event_generator.generate_event(user_id, i)
                    self.db.save_event(event.__dict__)
                    user_events.append((i,))
        else:
            max_event_type = max(event[0] for event in user_events)
            if max_event_type < max(EVENT_TYPES.keys()):
                next_event_type = max_event_type + 1
                event = self.event_generator.generate_event(
                    user_id,
                    next_event_type,
                )
                self.db.save_event(event.__dict__)
                user_events.append((next_event_type,))

    def generate_events_for_users(self, num_users: int) -> None:
        """
        Генерирует события для заданного числа пользователей.

        Args:
            num_users (int): Число пользователей, для которых нужно сгенерировать события.
        """
        for user_id in range(1, num_users + 1):
            self.generate_user_events(user_id)

    def export_statistics(self, filename: str) -> None:
        """
        Экспортирует статистику событий в файл CSV.

        Args:
            filename (str): Имя файла CSV для сохранения статистики.
        """
        self.db.export_statistics(filename)

    def close_connection(self) -> None:
        """
        Закрывает соединение с базой данных.
        """
        self.db.close_connection()


if __name__ == '__main__':
    event_manager = EventManager()
    event_manager.generate_events_for_users(int(os.getenv('NUM_USERS')))
    event_manager.export_statistics(os.getenv('CSV_FILENAME'))
    event_manager.close_connection()
