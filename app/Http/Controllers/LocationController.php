<?php

namespace App\Http\Controllers;

use App\Models\Location;
use App\Models\UserLocation;
use Illuminate\Http\Request;

class LocationController extends Controller
{
    public function index()
    {
        $locations = Location::active()
            ->orderBy('district')
            ->orderBy('name')
            ->get();

        return response()->json([
            'success' => true,
            'data' => $locations
        ]);
    }

    public function search(Request $request)
    {
        $keyword = $request->get('q', '');

        if (strlen($keyword) < 2) {
            return response()->json([
                'success' => false,
                'message' => 'Keyword minimal 2 karakter'
            ], 400);
        }

        $locations = Location::active()
            ->search($keyword)
            ->orderBy('district')
            ->orderBy('name')
            ->limit(10)
            ->get();

        return response()->json([
            'success' => true,
            'data' => $locations
        ]);
    }

    public function show($id)
    {
        $location = Location::find($id);

        if (!$location) {
            return response()->json([
                'success' => false,
                'message' => 'Location not found'
            ], 404);
        }

        return response()->json([
            'success' => true,
            'data' => $location
        ]);
    }

    public function setUserLocation(Request $request)
    {
        $request->validate([
            'user_id' => 'required|string',
            'location_id' => 'required|exists:locations,id'
        ]);

        $userLocation = UserLocation::updateOrCreate(
            ['user_id' => $request->user_id],
            ['location_id' => $request->location_id]
        );

        $userLocation->load('location');

        return response()->json([
            'success' => true,
            'message' => 'Location set successfully',
            'data' => $userLocation
        ]);
    }

    public function getUserLocation($userId)
    {
        $userLocation = UserLocation::where('user_id', $userId)
            ->with('location')
            ->first();

        if (!$userLocation) {
            return response()->json([
                'success' => false,
                'message' => 'User location not found'
            ], 404);
        }

        return response()->json([
            'success' => true,
            'data' => $userLocation
        ]);
    }
}
