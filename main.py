#Juan Gutierrez 25/3/26
import random
operadores = [1,2,3,4,5,6]
# 1 = suma|2 = resta|3 = divison|4 = multiplicacion|5 = raiz|6 = exponente

print("Facil - 1\nIntermedio - 2\nDificil - 3\nUniversidad - 4\n")
while True:
    seleccion1 = int(input("Seleccione el nivel de dificultad\n"))
    if seleccion1 < 1 or seleccion1 > 4:
        print("Seleccione un numero valido")
        
    elif seleccion1 == 1:
        print("Primaria")

        while True:
            operadoresAux = random.choice(operadores)
            while operadoresAux == 5 or operadoresAux == 6:
                operadoresAux = random.choice(operadores)
            if operadoresAux == 1:
                simbolo = "+"
                part1 = random.randint(1,100)
                part2 = random.randint(1,100)
                correct = part1 + part2
            elif operadoresAux == 2:
                simbolo = "-"
                part1 = random.randint(1,100)
                part2 = random.randint(1,100)
                correct = part1 - part2
            elif operadoresAux == 3:
                simbolo = "/"
                part1 = random.randint(1,20)
                part2 = random.randint(1,20)
                correct = round(part1 / part2, 2)
            elif operadoresAux == 4:
                simbolo = "*"
                part1 = random.randint(1,10)
                part2 = random.randint(1,10)
                correct = part1*part2
                
            print(f"{part1}{simbolo}{part2}")   
            result = float(input("Indique el resultado\n"))
            if result == correct:
                print("correcto!")
            else:
                print("incorrecto!")
        
    elif seleccion1 == 2:
        print("Secundaria")
        while True:
            operadoresAux = random.choice(operadores)
            
    elif seleccion1 == 3:
        print("preparatoria")
    else:
        print("universidad")