import requests
from bot.config.settings import LARAVEL_API_URL, API_KEY

class ApiService:
    def __init__(self):
        self.base_url = LARAVEL_API_URL
        self.headers = {
            'X-API-Key': API_KEY,
            'Content-Type': 'application/json'
        }

    def get_locations(self):
        """Ambil semua lokasi"""
        try:
            response = requests.get(
                f"{self.base_url}/locations",
                headers=self.headers,
                timeout=10
            )

            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"Error fetching locations: {e}")
            return None

    def search_locations(self, keyword):
        """Cari lokasi berdasarkan keyword"""
        try:
            response = requests.get(
                f"{self.base_url}/locations/search",
                headers=self.headers,
                params={'q': keyword},
                timeout=10
            )

            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"Error searching locations: {e}")
            return None

    def set_user_location(self, user_id, location_id):
        """Set lokasi user"""
        try:
            response = requests.post(
                f"{self.base_url}/user-location",
                headers=self.headers,
                json={
                    'user_id': str(user_id),
                    'location_id': location_id
                },
                timeout=10
            )

            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"Error setting user location: {e}")
            return None

    def get_user_location(self, user_id):
        """Ambil lokasi user"""
        try:
            response = requests.get(
                f"{self.base_url}/user-location/{user_id}",
                headers=self.headers,
                timeout=10
            )

            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            return None

    def get_today_weather(self, user_id=None, location_code=None):
        """Ambil data cuaca hari ini"""
        try:
            headers = self.headers.copy()
            if user_id:
                headers['X-User-Id'] = str(user_id)

            params = {}
            if location_code:
                params['location_code'] = location_code

            response = requests.get(
                f"{self.base_url}/weather/today",
                headers=headers,
                params=params,
                timeout=10
            )

            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"Error fetching today weather: {e}")
            return None

    def get_forecast(self, days=7, user_id=None, location_code=None):
        """Ambil data prakiraan cuaca"""
        try:
            headers = self.headers.copy()
            if user_id:
                headers['X-User-Id'] = str(user_id)

            params = {}
            if location_code:
                params['location_code'] = location_code

            response = requests.get(
                f"{self.base_url}/weather/forecast/{days}",
                headers=headers,
                params=params,
                timeout=10
            )

            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"Error fetching forecast: {e}")
            return None
