import random
import re

# Function to generate a personalized response based on user input and captured intents
def generate_response(question, name="Guest", time_of_day="day", food_item=None, drink_item=None):
    """ Generate a response based on the user's question, name, time of day, and any captured food/drink intent. """
    
    # Dictionary of question-answer pairs with multiple keywords for each intent
    question_answers = {
        ("hello", "hi", "hey"): [
            f"Hello, {name}! Good {time_of_day}!",
            f"Hi there, {name}! How's your {time_of_day} going?",
            f"Hey {name}, what's up? Good {time_of_day}!"
        ],
        ("how are you", "how do you do", "how’s it going"): [
            f"I'm doing well, {name}! How about you?",
            f"I'm great, {name}, thanks for asking! How are you?",
            f"I'm feeling good, {name}! How's everything on your side?"
        ],
        ("bye", "goodbye", "see you"): [
            f"Goodbye, {name}! Have a great day!",
            f"See you later, {name}! Take care!",
            f"Bye for now, {name}! Hope to chat again soon!"
        ],
        ("thank you", "thanks", "much appreciated"): [
            f"You're welcome, {name}! Let me know if you need anything else.",
            f"No problem, {name}! I'm happy to help.",
            f"Anytime, {name}! Feel free to reach out again!"
        ]
    }
    
    # Initialize the list of responses
    responses = []

    # Check for the presence of known keywords and generate responses
    for keywords, answers in question_answers.items():
        if any(keyword.lower() in question.lower() for keyword in keywords):
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


def chat():
    """ Main function to run the chatbot in the terminal interactively. """
    
    # Initial variables for user name and preferences
    name = "Guest"
    food_item = None
    drink_item = None
    time_of_day = "day"  # Customize this as needed

    print("Chatbot: Hi! Type 'quit' anytime to end the conversation.")

    # Start an interactive conversation
    while True:
        question = input("You: ")

        # End the conversation if the user types 'quit'
        if question.lower() == "quit":
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Check if user provides their name
        if "my name is" in question.lower():
            match = re.search(r"my name is ([a-zA-Z]+)", question, re.IGNORECASE)
            if match:
                name = match.group(1)
                print(f"Chatbot: Nice to meet you, {name}!")

        # Detect food and drink intents
        if "chicken" in question.lower():
            food_item = "chicken"
        if "cold drink" in question.lower() or "soft drink" in question.lower():
            drink_item = "cold drink"
        
        # Generate and display the chatbot's response
        response_text = generate_response(question, name=name, time_of_day=time_of_day, food_item=food_item, drink_item=drink_item)
        print(f"Chatbot: {response_text}")

# Run the chatbot
if __name__ == "__main__":
    chat()
