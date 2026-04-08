# Загрузка данных с JSONPlaceholder

Скрипт загружает пользователей, посты и комментарии из API и сохраняет в SQLite.

## Запуск
```bash
pip install requests
python main.py
Результат

Файл data.db с таблицами users, posts, comments (10, 100, 500 записей). При повторном запуске данные не дублируются.