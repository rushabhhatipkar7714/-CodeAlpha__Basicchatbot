"""Task 4: Basic rule-based chatbot using if-elif, functions, loops, and input/output."""


def get_response(user_input):
    """Return a predefined reply for the given user input."""
    text = user_input.lower().strip()

    if text in ("hello", "hi", "hey"):
        return "Hi!"
    elif text == "how are you":
        return "I'm fine, thanks!"
    elif text == "what is your name":
        return "I'm a simple chatbot."
    elif text in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."


def chat():
    """Run the chat loop until the user says goodbye."""
    print("Chatbot: Hello! Type 'bye' to end the chat.")

    while True:
        user_input = input("You: ")
        reply = get_response(user_input)
        print("Chatbot:", reply)

        if reply == "Goodbye!":
            break


if __name__ == "__main__":
    chat()
