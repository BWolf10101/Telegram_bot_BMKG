<?php

namespace App\Services;

use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\Cache;

class BMKGService
{
    protected $apiUrl;

    public function __construct()
    {
        $this->apiUrl = config('services.bmkg.api_url');
    }

    public function getWeatherData($locationCode)
    {
        $cacheKey = "bmkg_weather_{$locationCode}";

        return Cache::remember($cacheKey, 1800, function () use ($locationCode) {
            try {
                $response = Http::withOptions([
                    'verify' => false,
                ])->timeout(10)->get($this->apiUrl, [
                    'adm4' => $locationCode
                ]);

                if ($response->successful()) {
                    $data = $response->json();

                    // Cek apakah ada error dari BMKG
                    if (isset($data['error']) || isset($data['statusCode'])) {
                        \Log::warning("BMKG API returned error for code: {$locationCode}");
                        return null;
                    }

                    return $data;
                }

                \Log::error("BMKG API Failed: " . $response->status());
                return null;

            } catch (\Exception $e) {
                \Log::error("BMKG API Error: " . $e->getMessage());
                return null;
            }
        });
    }

    public function getTodayWeather($locationCode)
    {
        $data = $this->getWeatherData($locationCode);

        if (!$data) {
            return null;
        }

        // Data dari BMKG langsung
        return [
            'location' => $data['lokasi'] ?? null,
            'weather' => $data['data'][0] ?? null, // Hari pertama
        ];
    }

    public function getForecast($locationCode, $days = 7)
    {
        $data = $this->getWeatherData($locationCode);

        if (!$data) {
            return null;
        }

        // Data dari BMKG langsung
        return [
            'location' => $data['lokasi'] ?? null,
            'forecast' => array_slice($data['data'] ?? [], 0, $days),
        ];
    }
}
