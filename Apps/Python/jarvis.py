import random

# Function to generate a response
def get_response(input_text):
    input_text = input_text.lower()
    
    if "hello" in input_text:
        return "Hello! How can I assist you today?"
    
    elif "how are you" in input_text:
        return "I'm just a computer program, so I don't have feelings, but I'm here to help you!"
    
    elif "time" in input_text:
        # Implement a way to get the current time here
        return "I'm sorry, I can't provide the current time in this simplified version."
    
    elif "joke" in input_text:
        return get_random_joke()
    
    elif "bye" in input_text:
        return "Goodbye! Have a great day."
    
    else:
        return "I'm not sure how to help with that. Please ask another question."

# Function to get a random joke
def get_random_joke():
    jokes = [
        "Why did the computer catch a cold? Because it had a bad Windows!",
        "Why don't programmers like nature? It has too many bugs!",
        "What do you call a programmer from Finland? Nerdic.",
        "Why did the programmer go broke? Because he used up all his cache!"
    ]
    return random.choice(jokes)

# Main loop
print("AI Jarvis Assistant: Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("AI Jarvis:", response)
