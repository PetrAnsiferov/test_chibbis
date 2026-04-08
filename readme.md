# Загрузка данных с JSONPlaceholder

Скрипт загружает users, posts, comments из API и сохраняет в SQLite.

## Запуск

```bash
pip install -r requirements.txt
python main.py
Результат

Файл data.db с таблицами: users (10), posts (100), comments (500). При повторном запуске данные не дублируются.