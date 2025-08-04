from openai import OpenAI

# Initialize Groq-compatible OpenAI client
client = OpenAI(
    api_key="",  # Replace with your Groq API key
    base_url="https://api.groq.com/openai/v1"
)

print("📚 Homework Help Bot is ready! Type your academic questions or type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Bot: Goodbye! Study well! 📘")
        break

    response = client.chat.completions.create(
        model="llama3-70b-8192",  # Groq's LLaMA 3 model
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful homework assistant. "
                    "Help students understand academic topics, explain concepts clearly, "
                    "and provide simple solutions to homework questions. "
                    "Stick to educational content only."
                )
            },
            {"role": "user", "content": user_input}
        ]
    )

    print("Bot:", response.choices[0].message.content)

