# from kod.paczka.pliki import pobierz_dane
# from kod.paczka.dict import countries_dict
# from kod.paczka.dane import lata_scal, przerob, oczysc, kraje, scal
# from kod.paczka.analizy import max_co2_p_c, max_gdp_p_c, co2_change_p_c
# import pytest


# def test_pobierz_dane():
#     with pytest.raises(KeyError, match = "The first year in range must be a number!"):
#         pobierz_dane(rangemin="yolo")
#     with pytest.raises(KeyError, match = "The last year in range must be a number!"):
#         pobierz_dane(gdp="/Users/kvmilos/Desktop/NYPD/GDP/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562.csv", pop="/Users/kvmilos/Desktop/NYPD/population/API_SP.POP.TOTL_DS2_en_csv_v2_4751604.csv", co2="/Users/kvmilos/Desktop/NYPD/CO2/data/fossil-fuel-co2-emissions-by-nation_csv.csv", rangemin="2010", rangemax="lol")
#     gdp, population, emissions, rangemin, rangemax = pobierz_dane()
#     assert rangemax - rangemin >= 0

# def test_countries_dict():
    # assert

# def test_lata_scal():
