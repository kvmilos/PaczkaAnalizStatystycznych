from kod.paczka import dane
import pandas as pd
import numpy as np
import pytest

def test_lata_scal1():
    with pytest.raises(Exception, match="Określone nazwy kolumn w pliku GDP nie są liczbami, możliwe, że format pliku został zmieniony"):
        gdp = pd.DataFrame(np.array([[0,0,0,1,1,1,1],[0,0,0,2,2,2,2],[0,0,0,3,3,3,3]]), columns=[1,2,3,4,'a','b','c'])
        dane.lata_scal(gdp, ".", ".", 1980, 1990)

def test_lata_scal2():
    with pytest.raises(Exception, match="Określone nazwy kolumn w pliku Population nie są liczbami, możliwe, że format pliku został zmieniony"):
        gdp = pd.DataFrame(np.array([[0,1,2,3,4,5],[1,2,3,4,5,6],[2,3,4,5,6,7]]), columns = [6,5,4,3,2,1])
        pop = pd.DataFrame(np.array([[0,0,0,1,1,1,1],[0,0,0,2,2,2,2],[0,0,0,3,3,3,3]]), columns=[1,2,3,4,'a','b','c'])
        dane.lata_scal(gdp, pop, ".", 1980, 1990)

def test_kraje1():
    with pytest.raises(Exception, match="DataFrame nr 1 nie zawiera kolumny Country"):
        data1 = pd.DataFrame(np.array([[0,1],[0,1]]),columns=['.','Countr'])
        data2 = pd.DataFrame(np.array([[0,1],[0,1]]),columns=['.','Country'])
        dane.kraje(data1, data2)

def test_kraje2():
    with pytest.raises(Exception, match="DataFrame nr 2 nie zawiera kolumny Country"):
        data1 = pd.DataFrame(np.array([[0,1],[0,1]]),columns=['.','Country'])
        data2 = pd.DataFrame(np.array([[0,1],[0,1]]),columns=['.','Countr'])
        dane.kraje(data1, data2)


def test_przerob1():
    with pytest.raises(Exception, match="DataFrame GDP nie zawiera kolumny Country Name"):
        gdp = pd.DataFrame(np.array([[0,1],[0,1]]), columns=['.','Country'])
        dane.przerob(gdp, 'a', 'a', [])

def test_przerob2():
    with pytest.raises(Exception, match="DataFrame Population nie zawiera kolumny Country Name"):
        gdp = pd.DataFrame(np.array([[0,1],[0,1]]), columns=['.','Country Name'])
        pop = pd.DataFrame(np.array([[0,1],[0,1]]), columns=['.','Country'])
        dane.przerob(gdp, pop, 'a', [])

def test_przerob3():
    with pytest.raises(Exception, match="DataFrame Emissions nie zawiera kolumny Year"):
        gdp = pd.DataFrame(np.array([[0,1],[0,1]]), columns=['.','Country Name'])
        pop = pd.DataFrame(np.array([[0,1],[0,1]]), columns=['.','Country Name'])
        co2 = pd.DataFrame(np.array([[0,1],[0,1]]), columns=['.','Rok'])
        dane.przerob(gdp, pop, co2, [])

def test_przerob4():
    with pytest.raises(Exception, match="Podano pusty zakres lat"):
        gdp = pd.DataFrame(np.array([[0, 1], [0, 1]]), columns=['.', 'Country Name'])
        pop = pd.DataFrame(np.array([[0, 1], [0, 1]]), columns=['.', 'Country Name'])
        co2 = pd.DataFrame(np.array([[0, 1], [0, 1]]), columns=['.', 'Year'])
        dane.przerob(gdp, pop, co2, [])

