# Opis problemu (programu):
# --------------------------
# Program pobiera liczbę naturalną od uzytkownika i wypisuje slownie typ tej liczby.
# 1. Dla liczby wiekszej niz 100 wypisz ":-)"
# 2. Dla liczby rownej 100 wypisz ":-|"
# 3. Dla liczby mniejszej niz 100 wypisz ":-"


# Algorytm:
# --------------------------
# 1. PRZYPISZ parametr(number) do zmiennej
# 2. PRZEKONWERTUJ parametr(number) z ekranu na liczbę
# 2. JEZELI parametr > 100 TO wypisz ":-"
# 3. JEZELI parametr = 100 TO wypisz ":-|"
# 4. JEZELI parametr < 100 TO wypisz ":-)"

# Implementacja:
# --------------------------

# 1. Przypisać parametr do zmiennej (wczytać parametr)

import sys 

number = sys.argv[1]

if number == '100':
    print(":-|")
if number > '100':
    print(":-)")
if number < '100':
    print(":-")