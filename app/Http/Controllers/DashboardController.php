<?php

namespace App\Http\Controllers;

use Illuminate\Support\Facades\File;
use Inertia\Inertia;

class DashboardController extends Controller
{
    public function index()
    {
        $summaryPath = base_path('../python/output/summary.json');

        $summary = [];

        if (File::exists($summaryPath)) {
            $summary = json_decode(File::get($summaryPath), true);
        }

        return Inertia::render('Dashboard/Index', [
            'summary' => $summary,
        ]);
    }
}
