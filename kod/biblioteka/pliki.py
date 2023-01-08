import pandas as pd
def pobierz(sciezka1, sciezka2, sciezka3):
    return pd.read_csv(sciezka1, skiprows = 4), pd.read_csv(sciezka2, skiprows = 4), pd.read_csv(sciezka3)
