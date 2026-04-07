import random
import sys
import time

operadores = [1,2,3,4,5,6]
pts = 0
tiempo = []

print("Primaria - 1\nSecundaria - 2\nPreparatoria - 3\nUniversidad - 4\nSalir - 0\n")

while True:
    print(f"\n--- Pts ACTUALES: {pts} ---")
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
    seleccion1 = int(input("Seleccione el nivel de dificultad\n"))
=======
>>>>>>> Stashed changes
    try:
        seleccion1 = int(input("Seleccione el nivel de dificultad\n"))
    except ValueError:
        print("Seleccione un número válido")
        continue
<<<<<<< Updated upstream
=======
>>>>>>> effc2b71b49f8f86e4588e095c4df8ae03262c95
>>>>>>> Stashed changes
    if seleccion1 == 0:
        print(f"\nTerminaste con {pts} punto(s).")
        if tiempo:
            print("\n--- Tiempos ---")
            for i, (p, t) in enumerate(tiempo, 1):
                print(f"{i}. {p} → {t}s")
            tiempos = [t for _, t in tiempo]
            print(f"\nPromedio : {round(sum(tiempos)/len(tiempos), 2)}s")
            print(f"Mas rapido: {min(tiempos)}s")
            print(f"Mas lento : {max(tiempos)}s")
        sys.exit()
    elif seleccion1 < 0 or seleccion1 > 4:
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
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
            result = input("")
            if result.strip().lower() == "d":
                print(f"[DEBUG] Respuesta automática: {correct}")
                result = float(correct)
            else:
                result = float(result)
=======
>>>>>>> Stashed changes
            try:
                result = float(input(""))
            except ValueError:
                intentos -= 1
                print(f"¡INCORRECTO! Te quedan {intentos} intento(s).")
                if intentos == 0:
                    print("Se acabaron los intentos.")
                    break
                continue
<<<<<<< Updated upstream
=======
>>>>>>> effc2b71b49f8f86e4588e095c4df8ae03262c95
>>>>>>> Stashed changes
            elapsed = round(time.time() - inicio, 2)
            tiempo.append((pregunta, elapsed))
            print(f"Tiempo: {elapsed}s")

            if result == correct:
                print("¡Correcto!")
                pts += 1
            else:
                intentos -= 1
                print(f"¡INCORRECTO! Te quedan {intentos} intento(s).")
                if intentos == 0:
                    print("Se acabaron los intentos.")
                    break
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
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
            result = input("(2 decimales si aplica)\n")
            if result.strip().lower() == "d":
                print(f"[DEBUG] Respuesta automática: {correct}")
                result = float(correct)
            else:
                result = float(result)
=======
>>>>>>> Stashed changes
            try:
                result = float(input("(2 decimales si aplica)\n"))
            except ValueError:
                intentos -= 1
                print(f"¡INCORRECTO! La respuesta era {correct}. Te quedan {intentos} intento(s).")
                if intentos == 0:
                    print("Se acabaron los intentos.")
                    break
                continue
<<<<<<< Updated upstream
=======
>>>>>>> effc2b71b49f8f86e4588e095c4df8ae03262c95
>>>>>>> Stashed changes
            elapsed = round(time.time() - inicio, 2)
            tiempo.append((pregunta, elapsed))
            print(f"Tiempo: {elapsed}s")

            if result == correct:
                print("¡Correcto!")
                pts += 1
            else:
                intentos -= 1
                print(f"¡INCORRECTO! La respuesta era {correct}. Te quedan {intentos} intento(s).")
                if intentos == 0:
                    print("Se acabaron los intentos.")
                    break
    elif seleccion1 == 3:
        print("Preparatoria")
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
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
            result = input("")
            if result.strip().lower() == "d":
                print(f"[DEBUG] Respuesta automática: {correct}")
                result = float(correct)
            else:
                result = float(result)
=======
>>>>>>> Stashed changes
            try:
                result = float(input(""))
            except ValueError:
                intentos -= 1
                print(f"¡INCORRECTO! La respuesta era {correct}. Te quedan {intentos} intento(s).")
                if intentos == 0:
                    print("Se acabaron los intentos.")
                    break
                continue
<<<<<<< Updated upstream
=======
>>>>>>> effc2b71b49f8f86e4588e095c4df8ae03262c95
>>>>>>> Stashed changes
            elapsed = round(time.time() - inicio, 2)
            tiempo.append((pregunta, elapsed))
            print(f"Tiempo: {elapsed}s")

            if result == correct:
                print("¡Correcto!")
                pts += 1
            else:
                intentos -= 1
                print(f"¡INCORRECTO! La respuesta era {correct}. Te quedan {intentos} intento(s).")
                if intentos == 0:
                    print("Se acabaron los intentos.")
                    break
    else:
        print("Universidad")
        intentos = 3

        while True:
            tipo = random.randint(1, 2)

            if tipo == 1:
                exp = random.randint(1, 5)
                denIntegral = exp + 1
                pregunta = f"∫x^{exp}dx = x^{denIntegral}/?? + C"
                print(f"\n{pregunta}")
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
                correct = float(denIntegral)
                inicio = time.time()
                result = input("Denominador: ")
                if result.strip().lower() == "d":
                    print(f"[DEBUG] Respuesta automática: {correct}")
                    result = float(correct)
                else:
                    result = float(result)
=======
>>>>>>> Stashed changes
                inicio = time.time()
                try:
                    result = float(input("Denominador: "))
                    correct = float(denIntegral)
                except ValueError:
                    intentos -= 1
                    print(f"¡INCORRECTO! La respuesta era {correct}. Te quedan {intentos} intento(s).")
                    if intentos == 0:
                        print("Se acabaron los intentos.")
                        break
                    continue
                #correct = float(denIntegral)
<<<<<<< Updated upstream
=======
>>>>>>> effc2b71b49f8f86e4588e095c4df8ae03262c95
>>>>>>> Stashed changes
            else:
                a = random.randint(1, 8)
                correct = float(2 * a)
                pregunta = f"lim x→{a} de (x² - {a**2}) / (x - {a})"
                print(f"\n{pregunta}")
                inicio = time.time()
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
                result = input("")
                if result.strip().lower() == "d":
                    print(f"[DEBUG] Respuesta automática: {correct}")
                    result = float(correct)
                else:
                    result = float(result)

=======
>>>>>>> Stashed changes
                try:
                    result = float(input(""))
                except ValueError:
                    intentos -= 1
                    print(f"¡INCORRECTO! La respuesta era {correct}. Te quedan {intentos} intento(s).")
                    if intentos == 0:
                        print("Se acabaron los intentos.")
                        break
                    continue
<<<<<<< Updated upstream
=======
>>>>>>> effc2b71b49f8f86e4588e095c4df8ae03262c95
>>>>>>> Stashed changes
            elapsed = round(time.time() - inicio, 2)
            tiempo.append((pregunta, elapsed))
            print(f"Tiempo: {elapsed}s")
            if result == correct:
                print("¡Correcto!")
                pts += 1
            else:
                intentos -= 1
                print(f"¡INCORRECTO! La respuesta era {correct}. Te quedan {intentos} intento(s).")
                if intentos == 0:
                    print("Se acabaron los intentos.")
                    break