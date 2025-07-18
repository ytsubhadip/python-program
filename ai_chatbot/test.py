import google.generativeai as genai

# 🔐 Paste your free API key here
genai.configure(api_key="AIzaSyDxbT9YKZ46UUAq6zljAp5Iza128bItZhI")

# ✅ Use the Gemini 1.5 Pro model (supports memory too)
model = genai.GenerativeModel("gemini-1.5-pro")

while True:
    user_input = input("You: ")
    
    if user_input.lower() in ["exit", "quit"]:
        print("Jarvis: Goodbye!")
        break

    response = model.generate_content(user_input)
    print("Jarvis:", response.text)
