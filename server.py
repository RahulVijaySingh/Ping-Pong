from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Initial game state
game_state = {
    'ball': {'x': 400, 'y': 300, 'dx': 2, 'dy': 2},
    'paddle1': {'y': 250},
    'paddle2': {'y': 250},
    'score': {'player1': 0, 'player2': 0},
    'obstacles': [
        {'x': random.randint(100, 700), 'y': random.randint(100, 500), 'size': 50},
        {'x': random.randint(100, 700), 'y': random.randint(100, 500), 'size': 50}
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('move_paddle')
def move_paddle(data):
    player = data['player']
    direction = data['direction']
    if player == 1:
        game_state['paddle1']['y'] += 20 if direction == 'down' else -20
    else:
        game_state['paddle2']['y'] += 20 if direction == 'down' else -20
    emit('update', game_state, broadcast=True)

@socketio.on('update_ball')
def update_ball():
    ball = game_state['ball']
    ball['x'] += ball['dx']
    ball['y'] += ball['dy']
    
    # Bounce off top and bottom
    if ball['y'] <= 0 or ball['y'] >= 600:
        ball['dy'] *= -1
    
    # Paddle collisions
    if (ball['x'] <= 30 and game_state['paddle1']['y'] <= ball['y'] <= game_state['paddle1']['y'] + 100) or \
       (ball['x'] >= 770 and game_state['paddle2']['y'] <= ball['y'] <= game_state['paddle2']['y'] + 100):
        ball['dx'] *= -1
    
    # Score update
    if ball['x'] <= 0:
        game_state['score']['player2'] += 1
        reset_ball()
    elif ball['x'] >= 800:
        game_state['score']['player1'] += 1
        reset_ball()
    
    # Obstacle collisions
    for obs in game_state['obstacles']:
        if obs['x'] <= ball['x'] <= obs['x'] + obs['size'] and obs['y'] <= ball['y'] <= obs['y'] + obs['size']:
            ball['dx'] *= -1
            ball['dy'] *= -1
    
    emit('update', game_state, broadcast=True)

def reset_ball():
    game_state['ball']['x'] = 400
    game_state['ball']['y'] = 300
    game_state['ball']['dx'] *= random.choice([-1, 1])
    game_state['ball']['dy'] *= random.choice([-1, 1])

if __name__ == '__main__':
    socketio.run(app, debug=True)
