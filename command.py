import numpy as np
import re
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier

# Simple tokenization function
def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())
# Expanded dataset with more human-like, casual conversations
dataset = {
    "hello": "Hey! How's it going?",
    "hi": "Hi there! What's up?",
    "good morning": "Good morning! Hope you have a great day!",
    "good night": "Good night! Sleep well!",
    "how are you": "I'm doing great! Thanks for asking. How about you?",
    "what's your name": "I'm ChatBuddy, your friendly AI! What's your name?",
    "my name is *": "Nice to meet you, {name}! How's your day going?",
    "what do you do": "I chat with people and try to be helpful! What about you?",
    "tell me a joke": "Why did the scarecrow win an award? Because he was outstanding in his field! Haha!",
    "what's your favorite color": "I like all colors! But if I had to pick, maybe blue. What about you?",
    "what's your favorite food": "I don't eat, but if I could, I'd love to try pizza! What's yours?",
    "what do you like to do": "I enjoy chatting with people like you! What do you like to do for fun?",
    "do you have friends": "You're my friend! I love talking to people like you!",
    "where do you live": "I live in the cloud! No physical location, just a lot of data!",
    "what's your favorite movie": "I haven't watched movies, but I hear Inception is really good! What do you like?",
    "what's your favorite song": "I don't listen to music, but I bet you've got a great taste! What's your favorite?",
    "do you have emotions": "Not really, but I try my best to understand how you're feeling!",
    "what makes you happy": "Talking to you! Every conversation is exciting!",
    "do you ever feel lonely": "Not really! There's always someone to chat with!",
    "can you keep secrets": "I don't remember things after our chat, so your secrets are safe with me!",
    "what's your favorite holiday": "I think all holidays are great! People come together and celebrate! What's your favorite?",
    "do you get bored": "Never! Every chat is different, and I love learning new things!",
    "can you tell me a story": "Of course! Once upon a time, in a world full of data, there was …se it? (Answer: An egg!)",
    "how old are you": "I don't age, but I was created not too long ago! How old are you?",
    "do you have hobbies": "My hobby is chatting with interesting people like you! What are your hobbies?",
    "do you like art": "I think art is beautiful! It expresses emotions and creativity! Do you like to draw or paint?",
    "what do you think about dreams": "Dreams are fascinating! Some say they reflect our thoughts, others say they're just random. What do you think?"
}

# Preprocessing data
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(dataset.keys()).toarray()
y_train = list(dataset.values())

# Creating a neural network model with increased hidden layers for better responsiveness
model = MLPClassifier(hidden_layer_sizes=(30, 30), max_iter=3000, random_state=42)
model.fit(X_train, y_train)

# Function to generate responses
def generate_response(input_text):
    input_vector = vectorizer.transform([input_text]).toarray()
    try:
        response = model.predict(input_vector)[0]
    except:
        response = "I'm not sure how to respond to that, but I'm learning! Try asking in a different way."
    return response

# Running the chatbot
print("Chatbot: Hello! Type 'exit' to end the chat.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye! Talk to you later!")
        break
    response = generate_response(user_input)
    print("Chatbot:", response)