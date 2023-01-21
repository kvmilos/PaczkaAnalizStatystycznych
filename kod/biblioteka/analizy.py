def max_co2_p_c(dane):
    return dane.groupby('Year').apply(lambda df: df.nlargest(5, 'Per Capita')[['Country', 'Per Capita', 'Total']])


def max_gdp_p_c(dane):
    dane['GDP per capita'] = dane['GDP'] / dane['Population']
    return dane.groupby('Year').apply(lambda df: df.nlargest(5, 'GDP per capita'))[['Country', 'GDP per capita', 'GDP']]


def co2_change_p_c(dane):
    dane = dane.sort_values(by='Year')
    last_year = dane.Year.unique()[-1]
    year2 = last_year - 10
    pivot = dane[dane.Year.isin([year2, last_year])].pivot_table(values='Per Capita', index='Country', columns='Year')
    pivot['change'] = pivot[last_year] - pivot[year2]
    pivot = pivot.dropna()
    pivot = pivot.sort_values(by='change', ascending=False)
    pivot2 = pivot.sort_values(by='change', ascending=True)
    return pivot.head(5), pivot2.head(5)

