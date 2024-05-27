import re

# Define pairs of patterns and responses
pairs = [
    (
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ),
    (
        r"what is your name?",
        ["My name is ChatBot and I'm here to help you.",]
    ),
    (
        r"how are you?",
        ["I'm doing good. How about you?",]
    ),
    (
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind",]
    ),
    (
        r"(.*) thank you (.*)",
        ["You're welcome",]
    ),
    (
        r"exit",
        ["Bye, take care. See you soon!", "It was nice talking to you. Goodbye!"]
    ),
]

# Create a function to respond to user input
def respond(message):
    for pattern, responses in pairs:
        match = re.match(pattern, message.lower())
        if match:
            response = responses[0]  # Random response for now
            return response.replace("%1", match.group(1))

def chat():
    print("Hi, I'm ChatBot. How can I assist you today?")
    while True:
        user_input = input("> ")
        if user_input.lower() == 'exit':
            print("ChatBot: Bye, take care. See you soon!")
            break
        else:
            response = respond(user_input)
            if response:
                print("ChatBot:", response)
            else:
                print("ChatBot: I'm sorry, I don't understand that.")

if __name__ == "__main__":
    chat()
