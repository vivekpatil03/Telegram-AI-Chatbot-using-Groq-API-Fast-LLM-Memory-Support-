from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

from config import TELEGRAM_TOKEN
from memory import get_history, update_history
from llm import generate_reply

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat_id
    user_text = update.message.text

    # Get conversation history
    history = get_history(user_id)

    # Add system prompt (optional but powerful)
    if not history:
        history.append({
            "role": "system",
            "content": "You are a helpful and intelligent AI assistant."
        })

    # Add user message
    history.append({"role": "user", "content": user_text})

    # Generate response
    reply = generate_reply(history)

    # Save messages
    update_history(user_id, "user", user_text)
    update_history(user_id, "assistant", reply)

    # Send reply
    await update.message.reply_text(reply)


def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    print("🚀 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()