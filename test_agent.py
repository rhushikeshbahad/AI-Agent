# import ollama

# def chat_with_agent():
#     print("=== Ollama Local Agent Test ===")
#     model = 'llama3.2'

#     print("\n1. Testing greeting...")
#     response = ollama.chat(
#         model=model,
#         messages=[{'role': 'user', 'content': 'Hi!'}]
#     )
#     print("Agent:", response['message']['content'])

#     print("\n2. Testing general knowledge...")
#     response = ollama.chat(
#         model=model,
#         messages=[{'role': 'user', 'content': 'What is the capital of India?'}]
#     )
#     print("Agent:", response['message']['content'])

#     print("\n3. Testing science question...")
#     response = ollama.chat(
#         model=model,
#         messages=[{'role': 'user', 'content': 'Why is the sky blue?'}]
#     )
#     print("Agent:", response['message']['content'])


# if __name__ == "__main__":
#     chat_with_agent()





import ollama

def chat_with_agent():
    print("=== Ollama Local AI Agent ===")
    print("Type 'exit' to quit.\n")

    model = "llama3.2"
    conversation = []

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Agent: Goodbye 👋")
            break

        conversation.append({
            "role": "user",
            "content": user_input
        })

        response = ollama.chat(
            model=model,
            messages=conversation
        )

        reply = response["message"]["content"]
        print("Agent:", reply)

        conversation.append({
            "role": "assistant",
            "content": reply
        })


if __name__ == "__main__":
    chat_with_agent()
