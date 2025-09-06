from openai import OpenAI
import discord
import discord.ext.commands as commands
import logging
import asyncio


TRIGGER_WORDS = ["lily", "chocolate"]


class ShapeAI(commands.Cog):
    def __init__(self, bot, API_TOKEN, AI_MODEL):
        self.bot: commands.Bot = bot
        self.client = OpenAI(api_key=API_TOKEN, base_url="https://api.shapes.inc/v1")
        self.model = AI_MODEL
        self.message_log = []

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if self.bot.user and message.author.id == self.bot.user.id:
            return
        if self.bot.user and (
            self.bot.user.id in map(lambda pings: pings.id, message.mentions)
            or any(map(lambda trigger: trigger in message.content, TRIGGER_WORDS))
        ):
            logging.info(
                f'message! {message.author.display_name} sent "{message.content}"'
            )

            self.message_log.append(
                {
                    "role": "developer",
                    "content": f"{message.author.display_name} sent the following message in the text channel {(message.channel.name or "dms")}",
                }
            )
            if message.reference:
                reference = await message.channel.fetch_message(
                    message.reference.message_id
                )
                self.message_log.append(
                    {
                        "role": "developer",
                        "content": f"the following message was in reference to {reference.content} from {reference.author.display_name}",
                    }
                )

            self.message_log.append({"role": "user", "content": message.content})
            response = (
                self.client.chat.completions.create(
                    model=f"shapesinc/{self.model}", messages=self.message_log
                )
                .choices[0]
                .message.content
            )
            for msg in response.split("\n\n"):
                async with message.channel.typing():
                    await asyncio.sleep(len(msg) / 25)
                await message.channel.send(msg)
