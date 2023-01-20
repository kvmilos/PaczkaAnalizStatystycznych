from kod.biblioteka.pliki import pobierz_dane
from kod.biblioteka.dane import przerob, oczysc, scal
from kod.biblioteka.analizy import max_co2_per_capita, max_gdp_per_capita, co2_change_per_capita


def polecenie():
    gdp, pop, co2, rangemin, rangemax = pobierz_dane()
    gdp, pop, co2 = przerob(gdp, pop, co2, rangemin, rangemax)
    gdp, pop, co2 = oczysc(gdp, pop, co2)
    dane = scal(gdp, pop, co2)
    print(dane)
    print(max_co2_per_capita(dane))
    print(max_gdp_per_capita(dane))
    gora, dol = co2_change_per_capita(dane)
    print(gora)
    print(dol)


polecenie()
