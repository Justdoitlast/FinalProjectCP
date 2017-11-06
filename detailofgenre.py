import numpy  as np
import pygal
from pygal import *
from pygal.style import * 
import pandas as pd
import matplotlib.pyplot as plt
games = pd.read_csv('C:/Users/Chalermwong/Desktop/ign.csv')
genre = dict(games['genre'].value_counts())
platform = dict(games['platform'].value_counts())
release_year = dict(games['release_year'].value_counts())
pie_chart = pygal.Pie()
pie_chart.title = 'Generation of games'
n = 0
try:
    for i in genre:
        pie_chart.add(i, [genre[i]])
except Exception as e:
    print(e)
pie_chart.render_to_file('bar_chart.svg')
