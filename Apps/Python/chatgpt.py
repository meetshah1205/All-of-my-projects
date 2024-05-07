
responses = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm just a computer program, so I don't have feelings, but thanks for asking!",
    "goodbye": "Goodbye! Have a great day.",
    "is cod mobile the best game ever": "Ofcourse is it even a question, BRUH",
    "is kathan an idiot": "Hey, Don't say that again, Calling Kathan an idiot is an insult. OF IDIOTS",
    "eg. for -6g net": "VANSH",
    "do you ever lie": "A.I. can't lie.",
}

# Main conversation loop
while True:
    user_input = input("You: ").lower()
    
    if user_input == "exit":
        break
    
    # Check if there's a predefined response for the user's input
    response = responses.get(user_input, "I'm not sure how to respond to that.")
    
    print("AI: " + response)
