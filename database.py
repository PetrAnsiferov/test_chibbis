import sqlite3

def init_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            username TEXT,
            email TEXT,
            phone TEXT,
            website TEXT
         )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            title TEXT,
            body TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
           )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY,
            post_id INTEGER,
            name TEXT,
            email TEXT,
            body TEXT,
            FOREIGN KEY (post_id) REFERENCES posts (id)
          )
    ''')
    
    conn.commit()
    conn.close()

def save_users(users):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    
    for user in users:
        cursor.execute('''
            INSERT OR IGNORE INTO users (id, name, username, email, phone, website)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (user['id'], user['name'], user['username'], 
              user['email'], user['phone'], user['website']))
    
    conn.commit()
    conn.close()

def save_posts(posts):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    
    for post in posts:
        cursor.execute('''
            INSERT OR IGNORE INTO posts (id, user_id, title, body)
            VALUES (?, ?, ?, ?)
        ''', (post['id'], post['userId'], post['title'], post['body']))
    
    conn.commit()
    conn.close()

def save_comments(comments):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    
    for comment in comments:
        cursor.execute('''
            INSERT OR IGNORE INTO comments (id, post_id, name, email, body)
            VALUES (?, ?, ?, ?, ?)
        ''', (comment['id'], comment['postId'], comment['name'], 
              comment['email'], comment['body']))
    
    conn.commit()
    conn.close()