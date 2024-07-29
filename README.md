<img src="" alt="discord" style="width: 250px; height: auto;">

## 1-Click Deploy

Deploy on Railway

## Overview

This project is a simple Discord bot built using the discord.py library. It demonstrates the basic structure of a Discord bot and uses Poetry for dependency management. The bot responds to commands and can be easily extended with additional functionality.

## Key Features

- Minimal Discord bot application
- Responds to '!ping' and '!hello' commands
- Uses discord.py for bot functionality
- Implements command syncing for slash commands
- Uses Poetry for dependency management
- Easy to understand and extend

## Develop

To run the bot locally:

```bash
poetry run python bot.py
```

Make sure to set up your `.env` file with your Discord bot token:

```text
DISCORD_TOKEN=your_token_here
```

## Deploy

To deploy the bot on Railway:

```bash
railway up
```

Remember to set the `DISCORD_TOKEN` environment variable in your Railway project settings.

## Test

Open Discord, Add Discord to the channel and Try with `!hello` or `!ping`.

## Learn More

- [Discord.py Documentation](https://discordpy.readthedocs.io/)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [Discord Developer Portal](https://discord.com/developers/docs)
- [Railway Documentation](https://docs.railway.app/)
