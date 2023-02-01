import numpy as np
import pandas as pd
from paczka.dict import countries_dict


def lata_scal(gdp, pop, co2, rangemin, rangemax):
    try:
        lata_gdp = gdp.columns[4:-1].astype("int64")
    except:
        raise ValueError("Określone nazwy kolumn w pliku GDP nie są liczbami, możliwe, że format pliku został zmieniony")
    try:
        lata_pop = pop.columns[4:-1].astype("int64")
    except:
        raise ValueError("Określone nazwy kolumn w pliku Population nie są liczbami, możliwe, że format pliku został zmieniony")
    lata_co2 = list(np.unique(co2.Year))
    minimum = max(min(lata_gdp), min(lata_pop), min(lata_co2), rangemin)
    maksimum = min(max(lata_gdp), max(lata_pop), max(lata_co2), rangemax)
    lata = []
    for i in range(minimum, maksimum + 1):
        lata.append(str(i))
    return lata


def kraje(dane1, dane2):
    assert 'Country' in dane1.columns, "DataFrame nr 1 nie zawiera kolumny Country"
    assert 'Country' in dane2.columns, "DataFrame nr 2 nie zawiera kolumny Country"
    dane1['Country'] = dane1['Country'].str.upper()
    dic = countries_dict()
    for _, row in dane1.iterrows():
        if row['Country'] in dic:
            dane1.at[row.name, 'Country'] = dic[row['Country']]
    for _, row in dane2.iterrows():
        if row['Country'] in dic:
            dane2.at[row.name, 'Country'] = dic[row['Country']]
    return dane1, dane2


def przerob(gdp, pop, co2, lata):
    assert 'Country Name' in gdp.columns, "DataFrame GDP nie zawiera kolumny Country Name"
    assert 'Country Name' in pop.columns, "DataFrame Population nie zawiera kolumny Country Name"
    assert 'Year' in co2.columns, "DataFrame Emissions nie zawiera kolumny Year"
    assert len(lata)>0, "Podano pusty zakres lat"
    plik_gdp = pd.DataFrame(gdp[['Country Name'] + lata])
    plik_pop = pd.DataFrame(pop[['Country Name'] + lata])
    plik_co2 = pd.DataFrame(co2[co2.Year.astype(str).isin(lata)])
    return plik_gdp, plik_pop, plik_co2


def oczysc(gdp, pop, co2):
    for column in gdp.columns[1:]:
        assert gdp[column].dtype == int or gdp[column].dtype == float, f"Kolumna {column} w DF GDP nie zawiera wartości liczbowych"
        gdp[column] = gdp[column].fillna(value=gdp[column].mean())
    for column in pop.columns[1:]:
        assert pop[column].dtype == int or pop[column].dtype == float, f"Kolumna {column} w DF Population nie zawiera wartości liczbowych"
        pop[column] = pop[column].fillna(value=pop[column].mean())
    for column in co2.columns[2:]:
        assert co2[column].dtype == int or co2[column].dtype == float, f"Kolumna {column} w DF Emissions nie zawiera wartości liczbowych"
        co2[column] = co2[column].fillna(value=co2[column].mean())
    return gdp, pop, co2


def scal(gdp, pop, co2):
    assert 'Country Name' in gdp.columns, "DataFrame GDP nie zawiera kolumny Country Name"
    assert 'Country Name' in pop.columns, "DataFrame Population nie zawiera kolumny Country Name"
    gdp_melted = gdp.melt(id_vars=['Country Name'], var_name='Year', value_name="GDP")
    pop_melted = pop.melt(id_vars=['Country Name'], var_name='Year', value_name="Population")
    dane = pd.merge(gdp_melted, pop_melted, on=['Country Name', 'Year'], suffixes=['_GDP', '_Pop'])
    dane.rename(columns={'Country Name': 'Country'}, inplace=True)
    dane = dane.astype({'Year': 'int64'})
    dane, co2 = kraje(dane, co2)
    assert 'Year' in co2.columns, "DataFrame Emissions nie zawiera kolumny Year"
    dane = pd.merge(dane, co2, on=['Year', 'Country'])
    return dane
