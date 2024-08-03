import os
from openai import OpenAI
client = OpenAI(
api_key=os.environ.get(".env"))
def send_message(message_log):
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
        {"role": "user", "content": message_log}
        ]  
    )

    # If no response with text is found, return the first response's content (which may be empty)
    return completion.choices[0].message.content

# Main function that runs the chatbot
def main():
    # Initialize the conversation history with a message from the chatbot
    message_log = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    # Set a flag to keep track of whether this is the first request in the conversation
    first_request = True
    user_input = input("You: ")
    response = send_message(user_input)
    print(f"AI assistant: {response}")

if __name__ == "__main__":
    main()