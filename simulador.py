from utils import imprimir_encabezado, pausa, AMARILLO, VERDE, RESET

def ejecutar_simulacion():
    imprimir_encabezado("SIMULACIÓN PASO A PASO")
    print("Vamos a ver cómo funciona RSA con un ejemplo real.")
    pausa()

    print(f"\n{AMARILLO}Paso 1: Elegimos dos números primos.{RESET}")
    print("p = 17")
    print("q = 11")
    pausa()

    n = 17 * 11
    print(f"\n{AMARILLO}Paso 2: Calculamos el módulo n.{RESET}")
    print("n = p * q")
    print(f"n = 17 * 11 = {n}")
    print("Este número es parte de tu Clave Pública. Es el 'candado'.")
    pausa()

    phi = (17 - 1) * (11 - 1)
    print(f"\n{AMARILLO}Paso 3: Calculamos φ(n) (Función Fi).{RESET}")
    print("φ(n) = (p-1) * (q-1)")
    print(f"φ(n) = 16 * 10 = {phi}")
    print("Este número es SECRETO. Sirve para crear la Clave Privada.")
    pausa()

    e = 7
    print(f"\n{AMARILLO}Paso 4: Elegimos e (exponente público).{RESET}")
    print(f"Elegimos e = {e}, que es coprimo con {phi}.")
    print("La Clave Pública completa es el par (e, n) -> (7, 187).")
    pausa()

    # d tal que (d*7) mod 160 = 1 -> d=23
    d = 23
    print(f"\n{AMARILLO}Paso 5: Calculamos d (exponente privado).{RESET}")
    print(f"Buscamos d tal que (d * {e}) mod {phi} = 1")
    print(f"En este caso, d = {d} porque (23 * 7) = 161, y 161 mod 160 = 1.")
    print("La Clave Privada completa es el par (d, n) -> (23, 187).")
    pausa()

    m = 72 # 'H'
    print(f"\n{AMARILLO}Paso 6: Ciframos un mensaje.{RESET}")
    print(f"Queremos enviar la letra 'H', que en ASCII es {m}.")
    print(f"Operación: C = M^e mod n")
    print(f"C = 72^7 mod {n}")
    c = pow(m, e, n)
    print(f"Resultado Cifrado (C) = {c}")
    print("Ahora enviamos el número 30 por Internet. Si alguien lo intercepta,")
    print("no sabrá que significa 'H' sin la Clave Privada.")
    pausa()

    print(f"\n{AMARILLO}Paso 7: Desciframos el mensaje.{RESET}")
    print(f"El receptor usa su Clave Privada (d={d}) para recuperar el mensaje.")
    print(f"Operación: M = C^d mod n")
    print(f"M = {c}^{d} mod {n}")
    m_final = pow(c, d, n)
    print(f"Resultado Descifrado (M) = {m_final} (carácter '{chr(m_final)}')")
    
    print(f"\n{VERDE}¡Simulación completada!{RESET}")
    print(f"{AMARILLO}LECCIÓN APRENDIDA:{RESET}")
    print("1. RSA usa la dificultad de factorizar números grandes.")
    print("2. Multiplicar primos es fácil, pero deshacerlo es muy difícil.")
    print("3. La Clave Pública cifra, la Clave Privada descifra.")
    pausa()
