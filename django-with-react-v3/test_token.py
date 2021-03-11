import requests

TOKEN = 'c14a8ebace3b5b7d80d0849109a4138d0114c48b'

headers = {
    'Authorization': f'Token {TOKEN}'
}

req = requests.get('http://localhost:8000/post/1/', headers=headers)

print(req.json())