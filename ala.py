import sys

# Sprawdza, czy podano wystarczającą liczbę argumentów
if len(sys.argv) < 4:
    print("Użycie: python skrypt.py <liczba1> <operacja> <liczba2>")
    sys.exit(1)

try:
    # Pobiera argumenty i konwertuje je na liczby (lub je sprawdza)
    num1 = float(sys.argv[1]) # Użyj float dla obsługi liczb dziesiętnych
    operator = sys.argv[2]
    num2 = float(sys.argv[3])

    # Wykonuje operację w zależności od operatora
    if operator == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operator == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    else:
        print("Nieznany operator. Obsługiwane są tylko '+' i '*'.")

except ValueError:
    print("Błąd: Pierwszy i trzeci argument muszą być liczbami.")
except IndexError:
    print("Błąd: Brak argumentów lub nieprawidłowa liczba argumentów.")

