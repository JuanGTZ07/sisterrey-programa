import random
import sys
import time

operadores = [1,2,3,4,5,6]
pts = 0
tiempo = []
nivel_actual = 1

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

datos_ml = []

print("Primaria - 1\nSecundaria - 2\nPreparatoria - 3\nUniversidad - 4\nSalir - 0\n")

while True:

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

    if datos_ml:
      promedio_tiempo = round(sum([d[1] for d in datos_ml]) / len(datos_ml),2)

      if promedio_tiempo <= 5:
        nivel_estimado = "Avanzado"
      elif promedio_tiempo <= 10:
        nivel_estimado = "Intermedio"
      else:
        nivel_estimado = "Principiante"

      print(f"Clasificación del jugador según rendimiento: {nivel_estimado}")

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

  elif seleccion1 == 2:

    print("Secundaria")
    intentos = 5

    while True:

      tipo = random.randint(1, 3)

      if tipo == 1:

        a = random.randint(1, 20)
        b = random.randint(1, 10)
        c = random.randint(1, 10)

        simbolo1 = random.choice(["+", "-"])
        simbolo2 = random.choice(["*", "/"])

        if simbolo2 == "*":
          correct = a + b * c if simbolo1 == "+" else a - b * c
        else:
          correct = a + round(b / c, 2) if simbolo1 == "+" else a - round(b / c, 2)
          correct = round(correct, 2)

        pregunta = f"{a} {simbolo1} {b} {simbolo2} {c}"

      elif tipo == 2:

        a = random.randint(1, 20)
        b = random.randint(a + 1, a + 20)

        correct = a - b
        pregunta = f"{a} - {b}"

      else:

        a = random.randint(1, 9)
        b = random.randint(2, 9)

        correct = round(a / b, 2)
        pregunta = f"{a}/{b}"

      print(f"\n{pregunta}")

      inicio = time.time()

      try:
        result = float(input("(2 decimales si aplica)\n"))
      except ValueError:
        intentos -= 1
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

  elif seleccion1 == 3:

    print("Preparatoria")
    intentos = 5

    while True:

      tipo = random.randint(1, 3)

      if tipo == 1:

        cInprocess = random.randint(2, 8)
        c = cInprocess**2
        b = cInprocess*2

        pregunta = f"y = x²+{b}x+{c}"
        correct = float(cInprocess * -1)

      elif tipo == 2:

        a = random.randint(1, 10)
        b = random.randint(1, 20)
        c = random.randint(1, 30)

        correct = round((c - b) / a, 2)

        pregunta = f"{a}x + {b} > {c}  →  x > ?"

      else:

        a = random.randint(1, 8)
        n = random.randint(2, 6)

        coef = a * n
        new_exp = n - 1

        pregunta = f"f(x) = {a}x^{n}  →  f'(x) = {coef}x^?"
        correct = float(new_exp)

      print(f"\n{pregunta}")

      inicio = time.time()

      try:
        result = float(input(""))
      except ValueError:
        intentos -= 1
        print("Respuesta inválida")
        continue

      elapsed = round(time.time() - inicio, 2)

      if elapsed <= 15:
        puntos_ronda = 10
      elif elapsed <= 22:
        puntos_ronda = random.randint(6,9)
      elif elapsed <= 35:
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

  else:

    print("Universidad")
    intentos = 5

    while True:

        tipo = random.randint(1, 2)

        if tipo == 1:

          exp = random.randint(1, 5)
          denIntegral = exp + 1

          pregunta = f"∫x^{exp}dx = x^{denIntegral}/?? + C"

          print(f"\n{pregunta}")

          inicio = time.time()

          try:
            result = float(input("Denominador: "))
            correct = float(denIntegral)
          except ValueError:
            intentos -= 1
            print("Respuesta inválida")
            continue

        else:

          a = random.randint(1, 8)
          correct = float(2 * a)

          pregunta = f"lim x→{a} de (x² - {a**2}) / (x - {a})"

          print(f"\n{pregunta}")

          inicio = time.time()

          try:
            result = float(input(""))
          except ValueError:
            intentos -= 1
            print("Respuesta inválida")
            continue

        elapsed = round(time.time() - inicio, 2)

        puntos_ronda = 10

        tiempo.append((pregunta, elapsed))
        preguntas.append(pregunta)

        print(f"Tiempo: {elapsed}s")

        if result == correct:

          print("¡Correcto!")
          print("Puntos obtenidos: 10")

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