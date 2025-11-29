# Opis problemu (programu):
# --------------------------
# Program pobiera zmienna od uzytkownika i wypisuje slownie typ tej zmiennej.
# 1. Program pobiera zmienna z lini komend
# 2. Program wypisuje zmienna 
# 


# Algorytm:
# --------------------------
# 1. Podaj zmienna 
# 2. PRZEKONWERTUJ parametr z ekranu na liczbę
# 2. JEZELI parametr > 0 TO wypisz "dodatnia"
# 3. JEZELI parametr = 0 TO wypisz "zero"
# 4. JEZELI parametr < 0 TO wypisz "ujemna"

# Implementacja:
# --------------------------

# 1. Przypisać parametr do zmiennej (wczytać parametr)

import sys

parametr = sys.argv[1] 

print(":-)",parametr, ":-)")