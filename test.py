
import json
import requests
from flask import Flask, request,jsonify

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def msg_send():
    try:
        # 요청 데이터 받기
        ans = '{"writer": "zeun", "timestamp": "06/09 15:43", "content": "h2hh2"}'
        json_ans = json.loads('{"writer": "zeun", "timestamp": "06/09 15:43", "content": "h2hh2"}')

        # ui 서버에 api 통해 json_ans 전달
        url = 'http://localhost:8989/msg_send'

        # 요청 데이터
        data = json_ans

        # API 요청 보내기
        response = requests.post(url, json=data)


        # 응답 처리
        if response.status_code == 200:
            # API 응답을 이용한 작업 수행
            
            
            print("#######", response)
        else:
            print("실패")

        return jsonify({'message': 'ok'}), 200
    except Exception as e:
        # 예외 처리
        print(e)
        return jsonify({'message': 'Error', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0')