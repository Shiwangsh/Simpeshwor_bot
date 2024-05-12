import os
from dotenv import load_dotenv
from typing import Final 
from openai import OpenAI
from g4f.client import Client

# from g4f.client import Client
from g4f.Provider import BingCreateImages, OpenaiChat, Gemini

client = Client(provider=OpenaiChat, image_provider=Gemini)
# load_dotenv()


def  get_response(user_input: str) -> str:
    
    system_message = {
        "role": "system",
        "content": "You are a helpful assistant."
    }
    # Define the user message
    user_message = {
        "role": "user",
        "content": user_input
    }
    # # Combine the system and user messages
    messages = [system_message, user_message]
    # # Generate a response from ChatGPT
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
    except Exception as e:
        print(f'send message error{e}')

 
    # Return the content of the generated response
    return(response.choices[0].message.content)

