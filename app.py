from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite///:base.db'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('connect')
def handle_connect():
    print('User join')


@socketio.on('message')
def take_mess(message):
    print("Taken message:" + message)
    emit('message', message, broadcast = True)


if __name__ == '__main__':
    socketio.run(app, allow_unsafe_werkzeug=True)
