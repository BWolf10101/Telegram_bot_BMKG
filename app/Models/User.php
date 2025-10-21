<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class UserLocation extends Model
{
    protected $fillable = ['user_id', 'location_id'];

    public function location()
    {
        return $this->belongsTo(Location::class);
    }
}
