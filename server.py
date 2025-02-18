from flask import Flask, request, jsonify
from flask_cors import CORS
import Hangman

app = Flask(__name__)
CORS(app)

# Initialize the Hangman game instance
hangman_game = Hangman.Hangman()

@app.route('/start', methods=['GET'])
def start_game():
    # Start the game and send the current display and lives
    return jsonify({
        'display': hangman_game.get_display(),
        'lives': hangman_game.lives
    })

@app.route('/guess', methods=['POST'])
def guess_letter():
    data = request.get_json()  # Get JSON data from client
    letter = data.get('letter')  # Get the letter to guess

    if not letter:
        return jsonify({'error': 'No letter provided'}), 400

    result = hangman_game.guess(letter)  # Call the guess method
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
