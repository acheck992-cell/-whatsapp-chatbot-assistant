def whatsapp_chatbot():
    print("--- WhatsApp Chatbot Assistant Initialized ---")
    print("Type 'exit' to end the chat.\n")
    
    responses = {
        "hello": "Hello! Welcome to our service. How can I help you today?",
        "hi": "Hi there! How can I assist you?",
        "help": "I can help you with product info, pricing, and support. What do you need?",
        "pricing": "Our plans start at $10/month. Would you like more details?",
        "bye": "Goodbye! Have a wonderful day ahead!"
    }
    
    while True:
        user_input = input("User: ").strip().lower()
        if user_input == 'exit':
            print("Chatbot: Goodbye! Thanks for chatting.")
            break
        
        found = False
        for key in responses:
            if key in user_input:
                print(f"Chatbot: {responses[key]}")
                found = True
                break
        
        if not found:
            print("Chatbot: I'm sorry, I didn't understand that. Type 'help' for assistance.")

if __name__ == "__main__":
    whatsapp_chatbot()
