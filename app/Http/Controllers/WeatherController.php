<?php

namespace App\Http\Controllers;

use App\Services\BMKGService;
use App\Models\WeatherLog;
use App\Models\UserLocation;
use Illuminate\Http\Request;

class WeatherController extends Controller
{
    protected $bmkgService;

    public function __construct(BMKGService $bmkgService)
    {
        $this->bmkgService = $bmkgService;
    }

    private function getLocationCode(Request $request)
    {
        $userId = $request->header('X-User-Id');
        $locationCode = $request->get('location_code');

        // Jika ada location_code di parameter, gunakan itu
        if ($locationCode) {
            return $locationCode;
        }

        // Jika tidak, cari dari user location
        if ($userId) {
            $userLocation = UserLocation::where('user_id', $userId)
                ->with('location')
                ->first();

            if ($userLocation) {
                return $userLocation->location->code;
            }
        }

        // Default ke Pekanbaru umum
        return '14.71';
    }

    public function getToday(Request $request)
    {
        $locationCode = $this->getLocationCode($request);
        $data = $this->bmkgService->getTodayWeather($locationCode);

        if (!$data) {
            return response()->json([
                'success' => false,
                'message' => 'Failed to fetch weather data'
            ], 500);
        }

        WeatherLog::create([
            'type' => 'today',
            'user_id' => $request->header('X-User-Id'),
        ]);

        return response()->json([
            'success' => true,
            'data' => $data
        ]);
    }

    public function getForecast(Request $request)
    {
        return $this->getForecastDays(7, $request);
    }

    public function getForecastDays($days, Request $request)
    {
        $days = min(max((int)$days, 1), 7);
        $locationCode = $this->getLocationCode($request);

        $data = $this->bmkgService->getForecast($locationCode, $days);

        if (!$data) {
            return response()->json([
                'success' => false,
                'message' => 'Failed to fetch weather data'
            ], 500);
        }

        WeatherLog::create([
            'type' => 'forecast_' . $days,
            'user_id' => $request->header('X-User-Id'),
        ]);

        return response()->json([
            'success' => true,
            'data' => $data
        ]);
    }
}
