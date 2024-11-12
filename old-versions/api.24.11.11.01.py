# API version

from flask import Flask, request, jsonify
import random
import re

app = Flask(__name__)

# Chatbot functions and logic
def generate_response(question, name="Guest", time_of_day="day", food_item=None, drink_item=None):
    question_answers = {
        "hello": [
            f"Hello, {name}! Good {time_of_day}!",
            f"Hi there, {name}! How's your {time_of_day} going?",
            f"Hey {name}, what's up? Good {time_of_day}!"
        ],
        "how are you": [
            f"I'm doing well, {name}! How about you?",
            f"I'm great, {name}, thanks for asking! How are you?",
            f"I'm feeling good, {name}! How's everything on your side?"
        ],
        "bye": [
            f"Goodbye, {name}! Have a great day!",
            f"See you later, {name}! Take care!",
            f"Bye for now, {name}! Hope to chat again soon!"
        ],
        "thank you": [
            f"You're welcome, {name}! Let me know if you need anything else.",
            f"No problem, {name}! I'm happy to help.",
            f"Anytime, {name}! Feel free to reach out again!"
        ]
    }
    
    responses = []
    for keyword, answers in question_answers.items():
        if keyword.lower() in question.lower():
            responses.append(random.choice(answers))
    
    if food_item:
        responses.append(f"I see you're interested in ordering a {food_item}. Would you like to add anything else?")
    if drink_item:
        responses.append(f"How about a refreshing {drink_item} to go with your meal?")
    
    if not responses:
        responses.append(f"Sorry, I don't quite understand '{question}'. Can you rephrase?")
    
    return " ".join(responses)


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()

    # Extract parameters from JSON input, with defaults
    question = data.get("question", "")
    name = data.get("name", "Guest")
    food_item = data.get("food_item")
    drink_item = data.get("drink_item")
    
    # Check if user is providing a name in the input text
    if "my name is" in question.lower():
        match = re.search(r"my name is ([a-zA-Z]+)", question, re.IGNORECASE)
        if match:
            name = match.group(1)

    # Detect intents for food and drinks
    if "chicken" in question.lower():
        food_item = "chicken"
    if "cold drink" in question.lower() or "soft drink" in question.lower():
        drink_item = "cold drink"
    
    # Generate response
    response_text = generate_response(question, name=name, time_of_day="morning", food_item=food_item, drink_item=drink_item)
    
    # Return JSON response
    return jsonify({"response": response_text})


if __name__ == '__main__':
    app.run(debug=True)
