import os
import primos
from utils import imprimir_encabezado, pausa, validacion_entrada_int, mcd, inverso_modular, VERDE, AMARILLO, ROJO, RESET



def cifrar_archivo():
    imprimir_encabezado("CIFRAR ARCHIVO (texto.txt)")
    
    if not os.path.exists("texto.txt"):
        print(f"{ROJO}Error: No se encontró el archivo 'texto.txt' en el directorio.{RESET}")
        pausa()
        return

    n = sesion_rsa['n']
    e = sesion_rsa['e']

    if n is None or e is None:
        print(f"{AMARILLO}No hay claves en memoria. Ingrese datos manualmente:{RESET}")
        e = validacion_entrada_int("Ingrese Clave Pública (e): ")
        n = validacion_entrada_int("Ingrese Módulo (n): ")

    try:
        with open("texto.txt", "r", encoding="utf-8") as f:
            contenido = f.read()
        
        # Validación de tamaño de n frente a los caracteres
        max_char_val = max(ord(char) for char in contenido) if contenido else 0
        if max_char_val >= n:
            print(f"{ROJO}⚠️ ADVERTENCIA: El módulo n ({n}) es demasiado pequeño.{RESET}")
            print(f"El carácter más 'grande' en tu texto tiene valor {max_char_val}.")
            print(f"Para evitar corrupción, elige primos p y q tales que p*q > {max_char_val}.")
            if not input("¿Deseas continuar de todos modos? (s/n): ").lower().startswith('s'):
                return

        cifrados = [pow(ord(char), e, n) for char in contenido]
        
        with open("mensaje_cifrado.txt", "w") as f:
            f.write(",".join(map(str, cifrados)))
            
        print(f"{VERDE}¡Éxito! El contenido de 'texto.txt' ha sido cifrado.{RESET}")
        print(f"Archivo generado: {AMARILLO}mensaje_cifrado.txt{RESET}")
    except Exception as ex:
        print(f"{ROJO}Error al procesar el archivo: {ex}{RESET}")
    
    pausa()

def descifrar_archivo():
    imprimir_encabezado("DESCIFRAR ARCHIVO (mensaje_cifrado.txt)")
    
    if not os.path.exists("mensaje_cifrado.txt"):
        print(f"{ROJO}Error: No se encontró el archivo 'mensaje_cifrado.txt'.{RESET}")
        pausa()
        return

    n = sesion_rsa['n']
    d = sesion_rsa['d']

    if n is None or d is None:
        print(f"{AMARILLO}No hay claves en memoria. Ingrese datos manualmente:{RESET}")
        d = validacion_entrada_int("Ingrese Clave Privada (d): ")
        n = validacion_entrada_int("Ingrese Módulo (n): ")

    try:
        with open("mensaje_cifrado.txt", "r") as f:
            contenido = f.read()
        
        cifrados = [int(x.strip()) for x in contenido.split(',')]
        mensaje_recuperado = "".join([chr(pow(c, d, n)) for c in cifrados])
        
        with open("mensaje_recuperado.txt", "w", encoding="utf-8") as f:
            f.write(mensaje_recuperado)
            
        print(f"{VERDE}¡Éxito! El archivo ha sido descifrado.{RESET}")
        print(f"Archivo generado: {AMARILLO}mensaje_recuperado.txt{RESET}")
        print(f"Vista previa: {mensaje_recuperado[:50]}...")
    except Exception as ex:
        print(f"{ROJO}Error al procesar el archivo: {ex}{RESET}")
    
    pausa()

# Variables globales para guardar la sesión actual
sesion_rsa = {
    'p': None,
    'q': None,
    'n': None,
    'phi': None,
    'e': None,
    'd': None
}

