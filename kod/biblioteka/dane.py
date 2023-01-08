import numpy as np

def scal(gdp, pop, co2):
    lata_gdp = gdp.columns[4:-1].astype("int64")
    lata_pop = pop.columns[4:-1].astype("int64")
    lata_co2 = list(np.unique(co2.Year))
    minimum = min(min(lata_gdp), min(lata_pop), min(lata_co2))
    maksimum = max(max(lata_gdp), max(lata_pop), max(lata_co2)) + 1
    lata_scal = []
    for i in range(minimum, maksimum):
        if i in lata_gdp and i in lata_pop and i in lata_co2:
            lata_scal.append(str(i))
    plik_gdp = gdp[['Country Name'] + lata_scal]
    plik_pop = pop[['Country Name'] + lata_scal]
    plik_co2 = co2[co2.Year.astype(str).isin(lata_scal)]
    
