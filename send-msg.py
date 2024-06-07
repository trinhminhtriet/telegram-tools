import asyncio
import os
import sys
from datetime import datetime
from pyrogram import Client, enums
from dotenv import load_dotenv

load_dotenv()
api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_HASH")
slug = sys.argv[1]

async def main():
    async with Client("my", api_id, api_hash) as app:
        await app.send_message(
            "me",
            slug + " has been added at " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            parse_mode=enums.ParseMode.MARKDOWN
        )

asyncio.run(main())
