from g4f.client import Client
from g4f.Provider import BingCreateImages, OpenaiChat, Gemini

client = Client(provider=OpenaiChat, image_provider=Gemini)


def  get_response(user_input: str) -> str:
 
    # Generate a response from ChatGPT
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[ {
        "role": "system",
        "content": "You are a helpful assistant."
    }, {
        "role": "user",
        "content": user_input
    }]
        )

        response_message = response.choices[0].message.content
        
        # Check if response is longer than 2000 characters
        if len(response_message) > 2000:
            chunk_size = 2000
            response_chunks = [response_message[i:i+chunk_size] for i in range(0, len(response_message), chunk_size)]
            for chunk in response_chunks:
                # Send each chunk as a separate response
                return(chunk)
        else:
            # Send the response directly if it's within the 2000 character limit
            return(response_message)
    except Exception as e:
        print(f'send message error{e}') 

    # Return the content of the generated response
    return(response.choices[0].message.content)

def paint(prompt: str) -> str:
    try:
        response = client.images.generate(
        model="gemini",
        prompt=prompt,
    )
    except Exception as e:
        print(f'send message error{e}')

    return response.data[0].url

