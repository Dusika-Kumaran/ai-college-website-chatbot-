# Import required classes and functions from the Flask library
# Flask  → used to create the web application
# request → used to read data sent by the user
# jsonify → used to send JSON responses back to the user
from flask import Flask, request, jsonify


# Create a Flask application instance
# __name__ helps Flask know where this file is located
app = Flask(__name__)


# Define a route (API endpoint) called "/chat"
# This route will accept POST requests
@app.route("/chat", methods=["POST"])
def chat():
    
    # Get the user's message from the JSON request body
    # Example input: { "message": "Hi" }
    user_message = request.json.get("message")

    # Send a JSON response back to the user
    # This is the chatbot's reply
    return jsonify({
        "reply": "Hello! I am your college chatbot. How can I help you?"
    })


# This condition checks whether this file is being run directly
# If yes, start the Flask development server
if __name__ == "__main__":
    
    # Run the Flask app in debug mode
    # Debug mode helps by showing errors clearly during development
    app.run(debug=True)
