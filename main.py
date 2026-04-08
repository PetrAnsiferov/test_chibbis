from database import init_db, save_users, save_posts, save_comments
from fetcher import fetch_users, fetch_posts, fetch_comments

def main():
    print("Инициализация базы данных...")
    init_db()
    
    print("Загрузка пользователей...")
    users = fetch_users()
    save_users(users)
    print(f"Сохранено {len(users)} пользователей")
    
    print("Загрузка постов...")
    posts = fetch_posts()
    save_posts(posts)
    print(f"Сохранено {len(posts)} постов")
    
    print("Загрузка комментариев...")
    comments = fetch_comments()
    save_comments(comments)
    print(f"Сохранено {len(comments)} комментариев")
    
    print("Готово!")

if __name__ == "__main__":
    main()