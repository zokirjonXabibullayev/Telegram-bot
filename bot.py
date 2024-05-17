import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from telegram.constants import ParseMode

# Loggingni yoqish
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levellevel)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# /start buyrug'i uchun funksiya
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Salom! Men sizning botingizman. Qanday yordam bera olaman?')

# Har qanday matnli xabarni monospace formatda qaytarish uchun funksiya
async def echo(update: Update, context: CallbackContext) -> None:
    # Escaping Markdown V2 special characters
    escaped_text = update.message.text.replace('\\', '\\\\').replace('_', '\\_').replace('*', '\\*').replace('[', '\\[').replace(']', '\\]').replace('(', '\\(').replace(')', '\\)').replace('~', '\\~').replace('`', '\\`').replace('>', '\\>').replace('#', '\\#').replace('+', '\\+').replace('-', '\\-').replace('=', '\\=').replace('|', '\\|').replace('{', '\\{').replace('}', '\\}').replace('.', '\\.').replace('!', '\\!')
    formatted_text = f'```\n{escaped_text}\n```'  # Using triple backticks for monospace block
    await update.message.reply_text(formatted_text, parse_mode=ParseMode.MARKDOWN_V2)

def main() -> None:
    # Tokenni kiritish
    application = Application.builder().token("6558604988:AAFH-AXyDEu0_wb_5I610aEF-mg-lIHdHtM").build()

    # /start buyrug'ini qo'shish
    application.add_handler(CommandHandler("start", start))

    # Matnli xabarlarni qaytarish
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Botni boshlash
    application.run_polling()

if __name__ == '__main__':
    main()
