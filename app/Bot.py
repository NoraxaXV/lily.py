import discord
import discord.ext.commands as commands
import logging
from app.ShapeAI import ShapeAI
from app.Crystalizer import Crystalizer

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
    await bot.tree.sync()
    logging.info(f"Logged in as bot {bot.user}")


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


discord.utils.setup_logging()


async def start_bot(DISCORD_TOKEN, SHAPES_TOKEN, AI_MODEL):
    await bot.add_cog(ShapeAI(bot, SHAPES_TOKEN, AI_MODEL))
    await bot.add_cog(Crystalizer())
    await bot.start(DISCORD_TOKEN)
