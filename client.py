import requests

# 서버로 보낼 매트릭스
matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]

# 서버 URL
url = 'http://localhost:5000/matrix_multiply'

# POST 요청 보내기
response = requests.post(url, json={'matrix_a': matrix_a, 'matrix_b': matrix_b})

# 응답 출력
if response.status_code == 200:
    print('Result:', response.json()['result'])
else:
    print('Error:', response.json()['error'])
