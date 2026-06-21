import primos
import math
import random
from colores import VERDE, ROJO, AMARILLO, RESET

def imprimir_encabezado(titulo):
    print("\n" + "=" * 50)
    print(f"{AMARILLO}{titulo.center(50)}{RESET}")
    print("=" * 50)

def pausa():
    input("\n[Presiona Enter para continuar...]")

def obtener_primo_valido(mensaje):
    while True:
        try:
            p = int(input(mensaje))
            if primos.es_primo(p):
                print(f"{VERDE}¡Genial! {p} es un número primo.{RESET}")
                return p
            else:
                print(f"{ROJO}¡Vaya! {p} no es primo. Intenta con 2, 3, 5, 7, 11...{RESET}")
        except ValueError:
            print(f"{ROJO}Error: Por favor, introduce un número entero válido.{RESET}")

def ejecutar_mini_rsa():
    imprimir_encabezado("EL SECRETO DE LOS ESPÍAS")
    print("La criptografía moderna usa números primos")
    print("para proteger tus mensajes. ¡Probemos!")

    print("\n¿Qué quieres hacer hoy?")
    print("1. Ser el EMISOR (Cifrar un mensaje)")
    print("2. Ser el RECEPTOR (Descifrar un mensaje)")

    opcion = input("\nSelecciona una opción: ")

    if opcion == '1':
        jugar_como_emisor()
    elif opcion == '2':
        jugar_como_receptor()
    else:
        print("Opción no válida. Volviendo al menú principal.")

def jugar_como_emisor():
    imprimir_encabezado("ROL: EMISOR (Cifrando)")
    print("Vas a enviar un mensaje secreto a un amigo.")

    p = obtener_primo_valido("\nIntroduce un primer número primo (ej. 7): ")
    q = obtener_primo_valido("Introduce otro número primo (ej. 11): ")

    if p == q:
        print("Para este ejemplo, es mejor usar dos primos diferentes.")
        pausa()
        return

    n = p * q
    print(f"\nCalculando módulo: {p} x {q} = {n}")
    print(f"Tu 'Clave Pública' generada es: {n}")

    print("\nEXPLICACIÓN:")
    print(f"Cualquiera puede ver el número {n}, pero")
    print(f"solo tú sabes que vino de multiplicar {p} y {q}.")
    pausa()

    mensaje = -1
    while mensaje < 0 or mensaje >= n:
        try:
            mensaje = int(input(f"\nIntroduce un número secreto para cifrar (0 - {n-1}): "))
            if mensaje >= n:
                print(f"Error: El mensaje debe ser menor que {n}.")
        except ValueError:
            print("Error: Introduce un número entero.")

    # Simulación RSA: usamos e=3 por simplicidad educativa
    # Verificamos si e=3 es válido para estos primos (gcd(e, phi) == 1)
    phi = (p - 1) * (q - 1)
    e = 3
    if math.gcd(e, phi) != 1:
        e = 5 # Segunda opción común
        if math.gcd(e, phi) != 1:
            # Si ni 3 ni 5 funcionan, buscamos el primer impar coprimo
            e = 7
            while math.gcd(e, phi) != 1:
                e += 2

    cifrado = pow(mensaje, e, n)

    print(f"\n--- ENVIANDO MENSAJE ---")
    print(f"Mensaje original: {mensaje}")
    print(f"Operación: ({mensaje}^{e}) mod {n}")
    print(f"RESULTADO CIFRADO: {cifrado}")
    print("\n(Este mensaje cifrado es el que viajaría por Internet)")
    pausa()

def jugar_como_receptor():
    imprimir_encabezado("ROL: RECEPTOR (Descifrando)")
    print("Alguien te ha enviado un mensaje secreto.")
    print("Usarás tus números primos para generar la llave secreta.")

    p = obtener_primo_valido("\nUsa un primo para tu llave (ej. 13): ")
    q = obtener_primo_valido("Usa otro primo para tu llave (ej. 17): ")

    if p == q:
        print("Es más seguro usar primos diferentes.")
        pausa()
        return

    n = p * q
    phi = (p - 1) * (q - 1)

    # Elegir e
    e = 3
    while math.gcd(e, phi) != 1:
        e += 2

    # Calcular d (inverso modular)
    d = pow(e, -1, phi)

    print(f"\nGenerando tus llaves...")
    print(f"Módulo (Público): {n}")
    print(f"Llave Pública (e): {e}")
    print(f"Función de Euler (phi): {phi}  <-- ¡Esto es secreto!")
    pausa()

    # Generar un mensaje aleatorio para que el sistema lo "envíe"
    m_original = random.randint(2, n - 1)
    cifrado = pow(m_original, e, n)

    print(f"\n¡HAS RECIBIDO UN MENSAJE!")
    print(f"Mensaje Cifrado (C): {cifrado}")
    print("\n¿Cómo lo desciframos? Necesitamos la Llave Privada (d).")
    print(f"Se calcula buscando un número tal que: (d * {e}) mod {phi} = 1")
    print(f"Tu Llave Privada calculada es: {d}")
    pausa()

    print(f"\n--- OPERACIÓN DE DESCIFRADO ---")
    print(f"Fórmula: (C ^ d) mod n")
    print(f"Calculando: ({cifrado} ^ {d}) mod {n}...")

    m_descifrado = pow(cifrado, d, n)

    print(f"\n{VERDE}¡RESULTADO: El mensaje secreto era {m_descifrado}!{RESET}")
    if m_descifrado == m_original:
        print(f"{VERDE}¡La matemática de los primos ha funcionado perfectamente!{RESET}")

    pausa()

