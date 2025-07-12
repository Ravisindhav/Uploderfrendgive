import asyncio
import logging
import os
import sys
from pyrogram import Client, filters, idle
from config import API_ID, API_HASH, BOT_TOKEN

# Create base directory for all data
BASE_DIR = os.path.join(os.path.expanduser("~"), ".extractor_bot")
SESSION_DIR = os.path.join(BASE_DIR, "sessions")

# Ensure directories exist with proper permissions
try:
    os.makedirs(SESSION_DIR, mode=0o700, exist_ok=True)
except Exception as e:
    print(f"Error creating directories: {e}")
    sys.exit(1)

# Configure logging
logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Initialize event loop
loop = asyncio.get_event_loop()

# Initialize Pyrogram client with proper session path
try:
    app = Client(
        os.path.join(SESSION_DIR, "extractor_bot"),
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
        sleep_threshold=120,
        workers=500
    )
except Exception as e:
    logger.error(f"Failed to initialize client: {e}")
    sys.exit(1)

# ✅ Add command handler here
@app.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    await message.reply_text(
        f"👋 नमस्ते `{message.from_user.first_name}`!\n\n"
        "मैं तैयार हूँ आपकी मदद करने के लिए ✅"
    )

# Start bot and idle
async def info_bot():
    global BOT_ID, BOT_NAME, BOT_USERNAME
    try:
        await app.start()
        getme = await app.get_me()
        BOT_ID = getme.id
        BOT_USERNAME = getme.username
        BOT_NAME = f"{getme.first_name} {getme.last_name}" if getme.last_name else getme.first_name
        logger.info(f"Bot started as {BOT_USERNAME} (ID: {BOT_ID})")
        await idle()
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")
        sys.exit(1)

# Run the bot
loop.run_until_complete(info_bot())
