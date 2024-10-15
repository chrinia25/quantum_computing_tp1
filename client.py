import requests
from quantum_simulator import *

#서버로 보낼 data json

# 서버 URL
url = 'http://localhost:5000/observe_circuit'

# POST 요청 보내기
response = requests.post(url, json="test.json")

# 응답 출력
if response.status_code == 200:
    print('Result:', response.json()['result'])
else:
    print('Error:', response.json()['error'])