def test_oczysc1():
    gdp = pd.DataFrame({'Country': ['A', 'B', 'C', 'D'],
                        'Year1': [1, 2, 3, 'a'],
                        'Year2': [4, 5, 6, 7]})
    pop = pd.DataFrame({'Country': ['A', 'B', 'C', 'D'],
                        'Year1': [1, 2, 3, 4],
                        'Year2': [4, 5, 6, 7]})
    co2 = pd.DataFrame({'Country': ['A', 'B', 'C', 'D'],
                        'Year1': [1, 2, 3, 4],
                        'Year2': [4, 5, 6, 7],
                        'Emissions': [0.5, 0.6, 0.7, 0.8]})
    with pytest.raises(Exception, match="Kolumna Year1 w DF GDP nie zawiera wartości liczbowych"):
        dane.oczysc(gdp, pop, co2)

def test_oczysc2():
    gdp = pd.DataFrame({'Country': ['A', 'B', 'C', 'D'],
                        'Year1': [1, 2, 3, 4],
                        'Year2': [4, 5, 6, 7]})
    pop = pd.DataFrame({'Country': ['A', 'B', 'C', 'D'],
                        'Year1': [1, 2, 3, 4],
                        'Year2': [4, 5, 6, 'a']})
    co2 = pd.DataFrame({'Country': ['A', 'B', 'C', 'D'],
                        'Year1': [1, 2, 3, 4],
                        'Year2': [4, 5, 6, 7],
                        'Emissions': [0.5, 0.6, 0.7, 0.8]})
    with pytest.raises(Exception, match="Kolumna Year2 w DF Population nie zawiera wartości liczbowych"):
        dane.oczysc(gdp, pop, co2)

def test_oczysc3():
    gdp = pd.DataFrame({'Country': ['A', 'B', 'C', 'D'],
                        'Year1': [1, 2, 3, 4],
                        'Year2': [4, 5, 6, 7]})
    pop = pd.DataFrame({'Country': ['A', 'B', 'C', 'D'],
                        'Year1': [1, 2, 3, 4],
                        'Year2': [4, 5, 6, 7]})
    co2 = pd.DataFrame({'Country': ['A', 'B', 'C', 'D'],
                        'Year1': [1, 2, 3, 4],
                        'Year2': [4, 5, 6, 7],
                        'Emissions': [0.5, 0.6, 0.7, 'a']})
    with pytest.raises(Exception, match="Kolumna Emissions w DF Emissions nie zawiera wartości liczbowych"):
        dane.oczysc(gdp, pop, co2)

def test_scal1():
    gdp = pd.DataFrame({'Year': [2010, 2011, 2012], 'GDP': [1000, 2000, 3000]})
    pop = pd.DataFrame({'Year': [2010, 2011, 2012], 'Country Name': ['A', 'B', 'C'], 'Population': [100, 200, 300]})
    co2 = pd.DataFrame({'Year': [2010, 2011, 2012], 'Country': ['A', 'B', 'C'], 'Emissions': [10, 20, 30]})
    with pytest.raises(Exception, match="DataFrame GDP nie zawiera kolumny Country Name"):
        dane.scal(gdp, pop, co2)

def test_scal2():
    gdp = pd.DataFrame({'Year': [2010, 2011, 2012], 'Country Name': ['A', 'B', 'C'], 'GDP': [1000, 2000, 3000]})
    pop = pd.DataFrame({'Year': [2010, 2011, 2012], 'Population': [100, 200, 300]})
    co2 = pd.DataFrame({'Year': [2010, 2011, 2012], 'Country': ['A', 'B', 'C'], 'Emissions': [10, 20, 30]})
    with pytest.raises(Exception, match="DataFrame Population nie zawiera kolumny Country Name"):
        dane.scal(gdp, pop, co2)

def test_scal3():
    gdp = pd.DataFrame({'Year': [2010, 2011, 2012], 'Country Name': ['A', 'B', 'C'], 'GDP': [1000, 2000, 3000]})
    pop = pd.DataFrame({'Year': [2010, 2011, 2012], 'Country Name': ['A', 'B', 'C'], 'Population': [100, 200, 300]})
    co2 = pd.DataFrame({'Country': ['A', 'B', 'C'], 'Emissions': [10, 20, 30]})
    with pytest.raises(Exception, match="DataFrame Emissions nie zawiera kolumny Year"):
        dane.scal(gdp, pop, co2)

