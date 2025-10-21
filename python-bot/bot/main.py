import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
    ConversationHandler
)
from bot.config.settings import TELEGRAM_BOT_TOKEN
from bot.handlers.start_handler import start_command
from bot.handlers.weather_handler import cuaca_command, prakiraan_command
from bot.handlers.location_handler import (
    pilih_lokasi_command,
    lokasi_command,
    process_search,
    search_location_handler,
    SEARCHING
)
from bot.handlers.callback_handler import button_callback

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    """Jalankan bot"""
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Conversation handler untuk pencarian lokasi
    search_conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(search_location_handler, pattern='^search_location$')],  # PERBAIKAN 1: Tutup string dan tambahkan $
        states={
            SEARCHING: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_search)]
        },
        fallbacks=[CommandHandler('batal', lambda u, c: ConversationHandler.END)]
    )

    # Command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("cuaca", cuaca_command))
    application.add_handler(CommandHandler("prakiraan", prakiraan_command))
    application.add_handler(CommandHandler("pilihlokasi", pilih_lokasi_command))
    application.add_handler(CommandHandler("lokasi", lokasi_command))

    # Conversation handler
    application.add_handler(search_conv_handler)

    # Callback handlers (harus setelah conversation handler)
    application.add_handler(CallbackQueryHandler(button_callback))

    logger.info("Bot started...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
