<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Location extends Model
{
    protected $fillable = [
        'code', 'name', 'district', 'city', 'province', 'is_active'
    ];

    public function userLocations()
    {
        return $this->hasMany(UserLocation::class);
    }

    public function scopeActive($query)
    {
        return $query->where('is_active', true);
    }

    public function scopeSearch($query, $keyword)
    {
        return $query->where(function($q) use ($keyword) {
            $q->where('name', 'like', "%{$keyword}%")
              ->orWhere('district', 'like', "%{$keyword}%");
        });
    }
}
