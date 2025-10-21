import requests
from bot.config.settings import API_KEY, LARAVEL_API_URL

print("=" * 50)
print("🔍 Testing API Connection")
print("=" * 50)
print(f"API_KEY: {API_KEY[:10]}...")
print(f"LARAVEL_API_URL: {LARAVEL_API_URL}")
print("=" * 50)

headers = {'X-API-Key': API_KEY}

# Test 1: Get Locations
print("\n📍 Test 1: Get All Locations")
try:
    response = requests.get(f"{LARAVEL_API_URL}/locations", headers=headers, timeout=10)
    print(f"Status Code: {response.status_code}")
    data = response.json()
    print(f"Success: {data.get('success')}")
    print(f"Data Count: {len(data.get('data', []))}")
    if data.get('data'):
        print(f"First Location: {data['data'][0]['name']}")
except Exception as e:
    print(f"❌ Error: {e}")

# Test 2: Search Location
print("\n🔍 Test 2: Search Location 'Tampan'")
try:
    response = requests.get(
        f"{LARAVEL_API_URL}/locations/search",
        headers=headers,
        params={'q': 'Tampan'},
        timeout=10
    )
    print(f"Status Code: {response.status_code}")
    data = response.json()
    print(f"Success: {data.get('success')}")
    print(f"Results: {len(data.get('data', []))}")
except Exception as e:
    print(f"❌ Error: {e}")

print("\n" + "=" * 50)
