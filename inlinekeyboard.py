#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://github.com/python-telegram-bot/python-telegram-bot/wiki/InlineKeyboard-Example.
"""
import logging
import random
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton(".", callback_data="1"),
            InlineKeyboardButton(".", callback_data="2"),
        ],
        [InlineKeyboardButton(".", callback_data="3")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Сделай свой осознанный выбор. Иначе, возможно, ты в будущем будешь лежать в своей постели после тяжелого дня, пытаясь уснуть, но вспомнишь, что хотел выбрать другой вариант.", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

    folder = ''

    if query.data == '1':
        folder = 'images/cats'
    elif query.data == '2':
        folder = 'images/dogs'
    else:
        d = []
        img = 'images'
        for files in os.scandir(img):
            d.append(files.name)
        randfolder = random.choice(d)
        folder = f'images/{randfolder}'


    c = []
    for files in os.scandir(folder):
            c.append(files.name)
    image_name = random.choice(c)

    image_path = f'{folder}/{image_name}'

    await query.message.reply_photo(
        photo=open(image_path, 'rb'),
    )

    await query.edit_message_text(text=f"Ты выбрал: {query.data}")
    


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.")

def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    TOKEN = '7056450035:AAFvb0o1n16qZ0pOBZRI5zz7XDhCVOxF02c'
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()