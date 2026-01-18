import re
import random
import asyncio
from telegram import Bot
from telegram.ext import Updater, MessageHandler, Filters

# ======================
# SETTINGS
# ======================

BOT_TOKEN = "8368758559:AAGYAGnHiBeGQ6f6_L_XVGxTW_twrZ-DYeQ"
SOURCE_CHANNEL = "@rakeshtrickofficial"
TARGET_CHANNEL = "@ragetricks100008"

# ======================

bot = Bot(token=BOT_TOKEN)
updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher


async def process_message(text):
    match = re.search(r"[A-F0-9]{32}", text)
    if match:
        code = match.group()
        await asyncio.sleep(random.uniform(0.3, 0.6))
        bot.send_message(
            chat_id=TARGET_CHANNEL,
            text=f"{code}",
            parse_mode="Markdown"
        )


def handle(update, context):
    if update.channel_post and update.channel_post.text:
        asyncio.run(process_message(update.channel_post.text))


dispatcher.add_handler(
    MessageHandler(Filters.chat(username=SOURCE_CHANNEL), handle)
)

updater.start_polling()
updater.idle()
