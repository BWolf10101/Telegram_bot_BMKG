<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use App\Models\Location;

class LocationSeeder extends Seeder
{
    public function run()
    {
        // Disable foreign key checks
        DB::statement('SET FOREIGN_KEY_CHECKS=0;');

        // Hapus data lama
        Location::truncate();

        // Enable foreign key checks
        DB::statement('SET FOREIGN_KEY_CHECKS=1;');

        $locations = [
            // Kecamatan Binawidya
            ['code' => '14.71.08.1001', 'name' => 'Simpangbaru', 'district' => 'Binawidya'],
            ['code' => '14.71.08.1008', 'name' => 'Delima', 'district' => 'Binawidya'],
            ['code' => '14.71.08.1009', 'name' => 'Tobekgodang', 'district' => 'Binawidya'],
            ['code' => '14.71.08.1010', 'name' => 'Binawidya', 'district' => 'Binawidya'],
            ['code' => '14.71.08.1014', 'name' => 'Sungaisibam', 'district' => 'Binawidya'],

            // Kecamatan Sukajadi
            ['code' => '14.71.01.1002', 'name' => 'Jadirejo', 'district' => 'Sukajadi'],
            ['code' => '14.71.01.1003', 'name' => 'Kampung Tengah', 'district' => 'Sukajadi'],
            ['code' => '14.71.01.1004', 'name' => 'Kampung Melayu', 'district' => 'Sukajadi'],
            ['code' => '14.71.01.1005', 'name' => 'Kedung Sari', 'district' => 'Sukajadi'],
            ['code' => '14.71.01.1006', 'name' => 'Harjosari', 'district' => 'Sukajadi'],
            ['code' => '14.71.01.1007', 'name' => 'Sukajadi', 'district' => 'Sukajadi'],
            ['code' => '14.71.01.1008', 'name' => 'Pulau Karomah', 'district' => 'Sukajadi'],

            // Kecamatan Pekanbaru Kota
            ['code' => '14.71.02.1001', 'name' => 'Simpang Empat', 'district' => 'Pekanbaru Kota'],
            ['code' => '14.71.02.1002', 'name' => 'Sumahilang', 'district' => 'Pekanbaru Kota'],
            ['code' => '14.71.02.1003', 'name' => 'Tanah Datar', 'district' => 'Pekanbaru Kota'],
            ['code' => '14.71.02.1004', 'name' => 'Kota Baru', 'district' => 'Pekanbaru Kota'],
            ['code' => '14.71.02.1005', 'name' => 'Sukaramai', 'district' => 'Pekanbaru Kota'],
            ['code' => '14.71.02.1006', 'name' => 'Kota Tinggi', 'district' => 'Pekanbaru Kota'],

            // Kecamatan Sail
            ['code' => '14.71.03.1001', 'name' => 'Cinta Raja', 'district' => 'Sail'],
            ['code' => '14.71.03.1002', 'name' => 'Sukamulya', 'district' => 'Sail'],
            ['code' => '14.71.03.1003', 'name' => 'Sukamaju', 'district' => 'Sail'],

            // Kecamatan Lima Puluh
            ['code' => '14.71.04.1001', 'name' => 'Rintis', 'district' => 'Lima Puluh'],
            ['code' => '14.71.04.1002', 'name' => 'Tanjung Rhu', 'district' => 'Lima Puluh'],
            ['code' => '14.71.04.1003', 'name' => 'Pesisir', 'district' => 'Lima Puluh'],
            ['code' => '14.71.04.1004', 'name' => 'Sekip', 'district' => 'Lima Puluh'],

            // Kecamatan Senapelan
            ['code' => '14.71.05.1001', 'name' => 'Padang Bulan', 'district' => 'Senapelan'],
            ['code' => '14.71.05.1002', 'name' => 'Sago', 'district' => 'Senapelan'],
            ['code' => '14.71.05.1003', 'name' => 'Kampung Baru', 'district' => 'Senapelan'],
            ['code' => '14.71.05.1004', 'name' => 'Kampung Dalam', 'district' => 'Senapelan'],
            ['code' => '14.71.05.1005', 'name' => 'Kampung Bandar', 'district' => 'Senapelan'],
            ['code' => '14.71.05.1006', 'name' => 'Padang Terubuk', 'district' => 'Senapelan'],

            // Kecamatan Rumbai Barat
            ['code' => '14.71.06.1003', 'name' => 'Rumbai Bukit', 'district' => 'Rumbai Barat'],
            ['code' => '14.71.06.1004', 'name' => 'Muarafajar Timur', 'district' => 'Rumbai Barat'],
            ['code' => '14.71.06.1005', 'name' => 'Muarafajar Barat', 'district' => 'Rumbai Barat'],
            ['code' => '14.71.06.1006', 'name' => 'Rantaupanjang', 'district' => 'Rumbai Barat'],
            ['code' => '14.71.06.1007', 'name' => 'Maharani', 'district' => 'Rumbai Barat'],
            ['code' => '14.71.06.1008', 'name' => 'Agrowisata', 'district' => 'Rumbai Barat'],

            // Kecamatan Bukit Raya
            ['code' => '14.71.07.1005', 'name' => 'Simpang Tiga', 'district' => 'Bukit Raya'],
            ['code' => '14.71.07.1006', 'name' => 'Tangkerang Selatan', 'district' => 'Bukit Raya'],
            ['code' => '14.71.07.1007', 'name' => 'Tangkerang Utara', 'district' => 'Bukit Raya'],
            ['code' => '14.71.07.1008', 'name' => 'Tangkerang Labuai', 'district' => 'Bukit Raya'],
            ['code' => '14.71.07.1009', 'name' => 'Airdingin', 'district' => 'Bukit Raya'],

            // Kecamatan Marpoyan Damai
            ['code' => '14.71.09.1001', 'name' => 'Tangkerang Barat', 'district' => 'Marpoyan Damai'],
            ['code' => '14.71.09.1002', 'name' => 'Tangkerang Tengah', 'district' => 'Marpoyan Damai'],
            ['code' => '14.71.09.1003', 'name' => 'Sidomulyo Timur', 'district' => 'Marpoyan Damai'],
            ['code' => '14.71.09.1004', 'name' => 'Wonorejo', 'district' => 'Marpoyan Damai'],
            ['code' => '14.71.09.1005', 'name' => 'Maharatu', 'district' => 'Marpoyan Damai'],
            ['code' => '14.71.09.1006', 'name' => 'Perhentianmarpoyan', 'district' => 'Marpoyan Damai'],

            // Kecamatan Tenayan Raya
            ['code' => '14.71.10.1002', 'name' => 'Bencahlesung', 'district' => 'Tenayan Raya'],
            ['code' => '14.71.10.1003', 'name' => 'Tangkerang Timur', 'district' => 'Tenayan Raya'],
            ['code' => '14.71.10.1004', 'name' => 'Rejosari', 'district' => 'Tenayan Raya'],
            ['code' => '14.71.10.1005', 'name' => 'Bambukuning', 'district' => 'Tenayan Raya'],
            ['code' => '14.71.10.1010', 'name' => 'Melebung', 'district' => 'Tenayan Raya'],
            ['code' => '14.71.10.1011', 'name' => 'Industritenayan', 'district' => 'Tenayan Raya'],
            ['code' => '14.71.10.1012', 'name' => 'Sialangsakti', 'district' => 'Tenayan Raya'],
            ['code' => '14.71.10.1013', 'name' => 'Kulimjaya', 'district' => 'Tenayan Raya'],

            // Kecamatan Payung Sekaki
            ['code' => '14.71.11.1001', 'name' => 'Tampan', 'district' => 'Payung Sekaki'],
            ['code' => '14.71.11.1002', 'name' => 'Labuh Baru Timur', 'district' => 'Payung Sekaki'],
            ['code' => '14.71.11.1003', 'name' => 'Labuh Baru Barat', 'district' => 'Payung Sekaki'],
            ['code' => '14.71.11.1004', 'name' => 'Air Hitam', 'district' => 'Payung Sekaki'],
            ['code' => '14.71.11.1005', 'name' => 'Bandarraya', 'district' => 'Payung Sekaki'],
            ['code' => '14.71.11.1007', 'name' => 'Tirtasiak', 'district' => 'Payung Sekaki'],

            // Kecamatan Rumbai
            ['code' => '14.71.12.1001', 'name' => 'Meranti Pandak', 'district' => 'Rumbai'],
            ['code' => '14.71.12.1004', 'name' => 'Lembah Damai', 'district' => 'Rumbai'],
            ['code' => '14.71.12.1006', 'name' => 'Limbungan Baru', 'district' => 'Rumbai'],
            ['code' => '14.71.12.1009', 'name' => 'Sri Meranti', 'district' => 'Rumbai'],
            ['code' => '14.71.12.1010', 'name' => 'Palas', 'district' => 'Rumbai'],
            ['code' => '14.71.12.1011', 'name' => 'Umban Sari', 'district' => 'Rumbai'],

            // Kecamatan Tuahmadani
            ['code' => '14.71.13.1001', 'name' => 'Sidomulyo Barat', 'district' => 'Tuahmadani'],
            ['code' => '14.71.13.1002', 'name' => 'Sialangmunggu', 'district' => 'Tuahmadani'],
            ['code' => '14.71.13.1003', 'name' => 'Tuahkarya', 'district' => 'Tuahmadani'],
            ['code' => '14.71.13.1004', 'name' => 'Tuahmadani', 'district' => 'Tuahmadani'],

            // Kecamatan Kulim
            ['code' => '14.71.14.1001', 'name' => 'Kulim', 'district' => 'Kulim'],
            ['code' => '14.71.14.1002', 'name' => 'Mentangor', 'district' => 'Kulim'],
            ['code' => '14.71.14.1003', 'name' => 'Sialangrampai', 'district' => 'Kulim'],
            ['code' => '14.71.14.1004', 'name' => 'Pebatuan', 'district' => 'Kulim'],
            ['code' => '14.71.14.1005', 'name' => 'Pematangkapau', 'district' => 'Kulim'],

            // Kecamatan Rumbai Timur
            ['code' => '14.71.15.1001', 'name' => 'Tebing Tinggi Okura', 'district' => 'Rumbai Timur'],
            ['code' => '14.71.15.1002', 'name' => 'Sungaiukai', 'district' => 'Rumbai Timur'],
            ['code' => '14.71.15.1003', 'name' => 'Sungaiambang', 'district' => 'Rumbai Timur'],
            ['code' => '14.71.15.1004', 'name' => 'Lembah Sari', 'district' => 'Rumbai Timur'],
            ['code' => '14.71.15.1005', 'name' => 'Limbungan', 'district' => 'Rumbai Timur'],

        ];

        foreach ($locations as $location) {
            Location::create($location);
        }

        $this->command->info('✅ Seeded ' . count($locations) . ' locations successfully!');
    } 
}
