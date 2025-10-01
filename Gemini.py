import google.generativeai as genai

API_KEY = ""   
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat()
print("hey i am gemini how can i help you. Type exit to quit")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Gemini: Goodbye!")
        break
    response = chat.send_message(user_input)
    print("Gemini:", response.text)
