#Juan Gutierrez 25/3/26
import random
operadores = [1,2,3,4,5,6]
# 1 = suma|2 = resta|3 = divison|4 = multiplicacion|5 = raiz|6 = exponente

print("Facil - 1\nIntermedio - 2\nDificil - 3\n")
while True:
    seleccion1 = int(input("Seleccione el nivel de dificultad\n "))
    if seleccion1 < 1 or seleccion1 > 3:
        print("Seleccione un numero valido")
        
    elif seleccion1 == 1:
        print("Facil")
        part1 = random.randint(1,50)
        part2 = random.randint(1,50)

        operadoresAux = random.choice(operadores)
        while operadoresAux == 5 or operadoresAux == 6:
            operadoresAux = random.choice(operadores)
        if operadoresAux == 1:
            simbolo = "+"
            correct = part1 + part2
        elif operadoresAux == 2:
            simbolo = "-"
            correct = part1 - part2
        elif operadoresAux == 3:
            simbolo = "/"
            correct = round(part1 / part2, 2)
        elif operadoresAux == 4:
            simbolo = "*"
            correct = part1*part2
            
        print(f"{part1}{simbolo}{part2}")   
        result = float(input("Indique el resultado"))
        if result == correct:
            print("correcto!")
        else:
            print("incorrecto!")
        
    elif seleccion1 == 2:
        print("Intermedio")
    else:
        print("Dificil")