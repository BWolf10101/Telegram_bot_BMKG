<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\WeatherController;
use App\Http\Controllers\LocationController;

Route::prefix('v1')->middleware('api.key')->group(function () {
    // Weather endpoints
    Route::get('/weather/today', [WeatherController::class, 'getToday']);
    Route::get('/weather/forecast', [WeatherController::class, 'getForecast']);
    Route::get('/weather/forecast/{days}', [WeatherController::class, 'getForecastDays']);

    // Location endpoints
    Route::get('/locations', [LocationController::class, 'index']);
    Route::get('/locations/search', [LocationController::class, 'search']);
    Route::get('/locations/{id}', [LocationController::class, 'show']);
    Route::post('/user-location', [LocationController::class, 'setUserLocation']);
    Route::get('/user-location/{userId}', [LocationController::class, 'getUserLocation']);
});
