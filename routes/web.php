<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('Welcome');
});
Route::get('/database', function () {
    return view('database')->with('year', '0000');;
});
Route::get('/database/{year}', function ($year) {
    return view('database')->with('year', $year);;
});
