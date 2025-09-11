import discord
import discord.ext.commands as commands
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import io
import logging

@commands.hybrid_command()
async def crystalize(ctx: commands.Context, *, liberal: discord.User = None):
    if liberal == None:
        if ctx.message.reference != None:
            reply = await ctx.channel.fetch_message(ctx.message.reference.message_id)
            liberal = reply.author
        else:
            logging.error(
                f'Crystalizer failure for message <{ctx.message.id}>. liberal was "{liberal}" and reply was "{ctx.message.reference}"'
            )
            return

    avatar = await liberal.display_avatar.read()
    with io.BytesIO(create_image(avatar)) as avatarfile:
        await ctx.send(
            file=discord.File(fp=avatarfile, filename="crystalized_liberal.png")
        )


def create_image(avatar_bytes: bytes) -> bytes:
    with (
        Image.open("./crystal.png") as crystal,
        Image.open(io.BytesIO(avatar_bytes)) as avatar,
    ):
        avatar = avatar.resize((450, 450))
        mask = Image.new("L", avatar.size, 0)
        ImageDraw.Draw(mask).ellipse((0, 0, avatar.size[0], avatar.size[1]), fill=255)
        avatar.putalpha(mask)

        canvas = Image.new("RGBA", crystal.size)
        canvas.paste(avatar, (185, 150))

        # NOTE add a multiplication to the alpha values of the crystal to adjust the darkness
        blend = Image.alpha_composite(canvas, crystal)

        with io.BytesIO() as png:
            blend.save(png, "PNG")
            png.seek(0)
            return png.read()


async def setup(bot: commands.Bot):
    bot.add_command(crystalize)