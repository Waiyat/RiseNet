import asyncio
import logging
from telegram import Update, WebAppInfo, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "7529531389:AAE5jo4BKfdA65t0JseCWou5XUBJWVGNTzY"
WEB_APP_URL = "https://waiyat-rise.netlify.app/"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button = KeyboardButton(
        text="🔓 Open Wallet",
        web_app=WebAppInfo(url=WEB_APP_URL)
    )
    keyboard = [[button]]
    reply_markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Welcome to *RiseNet*\n\nTap the button below to open your wallet securely:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("🚀 RiseNetBot is now running...")

    # DO NOT close loop on macOS — just start polling manually
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    
    # Run forever
    await asyncio.Event().wait()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except RuntimeError as e:
        if "event loop is already running" in str(e):
            print("⚠️ Using existing macOS event loop...")
            loop = asyncio.get_event_loop()
            loop.create_task(main())
            loop.run_forever()
        else:
            raise
