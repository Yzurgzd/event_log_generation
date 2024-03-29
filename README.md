# Проект "Управление событиями"

Этот проект представляет собой систему управления событиями, которая генерирует случайные события для пользователей, сохраняет их в базе данных и экспортирует статистику в файл CSV.

## Установка

1. Клонируйте репозиторий на свой локальный компьютер.

2. Перейдите в каталог проекта.

3. Создайте файл `.env` по примеру `env_vars` в корне проекта и укажите необходимые настройки.

## Использование

1. Запустите файл `main.py` для генерации событий и экспорта статистики.

2. После выполнения программы будет создан файл `.csv` с экспортированной статистикой событий.

## Структура проекта

- `main.py`: Основной файл программы, который запускает процесс генерации событий и экспорта статистики.
- `const.py`: Файл с константами, такими как типы событий.
- `schemas/event.py`: Модуль с описанием события и его параметров.
- `services/event.py`: Модуль с классом для генерации событий.
- `utils/database.py`: Модуль с классом для работы с базой данных событий.
- `.env`: Файл с настройками проекта.

## Зависимости

- Python 3.x
- SQLite3
