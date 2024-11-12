import random
import re

# Function to generate a personalized response based on user input and captured intents
def generate_response(question, name="Guest", time_of_day="day", food_item=None, drink_item=None):
    """
    Generate a response based on the user's question, name, time of day, and any captured food/drink intent.
    """
    
    # Dictionary of question-answer pairs with multiple possible responses
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
    
    # Initialize the list of responses
    responses = []
    
    # Check for the presence of known questions and generate responses
    for keyword, answers in question_answers.items():
        if keyword.lower() in question.lower():
            responses.append(random.choice(answers))
    
    # If food and drink items are detected, add relevant responses
    if food_item:
        responses.append(f"I see you're interested in ordering a {food_item}. Would you like to add anything else?")
    if drink_item:
        responses.append(f"How about a refreshing {drink_item} to go with your meal?")
    
    # If no recognized question is found, provide a default response
    if not responses:
        responses.append(f"Sorry, I don't quite understand '{question}'. Can you rephrase?")
    
    # Combine and return all responses
    return " ".join(responses)

# Main chat function to handle user interaction
def chat():
    print("Welcome to the chatbot! Type 'quit' to end the conversation.")
    
    name = "Guest"  # Default name value
    food_item = None
    drink_item = None
    
    while True:
        # Get user input
        user_input = input("\nYou: ").strip()
        
        # Exit condition if the user types 'quit'
        if user_input.lower() == "quit":
            print("Goodbye! Take care!")
            break
        
        # Detect user's name if they mention it
        if "my name is" in user_input.lower():
            match = re.search(r"my name is ([a-zA-Z]+)", user_input, re.IGNORECASE)
            if match:
                name = match.group(1)  # Capture the name
        
        # Detect food and drink items based on user input
        if "chicken" in user_input.lower():
            food_item = "chicken"
        if "cold drink" in user_input.lower() or "soft drink" in user_input.lower():
            drink_item = "cold drink"
        
        # Get and print the chatbot response
        response = generate_response(user_input, name=name, time_of_day="morning", food_item=food_item, drink_item=drink_item)
        print("Bot:", response)

# Start the chat
chat()
