import app.Bot

import asyncio
import os
import dotenv

dotenv.load_dotenv()


async def main():
    await app.Bot.start_bot(
        os.getenv("DISCORD_BOT_TOKEN"), os.getenv("SHAPES_API_TOKEN")
    )


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
