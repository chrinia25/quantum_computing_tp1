from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

# 매트릭스 곱셈을 처리할 엔드포인트 설정
@app.route('/matrix_multiply', methods=['POST'])
def matrix_multiply():
    try:
        # 요청에서 두 개의 매트릭스 받기
        data = request.get_json()
        matrix_a = np.array(data['matrix_a'])
        matrix_b = np.array(data['matrix_b'])
        
        # 매트릭스 곱셈 수행을 여기서 진행
        result = np.dot(matrix_a, matrix_b)
        
        # 결과를 json으로 리턴
        return jsonify({'result': result.tolist()}), 200
    
    # 에러가 나면 json으로 에러 리턴
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    # 서버 실행
    app.run(debug=True)
