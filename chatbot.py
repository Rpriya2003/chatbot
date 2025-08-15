# Simple Chatbot using if-else

print("Hello! I am ChatBot 🤖. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Bot: Hi there! How can I help you?")
    elif user_input == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")
    elif user_input == "what is your name":
        print("Bot: I am your friendly chatbot!")
    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day ")
        break
    else:
        print("Bot: Sorry, I don't understand that.")
