import re

def chatbot():
    print("Hello! I'm a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input in ['bye', 'exit', 'quit']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif re.search(r'hii', user_input):
            print("Chatbot: Hello! How can I help you today?")
        elif re.search(r'how are you', user_input):
            print("Chatbot: I'm just a bot, but I'm doing great! How about you?")
        elif re.search(r'your name', user_input):
            print("Chatbot: I'm a simple chatbot created to assist you!")
        elif re.search(r'can you answer me', user_input):
            print("Chatbot: Sure! I can answer simple questions. Try asking about my name or how I am doing.")
        else:
            print("Chatbot: Sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()
