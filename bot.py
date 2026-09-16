import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome!\n\n"
        "🤖 Bot is now active.\n"
        "💰 Balance: 0 coins\n\n"
        "Use /balance to check your balance."
    )

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💰 Your balance: 0 coins"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commands:\n"
        "/start - Start the bot\n"
        "/balance - Check balance\n"
        "/refer - Referral link\n"
        "/stats - Statistics\n"
        "/withdraw - Withdrawal\n"
        "/help - Help"
    )

def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN is not set")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("balance", balance))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
