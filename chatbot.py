import random
import datetime

responses = {
    "fever": [
        "You may have a fever. Stay hydrated and take rest.",
        "Monitor your temperature regularly and drink fluids."
    ],
    "cough": [
        "It might be a cold. Drink warm water and avoid cold drinks.",
        "Try steam inhalation and stay warm."
    ],
    "headache": [
        "Take rest and avoid screen exposure.",
        "Stay hydrated and relax."
    ],
    "cold": [
        "Common cold detected. Drink warm fluids and rest.",
        "Take vitamin C and stay warm."
    ]
}

def get_response(user_input):
    for symptom in responses:
        if symptom in user_input:
            return random.choice(responses[symptom])
    return "I recommend consulting a doctor for proper diagnosis."

def chatbot():
    print("🤖 AI Health Chatbot")
    print("Type 'exit' to quit\n")

    name = input("Enter your name: ")
    print(f"Hello {name}! How can I help you today?\n")

    while True:
        user = input("You: ").lower()

        if user == "exit":
            print("Chatbot: Take care! Stay healthy 👋")
            break

        elif "time" in user:
            print("Chatbot:", datetime.datetime.now().strftime("%H:%M:%S"))

        elif "date" in user:
            print("Chatbot:", datetime.date.today())

        else:
            response = get_response(user)
            print("Chatbot:", response)

import random
import datetime

responses = {
    "fever": [
        "You may have a fever. Stay hydrated and take rest.",
        "Monitor your temperature regularly and drink fluids."
    ],
    "cough": [
        "It might be a cold. Drink warm water and avoid cold drinks.",
        "Try steam inhalation and stay warm."
    ],
    "headache": [
        "Take rest and avoid screen exposure.",
        "Stay hydrated and relax."
    ],
    "cold": [
        "Common cold detected. Drink warm fluids and rest.",
        "Take vitamin C and stay warm."
    ]
}

def get_response(user_input):
    for symptom in responses:
        if symptom in user_input:
            return random.choice(responses[symptom])
    return "I recommend consulting a doctor for proper diagnosis."

def chatbot():
    print("🤖 AI Health Chatbot")
    print("Type 'exit' to quit\n")

    name = input("Enter your name: ")
    print(f"Hello {name}! How can I help you today?\n")

    while True:
        user = input("You: ").lower()

        if user == "exit":
            print("Chatbot: Take care! Stay healthy 👋")
            break

        elif "time" in user:
            print("Chatbot:", datetime.datetime.now().strftime("%H:%M:%S"))

        elif "date" in user:
            print("Chatbot:", datetime.date.today())

        else:
            response = get_response(user)
            print("Chatbot:", response)

chatbot()
