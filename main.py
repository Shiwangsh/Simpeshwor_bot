import asyncio
from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, Interaction
from discord.ext import commands
from responses import get_response, paint


#  Loading token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
# OPEN_AI_KEY: Final[str] = os.getenv('OPENAI_API_KEY')

# Bot setup
intents: Intents = Intents.default()
intents.message_content = True 
bot: Client = Client(intents = intents)
bot = commands.Bot(command_prefix='!', intents=intents)


# Startup
@bot.event
async def on_ready() -> None:
    print(f'{bot.user} is now running')



@bot.command(name="chat", description="Have a chat with ChatGPT")
async def chat(interaction: Interaction, *, message: str):
        if interaction.author == bot.user:
            return
        username: str = str(interaction.author)
        channel: str = str(interaction.channel)
        print(f'[{channel}] {username}: "{message}"')
        
        if not message:
            print('Empty message detected!')
            return
            
        if is_private := message[0]=='?':
            message = message[1:]
        try:
            response: str = get_response(message)
            print('This is the returned messgae:' + response)
            async with interaction.typing():
                await asyncio.sleep(1)
            await interaction.author.send(response) if is_private else await interaction.channel.send(response)

        except Exception as e:
            print(f'{e}')       
 

    
@bot.command(name="draw", description="Generate images using")
async def draw(interaction:Interaction, *, prompt: str): 
    if interaction.author == bot.user:
        return
    username: str = str(interaction.author)
    channel: str = str(interaction.channel)
    print(f'[{channel}] {username}: "{prompt}"') 
    try:
        response: str = paint(prompt)  
        await interaction.send(response)  
    except Exception as e:
        print(f'{e}')    

# Main entry point
def main()->None:
    bot.run(token=TOKEN)

if __name__ =='__main__':
    main()