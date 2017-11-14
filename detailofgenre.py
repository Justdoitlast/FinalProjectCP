import numpy  as np
import pygal
from pygal import *
from pygal.style import * 
import pandas as pd
import matplotlib.pyplot as plt
from pygal.style import NeonStyle
games = pd.read_csv('C:/Users/Chalermwong/Desktop/ign.csv')
genre = dict(games['genre'].value_counts())
platform = dict(games['platform'].value_counts())
release_year = dict(games['release_year'].value_counts())
games.index = games['title']
def Generation():
    pie_chart = pygal.Pie()
    pie_chart.title = 'Generation of games'
    top = 10
    try:
        for i in genre:
            if top == 1:
                break
            pie_chart.add(i, [genre[i]])
            top -= 1
    except Exception as e:
        print(e)
    pie_chart.render_to_file('bar_chart.svg')

def genreofyear():
    #games['count'] = 0
    bar_chart = pygal.HorizontalBar()
    #fil = games.groupby(['release_year', 'genre']).count()
    sports = games[(games.genre == 'Sports') & (games.release_year == 2012)]
    action = games[(games.genre == 'Action') & (games.release_year == 2012)]
    shooter = games[(games.genre == 'Shooter') & (games.release_year == 2012)]
    racing = games[(games.genre == 'Racing') & (games.release_year == 2012)]
    adventure = games[(games.genre == 'Adventure') & (games.release_year == 2012)]
    strategy = games[(games.genre == 'Strategy') & (games.release_year == 2012)]
    rpg = games[(games.genre == 'RPG') & (games.release_year == 2012)]
    platformer = games[(games.genre == 'Platformer') & (games.release_year == 2012)]
    puzzle = games[(games.genre == 'Puzzle') & (games.release_year == 2012)]
    #games.loc[games['release_year']== 2012] 
    sports = sports.loc[0:,['genre', 'release_year']]
    action = action.loc[0:,['genre', 'release_year']]
    shooter = shooter.loc[0:,['genre', 'release_year']]
    racing = racing.loc[0:,['genre', 'release_year']]
    adventure = adventure.loc[0:,['genre', 'release_year']]
    strategy = strategy.loc[0:,['genre', 'release_year']]
    rpg = rpg.loc[0:,['genre', 'release_year']]
    platformer = platformer.loc[0:,['genre', 'release_year']]
    puzzle = puzzle.loc[0:,['genre', 'release_year']]

    sports = sports.count()[0]
    action = action.count()[0]
    shooter = shooter.count()[0]
    racing = racing.count()[0]
    adventure = adventure.count()[0]
    strategy = strategy.count()[0]
    rpg = rpg.count()[0]
    platformer = platformer.count()[0]
    puzzle = puzzle.count()[0]

    bar_chart.title = 'the most genre of 2012 '+str(2012)
    bar_chart.add('Sports', int(sports))
    bar_chart.add('Action', action)
    bar_chart.add('Shooter', shooter)
    bar_chart.add('racing', racing)
    bar_chart.add('adventure', adventure)
    bar_chart.add('strategy', strategy)
    bar_chart.add('platformer', platformer)
    bar_chart.add('puzzle', puzzle)
    bar_chart.render_to_file('genreofyear.svg')
    

    #bar_chart.render_to_file('bar_of_year.svg')
    #print(fil])
    #print(sports
def yearofgame():
    bar_chart = pygal.StackedLine(fill=True, interpolate='cubic', style=NeonStyle)
    bar_chart.title  = 'The most games release'
    get = SortedDisplayDict(release_year)
    get = dict(sorted(get.items()))
    bar_chart.x_labels = map(str, get.keys())
    bar_chart.add('games', get.values())
    bar_chart.render_to_file('yearofgame.svg')

def splityear():
    get = games['release_year'].unique()
    print(get[1])




class SortedDisplayDict(dict):
   def __str__(self):  #sorted keys of dict
       return "{" + ", ".join("%r: %r" % (key, self[key]) for key in sorted(self)) + "}"

genreofyear()
