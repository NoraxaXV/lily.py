import asyncio
import logging
import discord
import discord.ext.commands as commands
import config

discord.utils.setup_logging()

bot = commands.Bot(
    command_prefix="!",
    intents=discord.Intents(
        message_content=True,
        guilds=True,
        guild_messages=True,
    ),
)

@bot.event
async def on_ready():
    for cog in config.get("EXTENSIONS"):
        await bot.load_extension(f"cogs.{cog}")
    await bot.tree.sync()
    logging.info(f"found command: {bot.get_command("crystalize")}")
    logging.info(f"Logged in as bot {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

if __name__ == "__main__":
    try:
        asyncio.run(bot.start(config.get("DISCORD_BOT_TOKEN")))
    except KeyboardInterrupt:
        pass
