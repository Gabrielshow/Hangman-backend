
# Hangman Game (React + Flask)

This project is a simple yet engaging Hangman game where users can guess letters to uncover a hidden word. The backend is powered by Flask and handles all the game logic, while the frontend is built using React and TypeScript for an interactive user experience.


Backend
Built using Flask for handling game logic and RESTful API endpoints.
CORS enabled for smooth communication with the frontend.
Frontend
Built using React and TypeScript for dynamic rendering and state management.
User-friendly interface with input fields, guess button, and visual feedback on guesses.
Toast notifications to show win/loss messages and game status.
Installation & Setup
Clone this repository to your local machine.



## Features

- Game Flow: Users are prompted to guess letters, with the game progressing based on the number of lives left.
- Game End Handling: If the user runs out of lives, they lose, and if they guess all the letters correctly, they win.
- New Game Option: Users can start a fresh game by clicking the "New Game" button.
- Responsive Interface: Built with React and styled for a smooth user experience.



## Run Locally

Clone the project

```bash
  git clone https://github.com/Gabrielshow/Hangman-frontend.git
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run dev
```

For the backend, clone
```bash
  git clone https://github.com/Gabrielshow/Hangman-backend.git
```
 and then run: 
 ```bash
 pip install -r requirements.txt
```

Start the backend server with
```bash
 python server.py.
```
Open your browser and enjoy the game!

