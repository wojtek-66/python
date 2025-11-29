import sys


num_1 = int(sys.argv[1])
operation = sys.argv[2]
num_2 = int(sys.argv[3])

if operation == "+":
    result = num_1 + num_2
    print("Wynik dodawania wynosi: " ,result)
if operation == "-":
    result = num_1 - num_2
    print("Wynik odejmowania wwynosi: " ,result)
if  operation == "*":
    result = num_1 * num_2
    print("Wynik mnozenia wynosi: " ,result)
if  operation == "/":
    result = num_1 // num_2
    print("Wynik dzielenia wynosi: " ,result)
if  num_2 == 0:
    print("Nie mozna dzielic przez 0")




