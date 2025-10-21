<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class UserLocation extends Model
{
    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'user_id',
        'location_id',
    ];

    /**
     * Get the location that belongs to the user location.
     */
    public function location()
    {
        return $this->belongsTo(Location::class);
    }
}
