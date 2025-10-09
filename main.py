import random
import re

chatbot_responses = {
    # Greetings
    "greeting": {
        "patterns": [
            r"hello|hi|hey|good morning|good afternoon|good evening",
            r"how are you|how's it going|what's up"
        ],
        "responses": [
            "Hello! How can I help you today?",
            "Hi there! What's on your mind?",
            "Hey! Nice to see you. How can I assist?",
            "Good day! I'm here to help with any questions."
        ]
    },
    
    # Farewells
    "goodbye": {
        "patterns": [
            r"bye|goodbye|see you|farewell|exit|quit"
        ],
        "responses": [
            "Goodbye! Have a great day!",
            "See you later! Take care!",
            "Farewell! Feel free to come back anytime.",
            "Thanks for chatting! Bye!"
        ]
    },
    
    # Name inquiries
    "name": {
        "patterns": [
            r"what's your name|who are you|your name"
        ],
        "responses": [
            "I'm Grok, your helpful AI assistant!",
            "You can call me Grok. How can I help?",
            "I'm an AI chatbot named Grok, built to assist you!"
        ]
    },
    
    # Help requests
    "help": {
        "patterns": [
            r"help|assist|what can you do"
        ],
        "responses": [
            "I can help with general questions, provide information, and chat about various topics. Just ask me anything!",
            "I'm here to answer questions, provide explanations, and help with various tasks. What do you need?",
            "I can assist with information, explanations, and casual conversation. Let me know what you're curious about!"
        ]
    },
    
    # Time/Weather (placeholder patterns)
    "time_weather": {
        "patterns": [
            r"what time|what's the time|current time",
            r"weather|how's the weather"
        ],
        "responses": [
            "I don't have access to real-time data, but you can check your device's clock or a weather app!",
            "For current time and weather, please check a reliable source like your phone or weather website.",
            "I'm not connected to live data services, but I'd be happy to help with other questions!"
        ]
    },
    
    # General questions
    "general": {
        "patterns": [
            r"what is|define|explain|tell me about"
        ],
        "responses": [
            "That's an interesting question! Could you be more specific about what you'd like to know?",
            "I'd be happy to explain. Please provide more details about the topic.",
            "Great question! What specifically would you like to learn about?"
        ]
    },
    
    # Jokes/Fun
    "jokes": {
        "patterns": [
            r"joke|funny|tell me a joke|humor"
        ],
        "responses": [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "What do you call fake spaghetti? An impasta!",
            "Why don't eggs tell jokes? They'd crack each other up!"
        ]
    }

    
    
    
}

def bot_response(prompt):
    prompt = prompt.lower().strip()

    for category,data in chatbot_responses.items():
        patterns = data["patterns"]
        responses = data["responses"]
        for pattern in patterns:
            if re.search(pattern,prompt):
                print(random.choice(responses))
                return
    
        

    print("I don't have a response for that yet. Try asking about greetings, help, or tell me a joke!")


  
exit_ai = 0

while exit_ai==0:
    print("Enter 1 to leave the AI")
    prompt = input("Enter a prompt for the AI: ")
    if prompt=="1":
        exit_ai = 1
    
    else:
        bot_response(prompt)



        

    
    