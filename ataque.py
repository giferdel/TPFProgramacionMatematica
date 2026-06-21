import time
import sys,os
from utils import imprimir_encabezado, pausa, validacion_entrada_int, AMARILLO, VERDE, ROJO, RESET
from main import mostrar_menu


#Control de desbordamiento y colapso en tiempos de ejecución
def control_tamanio_numero(n):
    # Conta los dígitos usando el método str()
    if len(str(abs(n))) > 200:
        # Lanzamos un error controlado
        raise ValueError(
            "El número es demasiado grande para la fuerza bruta. "
            "Por favor, utiliza el Test de Miller-Rabin."
        )
    
def iniciar_ataque():
    os.system("cls")
    imprimir_encabezado("MODO ATAQUE: FACTORIZACIÓN POR FUERZA BRUTA")
    print("""Descifrar claves por fuerza bruta es el método más simple, pero más tardío,
que existe en la informática para romper una contraseña: consiste en probar 
TODAS LAS COMBINACIONES POSIBLES una por una hasta encontrar la correcta. """)
    pausa()
    print(F"{AMARILLO}\nRSA y Fuerza Bruta: una aventura peligrosa {RESET}\n")
    print("""Para descifrar una clave RSA por fuerza bruta, el ataque no consiste en adivinar la 
contraseña final probando palabras, sino en atacar la matemática del algoritmo.
          
En RSA, la seguridad depende de que es extremadamente fácil multiplicar dos números primos enormes, 
pero infinitamente difícil hacer el camino inverso.
        
El procedimiento exacto para romper RSA por fuerza bruta se basa en la factorización, es decir,
la seguridad de RSA depende de que es DIFÍCIL encontrar dos números primos p y q a partir de un número n
extremadamente grande (617 dígitos).""")

    print(f"{AMARILLO}\n¿Te animas a intentarlo? {RESET}")
    pausa()
    os.system("cls")
    print(f"{VERDE}¡EMPECEMOS!{RESET}")
    n = validacion_entrada_int("\nIntroduce un número n para intentar romper (ej. 187 o 323): ", minimo=4)
    cantidad_bits = n.bit_length()
    
    print(f"\n{AMARILLO}Iniciando ataque de fuerza bruta...{RESET}")
    inicio = time.time()
    
    
    
    try:
    # Primero controlamos el tamaño. Si tiene más de 200 dígitos, salta directo al 'except'
        control_tamanio_numero(n)
        encontrado = False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                p = i
                q = n // i
                fin = time.time()
                print(f"\n{VERDE}¡ÉXITO! Encontrado en {fin - inicio:.6f} segundos.{RESET}")
                print(f"n = {p} * {q}")
                print(f"Ahora que conocemos p y q, podemos calcular la Clave Privada y leer los mensajes.")
                encontrado = True
                break
        
        if not encontrado:
            print(f"\n{ROJO}No se encontraron factores primos en el rango.{RESET}")
            print("Es posible que el número que ingresaste sea Primo")
            print("Podés verificarlo en la opción 2 del menú principal")

        if encontrado:
            print(f"\n{AMARILLO}REFLEXIÓN:{RESET}")
            print("En este ejemplo, tu número tiene pocos dígitos y se rompe en milisegundos.")
            
            print(f"\n{VERDE}¿POR QUÉ IMPORTA EL TAMAÑO?{RESET}")
            print(f"El número n que rompiste tiene {len(str(n))} dígitos. Una clave RSA real usa 617 dígitos.")
            print("Para que te des una idea:")
            print(f"- Tu número ({cantidad_bits} bits): {n}")
            print("- Una clave RSA real (2048 bits):")
            print("32317006071311007300714876688669951960444102669715484032130345427524633788861309197123569032101123411444445555566666777778888899999000000...")
            print("  (¡Y así hasta completar más de 600 dígitos!)")
            
            print(f"\n{AMARILLO}CONCLUSIÓN:{RESET}")
            print("Factorizar un número de 2048 bits tomaría aproximadamente")
            print("300,000,000,000,000 de años con una PC normal.")
            print("Por eso tus mensajes de WhatsApp y tus compras online están seguros.")
    
    except ValueError as error:
        # Este bloque SÓLO se ejecuta si control_tamanio_numero(n) tiró el error
        print(f"\n⚠️ ALERTA: {error}")
        print(f"\n{VERDE}¿POR QUÉ IMPORTA EL TAMAÑO?{RESET}")
        print(f"""El número n que intentaste romper tiene {len(str(n))} dígitos y se requiere una supercomputadora para factorizarlo. 
\nRSA real usa 617 dígitos.""")
        print("Para que te des una idea:")
        print("una clave RSA real (2048 bits) se parecería a:")
        print("  32317006071311007300714876688669951960444102669715484032130345427524633788861309197123569032101123411444445555566666777778888899999000000...")
        print("  (¡Y así hasta completar más de 600 dígitos!)")

    finally:
        # Esto se ejecuta SIEMPRE (haya o no error) para dejar la consola limpia
        pausa() 
        os.system("cls")
        mostrar_menu

    
            
