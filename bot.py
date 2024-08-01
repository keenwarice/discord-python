import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up the bot
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True  # Required for receiving guild (server) events
bot = commands.Bot(command_prefix='!', intents=intents)

SPECIFIC_CHANNEL_ID = 1268619281483173980  # Replace with your channel ID

@bot.event
async def on_ready():
    # Set the bot's status
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
        # Create a thread from the message
        thread = await message.create_thread(
            name=f"Thread for {message.author.name}",
            auto_archive_duration=1440  # Auto archive after 24 hours
        )
        await thread.send(f"Thread created for {message.author.mention}'s message!")

    # Ensure commands are processed
    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# Run the bot
if __name__ == "__main__":
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        raise ValueError("No token found. Make sure DISCORD_TOKEN is set in your environment variables.")
    bot.run(token)
