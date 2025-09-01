import asyncio
import os
import dotenv
dotenv.load_dotenv()

import app.Bot

async def main():
    await app.Bot.start_bot(os.getenv('DISCORD_BOT_TOKEN'))


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
