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


