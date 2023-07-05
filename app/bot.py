import discord

class BotClient(discord.Client):
  async def on_ready(self):
    print(f'We have logged in as {self.user}')

  async def on_message(self, message):
    if message.author == self.user:
      return

    if message.content.startswith('/ask'):
      message_content = message.content[4:]
      if len(message_content) == 0:
        await message.channel.send('Please feel free to ask!')
      else:
        await message.channel.send(message_content)
