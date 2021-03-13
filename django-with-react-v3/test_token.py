import requests
from base64 import b64decode, b64encode

# TOKEN = 'c14a8ebace3b5b7d80d0849109a4138d0114c48b'
JWT_TOKEN = (
    'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6ImRlbW8iLCJleHAiOjE2MTU2MDcwOTksImVtYWlsIjoiIiwib3JpZ19pYXQiOjE2MTU2MDY3OTl9.M-sFcJZXT5WfK4llQmgt9TwQILoM16ODN-ORSe9FpBY')
headers = {
    # 'Authorization': f'Token {JWT_TOKEN}' # Token 인증
    'Authorization': f'JWT {JWT_TOKEN}'  # JWT Token 인증
}

# print(b64decode(
#     'eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6ImRlbW8iLCJleHAiOjE2MTU2MDQzMzgsImVtYWlsIjoiIiwib3JpZ19pYXQiOjE2MTU2MDQwMzh9'))
# print(b64encode(b'{"user_id":4,"username":"demo","exp":1615603844,"email":"","orig_iat":1615603544}'))

req = requests.get('http://localhost:8000/post/1/', headers=headers)

print(req.json())
