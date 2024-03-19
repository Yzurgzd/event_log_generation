import csv
import sqlite3


class EventDatabase:
    """
    Класс для работы с базой данных событий.

    Attributes:
        db_name (str): Имя базы данных SQLite3.
        conn: Соединение с базой данных SQLite3.
    """

    def __init__(self, db_name: str = 'events') -> None:
        """
        Инициализация объекта класса EventDatabase.

        Args:
            db_name (str, optional): Имя базы данных SQLite3. По умолчанию 'events.db'.
        """
        self.db_name = f'{db_name}.db'
        self.conn = sqlite3.connect(self.db_name)
        self.create_event_table()

    def create_event_table(self) -> None:
        """
        Создает таблицу событий в базе данных, если она не существует.
        """
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS events (
                            event_id INTEGER PRIMARY KEY,
                            user_id INTEGER,
                            event_type INTEGER,
                            source TEXT,
                            browser TEXT,
                            amount REAL,
                            pages_viewed INTEGER,
                            call_successful INTEGER,
                            timestamp TEXT
                        )''')
        self.conn.commit()

    def save_event(self, event) -> None:
        """
        Сохраняет событие в базу данных.

        Args:
            event (dict): Словарь, содержащий информацию о событии.
                Обязательные ключи: 'user_id', 'event_type', 'timestamp'.
                Дополнительные ключи: 'source', 'browser', 'amount', 'pages_viewed', 'call_successful'.

        Raises:
            sqlite3.Error: Ошибка при выполнении операции сохранения в базе данных.
        """
        cursor = self.conn.cursor()
        cursor.execute(
            '''INSERT INTO events (
                user_id,
                event_type,
                source,
                browser,
                amount,
                pages_viewed,
                call_successful,
                timestamp
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
            (
                event['user_id'],
                event['event_type'],
                event.get('source'),
                event.get('browser'),
                event.get('amount'),
                event.get('pages_viewed'),
                event.get('call_successful'),
                event['timestamp'],
            ),
        )
        self.conn.commit()

    def close_connection(self) -> None:
        """
        Закрывает соединение с базой данных.
        """
        self.conn.close()

    def get_user_events(self, user_id):
        """
        Получает все события для указанного пользователя из базы данных.

        Args:
            user_id (int): Идентификатор пользователя.

        Returns:
            list: Список кортежей с информацией о событиях пользователя.
        """
        cursor = self.conn.cursor()
        cursor.execute(
            'SELECT event_type FROM events WHERE user_id = ?',
            (user_id,),
        )
        return cursor.fetchall()

    def export_statistics(self, filename: str) -> None:
        """
        Экспортирует статистику событий в файл CSV согласно требованиям.

        Args:
            filename (str): Имя файла CSV для сохранения статистики.
        """
        query = '''
            SELECT e.user_id, e.event_type,
                e.source, e.browser, e.amount,
                e.pages_viewed, e.call_successful,
                e.timestamp
            FROM events e
            ORDER BY e.user_id, e.event_type
        '''

        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        with open(f'{filename}.csv', 'w', newline='') as csvfile:
            fieldnames = [
                'user_id',
                'event_type',
                'source',
                'browser',
                'amount',
                'pages_viewed',
                'call_successful',
                'timestamp',
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in rows:
                writer.writerow({
                    'user_id': row[0],
                    'event_type': row[1],
                    'source': row[2] if row[2] else '',
                    'browser': row[3] if row[3] else '',
                    'amount': row[4] if row[4] else '',
                    'pages_viewed': row[5] if row[5] else '',
                    'call_successful': row[6] if row[6] else '',
                    'timestamp': row[7],
                })
