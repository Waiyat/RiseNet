from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from db import register_user, get_balance

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    register_user(str(user.id), user.full_name)

    keyboard = [
        [InlineKeyboardButton("💰 Check Balance", callback_data="check_balance")],
        [InlineKeyboardButton("📥 Deposit", callback_data="deposit")],
        [InlineKeyboardButton("📤 Withdraw", callback_data="withdraw")],
        [InlineKeyboardButton("ℹ️ About RiseNet", callback_data="about")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"Welcome to RiseNet, {user.first_name}!\nSelect an option below 👇",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = query.from_user
    await query.answer()

    if query.data == "check_balance":
        balance = get_balance(str(user.id))
        await query.edit_message_text(f"💰 Your current balance is: KES {balance:.2f}")
    
    elif query.data == "about":
        await query.edit_message_text(
            "RiseNet is a smart wallet system powered by Telegram, designed to make your finances simple, fast, and secure.\n\nBuilt with ❤️ by Waiyat & Juliet."
        )
    
    elif query.data == "deposit":
        await query.edit_message_text(
            "To deposit, use M-PESA STK Push. We'll guide you next when STK is integrated."
        )

    elif query.data == "withdraw":
        await query.edit_message_text(
            "Withdrawals will be processed via M-PESA or Airtel once activated."
        )

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please use the menu buttons to navigate.")
