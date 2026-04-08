import requests

def fetch_users():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    response.raise_for_status()  # выбросит ошибку, если запрос неудачный
    return response.json()

def fetch_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    response.raise_for_status()
    return response.json()

def fetch_comments():
    response = requests.get('https://jsonplaceholder.typicode.com/comments')
    response.raise_for_status()
    return response.json()