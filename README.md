# Multiplayer Ping Pong Game with Dynamic Obstacles

This project is a real-time multiplayer ping pong game where two players compete across different browser tabs. The game includes dynamic obstacles that affect gameplay, creating an engaging experience.

## Features

- Real-time multiplayer gameplay across browser tabs.
- Keyboard-controlled paddles for both players.
- Dynamic obstacles:
  - Randomly positioned at game start.
  - Cause the ball to bounce on collision.
- Scoring system to track each player's performance.
- Backend-powered state management with WebSocket communication.

---

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/RahulVijaySingh/Ping-Pong.git

   ```

### Set Up Backend

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the backend server: python server.py

## How to Run the Game

Follow these steps to play the Multiplayer Ping Pong Game:

1. **Start the Backend Server**

   - Ensure the backend server is running as described in the setup instructions.

2. **Open the Frontend**

   - Open the `index.html` file in two separate browser tabs. These will serve as the game interfaces for Player 1 and Player 2.

3. **Control Paddles**

   - Use the following keys to control the paddles:
     - **Player 1:**
       - `W` key to move the paddle up.
       - `S` key to move the paddle down.
     - **Player 2:**
       - `Up Arrow` key to move the paddle up.
       - `Down Arrow` key to move the paddle down.

4. **Scoring**

   - Score points by making the ball go out of bounds on your opponent's side.

5. **Dynamic Obstacles**
   - Watch how the ball interacts with the two dynamic obstacles that bounce the ball on collision.

Enjoy the game!
