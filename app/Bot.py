import discord
import discord.ext.commands as commands
import logging
from app.ShapeAI import ShapeAI

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
    logging.info(f"Logged in as bot {bot.user}")


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


discord.utils.setup_logging()


async def start_bot(DISCORD_TOKEN, SHAPES_TOKEN):
    await bot.add_cog(ShapeAI(bot, SHAPES_TOKEN))
    await bot.start(DISCORD_TOKEN)
