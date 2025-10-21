from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class FormatterService:
    @staticmethod
    def format_today(data):
        """Format data cuaca hari ini"""
        try:
            if not data or not isinstance(data, dict):
                return "❌ Data cuaca tidak valid"

            if not data.get('success'):
                return "❌ Gagal mengambil data cuaca dari server"

            weather_info = data.get('data', {})
            location = weather_info.get('location', {})
            weather = weather_info.get('weather', {})

            if not location or not weather:
                return "❌ Data cuaca tidak lengkap"

            # Ambil data lokasi
            provinsi = location.get('provinsi', 'N/A')
            kotkab = location.get('kotkab', 'N/A')
            kecamatan = location.get('kecamatan', 'N/A')
            desa = location.get('desa', 'N/A')

            msg = f"🌤 *Cuaca Hari Ini*\n\n"
            msg += f"📍 *Lokasi:* {desa}, Kec. {kecamatan}\n"
            msg += f"🏙 {kotkab}, {provinsi}\n\n"

            # Data cuaca dalam format array of arrays
            cuaca_data = weather.get('cuaca', [])

            if not cuaca_data:
                return msg + "⚠️ Data cuaca detail tidak tersedia"

            # Ambil 3 periode pertama (pagi, siang, sore/malam)
            periods = ["🌅 Pagi", "☀️ Siang", "🌙 Sore/Malam"]

            for idx, period_name in enumerate(periods):
                if idx >= len(cuaca_data):
                    break

                period_data = cuaca_data[idx]
                if not period_data or len(period_data) == 0:
                    continue

                # Ambil data pertama dari periode
                weather_item = period_data[0]

                msg += f"*{period_name}*\n"
                msg += f"  ☁️ {weather_item.get('weather_desc', 'N/A')}\n"
                msg += f"  🌡 Suhu: {weather_item.get('t', 'N/A')}°C\n"
                msg += f"  💧 Kelembaban: {weather_item.get('hu', 'N/A')}%\n"
                msg += f"  🌊 Angin: {weather_item.get('ws', 'N/A')} km/h dari {weather_item.get('wd', 'N/A')}\n"

                # Info hujan jika ada
                tp = weather_item.get('tp', 0)
                if tp > 0:
                    msg += f"  🌧 Curah Hujan: {tp} mm\n"

                msg += "\n"

            return msg

        except Exception as e:
            logger.error(f"Error formatting today: {e}", exc_info=True)
            return f"❌ Gagal memformat data cuaca: {str(e)}"

    @staticmethod
    def format_forecast(data, days):
        """Format data prakiraan cuaca"""
        try:
            if not data or not isinstance(data, dict):
                return "❌ Data cuaca tidak valid"

            if not data.get('success'):
                return "❌ Gagal mengambil data cuaca dari server"

            weather_info = data.get('data', {})
            location = weather_info.get('location', {})
            forecast = weather_info.get('forecast', [])

            if not location or not forecast:
                return "❌ Data prakiraan tidak lengkap"

            provinsi = location.get('provinsi', 'N/A')
            kotkab = location.get('kotkab', 'N/A')
            kecamatan = location.get('kecamatan', 'N/A')
            desa = location.get('desa', 'N/A')

            msg = f"📅 *Prakiraan Cuaca {days} Hari*\n\n"
            msg += f"📍 *Lokasi:* {desa}, Kec. {kecamatan}\n"
            msg += f"🏙 {kotkab}, {provinsi}\n\n"

            for day_idx, day_data in enumerate(forecast[:days]):
                # Ambil data cuaca untuk hari ini
                cuaca_data = day_data.get('cuaca', [])

                if not cuaca_data or len(cuaca_data) == 0:
                    continue

                # Ambil periode siang (index 1) atau pagi jika tidak ada
                period_idx = 1 if len(cuaca_data) > 1 else 0
                period_data = cuaca_data[period_idx]

                if not period_data or len(period_data) == 0:
                    continue

                weather_item = period_data[0]

                # Format tanggal
                try:
                    local_dt = weather_item.get('local_datetime', '')
                    if local_dt:
                        date_obj = datetime.strptime(local_dt.split()[0], '%Y-%m-%d')
                        date_str = date_obj.strftime('%d %B %Y')
                    else:
                        date_str = f"Hari {day_idx + 1}"
                except:
                    date_str = f"Hari {day_idx + 1}"

                msg += f"📆 *{date_str}*\n"
                msg += f"  ☁️ {weather_item.get('weather_desc', 'N/A')}\n"

                # Hitung min/max temperature dari semua periode hari itu
                temps = []
                for period in cuaca_data:
                    if period and len(period) > 0:
                        t = period[0].get('t')
                        if t is not None:
                            temps.append(t)

                if temps:
                    msg += f"  🌡 Suhu: {min(temps)}°C - {max(temps)}°C\n"
                else:
                    msg += f"  🌡 Suhu: {weather_item.get('t', 'N/A')}°C\n"

                msg += f"  💧 Kelembaban: {weather_item.get('hu', 'N/A')}%\n"

                # Total curah hujan
                total_rain = sum(
                    period[0].get('tp', 0)
                    for period in cuaca_data
                    if period and len(period) > 0
                )
                if total_rain > 0:
                    msg += f"  🌧 Curah Hujan: {total_rain:.1f} mm\n"

                msg += "\n"

            return msg

        except Exception as e:
            logger.error(f"Error formatting forecast: {e}", exc_info=True)
            return f"❌ Gagal memformat data prakiraan: {str(e)}"
