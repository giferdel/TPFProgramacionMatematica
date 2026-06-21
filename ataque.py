import time
from utils import imprimir_encabezado, pausa, validacion_entrada_int, AMARILLO, VERDE, ROJO, RESET

def iniciar_ataque():
    imprimir_encabezado("MODO ATAQUE: FACTORIZACIÓN")
    print("La seguridad de RSA depende de que es DIFÍCIL encontrar")
    print("los primos p y q a partir de n.")
    pausa()

    n = validacion_entrada_int("\nIntroduce un número n para intentar romper (ej. 187 o 323): ", minimo=4)
    
    print(f"\n{AMARILLO}Iniciando ataque de fuerza bruta...{RESET}")
    inicio = time.time()
    
    encontrado = False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            p = i
            q = n // i
            fin = time.time()
            print(f"\n{VERDE}¡ÉXITO! Encontrado en {fin - inicio:.4f} segundos.{RESET}")
            print(f"n = {p} * {q}")
            print(f"Ahora que conocemos p y q, podemos calcular d y leer los mensajes.")
            encontrado = True
            break
    
    if not encontrado:
        print(f"\n{ROJO}No se encontraron factores primos en el rango.{RESET}")

    print(f"\n{AMARILLO}REFLEXIÓN EDUCATIVA:{RESET}")
    print("En este ejemplo, n tiene pocos dígitos y se rompe en milisegundos.")
    
    print(f"\n{VERDE}¿POR QUÉ IMPORTA EL TAMAÑO?{RESET}")
    print("El número n que rompiste tiene 3 dígitos. RSA real usa 617 dígitos.")
    print("Para que te des una idea:")
    print("- n educativo (8 bits): 187")
    print("- n real (2048 bits):")
    print("  323170060713110073007148766886699519604441026697154840321303454275246")
    print("  33788861309197123569032101123411444445555566666777778888899999000000...")
    print("  (¡Y así hasta completar más de 600 dígitos!)")
    
    print(f"\n{AMARILLO}CONCLUSIÓN:{RESET}")
    print("Factorizar un número de 2048 bits tomaría aproximadamente")
    print("300,000,000,000,000 de años con una PC normal.")
    print("Por eso tus mensajes de WhatsApp y tus compras online están seguros.")
    pausa()
