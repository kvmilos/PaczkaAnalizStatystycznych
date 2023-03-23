# Paczka Analiz Statystycznych
Projekt indywidualny wykonany w ramach zaliczenia przedmiotu "Narzędzia programistyczne w Pythonie wspierające analizę danych"

Individaul project prepared as part of the 'Tools Supporting Data Analysis in Python' course

Treść polecenia:  
Zadanie zaliczeniowe z NYPD  
12 XII 2022 Wersja 1.0  

Polecenie  
Należy napisać w Pythonie program, który:  
&emsp;● Pobiera (używając argparse) z wiersza poleceń ścieżki do plików (w formacie csv) z danymi o GDP, populacji i emisji.  
&emsp;● Zakłada że są w formacie jaki dziś (choć w przyszłości danych może być więcej, czyli nie można założyć, że program ma działać dokładnie na tych plikach, które są dołączone do zadania, natomiast należy założyć, że format będzie zachowany) i je wczytuje.  
&emsp;● Czyści te dane (w tym punkcie nie ma wiele do zrobienia w odniesieniu do podanych źródeł danych).  
&emsp;● Wybiera tylko te lata, które są we wszystkich tabelach. Uwaga: chodzi o lata faktycznie występujące w tych tabelach, także w przyszłości, tzn. nie można w docelowej wersji na sztywno założyć (zaszyć w kodzie), że są to dane za lata 1960-2014), choć w pierwszych wersjach rozwiązania to może być wygodne.  
&emsp;● Scala dane po krajach i latach.  
&emsp;● Przeprowadza analizy (za pomocą bibliotek numpy lub panadas):  
&emsp;&emsp;○ Które kraje w poszczególnych latach z danymi, emitują najwięcej CO2 w przeliczeniu na mieszkańca. To znaczy generuje posortowaną po latach tabelkę pięcioma krajami o największej emisji na osobę (z podaną nazwą kraju, emisją na osobę i całkowitą emisją.  
&emsp;&emsp;○ Które kraje w poszczególnych latach z danymi mają największy przychód mieszkańca. To znaczy generuje posortowaną po latach tabelkę pięcioma krajami o największym dochodzie na mieszkańca (z podaną nazwą kraju, dochodem na mieszkańca i całkowitym dochodem).  
&emsp;&emsp;○ Które kraje (w przeliczeniu na mieszkańca) najbardziej zmniejszyły i zwiększyły przez ost. 10 lat (z danych) emisję CO2.

Dodatkowe wymagania  
&emsp;● Program powinien być podzielony na (co najmniej) dwa pythonowe moduły (nie muszą być duże) jeden zawierający bibliotekę operacji analizujących dane zgodnie z treścią zadania i drugi wywołujący te operacje.  
&emsp;● Oczekujemy, że źródła programu będą w repozytorium gita, z co najmniej pięcioma (5) uaktualnieniami (ang. commit),  
&emsp;● Oczekujemy złożenia (i przyjęcia) jednej prośby o dołączenie kodu (ang. pull requesta)?  
&emsp;● Testów jednostkowych kodu (tam gdzie to ma sens).  
&emsp;● Sprofilowania działania programu (należy dołączyć do rozwiązania plik z wynikiem
profilowania, nie ma obowiązku przeprowadzania samych optymalizacji).  
&emsp;● Program powinien pozwalać zadawać w wierszu poleceń zakres lat (parametry -start rok i -koniec rok), wówczas badanych okres jest dodatkowo skracany do do podanego przedziału. Jeśli przedział po tej operacji okaże się pusty, należy zgłosić
(i gdzieś w programie obsłużyć) wyjątek.  
&emsp;● Program może mieć postać zwykłego programu lub Jupyterowego notatnika.  
&emsp;● Program należy dostarczyć w postaci pakietu instalowalnego poleceniem pip (w
postaci `pip install ./ścieżka/do_pakietu`).  
&emsp;● Jeśli program wykryje jakieś niezgodności w danych (np. brak jakiegoś Państwa w
niektórych danych), to powinien wypisać czytelny komunikat i działać dalej.  

W programie oceniamy:  
&emsp;● Podział na moduły, funkcje, wprowadzenie parametrów,  
&emsp;● Jakość kodu (nazwy zmiennych i funkcji, komentarze).  
&emsp;● Sugerujemy stosowanie narzędzi automatycznie sprawdzających (część)  
zaleceń dotyczących czytelności kodu. Takie narzędzia mogą Państwo mieć wbudowane w Państwa IDE (np. W Pycharma) lub mogą Państwo skorzystać z zewnętrznych narzędzi (pylint, flake, ...),  
&emsp;● Warto również przeczytać zalecenia z Przewodnika po stylu kodu w Pythonie PEP-8.  
&emsp;● Pokrycie kodu testami.  
&emsp;● Użycie bibliotek przedstawianych podczas zajęć.  
&emsp;● Dostarczone pliki (np. wynik profilowania).  
