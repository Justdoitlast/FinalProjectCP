<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class gamedb extends Model
{
    protected $table = 'gamedb';
    //SELECT DISTINCT release_year FROM gamedb ORDER BY `gamedb`.`release_year` ASC
}
