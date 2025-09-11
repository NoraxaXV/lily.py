import discord
import discord.ext.commands as commands
import discord.ext.tasks as tasks
import random
import logging
import datetime

ADO_TIME = datetime.time(hour=11, tzinfo=datetime.timezone.utc)


class AdoPoster(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.channel: discord.TextChannel | None = None
        self.post_ado.start()

    def cog_unload(self):
        self.post_ado.stop()

    @commands.hybrid_command()
    async def setadopostchannel(self, ctx, channel_id: int):
        ado_channel = self.bot.get_channel(channel_id)
        if ado_channel:
            self.channel = ado_channel
            await self.channel.send("Sending PEAK ADO MUSIC TO THIS CHANNEL YAY")
            logging.info(
                f"Set Ado music channel to channel {ado_channel.name}:{ado_channel.id}!"
            )
        else:
            logging.warning(f"Sent an invalid channel id: {channel_id}")

    @tasks.loop(time=ADO_TIME)
    async def post_ado(self):
        if not self.channel:
            logging.warning(
                "No ado channel set :( please set one with /setadopostchannel NOW"
            )
            return
        with open("./ado_videos.txt") as links:
            await self.channel.send(
                "ADO POSTING OF THE DAY: \n"
                + random.choice(
                    list(
                        filter(
                            lambda line: not line.strip().startswith("#"),
                            links.readlines(),
                        )
                    )
                )
            )


async def setup(bot: commands.Bot):
    await bot.add_cog(AdoPoster(bot))
