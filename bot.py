import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.threads = True
bot = commands.Bot(command_prefix='!', intents=intents)

SPECIFIC_CHANNEL_ID = 1268619281483173980

@bot.event
async def on_ready():
    activity = discord.Game(name="hosting provided by KeenWa Corp. discord.py running.")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f'{bot.user} has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

@bot.event
async def on_message(message):
    if message.channel.id == SPECIFIC_CHANNEL_ID and not message.author.bot:
        try:
            thread = await message.create_thread(
                name=f"Thread for {message.author.name}",
                auto_archive_duration=1440
            )
            await thread.send(f"Thread created for {message.author.mention}'s message!")
            print(f"Created thread {thread.name} for message {message.id}")
        except Exception as e:
            print(f"Error creating thread: {e}")

    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

if __name__ == "__main__":
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        raise ValueError("No token found. Make sure DISCORD_TOKEN is set in your environment variables.")
    bot.run(token)