def mostrar_introduccion():
    imprimir_encabezado("INTRODUCCIÓN A RSA")
    
    print(f"{AMARILLO}¿Qué es la criptografía?{RESET}")
    print(
        """Es el arte y la ciencia de proteger la información mediante
    el uso de matemáticas, para que solo las personas autorizadas
    puedan leer los datos.""")
    pausa()

    print(f"\n{AMARILLO}CONCEPTOS CLAVE:{RESET}")
    print(f"- {VERDE}Texto Plano:{RESET} El mensaje original (ej: 'HOLA').")
    print(f"- {VERDE}Cifrado:{RESET} Transformar el mensaje en algo ilegible.")
    print(f"- {VERDE}Descifrado:{RESET} Recuperar el mensaje original.")
    print(f"- {VERDE}Módulo (n):{RESET} El número que sirve como 'escenario' de las operaciones.")
    pausa()

    print(f"\n{AMARILLO}1. Criptografía Simétrica{RESET}")
    print("Usa la misma llave para cerrar y abrir. Es como una caja fuerte.")
    print("Problema: ¿Cómo le das la llave a tu amigo sin que nadie la robe?")
    pausa()

    print(f"""\n{AMARILLO}2. Criptografía Asimétrica (RSA){RESET}")
    Usa un par de llaves matemáticas relacionadas:""")
    print(f"""- {VERDE}Clave Pública (e):{RESET} Se usa para CIFRAR. Es como un candado")
    abierto que cualquiera puede usar para cerrarte un mensaje.""")
    print(f"""- {VERDE}Clave Privada (d):{RESET} Se usa para DESCIFRAR. Es la única")
    llave física que abre ese candado. ¡Solo tú la tienes!""")
    pausa()

    print(f"\n{AMARILLO}El flujo de RSA:{RESET}")
    print("""
    Mensaje original (M)
       │
       ▼
    C = M^e mod n  <-- (Cifrado con Clave Pública)
       │
       ▼
    Mensaje Cifrado (C)
       │
       ▼
    M = C^d mod n  <-- (Descifrado con Clave Privada)
       │
       ▼
    Mensaje recuperado (M)
    """)
    pausa()

def obtener_primo_valido(mensaje):
    while True:
        p = validacion_entrada_int(mensaje, minimo=2)
        if primos.es_primo(p):
            print(f"{VERDE}¡Genial! {p} es un número primo.{RESET}")
            return p
        else:
            print(f"{ROJO}¡Vaya! {p} no es primo. Intenta de nuevo.{RESET}")

def generar_claves():
    global sesion_rsa
    imprimir_encabezado("GENERACIÓN DE CLAVES RSA")
    
    p = obtener_primo_valido("Introduce p (ej. 17): ")
    q = obtener_primo_valido("Introduce q (ej. 11): ")

    if p == q:
        print(f"{ROJO}Error: p y q deben ser diferentes.{RESET}")
        pausa()
        return

    n = p * q
    phi = (p - 1) * (q - 1)

    if n < 256:
        print(f"""\n{ROJO}⚠️ NOTA: Tu módulo n ({n}) es menor a 256.{RESET}
               Esto funcionará para letras básicas (A-Z), pero fallará con
               tildes, eñes o símbolos especiales. ¡Tenlo en cuenta!""")

    print(f"\n{AMARILLO}Cálculos paso a paso:{RESET}")
    print(f"1. Módulo n = p * q = {p} * {q} = {n}")
    print(f"   (Este número se compartirá públicamente)")
    
    print(f"\n2. Función Fi φ(n) = (p-1)*(q-1) = {phi}")
    print(f"   (¡Este es el SECRETO! Fi nos dice cuántos números son ")
    print(f"   'parientes' de n. Solo se puede calcular si conoces p y q).")

    e_sugerido = 3
    while mcd(e_sugerido, phi) != 1:
        e_sugerido += 2
    
    print(f"\n3. El exponente 'e' debe ser coprimo con φ(n) (no compartir factores).")
    entrada_e = input(f"   Elige 'e' (ENTER para usar {e_sugerido}): ").strip()
    e = e_sugerido if entrada_e == "" else int(entrada_e)
    
    if mcd(e, phi) != 1:
        print(f"   {ROJO}Error: {e} no es coprimo con {phi}. Usando {e_sugerido}.{RESET}")
        e = e_sugerido

    d = inverso_modular(e, phi)
    print(f"\n4. La Clave Privada 'd' es el inverso de 'e' mod φ(n).")
    print(f"   d = {d}")
    print(f"   (Esto garantiza que (e * d) mod φ(n) = 1, la 'magia' que")
    print(f"   permite que una llave deshaga lo que hizo la otra).")

    sesion_rsa.update({'p': p, 'q': q, 'n': n, 'phi': phi, 'e': e, 'd': d})
    print(f"\n{VERDE}¡Claves generadas con éxito!{RESET}")
    print(f"\n{AMARILLO}Tu clave PÚBLICA es: {RESET}{n}")
    print(f"\n{AMARILLO}Tu clave PRIVADA es: {RESET}{d}")
    pausa()

