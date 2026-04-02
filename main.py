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
            tipo = random.randint(1, 3)

            # 1 = operación combinada
            # 2 = resultado negativo
            # 3 = fracción (división)

            if tipo == 1:
                # Operación combinada simple
                a = random.randint(1, 20)
                b = random.randint(1, 10)
                c = random.randint(1, 10)

                simbolo1 = random.choice(["+", "-"])
                simbolo2 = random.choice(["*", "/"])

                if simbolo2 == "*":
                    correct = a + b * c if simbolo1 == "+" else a - b * c
                else:
                    c = random.randint(1, 10)
                    correct = a + round(b / c, 2) if simbolo1 == "+" else a - round(b / c, 2)
                    correct = round(correct, 2)

                print(f"{a} {simbolo1} {b} {simbolo2} {c}")

            elif tipo == 2:
                # Resultado negativo
                a = random.randint(1, 20)
                b = random.randint(a + 1, a + 20)

                correct = a - b
                print(f"{a} - {b}")

            else:
                # Fracción simple (división)
                a = random.randint(1, 9)
                b = random.randint(2, 9)

                correct = round(a / b, 2)
                print(f"{a}/{b}")

            result = float(input("Indique el resultado (2 decimales si aplica)\n"))

            if result == correct:
                print("correcto!")
            else:
                print(f"incorrecto! La respuesta era {correct}")
            
    elif seleccion1 == 3:
        print("preparatoria")

    else:
        #Fer
        Pnfu = [0, 1, 2, 3, 4, 5, 6, 7]
        print("Nivel de dificultad: \n UNIVERSIDAD:")
        print("Estos son los temas que verás: \n Integrales \n Área de gráficas \n ")
        backtrackdec = int(input("Quieres continuar o deseas intentar otra dificultad? \n 0: Intentar otro nivel \n 1:Intentaré este nivel\n"))
        while True:
            backtrackdec = int(input("Quieres continuar o deseas intentar otra dificultad? \n 0: Intentar otro nivel \n 1:Intentaré este nivel\n Elija una opción de las indicadas\n"))
            if backtrackdec < 0 or backtrackdec > 1:
                print("Elija una opción de las indicadas por favor")
            else:
                break
        if backtrackdec == 0:
            print("Reinicie el programa para intentar otra vez (In progress):") #In progress

        elif backtrackdec == 1:
            print("Prepárate...\n Primer tema: Integrales (Nivel 1): \n Calcula:\n")
            #Nivel 1:
            lvl4 = 1
            #while lvl4 == 1:
            indef = "x"
            exp = random.randint(1, 6)
            correct = (1/(exp+1))
            print(f"{1}/{exp+1}") 












            #big = random.randint(1, 6)
            #small = random.randint(-5,)






        
