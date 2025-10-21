# ============================================
# FILE: python-bot/bot/config/settings.py
# ============================================

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Path dari settings.py ke root project
# python-bot/bot/config/settings.py
# .parent -> python-bot/bot/config/
# .parent.parent -> python-bot/bot/
# .parent.parent.parent -> python-bot/
# .parent.parent.parent.parent -> weather-bot-project/ (ROOT)
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
ENV_PATH = BASE_DIR / '.env'

# Load environment variables dari file .env
if ENV_PATH.exists():
    load_dotenv(dotenv_path=ENV_PATH)
    print(f"✅ Loaded .env from: {ENV_PATH}")
else:
    print(f"⚠️  File .env tidak ditemukan di: {ENV_PATH}")
    print(f"💡 Mencoba load .env dari current directory...")
    load_dotenv()

    # Cek sekali lagi setelah load dari current directory
    if not Path('.env').exists():
        print(f"\n❌ CRITICAL: File .env tidak ditemukan!")
        print(f"   Lokasi yang dicari:")
        print(f"   1. {ENV_PATH}")
        print(f"   2. {Path.cwd() / '.env'}")
        print(f"\n💡 Solusi:")
        print(f"   Buat file .env di: {BASE_DIR}")
        print(f"   Atau di: {Path.cwd()}")
        sys.exit(1)

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Laravel API Configuration
LARAVEL_API_URL = os.getenv('LARAVEL_API_URL', 'http://localhost:8000/api/v1')
API_KEY = os.getenv('API_KEY')

# Debug info
print(f"\n🔍 Configuration:")
print(f"   BASE_DIR: {BASE_DIR}")
print(f"   ENV_PATH: {ENV_PATH}")
print(f"   ENV_EXISTS: {ENV_PATH.exists()}")
print(f"   TELEGRAM_BOT_TOKEN: {'✓ Set' if TELEGRAM_BOT_TOKEN else '✗ Not Set'}")
print(f"   LARAVEL_API_URL: {LARAVEL_API_URL}")
print(f"   API_KEY: {'✓ Set' if API_KEY else '✗ Not Set'}")
print("")

# Validasi konfigurasi wajib
if not TELEGRAM_BOT_TOKEN:
    print(f"\n❌ TELEGRAM_BOT_TOKEN tidak ditemukan di file .env!")
    print(f"   Path .env: {ENV_PATH}")
    print(f"\n💡 Tambahkan baris ini ke file .env:")
    print(f"   TELEGRAM_BOT_TOKEN=your_telegram_bot_token")
    print(f"\n📝 Cara mendapatkan token:")
    print(f"   1. Buka @BotFather di Telegram")
    print(f"   2. Kirim /newbot")
    print(f"   3. Ikuti instruksi")
    print(f"   4. Copy token yang diberikan")
    sys.exit(1)

if not API_KEY:
    print(f"\n❌ API_KEY tidak ditemukan di file .env!")
    print(f"   Path .env: {ENV_PATH}")
    print(f"\n💡 Tambahkan baris ini ke file .env:")
    print(f"   API_KEY=your_secret_api_key")
    print(f"\n🔐 Generate API key dengan:")
    print(f"   python -c \"import secrets; print(secrets.token_urlsafe(32))\"")
    sys.exit(1)

# Optional: Logging configuration
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

# Optional: Cache timeout (dalam detik)
try:
    CACHE_TIMEOUT = int(os.getenv('CACHE_TIMEOUT', '1800'))
except ValueError:
    print(f"⚠️  CACHE_TIMEOUT invalid, using default: 1800")
    CACHE_TIMEOUT = 1800

# Optional: Request timeout (dalam detik)
try:
    REQUEST_TIMEOUT = int(os.getenv('REQUEST_TIMEOUT', '10'))
except ValueError:
    print(f"⚠️  REQUEST_TIMEOUT invalid, using default: 10")
    REQUEST_TIMEOUT = 10

# Success message
print("✅ Configuration loaded successfully!")
print("=" * 50)
