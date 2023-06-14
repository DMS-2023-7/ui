from chat import create_app, socketio
from flask import session, redirect,  request, jsonify
from flask_cors import CORS
import json


app = create_app(debug=True)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# api 통해 이미지 url 받아 socket에 emit해 채팅에 띄움
@app.route('/image', methods=['GET'])
def image():
    url = request.args.get('url')
    session['url']=url
    socketio.emit('image', {'image_url': session['url']}, broadcast=True, namespace='/test')
 
    return jsonify({'status': 'success'})

# api 통해 consumer에서 메시지 받아 socket emit
@app.route('/consumer', methods=['POST'])
def message_get():
    message = request.get_json()
    message = json.loads(message);
    print("#########################################",message)
    print("########### writer##############", message['writer'])
    # socketio.emit('text',{'writer': message['writer'], 'content':message['content'], 'timestamp':message['timestamp']}, broadcast=True, namespace='/chat')
    socketio.emit('text',message, broadcast=True, namespace='/chat')
    return jsonify({'status': 'success'})


if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0', debug=True)
