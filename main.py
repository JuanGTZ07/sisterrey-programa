#Juan Gutierrez 25/3/26
import random
operadores = [1,2,3,4,5,6]
# 1 = suma|2 = resta|3 = divison|4 = multiplicacion|5 = raiz|6 = exponente

print("Facil - 1\nsecundaria - 2\nDificil - 3\nUniversidad - 4\n")
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
        #Fer V
        print("Nivel de dificultad: PREPARATORIA")
        print("Estos son los temas que verás: \n Ecuaciones algebraicas \n Desigualdades e igualdades \n Derivadas ")
        while True:
            options = [0, 1]
            try:
                backtrackdec = int(input("Quieres continuar o deseas intentar otra dificultad? \n 0: Intentar otro nivel \n 1:Intentaré este nivel\n Elija una opción de las indicadas\n"))
                if backtrackdec in options:   
                    if backtrackdec < 0 or backtrackdec > 1:
                        print("Elija una opción de las indicadas por favor")
                    else:
                        break
            except ValueError:
                print("Escribe una opción válida")
        if backtrackdec == 0:
            print("Se reiniciará el programa para intentar otra vez:") 

        elif backtrackdec == 1:
            print("Prepárate...\n Primer tema: Ecuaciones algebraicas (Binomios al cuadrado perfecto) (Nivel 1): \n Calcula el valor de 'x':\n")
            #Nivel 1: Ecuaciones algebraicas
            for i in range(3):
                cInprocess = random.randint(2, 8)
                c = cInprocess**2
                b = cInprocess*2
                print(f"y = x²+{b}x+{c}")
                correct = cInprocess * -1
                while True:
                    try:
                        userxAnswer = int(input("¿Cuál es el valor de x??"))
                        if userxAnswer != correct:
                            print("\nRespuesta incorrecta, intenta otra vez\n")
                        elif userxAnswer == correct:
                            print("\nCorrecto! avanza al siguiente ejercicio\n")
                            break
                    except ValueError:
                        print("Escribe una opción válida")
            #Nivel 2: Desigualdades e igualdades:
            for i in range(3):
                operators = [0, 1]
                x = random.randint(1, 20)
                operator = random.choice(operators)
                y = random.randint(1, 75)
                randomNum = random.randint(10, 75 )
                if operator == 1:
                    symbol = "+"
                    compare = x + y
                    if compare < randomNum:
                        correct = 2
                    elif compare > randomNum:
                        correct = 1
                    elif compare == randomNum:
                        correct = 3 
                elif operator == 0:
                    symbol = "-"
                    compare = x - y
                    if compare < randomNum:
                        correct = 2
                    elif compare > randomNum:
                        correct = 1
                    elif compare == randomNum:
                        correct = 3 

                print(f"{x}{symbol}{y} ?? {randomNum}")
                
                while True:
                    options = [1, 2, 3]
                    try:
                        DesAnswer = int(input("Escribe '1' si la parte de la izquierda es mayor que la parte derecha\nEscribe '2' si la parte izquierda es menor que la parte derecha\nO 3 si las dos partes son iguales"))
                        if DesAnswer in options:
                            if DesAnswer != correct:
                                print("Respuesta incorrecta, checa bien el problema")
                            elif DesAnswer == correct:
                                print("\nCorrecto! intenta el siguiente ejercicio\n")
                                break
                        else:
                            print("Escribe una opción válida (1, 2, 3)")
                    except ValueError:
                        print("Escribe una opción válida")
            #Nivel 3: Derivadas:
            for i in range(3):
                exp = random.randint(1, 5)
                print("Responderás con el coeficiente final al derivar y el exponenete final de x al derivar igualmente\nEsta es la manera de la que se escribe una derivada:")
                print(f"D(x^{exp})")
                print("Esta es la fórmula para derivar" f"(exponente inicial)*x^(exponente inicial - 1)")
                coefRich = exp
                expRich = exp - 1
                
                while True:
                    try:
                        coef = int(input("¿Cuál es el coeficiente de la derivada?"))
                        if coef != coefRich:
                            print("Respuesta incorrecta, intenta otra vez")
                        elif coef == coefRich:
                            print("\nCorrecto! avanza con el exponente")
                            break
                    except ValueError:
                        print("Escribe una opción válida")
                while True:
                    try:
                        expAnswer = int(input("¿Cuál sería el exponente ahora después de derivar?"))
                        if expAnswer != expRich:
                            print("Respuesta incorrecta, intenta otra vez")
                        elif expAnswer == expRich:
                            print("\nCorrecto! ahora puedes intentar otra dificultad\n")
                            break
                    except ValueError:
                        print("Escribe una opción válida")
    else:
        #Fer V
        print("Nivel de dificultad: \n UNIVERSIDAD:")
        print("Estos son los temas que verás: \n Integrales indefinidas \n Integrales definidas \n ")
        
        while True:
            options = [0, 1]
            try:

                backtrackdec = int(input("Quieres continuar o deseas intentar otra dificultad? \n 0: Intentar otro nivel \n 1:Intentaré este nivel\n Elija una opción de las indicadas\n"))
                if backtrackdec in options:   
                    if backtrackdec < 0 or backtrackdec > 1:
                        print("Elija una opción de las indicadas por favor")
                    else:
                        break
            except ValueError:
                print("Escribe una opción válida")
        if backtrackdec == 0:
            print("Se reiniciará el programa para intentar otra vez:") 

        elif backtrackdec == 1:
            print("Prepárate...\n Primer tema: Integrales indefinidas (Nivel 1): \n Calcula:\n")

            #Nivel 1: Integrales indefinidas
            for i in range(3):
                exp = random.randint(1, 5)
                print("Completa la respuesta, está en este orden (Lo que está en paréntesis te pediremos):")
                print("(1/(denominador))x^(exponente final) + C \n **La C es para todos las integrales indefinidas**\n\n")

                print(f"∫x^{exp}dx")
                denIntegral = exp + 1 
                expIntegral = exp + 1
                while True:
                    try:
                        denR = int(input("Escribe el denominador de la integral: \n"))
                        if denR != denIntegral:
                            print("Eso es incorrecto, intenta otra vez\n Recuerda la fórmula: (1/(denominador))x^(exponente final) + C\n Tip: Al denominador se le suma 1 siempre")
                        else:
                            print("Es correcto!")
                            break
                    except ValueError:
                        print("Escribe una opción válida")

                while True:
                    try:
                        expR = int(input("Escribe el exponente final de la integral: \n"))
                        if expR != expIntegral:
                            print("Eso es incorrecto, intenta otra vez\n Recuerda la fórmula: (1/(denominador))x^(exponente final) + C\n Tip: Al exponente de la integral se le suma 1 siempre")
                        else:
                            print("Es correcto!")
                            break
                    except ValueError:
                        print("Escribe una opción válida")
            
            #Nivel 2: Integrales definidas
            for i in range(3):
                exp = random.randint(1, 5)
                integralMax = random.randint(1, 3)
                integralMin = random.randint(1, 3)
                while True:
                    if integralMax == integralMin:
                        integralMin = random.randint(1, 3)
                        if integralMax > integralMin:
                            break
                        elif integralMax < integralMin:
                            aux = integralMax + integralMin
                            integralMax = aux - integralMax
                            integralMin = aux - integralMin
                    elif integralMax > integralMin:
                        break
                    elif integralMax < integralMin:
                        aux = integralMax + integralMin
                        integralMax = aux - integralMax
                        integralMin = aux - integralMin
                print("\nPara calcular una integral definida, se necesita primero integrar el integrando y después multiplicar el límite superior por este;\n y después hacer lo mismo con el límite inferior, pero al final restar el límite superior del límite inferior. ")
                print("Fórmula: "f"∫(límite inferior a límite superior) de x^y dx" )
                print("[(límite superior) * ∫x^y dx] - [(límite inferior) * ∫x^y dx]")
                print("Calcula la integral definida:\n" f"(∫{integralMin} a {integralMax} de (x^{exp}dx)")
                #Integral inicial:

                print("Calcula primero la integral: ")
                denIntegral = exp + 1 
                expIntegral = exp + 1
                while True:
                    try:
                        denR = int(input("Escribe el denominador de la integral: \n"))
                        if denR != denIntegral:
                            print("Eso es incorrecto, intenta otra vez\n Recuerda la fórmula: (1/(denominador))x^(exponente final)\n Tip: Al denominador se le suma 1 siempre")
                        else:
                            print("Es correcto!")
                            break
                    except ValueError:
                        print("Escribe una opción válida")
                while True:
                    try:
                        expR = int(input("Escribe el exponente final de la integral: \n"))
                        if expR != expIntegral:
                            print("Eso es incorrecto, intenta otra vez\n Recuerda la fórmula: (1/(denominador))x^(exponente final)\n Tip: Al exponente de la integral se le suma 1 siempre")
                        else:
                            print("Es correcto!")
                            break
                    except ValueError:
                        print("Escribe una opción válida")
                #Límites de la integral después:
                while True:
                    try:
                        limiteSUPIntegral = float(input(""))
                    except ValueError:
                        print("Escribe una opción válida")






        
