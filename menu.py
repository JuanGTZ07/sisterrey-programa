# Juan Gutierrez 25/3/26 - Modificado para incluir sistema de puntos
import random

operadores = [1, 2, 3, 4, 5, 6]
puntos = 0  # <--- Inicializamos los puntos

print("Facil - 1\nsecundaria - 2\nDificil - 3\nUniversidad - 4\n")

while True:
    seleccion1 = int(input("Seleccione el nivel de dificultad\n"))
    if seleccion1 < 1 or seleccion1 > 4:
        print("Seleccione un numero valido")
        continue
    break

# --- LÓGICA DE JUEGO (Ejemplo aplicado a Primaria y Secundaria) ---
while True:
    print(f"\nPUNTOS ACTUALES: {puntos}") # Mostrar puntuación
    
    if seleccion1 == 1:
        operadoresAux = random.choice(operadores)
        while operadoresAux == 5 or operadoresAux == 6:
            operadoresAux = random.choice(operadores)
            
        if operadoresAux == 1:
            simbolo, part1, part2 = "+", random.randint(1,100), random.randint(1,100)
            correct = part1 + part2
        elif operadoresAux == 2:
            simbolo, part1, part2 = "-", random.randint(1,100), random.randint(1,100)
            correct = part1 - part2
        elif operadoresAux == 3:
            simbolo, part1, part2 = "/", random.randint(1,20), random.randint(1,20)
            correct = round(part1 / part2, 2)
        elif operadoresAux == 4:
            simbolo, part1, part2 = "*", random.randint(1,10), random.randint(1,10)
            correct = part1 * part2

        print(f"Calcula: {part1} {simbolo} {part2}")
        result = float(input("Resultado: "))

        if result == correct:
            puntos += 1 # <--- SUMA PUNTO
            print(f"¡Correcto! Tienes {puntos} puntos.")
        else:
            print(f"¡Incorrecto! Te has quedado sin puntos. Juego terminado.")
            puntos = 0 # <--- PIERDE PUNTOS
            break # El juego termina según el documento

    elif seleccion1 == 2:
        tipo = random.randint(1, 3)
        if tipo == 1:
            a, b, c = random.randint(1, 20), random.randint(1, 10), random.randint(1, 10)
            s1, s2 = random.choice(["+", "-"]), random.choice(["*", "/"])
            if s2 == "*":
                correct = a + b * c if s1 == "+" else a - b * c
            else:
                correct = round(a + (b / c), 2) if s1 == "+" else round(a - (b / c), 2)
            print(f"Calcula: {a} {s1} {b} {s2} {c}")
        elif tipo == 2:
            a = random.randint(1, 20)
            b = random.randint(a + 1, a + 20)
            correct = a - b
            print(f"Calcula: {a} - {b}")
        else:
            a, b = random.randint(1, 9), random.randint(2, 9)
            correct = round(a / b, 2)
            print(f"Calcula: {a}/{b}")

        result = float(input("Resultado: "))
        if result == correct:
            puntos += 1
            print(f"¡Correcto! Tienes {puntos} puntos.")
        else:
            print(f"¡Incorrecto! La respuesta era {correct}. Juego terminado.")
            puntos = 0
            break