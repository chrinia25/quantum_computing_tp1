from flask import Flask, request, jsonify
import numpy as np
from quantum_simulator import *

app = Flask(__name__)

# 매트릭스 곱셈을 처리할 엔드포인트 설정
@app.route('/observe_circuit', methods=['POST'])
def observe_circuit():
    try:
        # request body에서 get json을 통해 data json형태로 받아옴
        data = request.get_json()
        
        server_qc = quantum_circuit(data)
        
        # 결과를 json으로 리턴
        return jsonify({'result': server_qc.run()}), 200
    
    # 에러가 나면 json으로 에러 리턴
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    # 서버 실행
    app.run(debug=True)
