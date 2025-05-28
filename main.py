import logging
import random
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


TOKEN = '7813563323:AAFAz5xbH1fElCEIvfRRHH9R3_qs1BdVw2M'


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}, хочешь узнать насколькы ты сегодня nicita55?",
        reply_markup=ForceReply(selective=True),
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Чтоб узнать насколько ты nicita55, введи команду /nicita55")


async def generate_nicita55(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(rf"ты на {random.randint(1,100)}% nicita55")


def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("nicita55", generate_nicita55))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
