# Ejercicio 1 ---------------------------------------------------------------
def dibujar_cuadrado(lado):
    # Dibuja un cuadrado de tamaño 'lado' usando asteriscos
    for i in range(lado):
        print('*' * lado)  # Imprime una línea de 'lado' asteriscos

def dibujar_rectangulo(base, altura):
    # Dibuja un rectángulo de base 'base' y altura 'altura' usando asteriscos
    for i in range(altura):
        print('*' * base)  # Imprime una línea de 'base' asteriscos

while True:
    print("Selecciona una figura:")
    print("1 - Cuadrado")
    print("2 - Rectángulo")
    print("3 - Salir")
    
    opcion = input("Ingresa tu opción: ")
    if opcion == '1':
        lado = int(input("Ingresa el lado del cuadrado: "))  # Solicita el tamaño del cuadrado
        dibujar_cuadrado(lado)  # Llama a la función para dibujar el cuadrado
        area = lado ** 2  # Calcula el área del cuadrado
        perimetro = 4 * lado  # Calcula el perímetro del cuadrado
        print(f"Área: {area}, Perímetro: {perimetro}")  # Muestra el área y el perímetro
    elif opcion == '2':
        base = int(input("Ingresa la base del rectángulo: "))  # Solicita la base del rectángulo
        altura = int(input("Ingresa la altura del rectángulo: "))  # Solicita la altura del rectángulo
        dibujar_rectangulo(base, altura)  # Llama a la función para dibujar el rectángulo
        area = base * altura  # Calcula el área del rectángulo
        perimetro = 2 * (base + altura)  # Calcula el perímetro del rectángulo
        print(f"Área: {area}, Perímetro: {perimetro}")  # Muestra el área y el perímetro
    elif opcion == '3':
        print("Saliendo...")  # Mensaje de salida
        break  # Sale del bucle
    else:
        print("Opción no válida. Intenta de nuevo.")  # Mensaje de error si la opción no es válida


# Ejercicio 2 ---------------------------------------------------------------
import random  # Importa el módulo random para generar números aleatorios
lucas = random.randint(1, 3)  # Genera una elección aleatoria para Lucas (1: piedra, 2: papel, 3: tijera)

# Define las opciones del juego
piedra = 1
papel = 2
tijera = 3

contador_lucas = 0  # Contador de victorias de Lucas
contador_tu = 0  # Contador de tus victorias

while contador_lucas != 3 and contador_tu != 3:  # El juego continúa hasta que uno gane 3 veces
    eleccion = int(input("Selecciona piedra(1), papel(2) o tijera(3): "))  # Solicita la elección del jugador
    
    # Comparaciones para determinar el ganador
    if lucas == 1 and eleccion == 1:
        print("Lucas ha sacado piedra, y tú también")  # Empate
        print("Empate")
        
    elif lucas == 1 and eleccion == 2:
        print("Lucas ha sacado piedra y tú papel, el ganador eres tú")  # Tú ganas
        contador_tu += 1  # Incrementa tu contador
        print(f"Llevas {contador_tu} partidas ganadas")
    
    elif lucas == 1 and eleccion == 3:
        print("Lucas ha sacado piedra y tú tijera, el ganador es Lucas")  # Lucas gana
        contador_lucas += 1  # Incrementa el contador de Lucas
        print(f"Lucas lleva {contador_lucas} partidas ganadas")
    
    elif lucas == 2 and eleccion == 1:
        print("Lucas ha sacado papel y tú piedra, ha ganado Lucas")  # Lucas gana
        contador_lucas += 1 
        print(f"Lucas lleva {contador_lucas} partidas ganadas")
        
    elif lucas == 2 and eleccion == 2:
        print("Lucas y tú habéis sacado papel")  # Empate
        print("Empate")
        
    elif lucas == 2 and eleccion == 3:
        print("Lucas ha sacado papel y tú tijeras, el ganador eres tú")  # Tú ganas
        contador_tu += 1 
        print(f"Llevas {contador_tu} partidas ganadas")
    
    elif lucas == 3 and eleccion == 1:
        print("Lucas ha sacado tijera y tú piedra, el ganador es Lucas")  # Lucas gana
        contador_lucas += 1
        print(f"Lucas lleva {contador_lucas} partidas ganadas")
        
    elif lucas == 3 and eleccion == 2:
        print("Lucas ha sacado tijera y tú papel, el ganador eres tú")  # Tú ganas
        contador_tu += 1
        print(f"Llevas {contador_tu} partidas ganadas")
        
    elif lucas == 3 and eleccion == 3:
        print("Los dos habéis sacado tijera, empate")  # Empate
    
    # Verifica si alguien ha ganado 3 partidas
    if contador_lucas == 3:
        print("¡¡¡El ganador ha sido Lucas!!!")   
    elif contador_tu == 3:
        print("¡¡¡El ganador eres tú!!!")  # Mensaje de victoria para el jugador


# Ejercicio 3 ---------------------------------------------------------------
# Solicitar saldo inicial
saldo = float(input("Introduce el saldo inicial de la cuenta: "))  # Pide el saldo inicial
while saldo < 0:
    print("El saldo no puede ser negativo. Inténtalo de nuevo.")  # Mensaje de error si el saldo es negativo
    saldo = float(input("Introduce el saldo inicial de la cuenta: "))  # Vuelve a pedir el saldo

ingresos = 0  # Contador de ingresos
retiros = 0  # Contador de retiros

while True:
    print("\nMenú:")  # Muestra el menú de opciones
    print("1. Ingresar dinero")
    print("2. Retirar dinero")
    print("3. Mostrar saldo")
    print("4. Estadísticas")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")  # Solicita la opción al usuario

    if opcion == '1':
        cantidad = float(input("Introduce la cantidad a ingresar: "))  # Solicita la cantidad a ingresar
        if cantidad < 0:
            print("No se pueden ingresar cantidades negativas.")  # Mensaje de error si la cantidad es negativa
        else:
            saldo += cantidad  # Suma la cantidad al saldo
            ingresos += 1  # Incrementa el contador de ingresos
            print(f"Ingreso exitoso. Nuevo saldo: {saldo}")  # Muestra el nuevo saldo

    elif opcion == '2':
        cantidad = float(input("Introduce la cantidad a retirar: "))  # Solicita la cantidad a retirar
        if cantidad < 0:
            print("No se pueden retirar cantidades negativas.")  # Mensaje de error si la cantidad es negativa
        elif saldo - cantidad < 0:
            print("No puedes retirar esa cantidad. Saldo insuficiente.")  # Mensaje si el saldo es insuficiente
        else:
            saldo -= cantidad  # Resta la cantidad del saldo
            retiros += 1  # Incrementa el contador de retiros
            print(f"Retiro exitoso. Nuevo saldo: {saldo}")  # Muestra el nuevo saldo

    elif opcion == '3':
        print(f"Saldo actual: {saldo}")  # Muestra el saldo actual

    elif opcion == '4':
        print(f"Ingresos realizados: {ingresos}")  # Muestra el número de ingresos
        print(f"Retiros realizados: {retiros}")  # Muestra el número de retiros

    elif opcion == '5':
        print("Saliendo del programa.")  # Mensaje de salida
        break  # Sale del bucle

    else:
        print("Opción no válida. Inténtalo de nuevo.")  # Mensaje de error si la opción no es válida


