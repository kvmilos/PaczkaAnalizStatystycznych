def max_co2_per_capita(dane):
    if 'Per Capita' not in dane.columns:
        raise Exception("DataFrame nie zawiera kolumny Per Capita")
    return dane.groupby('Year').apply(lambda df: df.nlargest(5, 'Per Capita')[['Country', 'Per Capita', 'Total']])



def max_gdp_per_capita(dane):
    if 'GDP' not in dane.columns:
        raise Exception("DataFrame nie zawiera kolumny GDP")
    if 'Population' not in dane.columns:
        raise Exception("DataFrame nie zawiera kolumny Population")
    dane['GDP per capita'] = dane['GDP'] / dane['Population']
    return dane.groupby('Year').apply(lambda df: df.nlargest(5, 'GDP per capita'))[['Country', 'GDP per capita', 'GDP']]


def co2_change_per_capita(dane, rangemin, rangemax):
    if 'Year' not in dane.columns:
        raise Exception("DataFrame nie zawiera kolumny Year")
    if rangemax < rangemin + 10:
        raise ValueError("Zakres wynosi mniej niż 10 lat")
    dane = dane.sort_values(by='Year')
    last_year = dane.Year.unique()[-1]
    year2 = last_year - 10
    pivot = dane[dane.Year.isin([year2, last_year])].pivot_table(values='Per Capita', index='Country', columns='Year')
    pivot['change'] = pivot[last_year] - pivot[year2]
    pivot = pivot.dropna()
    pivot = pivot.sort_values(by='change', ascending=False)
    pivot2 = pivot.sort_values(by='change', ascending=True)
    return pivot.head(5), pivot2.head(5)

