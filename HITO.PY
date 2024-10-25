#Ejercicio1---------------------------------------------------------------
# def dibujar_cuadrado(lado):
#     for i in range(lado):
#         print('*' * lado)

# def dibujar_rectangulo(base, altura):
#     for i in range(altura):
#         print('*' * base)

# while True:
#     print("Selecciona una figura:")
#     print("1 - Cuadrado")
#     print("2 - Rectángulo")
#     print("3 - Salir")
        
#     opcion = input("Ingresa tu opción: ")

#     if opcion == '1':
#         lado = int(input("Ingresa el lado del cuadrado: "))
#         dibujar_cuadrado(lado)
#         area = lado ** 2
#         perimetro = 4 * lado
#         print(f"Área: {area}, Perímetro: {perimetro}")

#     elif opcion == '2':
#         base = int(input("Ingresa la base del rectángulo: "))
#         altura = int(input("Ingresa la altura del rectángulo: "))
#         dibujar_rectangulo(base, altura)
#         area = base * altura
#         perimetro = 2 * (base + altura)
#         print(f"Área: {area}, Perímetro: {perimetro}")

#     elif opcion == '3':
#         print("Saliendo...")
#         break

#     else:
#         print("Opción no válida. Intenta de nuevo.")


#Ejercicio2---------------------------------------------------------------
import random
lucas = random.randint(1,3)

piedra = 1
papel = 2
tijera = 3


contador_lucas = 0
contador_tu = 0


while contador_lucas != 3 and contador_tu != 3 : 
    
    eleccion = int(input("selecciona priedra(1),papel(2) o tijera(3)"))
    if lucas == 1 and eleccion == 1:
        print("Lucas ha sacado piedra, y tu también")
        print("Empate")
        
    elif lucas == 1 and eleccion == 2 :
        print("lucas ha sacado piedra y tu papel el ganador eres tu")
        contador_tu = contador_tu + 1
        print(f"Llevas {contador_tu} partidas ganadas")
    
    elif lucas == 1 and eleccion == 3:
        print("lucas ha sacaodo piedra y tu tijera el ganador es lucas")
        contador_lucas = contador_lucas +1 
        print(f"lucas lleva {contador_lucas} partidas ganadas")
    
    elif lucas == 2 and eleccion == 1:
        print("lucas ha sacado papel y tu piedra ha ganado lucas")
        contador_lucas = contador_lucas + 1 
        print(f"lucas lleva {contador_lucas} partidas ganadas ")
        
    elif lucas == 2 and eleccion == 2:
        print("lucas y tu habeis sacado paple")
        print("empate")
        
    elif lucas == 2 and eleccion == 3:
        print ("lucas ha sacado papel y tu tijeras el ganador eres tu  ")
        contador_tu = contador_tu + 1 
        print(f"llevas {contador_tu} partidas ganadas")
    
    elif lucas == 3 and eleccion == 1:
        print("lucas ha sacado tijera y tu tijeras el ganador es lucas ")
        contador_lucas = contador_lucas + 1
        print(f"lucas lleva {contador_lucas} partidas ganadas ")
        
    elif lucas == 3 and eleccion == 2:
        print("lucas ha sacado tijera y tu paple el ganador eres tu ")
        contador_lucas = contador_lucas + 1
        print(f"llevas {contador_tu} partidas ganadas")
    elif lucas == 3 and eleccion == 3:
        print("los dos habeis sacado tijera empate")
         
    if contador_lucas == 3:
     print("¡¡¡el ganador ha sido lucas!!!")   
    else: contador_tu == 3
    print("¡¡¡el ganador eres tu !!!")  

