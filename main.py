# Juan Gutierrez 25/3/26
import random
import sys

operadores = [1,2,3,4,5,6]

puntos = 0

print("Facil - 1\nsecundaria - 2\nDificil - 3\nUniversidad - 4\n")
while True:
    print(f"\n--- PUNTOS ACTUALES: {puntos} ---")
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
                print("¡Correcto!")
                puntos += 1
            else:
                print(f"\n¡INCORRECTO! GAME OVER.")
                print(f"Puntuación final: {puntos}")
                sys.exit()
        
    elif seleccion1 == 2:
        print("Secundaria")
       
        while True:
            tipo = random.randint(1, 3)

            if tipo == 1:
                a = random.randint(1, 20); b = random.randint(1, 10); c = random.randint(1, 10)
                simbolo1 = random.choice(["+", "-"]); simbolo2 = random.choice(["*", "/"])
                if simbolo2 == "*":
                    correct = a + b * c if simbolo1 == "+" else a - b * c
                else:
                    c = random.randint(1, 10)
                    correct = a + round(b / c, 2) if simbolo1 == "+" else a - round(b / c, 2)
                    correct = round(correct, 2)
                print(f"{a} {simbolo1} {b} {simbolo2} {c}")
            elif tipo == 2:
                a = random.randint(1, 20); b = random.randint(a + 1, a + 20)
                correct = a - b
                print(f"{a} - {b}")
            else:
                a = random.randint(1, 9); b = random.randint(2, 9)
                correct = round(a / b, 2)
                print(f"{a}/{b}")

            result = float(input("Indique el resultado (2 decimales si aplica)\n"))

            if result == correct:
                print("¡Correcto!")
                puntos += 1
            else:
                print(f"\n¡INCORRECTO! La respuesta era {correct}. GAME OVER.")
                print(f"Puntuación final: {puntos}")
                sys.exit()
            
    elif seleccion1 == 3:
        #Fer V
        print("Nivel de dificultad: PREPARATORIA")
        print("Estos son los temas que verás: \n Ecuaciones algebraicas \n Desigualdades e igualdades \n Derivadas ")
        while True:
            options = [0, 1]
            try:
                backtrackdec = int(input("Quieres continuar o deseas intentar otra dificultad? \n 0: Intentar otro nivel \n 1:Intentaré este nivel\n Elija una opción de las indicadas\n"))
                if backtrackdec in options:   
                    break
                else:
                    print("Elija una opción de las indicadas por favor")
            except ValueError:
                print("Escribe una opción válida")
        
        if backtrackdec == 0:
            print("Se reiniciará el programa para intentar otra vez:") 

        elif backtrackdec == 1:
            print("Prepárate...\n Primer tema: Ecuaciones algebraicas (Binomios al cuadrado perfecto) (Nivel 1): \n Calcula el valor de 'x':\n")
            for i in range(3):
                cInprocess = random.randint(2, 8); c = cInprocess**2; b = cInprocess*2
                print(f"y = x²+{b}x+{c}")
                correct = cInprocess * -1
                try:
                    userxAnswer = int(input("¿Cuál es el valor de x?? "))
                    if userxAnswer == correct:
                        print("\nCorrecto! +1 punto\n")
                        puntos += 1
                    else:
                        print(f"\n¡INCORRECTO! GAME OVER.")
                        print(f"Puntuación final: {puntos}")
                        sys.exit()
                except ValueError: sys.exit()

            print("Avanzando a Desigualdades...")

    else:
        #Fer V - Universidad
        print("Nivel de dificultad: \n UNIVERSIDAD:")
        print("Módulo de Universidad: Responde correctamente para ganar puntos o sal del juego.")
        exp = random.randint(1, 5)
        print(f"∫x^{exp}dx")
        denIntegral = exp + 1
        denR = int(input("Escribe el denominador: "))
        if denR == denIntegral:
            print("¡Correcto!")
            puntos += 1
        else:
            print("¡Error! Fin del juego.")
            sys.exit()




        
