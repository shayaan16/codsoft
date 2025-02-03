def chatbot_response(user_input):
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a great day!",
        "what color is the sky": "The color of the sky is blue",
        "what is your favorite color": "I don't have a favorite color, but I think blue is nice!",
    "can you help me": "Of course! What do you need help with?",
    "what is AI": "AI stands for Artificial Intelligence, the simulation of human intelligence in machines.",
    "who created you": "I was created by Shayaan!",
    "what is the weather like": "I can't check the weather, but I hope it's nice!",
    "tell me a joke": "Why don't skeletons fight each other? They don't have the guts!",
    "what is your favorite food": "I don't eat, but I imagine pizza would be great!",
    "where are you from": "I'm from the world of code, created by you!",
    "can you play games": "I can't play games, but I can help you with them!",
    "what is the time": "I can't check the time, but you can!",
    "do you like music": "I can't listen to music, but I know many good songs!",
    "what is your age": "I don't age, I'm always here to help!",
    "are you a robot": "I'm not a robot, just a chatbot!",
    "can you learn new things": "I can process new information, but I don't learn the way humans do.",
    "do you have a body": "No, I exist only as code!",
    "can you speak other languages": "Yes, I can understand and respond in multiple languages!",
    "what do you do": "I help answer your questions and assist with tasks.",
    "are you always on": "Yes, I'm always available to chat!",
    "what is your purpose": "My purpose is to assist you with information and tasks.",
    "can you tell me a fun fact": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient tombs!",
        "your name": "I'm a simple chatbot created by Shayaan!"
    }

    user_input = user_input.lower()
    return responses.get(user_input, "I'm sorry, I don't understand.")

# Running the chatbot in a loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)