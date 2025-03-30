from flask import Flask, request, jsonify
import numpy as np
import re
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
from flask_cors import CORS  # Allows frontend to access backend

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Tokenization function
def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

# Chatbot dataset
dataset = {
    "hello": "Hey! How's it going?",
    "hi": "Hi there! What's up?",
    "good morning": "Good morning! Hope you have a great day!",
    "how are you": "I'm doing great! How about you?",
    "what's your name": "I'm ChatBuddy, your AI assistant!",
}

# Train model
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(dataset.keys()).toarray()
y_train = list(dataset.values())

model = MLPClassifier(hidden_layer_sizes=(30, 30), max_iter=3000, random_state=42)
model.fit(X_train, y_train)

# Generate response function
def generate_response(input_text):
    input_vector = vectorizer.transform([input_text]).toarray()
    try:
        response = model.predict(input_vector)[0]
    except:
        response = "I'm not sure how to respond to that, but I'm learning!"
    return response

# API endpoint for chatbot
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    bot_response = generate_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
