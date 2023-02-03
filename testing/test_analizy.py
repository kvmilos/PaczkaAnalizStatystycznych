import pandas as pd
from kod.paczka import analizy
import pytest

def test_max_co2_per_capita():
    with pytest.raises(Exception, match="DataFrame nie zawiera kolumny Per Capita"):
        data = pd.DataFrame({'Country': ['A', 'B', 'C', 'D'],
                             'Year': [1, 2, 3, 4],
                             'Population': [4, 5, 6, 7],
                             'Total': [0.5, 0.6, 0.7, 0.8]})
        analizy.max_co2_per_capita(data)

def test_max_gdp_per_capita1():
    with pytest.raises(Exception, match="DataFrame nie zawiera kolumny GDP"):
        data = pd.DataFrame({'Country': ['A', 'B', 'C', 'D'],
                             'Year': [1, 2, 3, 4],
                             'Population': [4, 5, 6, 7],
                             'Total': [0.5, 0.6, 0.7, 0.8]})
        analizy.max_gdp_per_capita(data)

def test_max_gdp_per_capita2():
    with pytest.raises(Exception, match="DataFrame nie zawiera kolumny Population"):
        data = pd.DataFrame({'Country': ['A', 'B', 'C', 'D'],
                             'Year': [1, 2, 3, 4],
                             'GDP': [4, 5, 6, 7],
                             'Total': [0.5, 0.6, 0.7, 0.8]})
        analizy.max_gdp_per_capita(data)

def test_co2_change_per_capita1():
    with pytest.raises(Exception, match="DataFrame nie zawiera kolumny Year"):
        data = pd.DataFrame({'Country': ['A', 'B', 'C', 'D'],
                             'GDP': [4, 5, 6, 7],
                             'Total': [0.5, 0.6, 0.7, 0.8]})
        rangemin = 2010
        rangemax = 2020
        analizy.co2_change_per_capita(data, rangemin, rangemax)

def test_co2_change_per_capita2():
    with pytest.raises(ValueError, match="Zakres wynosi mniej niż 10 lat"):
        data = pd.DataFrame({'Country': ['A', 'B', 'C', 'D'],
                             'Year': [2000, 2005, 2010, 2015],
                             'GDP': [4, 5, 6, 7],
                             'Total': [0.5, 0.6, 0.7, 0.8]})
        rangemin = 2010
        rangemax = 2019
        analizy.co2_change_per_capita(data, rangemin, rangemax)
