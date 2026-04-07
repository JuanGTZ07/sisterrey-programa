# Juan
import random
import sys
import time

operadores = [1,2,3,4,5,6]

puntos = 0
historial_tiempo = []

def registrar_tiempo(pregunta, inicio):
    elapsed = round(time.time() - inicio, 2)
    historial_tiempo.append((pregunta, elapsed))
    print(f"Tiempo: {elapsed}s")

def mostrar_resumen():
    print(f"\nPuntuación final: {puntos}")
    if historial_tiempo:
        print("\n--- RESUMEN DE TIEMPOS ---")
        for i, (pregunta, t) in enumerate(historial_tiempo, 1):
            print(f"{i}. {pregunta} → {t}s")
        tiempos = [t for _, t in historial_tiempo]
        print(f"\nPromedio : {round(sum(tiempos)/len(tiempos), 2)}s")
        print(f"Más rápida: {min(tiempos)}s")
        print(f"Más lenta : {max(tiempos)}s")

print("Primaria - 1\nSecundaria - 2\nPreparatoria - 3\nUniversidad - 4\n")
while True:
    print(f"\n--- PUNTOS ACTUALES: {puntos} ---")
    seleccion1 = float(input("Seleccione el nivel de dificultad\n"))
    if seleccion1 < 1 or seleccion1 > 4:
        print("Seleccione un numero valido")

    elif seleccion1 == 1:
        print("Primaria")
        intentos = 5

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

            pregunta = f"{part1}{simbolo}{part2}"
            print(f"\n{pregunta}")
            inicio = time.time()
            result = float(input("Indique el resultado\n"))
            registrar_tiempo(pregunta, inicio)

            if result == correct:
                print("¡Correcto!")
                puntos += 1
            else:
                intentos -= 1
                print(f"¡INCORRECTO! Te quedan {intentos} intento(s).")
                if intentos == 0:
                    print("GAME OVER.")
                    mostrar_resumen()
                    sys.exit()

    elif seleccion1 == 2:
        print("Secundaria")
        intentos = 5

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
                pregunta = f"{a} {simbolo1} {b} {simbolo2} {c}"
            elif tipo == 2:
                a = random.randint(1, 20); b = random.randint(a + 1, a + 20)
                correct = a - b
                pregunta = f"{a} - {b}"
            else:
                a = random.randint(1, 9); b = random.randint(2, 9)
                correct = round(a / b, 2)
                pregunta = f"{a}/{b}"

            print(f"\n{pregunta}")
            inicio = time.time()
            result = float(input("Indique el resultado (2 decimales si aplica)\n"))
            registrar_tiempo(pregunta, inicio)

            if result == correct:
                print("¡Correcto!")
                puntos += 1
            else:
                intentos -= 1
                print(f"¡INCORRECTO! La respuesta era {correct}. Te quedan {intentos} intento(s).")
                if intentos == 0:
                    print("GAME OVER.")
                    mostrar_resumen()
                    sys.exit()

    elif seleccion1 == 3:
        #Fer V
        print("Nivel de dificultad: PREPARATORIA")
        intentos = 3

        while True:
            tipo = random.randint(1, 3)

            if tipo == 1:
                cInprocess = random.randint(2, 8); c = cInprocess**2; b = cInprocess*2
                pregunta = f"y = x²+{b}x+{c}"
                print(f"\n{pregunta}")
                correct = float(cInprocess * -1)
            elif tipo == 2:
                a = random.randint(1, 10); b = random.randint(1, 20); c = random.randint(1, 30)
                correct = round((c - b) / a, 2)
                pregunta = f"{a}x + {b} > {c}  →  x > ?"
                print(f"\n{pregunta}")
            else:
                a = random.randint(1, 8); n = random.randint(2, 6)
                coef = a * n; new_exp = n - 1
                pregunta = f"f(x) = {a}x^{n}  →  f'(x) = {coef}x^?"
                print(f"\n{pregunta}")
                correct = float(new_exp)

            inicio = time.time()
            result = float(input("Indique el resultado\n"))
            registrar_tiempo(pregunta, inicio)

            if result == correct:
                print("¡Correcto!")
                puntos += 1
            else:
                intentos -= 1
                print(f"¡INCORRECTO! La respuesta era {correct}. Te quedan {intentos} intento(s).")
                if intentos == 0:
                    print("GAME OVER.")
                    mostrar_resumen()
                    sys.exit()

    else:
        #Fer V - Universidad
        print("Nivel de dificultad: UNIVERSIDAD")
        intentos = 3

        while True:
            tipo = random.randint(1, 2)

            if tipo == 1:
                exp = random.randint(1, 5)
                denIntegral = exp + 1
                pregunta = f"∫x^{exp}dx = x^{denIntegral}/? + C"
                print(f"\n{pregunta}")
                inicio = time.time()
                result = float(input("Escribe el denominador: "))
                correct = float(denIntegral)
            else:
                a = random.randint(1, 8)
                correct = float(2 * a)
                pregunta = f"lim x→{a} de (x² - {a**2}) / (x - {a})"
                print(f"\n{pregunta}")
                inicio = time.time()
                result = float(input("Indique el resultado\n"))

            registrar_tiempo(pregunta, inicio)

            if result == correct:
                print("¡Correcto!")
                puntos += 1
            else:
                intentos -= 1
                print(f"¡INCORRECTO! La respuesta era {correct}. Te quedan {intentos} intento(s).")
                if intentos == 0:
                    print("GAME OVER.")
                    mostrar_resumen()
                    sys.exit()