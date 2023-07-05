import discord
from app.gpt import gpt_response

class BotClient(discord.Client):
  async def on_ready(self):
    print(f'We have logged in as {self.user}')

  async def on_message(self, message):
    if message.author == self.user:
      return

    if message.content.startswith('/ask'):
      question = message.content[4:]
      if len(question) == 0:
        await message.channel.send('Please feel free to ask!')
      else:
        response = gpt_response(question)
        await message.channel.send(response)
