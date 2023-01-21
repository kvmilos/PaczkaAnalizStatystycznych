import numpy as np
import pandas as pd
from kod.biblioteka.dict import countries_dict


def lata_scal(gdp, pop, co2, rangemin, rangemax):
    lata_gdp = gdp.columns[4:-1].astype("int64")
    lata_pop = pop.columns[4:-1].astype("int64")
    lata_co2 = list(np.unique(co2.Year))

    minimum = max(min(lata_gdp), min(lata_pop), min(lata_co2), rangemin)
    maksimum = min(max(lata_gdp), max(lata_pop), max(lata_co2), rangemax)
    lata = []
    for i in range(minimum, maksimum + 1):
        lata.append(str(i))
    return lata


def kraje(dane1, dane2):
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
    plik_gdp = pd.DataFrame(gdp[['Country Name'] + lata])
    plik_pop = pd.DataFrame(pop[['Country Name'] + lata])
    plik_co2 = pd.DataFrame(co2[co2.Year.astype(str).isin(lata)])
    return plik_gdp, plik_pop, plik_co2


def oczysc(gdp, pop, co2):
    for column in gdp.columns[1:]:
        gdp[column] = gdp[column].fillna(value=gdp[column].mean())
    for column in pop.columns[1:]:
        pop[column] = pop[column].fillna(value=pop[column].mean())
    for column in co2.columns[2:]:
        co2[column] = co2[column].fillna(value=co2[column].mean())
    return gdp, pop, co2


def scal(gdp, pop, co2):
    gdp_melted = gdp.melt(id_vars=['Country Name'], var_name='Year', value_name="GDP")
    pop_melted = pop.melt(id_vars=['Country Name'], var_name='Year', value_name="Population")
    dane = pd.merge(gdp_melted, pop_melted, on=['Country Name', 'Year'], suffixes=['_GDP', '_Pop'])
    dane.rename(columns={'Country Name': 'Country'}, inplace=True)
    dane = dane.astype({'Year': 'int64'})
    dane, co2 = kraje(dane, co2)
    dane = pd.merge(dane, co2, on=['Year', 'Country'])
    return dane
