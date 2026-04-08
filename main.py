import random
import sys
import time

operadores = [1,2,3,4,5,6]
pts = 0
tiempo = []
nivel_actual = 1
datos_ml = []

try:
    jugador = input("Nombre o alias del jugador: \n")
except ValueError:
    print("ingrese bien sus datos")

while True:
  genero = input("Genero del jugador (Masculino/Femenino): \n").strip().lower()
  if genero == "masculino":
    genero = "Masculino"
    break
  elif genero == "femenino":
    genero = "Femenino"
    break
  else:
    print("Solo puede ingresar Masculino o Femenino")

while True:
  try:
    edad = int(input("Edad del jugador: \n"))
    if (edad < 0) or (edad > 100):
      print("Elija una edad válida")
    else:
      break
  except ValueError:
    print("ingrese bien sus datos")

preguntas = []
aciertos = 0
errores = 0

print("Primaria - 1\nSecundaria - 2\nPreparatoria - 3\nUniversidad - 4\nSalir - 0\n")

def recomendacion_ml():
  if not datos_ml:
    return nivel_actual

  promedio_tiempo = sum(d[1] for d in datos_ml) / len(datos_ml)
  precision = sum(d[2] for d in datos_ml) / len(datos_ml)

  if precision > 0.8 and promedio_tiempo < 5:
    return 4
  elif precision > 0.6:
    return 3
  elif precision > 0.4:
    return 2
  else:
    return 1

while True:

  if datos_ml:
    nivel_sugerido = recomendacion_ml()
    print(f"\nSistema recomienda nivel: {nivel_sugerido}")

  print(f"\n--- Pts ACTUALES: {pts} ---")

  try:
    seleccion1 = int(input("Seleccione el nivel de dificultad\n"))
    nivel_actual = seleccion1
  except ValueError:
    print("Seleccione un número válido")
    continue

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

    print("\n--- Resultados ---")
    print(f"Jugador: {jugador}")
    print(f"Genero: {genero}")
    print(f"Edad: {edad}")
    print(f"Preguntas contestadas: {len(preguntas)}")
    print(f"Aciertos: {aciertos}")
    print(f"Errores: {errores}")

    if preguntas:
      porcentaje = round((aciertos / len(preguntas)) * 100, 2)
      print(f"Porcentaje de aciertos: {porcentaje}%")

    break

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
          part2 = random.randint(1,20)
          correct = random.randint(1,20)
          part1 = correct * part2

        elif operadoresAux == 4:
          simbolo = "*"
          part1 = random.randint(1,10)
          part2 = random.randint(1,10)
          correct = part1 * part2

        pregunta = f"{part1}{simbolo}{part2}"

        print(f"\n{pregunta}")

        inicio = time.time()

        try:
          result = float(input(""))
        except ValueError:
          intentos -= 1
          errores += 1
          print("Respuesta inválida")
          continue

        elapsed = round(time.time() - inicio, 2)

        if elapsed <= 3:
          puntos_ronda = 10
        elif elapsed <= 7:
          puntos_ronda = random.randint(6,9)
        elif elapsed <= 15:
          puntos_ronda = random.randint(1,5)
        else:
          puntos_ronda = 0

        tiempo.append((pregunta, elapsed))
        preguntas.append(pregunta)

        print(f"Tiempo: {elapsed}s")

        if result == correct:

          print("¡Correcto!")
          print(f"Puntos obtenidos: {puntos_ronda}")

          pts += puntos_ronda
          aciertos += 1

          datos_ml.append((edad, elapsed, 1))

        else:

          intentos -= 1
          errores += 1

          print("Incorrecto")
          print(f"Respuesta correcta: {correct}")
          print("Puntos obtenidos: 0")

          datos_ml.append((edad, elapsed, 0))

          if intentos == 0:
            print("Se acabaron los intentos")
            break