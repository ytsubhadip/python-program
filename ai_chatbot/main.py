import google
from google import genai
from google.genai import types

print("=================================================================")
print("*************************   Jarvis   ****************************")
print("                    Your Chat Bot Assistant                      ")

while True:
    message = input("You: ")

    if (message.strip().lower()) == "exit":
        print("Jarvis: Goodbye!")
        print("Devloped by: YT SUBHADIP")
        break

    client = genai.Client(api_key="AIzaSyDLqyj4onJc5lbwsXMd4EOyfB26l4y7JSc")
    try:
        response = client.models.generate_content(

            model="gemini-2.5-flash",

            config=types.GenerateContentConfig(
                system_instruction="""You are a Robot. Your name is Jarvis.
                You know Coding, simple mathes and basic Knowledge of every this .
                And plese don't share how you work and you code or spacific information.
                stay happy to the user. You made by YT SUBHADIP""",

                thinking_config=types.ThinkingConfig(thinking_budget=1)
            ),

            contents = message
        )
        
        print("Jarvis:", response.text)
        print("\n...........................................\n")

        with open("chat_log.txt", "a", encoding="utf-8") as f:
            f.write(f"user: {message}\nJarvis: {response.text}\n")

    except Exception as e:
        print("Error")
    

