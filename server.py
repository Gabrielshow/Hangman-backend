from flask import Flask, request, jsonify
from flask_cors import CORS
import Hangman

app = Flask(__name__)
CORS(app)

# Initialize the Hangman game instance
hangman_game = Hangman.Hangman()

@app.route('/start', methods=['GET'])
def start_game():
    """Start a new game."""
    hangman_game.start_new_game()  # Reset the game state
    return jsonify({
        'display': hangman_game.get_display()['display'],
        'lives': hangman_game.lives,
        'end_of_game': hangman_game.end_of_game
    })

@app.route('/guess', methods=['POST'])
def guess_letter():
    data = request.get_json()  # Get JSON data from client
    letter = data.get('letter')  # Get the letter to guess

    if not letter:
        return jsonify({'error': 'No letter provided'}), 400

    result = hangman_game.guess(letter)  # Call the guess method

    if result.get('error'):
        return jsonify(result), 400

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
