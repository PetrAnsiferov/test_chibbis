# Загрузка данных с JSONPlaceholder

Скрипт загружает users, posts, comments из API и сохраняет в SQLite.

## Что делаем по порядку

1. **Открываем терминал** 
2. **Клонируем репозиторий:**

git clone https://github.com/PetrAnsiferov/test_chibbis.git

cd test_chibbis

3. **Устанавливаем зависимости:**

pip install -r requirements.txt

4. **Запускаем скрипт:**
python main.py

**Что получим**

Файл data.db с таблицами:

users (10 записей)

posts (100 записей)

comments (500 записей)

**Важно:** при повторном запуске данные не дублируются.


## Как проверить результат

### Способ 1 — через терминал (sqlite3)


sqlite3 data.db ".tables"              # показать все таблицы

sqlite3 data.db "SELECT COUNT(*) FROM users;"   # сколько записей в users

sqlite3 data.db "SELECT * FROM users;"          # показать всех пользователей

### Способ 2 — через DB Browser

Скачайте DB Browser for SQLite
Откройте → Open Database → выберите data.db
Вкладка Browse Data → выберите таблицу (users, posts, comments)