from g4f.client import Client
from g4f.Provider import HuggingChat

client = Client(
    provider = HuggingChat
)

def generate(prompt):
    chat_completion = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-70B-Instruct",
        messages=[{"role": "user", "content": prompt}],
    )

    print(chat_completion.choices[0].message.content or "")

generate('Hello! How are you doing?')
