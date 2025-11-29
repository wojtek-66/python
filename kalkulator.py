# Opis problemu (programu):
# --------------------------
# Program pobiera liczbę naturalną od uzytkownika i wypisuje slownie typ tej liczby.
# 1. Dla liczby wiekszej niz 0 wypisz "dodatnia"
# 2. Dla zera wypisz zero
# 3. Dla liczby ujemnej wypisz "ujemna"


# Algorytm:
# --------------------------
# 1. PRZYPISZ parametr do zmiennej
# 2. PRZEKONWERTUJ parametr z ekranu na liczbę
# 2. JEZELI parametr > 0 TO wypisz "dodatnia"
# 3. JEZELI parametr = 0 TO wypisz "zero"
# 4. JEZELI parametr < 0 TO wypisz "ujemna"

# Implementacja:
# --------------------------

# 1. Przypisać parametr do zmiennej (wczytać parametr)

import sys

num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == "+":
    result = num1 + num2
    print(" Wynik dodawania wynosi: " ,result)
elif operation == "-":
    result = num1 - num2
    print("Wynik odejmowania wwynosi: " ,result)
elif operation == "*":
    result = num1 * num2
    print("Wynik mnozenia wynosi: " ,result)
else:
    print("Nieznany operator. Obsługiwane są tylko '+','*' i '-'")


