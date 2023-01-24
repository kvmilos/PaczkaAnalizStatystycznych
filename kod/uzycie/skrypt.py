from kod.paczka.pliki import pobierz_dane, wczytaj_dane
from kod.paczka.dane import lata_scal, przerob, oczysc, scal
from kod.paczka.analizy import max_co2_per_capita, max_gdp_per_capita, co2_change_per_capita


def polecenie():
    gdp, pop, co2, rangemin, rangemax = wczytaj_dane(pobierz_dane())
    lata = lata_scal(gdp, pop, co2, rangemin, rangemax)
    gdp, pop, co2 = przerob(gdp, pop, co2, lata)
    gdp, pop, co2 = oczysc(gdp, pop, co2)
    dane = scal(gdp, pop, co2)
    gora, dol = co2_change_per_capita(dane)
    print(max_co2_per_capita(dane))
    print(max_gdp_per_capita(dane))
    print(gora)
    print(dol)


if __name__ == "__main__":
    polecenie()