def cifrar_mensaje():
    imprimir_encabezado("CIFRAR MENSAJE")
    n = sesion_rsa['n']
    e = sesion_rsa['e']

    if n is None or e is None:
        print(f"{AMARILLO}No hay claves en memoria. Ingrese datos manualmente:{RESET}")
        e = validacion_entrada_int("Ingrese Clave Pública (e): ")
        n = validacion_entrada_int("Ingrese Módulo (n): ")

    mensaje_texto = input("\nIngrese el mensaje a cifrar: ")
    print(f"\n{AMARILLO}Proceso de cifrado:{RESET}")
    print("+--------+-------+---------+")
    print("| Letra  | ASCII | Cifrado |")
    print("+--------+-------+---------+")
    
    cifrados = []
    for char in mensaje_texto:
        m = ord(char)
        c = pow(m, e, n)
        cifrados.append(c)
        print(f"| {char:^6} | {m:^5} | {c:^7} |")
    
    print("+--------+-------+---------+")
    print(f"\n{VERDE}Mensaje cifrado completo:{RESET}")
    print(", ".join(map(str, cifrados)))
    pausa()

def descifrar_mensaje():
    imprimir_encabezado("DESCIFRAR MENSAJE")
    n = sesion_rsa['n']
    d = sesion_rsa['d']

    if n is None or d is None:
        print(f"{AMARILLO}No hay claves en memoria. Ingrese datos manualmente:{RESET}")
        d = validacion_entrada_int("Ingrese Clave Privada (d): ")
        n = validacion_entrada_int("Ingrese Módulo (n): ")

    entrada = input("\nIngrese los números cifrados separados por comas: ")
    try:
        cifrados = [int(x.strip()) for x in entrada.split(',')]
    except ValueError:
        print(f"{ROJO}Error: Entrada no válida.{RESET}")
        return

    print(f"\n{AMARILLO}Proceso de descifrado:{RESET}")
    mensaje_recuperado = ""
    for c in cifrados:
        m = pow(c, d, n)
        char = chr(m)
        mensaje_recuperado += char
        print(f"Cifrado {c} -> ASCII {m} -> Letra '{char}'")
    
    print(f"\n{VERDE}Mensaje recuperado: {mensaje_recuperado}{RESET}")
    pausa()

def exportar_sesion():
    imprimir_encabezado("EXPORTAR SESIÓN")
    if sesion_rsa['n'] is None:
        print(f"{ROJO}No hay datos de sesión para exportar. Genera claves primero.{RESET}")
        pausa()
        return

    nombre_archivo = "sesion_rsa.txt"
    try:
        with open(nombre_archivo, "w") as f:
            f.write("=== SESIÓN CRIPTO-PRIMOS ===\n")
            f.write(f"p: {sesion_rsa['p']}\n")
            f.write(f"q: {sesion_rsa['q']}\n")
            f.write(f"Modulo (n): {sesion_rsa['n']}\n")
            f.write(f"Phi (n): {sesion_rsa['phi']}\n")
            f.write(f"Clave Publica (e): {sesion_rsa['e']}\n")
            f.write(f"Clave Privada (d): {sesion_rsa['d']}\n")
        print(f"{VERDE}Sesión exportada exitosamente a '{nombre_archivo}'.{RESET}")
    except Exception as e:
        print(f"{ROJO}Error al exportar: {e}{RESET}")
    pausa()
