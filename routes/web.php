<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

Route::get('/debug-api-key', function () {
    return [
        'env_api_key' => env('API_KEY'),
        'config_api_key' => config('services.api_key'),
        'match' => env('API_KEY') === 'wB0t_P3k4nB4ru_2024_S3cr3t_K3y_xYz789',
    ];
});
