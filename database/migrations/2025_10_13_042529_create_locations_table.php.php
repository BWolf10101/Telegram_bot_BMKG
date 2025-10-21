<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up()
    {
        Schema::create('locations', function (Blueprint $table) {
            $table->id();
            $table->string('code')->unique(); // Kode BMKG (adm4)
            $table->string('name'); // Nama Kelurahan
            $table->string('district'); // Kecamatan
            $table->string('city')->default('Pekanbaru');
            $table->string('province')->default('Riau');
            $table->boolean('is_active')->default(true);
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('locations');
    }
};
