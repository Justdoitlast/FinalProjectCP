<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class GameDB extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('gamedb', function (Blueprint $table) {
            $table->increments('id');
            $table->string('score_phrase');
            $table->string('title');
            $table->string('url');
            $table->string('platform');
            $table->string('score');
            $table->string('genre');
            $table->string('release_year');
            $table->string('release_month');
            $table->string('release_day');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::drop('gamedb');
    }
}
