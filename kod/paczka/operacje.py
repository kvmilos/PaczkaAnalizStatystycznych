from paczka import dane, analizy, pliki

def operacje():
    args = pliki.pobierz_dane()
    gdp, pop, co2, rangemin, rangemax = pliki.wczytaj_dane(args)
    lata = dane.lata_scal(gdp, pop, co2, rangemin, rangemax)
    gdp, pop, co2 = dane.przerob(gdp, pop, co2, lata)
    gdp, pop, co2 = dane.oczysc(gdp, pop, co2)
    data = dane.scal(gdp, pop, co2)
    print(analizy.max_co2_per_capita(data))
    print(analizy.max_gdp_per_capita(data))
    gora, dol = analizy.co2_change_per_capita(data, rangemin, rangemax)
    print(gora)
    print(dol)

if __name__ == "__main__":
    operacje()
