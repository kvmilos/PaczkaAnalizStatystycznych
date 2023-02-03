from kod.paczka import pliki
import pytest
import argparse as ap
def test_wczytaj_dane1():
    parser = ap.ArgumentParser()
    parser.add_argument("GDP")
    parser.add_argument("Population")
    parser.add_argument("Emissions")
    parser.add_argument("rangemin")
    parser.add_argument("rangemax")
    args = parser.parse_args(["../dane/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562.csv",
                            "../dane/API_SP.POP.TOTL_DS2_en_csv_v2_4751604.csv",
                            "../dane/fossil-fuel-co2-emissions-by-nation_csv.csv",
                            "ahah",
                            "2005"])
    with pytest.raises(KeyError, match="The first year in range must be a number!"):
        pliki.wczytaj_dane(args)

def test_wczytaj_dane2():
    parser = ap.ArgumentParser()
    parser.add_argument("GDP")
    parser.add_argument("Population")
    parser.add_argument("Emissions")
    parser.add_argument("rangemin")
    parser.add_argument("rangemax")
    args = parser.parse_args(["../dane/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562.csv",
                            "../dane/API_SP.POP.TOTL_DS2_en_csv_v2_4751604.csv",
                            "../dane/fossil-fuel-co2-emissions-by-nation_csv.csv",
                            "1980",
                            "haha"])
    with pytest.raises(KeyError, match="The last year in range must be a number!"):
        pliki.wczytaj_dane(args)

def test_wczytaj_dane3():
    parser = ap.ArgumentParser()
    parser.add_argument("GDP")
    parser.add_argument("Population")
    parser.add_argument("Emissions")
    parser.add_argument("rangemin")
    parser.add_argument("rangemax")
    args = parser.parse_args(["../dane/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562.csv",
                            "../dane/API_SP.POP.TOTL_DS2_en_csv_v2_4751604.csv",
                            "../dane/fossil-fuel-co2-emissions-by-nation_csv.csv",
                            "1990",
                            "1980"])
    with pytest.raises(ValueError, match="The last year must be a value higher than the first year!"):
        pliki.wczytaj_dane(args)
