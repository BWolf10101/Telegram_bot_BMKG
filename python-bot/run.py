# ============================================
# FILE: python-bot/run.py (Versi Simple)
# ============================================

"""
Weather Bot Runner
Titik masuk utama untuk menjalankan Telegram Bot
"""

import sys
import os
import logging
from datetime import datetime

# Tambahkan direktori bot ke Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def print_banner():
    """Print banner saat bot dimulai"""
    banner = """
    ╔══════════════════════════════════════════╗
    ║     🌤️  WEATHER BOT PEKANBARU 🌤️        ║
    ║     Powered by BMKG API                  ║
    ╚══════════════════════════════════════════╝
    """
    print(banner)
    print(f"    Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"    Python Version: {sys.version.split()[0]}")
    print("=" * 50)

if __name__ == '__main__':
    try:
        print_banner()

        from bot.main import main

        logger.info("🚀 Initializing bot...")
        main()

    except KeyboardInterrupt:
        print("\n" + "=" * 50)
        logger.info("🛑 Bot stopped by user")
        print("=" * 50)

    except ImportError as e:
        print("\n" + "=" * 50)
        logger.error(f"❌ Import Error: {e}")
        logger.info("💡 Pastikan semua dependencies sudah terinstall:")
        logger.info("   pip install -r requirements.txt")
        print("=" * 50)
        import traceback
        traceback.print_exc()
        sys.exit(1)

    except Exception as e:
        print("\n" + "=" * 50)
        logger.error(f"❌ Error: {e}")
        print("=" * 50)
        import traceback
        traceback.print_exc()
        sys.exit(1)
