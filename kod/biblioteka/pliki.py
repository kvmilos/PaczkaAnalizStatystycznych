import pandas as pd
import argparse as ap


def pobierz_dane():
    parser = ap.ArgumentParser()
    parser.add_argument('GDP', help='GDP_file to be read')
    parser.add_argument('Population', help='Population_file to be read')
    parser.add_argument('Emissions', help='Emissions_file to be read')
    parser.add_argument('rangemin', default=0, help='First year in range')
    parser.add_argument('rangemax', default=0, help='Last year in range')
    args = parser.parse_args()
    return pd.read_csv(args.GDP, skiprows=4), pd.read_csv(args.Population, skiprows=4), pd.read_csv(
        args.Emissions), args.rangemin, args.rangemax
