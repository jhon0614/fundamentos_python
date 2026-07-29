"""
#Ejercicio1
# Solicitar los puntos de cada nivel
nivel1 = int(input("Puntos del nivel 1: "))
nivel2 = int(input("Puntos del nivel 2: "))
nivel3 = int(input("Puntos del nivel 3: "))

# Calcular el puntaje total
puntaje_total = nivel1 + nivel2 + nivel3

print("Puntaje total:", puntaje_total)

#Ejercicio 2
# Solicitar el tiempo jugado
horas = int(input("Horas jugadas: "))
minutos = int(input("Minutos jugados: "))
segundos = int(input("Segundos jugados: "))

# Convertir todo a segundos
tiempo_total = horas * 3600 + minutos * 60 + segundos

print("Tiempo total en segundos:", tiempo_total)

#Ejercicio 3
# Solicitar el daño de cada ataque
ataque1 = float(input("Daño del ataque 1: "))
ataque2 = float(input("Daño del ataque 2: "))
ataque3 = float(input("Daño del ataque 3: "))

# Calcular el daño total
dano_total = ataque1 + ataque2 + ataque3

print("Daño total:", dano_total)

#Ejercicio 4
# Solicitar la experiencia de cada misión
mision1 = int(input("Experiencia de la misión 1: "))
mision2 = int(input("Experiencia de la misión 2: "))
mision3 = int(input("Experiencia de la misión 3: "))

# Calcular la experiencia total
experiencia_total = mision1 + mision2 + mision3

print("Experiencia total:", experiencia_total)

#Ejercicio 5
# Solicitar la vida máxima y actual
vida_maxima = float(input("Vida máxima: "))
vida_actual = float(input("Vida actual: "))

# Calcular el porcentaje de vida
porcentaje_vida = vida_actual * 100 / vida_maxima

print("Porcentaje de vida restante:", porcentaje_vida, "%")

#Ejercicio 6
# Solicitar el oro de cada misión
mision1 = int(input("Oro de la misión 1: "))
mision2 = int(input("Oro de la misión 2: "))
mision3 = int(input("Oro de la misión 3: "))

# Calcular el oro total
oro_total = mision1 + mision2 + mision3

print("Oro total:", oro_total)

#Ejercicio 7
# Solicitar la distancia y el tiempo
distancia = float(input("Distancia recorrida en kilómetros: "))
tiempo = float(input("Tiempo tomado en horas: "))

# Calcular la velocidad promedio
velocidad_promedio = distancia / tiempo

print("Velocidad promedio:", velocidad_promedio, "km/h")

#Ejercicio 8
# Solicitar el costo de las mejoras
mejora1 = float(input("Costo de la mejora 1: "))
mejora2 = float(input("Costo de la mejora 2: "))
mejora3 = float(input("Costo de la mejora 3: "))

# Calcular el costo total
costo_total = mejora1 + mejora2 + mejora3

print("Costo total de las mejoras:", costo_total)

#Ejercicio 9
# Solicitar los tiempos de la misión
tiempo_total = float(input("Tiempo total de la misión: "))
tiempo_transcurrido = float(input("Tiempo transcurrido: "))

# Calcular el tiempo restante
tiempo_restante = tiempo_total - tiempo_transcurrido

print("Tiempo restante:", tiempo_restante)

#Ejercicio 10
# Solicitar el nivel de cada jugador
jugador1 = int(input("Nivel del jugador 1: "))
jugador2 = int(input("Nivel del jugador 2: "))
jugador3 = int(input("Nivel del jugador 3: "))

# Calcular el nivel promedio
nivel_promedio = (jugador1 + jugador2 + jugador3) / 3

print("Nivel promedio del equipo:", nivel_promedio)

#Ejercicio 11
# Solicitar el daño base y el multiplicador
dano_base = float(input("Daño base: "))
multiplicador = float(input("Multiplicador crítico: "))

# Calcular el daño crítico
dano_critico = dano_base * multiplicador

print("Daño crítico:", dano_critico)

#Ejercicio 12
# Solicitar el tiempo total en minutos
minutos_totales = int(input("Tiempo total en minutos: "))

# Calcular las horas y minutos
horas = minutos_totales // 60
minutos = minutos_totales % 60

print("Tiempo total:", horas, "horas y", minutos, "minutos")

#Ejercicio 13
# Solicitar el total de misiones
total_misiones = int(input("Número total de misiones: "))
misiones_completadas = int(input("Misiones completadas: "))

# Calcular el porcentaje completado
porcentaje = misiones_completadas * 100 / total_misiones

print("Porcentaje de misiones completadas:", porcentaje, "%")

#Ejercicio 14
# Solicitar el costo de cada objeto
objeto1 = float(input("Costo del objeto 1: "))
objeto2 = float(input("Costo del objeto 2: "))
objeto3 = float(input("Costo del objeto 3: "))

# Calcular el costo total
costo_total = objeto1 + objeto2 + objeto3

print("Costo total de los objetos:", costo_total)

#Ejercicio 15
# Solicitar el tiempo de cada partida
partida1 = float(input("Tiempo de la partida 1: "))
partida2 = float(input("Tiempo de la partida 2: "))
partida3 = float(input("Tiempo de la partida 3: "))

# Calcular el tiempo promedio
tiempo_promedio = (partida1 + partida2 + partida3) / 3

print("Tiempo promedio de las partidas:", tiempo_promedio)
"""
#Ejercicio 16
# Solicitar el total de enemigos
total_enemigos = int(input("Número total de enemigos: "))
enemigos_derrotados = int(input("Enemigos derrotados: "))

# Calcular el porcentaje derrotado
porcentaje = enemigos_derrotados * 100 / total_enemigos

print("Porcentaje de enemigos derrotados:", porcentaje, "%")