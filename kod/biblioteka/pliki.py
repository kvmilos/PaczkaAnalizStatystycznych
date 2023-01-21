import pandas as pd
import argparse as ap


def pobierz_dane():
    parser = ap.ArgumentParser()
    parser.add_argument('GDP', help='GDP_file to be read')
    parser.add_argument('Population', help='Population_file to be read')
    parser.add_argument('Emissions', help='Emissions_file to be read')
    parser.add_argument('rangemin', default=0, help='First year in range', nargs="?")
    parser.add_argument('rangemax', default=3000, help='Last year in range', nargs="?")
    args = parser.parse_args()
    try:
        assert isinstance(int(args.rangemin), int)
    except ValueError:
        raise KeyError("The first year in range must be a number!")
    try:
        assert isinstance(int(args.rangemax), int)
    except ValueError:
        raise KeyError("The last year in range must be a number!")
    return pd.read_csv(args.GDP, skiprows=4), pd.read_csv(args.Population, skiprows=4), pd.read_csv(
        args.Emissions), int(args.rangemin), int(args.rangemax)
