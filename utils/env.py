import os


def load_env():
    """
    Загружает переменные окружения из файла .env в текущую среду выполнения.

    Формат файла .env:
    Каждая строка должна содержать пару "ключ=значение", где ключ - это имя переменной окружения,
    а значение - соответствующее ему значение. Пустые строки и строки, начинающиеся с "#" игнорируются.

    Пример файла .env:
    ```
    SECRET_KEY=your_secret_key
    DATABASE_URL=your_database_url
    ```

    Примечание:
    Функция заменяет переменные окружения текущего процесса и не возвращает никаких значений.

    Raises:
        FileNotFoundError: Если файл .env не найден.
        ValueError: Если строка в файле .env имеет неверный формат.

    """
    try:
        with open('.env', 'r') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value
    except FileNotFoundError:
        raise FileNotFoundError('Файл .env не найден.')
    except ValueError:
        raise ValueError('Строка в файле .env имеет неверный формат.')
