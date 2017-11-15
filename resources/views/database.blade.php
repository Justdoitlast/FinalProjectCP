<!DOCTYPE html>
<html lang="{{ app()->getLocale() }}">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- CSRF Token -->
    <meta name="csrf-token" content="{{ csrf_token() }}">
    <title>{{ config('app.name', 'Laravel') }}</title>
    <link href="{{ asset('css/app.css') }}" rel="stylesheet">
</head>
<body>
    <div id="app">
        <div class="row" style="margin-right: 0;">
            <div class="col-md-4 aside">
                <a href="/">
                    <h1 class="col-md-12" align="center">{{ config('app.name', 'Laravel') }}</h1>
                </a>
                <a class="aside-btn col-md-12" href="/database/">Home</a>
                @php
                    use App\gamedb;
                    $gamedbs = App\gamedb::distinct('release_year') -> select('release_year') -> orderBy('release_year', 'asc') -> get();
                    foreach($gamedbs as $key => $value){
                        echo '<a class="aside-btn col-md-12" href="/database/'.$value['release_year'].'">'.$value['release_year'].'</a>';
                    }
                @endphp
                
            </div>
            <div class="col-md-8" style="padding-top:2em;">
                <div class="panel panel-default col-md-10">
                @if($year != '0000')
                    <div class="panel-heading">{{ $year }}</div>
                    <div class="panel-body">
                        <img src='/svg/year{{ $year }}.svg' />
                        <img src='/svg/plat{{ $year }}.svg' />
                    </div>
                @else
                    <div class="panel-body">
                        <img src='/svg/top_nine.svg' />
                        <img src='/svg/day_of_game.svg' />
                    </div>
                @endif
                </div>
            </div>
            
        </div>
    </div>


    <!-- Scripts -->
    <script src="{{ asset('js/app.js') }}"></script>
</body>
</html>
