import discord
import discord.ext.commands as commands
import logging

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
    logging.info(f'Logged in as bot {bot.user}')
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

discord.utils.setup_logging()

async def start_bot(TOKEN):
    await bot.start(TOKEN)
