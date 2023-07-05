import os
import discord

from dotenv import load_dotenv

from app.bot import BotClient

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

if __name__ == '__main__':
  intents = discord.Intents.default()
  intents.message_content = True
  client = BotClient(intents=intents)
  client.run(DISCORD_TOKEN)