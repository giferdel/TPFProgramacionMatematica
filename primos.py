import sys,os
import random
from utils import imprimir_encabezado, pausa, ROJO, VERDE, RESET
"""
MÓDULO DE TEORÍA DE NÚMEROS: PRIMOS
----------------------------------
Los números primos son los "átomos" de las matemáticas. 
En criptografía RSA, su importancia radica en que son fáciles de multiplicar,
pero extremadamente difíciles de separar (factorizar) una vez multiplicados.

Este concepto se llama 'Función de Trampilla':
- Hacia adelante (Multiplicar p * q = n): Muy fácil.
- Hacia atrás (Factorizar n para hallar p y q): Casi imposible para números grandes.
"""
def def_primos():
    imprimir_encabezado("¿QUÉ SON LOS NÚMEROS PRIMOS?")
    print("""
    Los números primos son, en esencia, los "ladrillos" de las matemáticas.
    Aunque su definición es extremadamente simple, esconden un comportamiento tan complejo y misterioso
    que lleva miles de años desconcertando a las mentes más brillantes de la historia.\n

    Un número primo es un número entero mayor que 1 que solo puede dividirse exactamente por 1 y por sí mismo.
    Si un número tiene otros divisores, se le llama número compuesto.

    - Primos: 2, 3, 5, 7, 11, 13, 17, 19, 23...

    - Compuestos: 4 (divisible por 2), 6 (divisible por 2 y 3), 9 (divisible por 3)...
          
    - Coprimos: Dos números enteros son coprimos (también llamados primos entre sí o primos relativos) 
      cuando no tienen ningún divisor común mayor que 1.
      Por ejemplo el 8 y el 15 son coprimos pues no tienen divisores en común.
          
    El Teorema Fundamental de la Aritmética: 
          Este teorema demuestra por qué son tan importantes. 
          Establece que cualquier número entero mayor que 1 es primo o puede descomponerse como 
          un producto único de números primos. 
          Por ejemplo, el 60 no es primo, pero se construye de forma única como 2 x 2 x 3 x 5. 
          De ahí que se consideren los ladrillos de todos los demás números.
    """)
    pausa()
    imprimir_encabezado("¿POR QUÉ SON TAN COMPLEJOS?")
    print(
    """
    A pesar de su definición tan limpia, cuando los matemáticos intentan analizar cómo se comportan, 
    se topan con un muro de alta complejidad. Estas son sus principales dificultades:
    1. La aparente aleatoriedad de su distribución:
        Si miras la recta numérica, los números primos parecen aparecer al azar. 
        No hay un intervalo fijo entre ellos. A veces están pegados (como el 11 y el 13, llamados "primos gemelos") 
        y a veces hay desiertos gigantescos de números compuestos sin un solo primo.
        No existe una fórmula polinómica simple y exacta que te diga: "Pones la posición n y te devuelvo el n-ésimo número primo". 
        Predecir dónde aparecerá el próximo primo es uno de los mayores desafíos de la ciencia.

    2. La asimetría de la factorización (La base de la criptografía)
        Esta complejidad es, irónicamente, lo que hace que internet sea seguro hoy en día (a través de sistemas como el cifrado RSA).
        Hacia adelante es fácil: Si te pido que multipliques dos números primos grandes, por ejemplo, 61 X 53, una computadora lo hace 
        al instante: 3233.
        Hacia atrás es extremadamente difícil: Si te doy el número 3233 y te pido que descubras qué dos números primos se multiplicaron 
        para obtenerlo, el proceso de "factorización" es computacionalmente lento.
        Cuando los números primos tienen cientos de dígitos, a las supercomputadoras actuales les tomaría miles de años encontrar 
        esos dos factores primos originarios. 
        
        Esta asimetría genera la complejidad que protege nuestras contraseñas y cuentas bancarias.

    3. El problema de la primalidad
        Saber si un número extremadamente grande es primo o compuesto (sin necesidad de encontrar sus factores) es un campo de 
        estudio complejo en computación.
        Aunque existen algoritmos modernos muy eficientes para esto —como el test de Miller-Rabin (que usa probabilidades) 
        o el algoritmo AKS (que es determinista)—, diseñar pruebas que funcionen a gran velocidad con números de millones 
        de dígitos sigue requiriendo matemáticas increíblemente avanzadas.
    """)
    pausa()
    print(f"{VERDE}¡Empecemos a jugar con los Números Primos!.{RESET}")
    pausa()
    os.system('cls')

# def es_primo(n):
#     """Alias para el método por defecto (División por Ensayo)."""
#     return es_primo_division_ensayo(n)

#DIVISIONES SUCESIVAS
def es_primo_division_ensayo(n):
    """
    MÉTODO: DIVISIÓN POR ENSAYO
    ---------------------------
    Concepto: Intentar dividir el número por todos los posibles factores menores.
    
    Fortalezas: 100% exacto (determinista), fácil de entender.
    Debilidades: Se vuelve muy lento. Si n tiene 100 dígitos, ¡no terminaría nunca!
    """
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    print(f"Para {n} tenemos que: Ningún numero entre 2 y {n-1} es divisor de {n}")
    return True


def explicar_no_primo_DS(n):
    """Encuentra el divisor más pequeño y retorna un mensaje educativo."""
    if n <= 1:
        return f"El número {n} no se considera primo por definición (un número primo debe ser mayor que 1)."
    
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            otro_factor = n // divisor
            print(f"{divisor} es divisor de {n}")
            return f"El número {n} NO es primo.\n¿Sabes por qué? Porque puede dividirse por {divisor} ({divisor} x {otro_factor} = {n}).\nUn número primo solo puede dividirse por 1 y por sí mismo."
        else:
            print(f"Divisor de prueba: {divisor} \nCociente: {n//divisor} - Resto: {n%divisor} ----> {divisor} No es divisor")
        divisor += 1
        print(f"\nNUEVO divisor de prueba: {divisor}")
    return f"El número {n} es primo."
#*****************************************************************************************************************************

#TEST DE FERMAT
def es_primo_fermat(n, k=5):
    """
    TEST DE FERMAT
    --------------
    Concepto: Basado en el 'Pequeño Teorema de Fermat'. Si n es primo, 
    entonces para cualquier 'a': a^(n-1) ≡ 1 mod n.
    
    Fortalezas: Increíblemente rápido.
    Debilidades: Probabilístico. Existen números compuestos llamados 'Números de Carmichael' 
    (como el 561) que engañan a este test haciéndose pasar por primos.
    """
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0: return False
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    print(f"Para {n} tenemos que: {a}^{n-1} ≡ 1 mod ({n})")
    return True

def explicar_no_primo_TF(n):
     #mostrar cuando falla el test de fermat
    if n <= 1:
        return f"El número {n} no se considera primo por definición (un número primo debe ser mayor que 1)."
    
    for i in range(n-2):
        a = random.randint(2, n - 2)
        
        if pow(a, n - 1, n) != 1:
            print(f"Prueba {i+1} -> Base:{a} - Exponente:{n-1} - Divisor: {n} ---> MODULO: {pow(a, n - 1, n)}")
            
            return f"El número {n} No ES PRIMO."
        else:
            # Si da 1, el número pasa la ronda actual (Fermat "piensa" que podría ser primo)
            print(f"Prueba {i+1} -> Base {a}: Pasó la prueba (módulo dio 1). Hasta ahora ES PRIMO. Continuando...")
            print(f"Pruebo con nueva base\n")
                
    return True
    
    # divisor = 2
    # while divisor * divisor <= n:
    #     if n % divisor == 0:
    #         otro_factor = n // divisor
    #         print(f"{divisor} es divisor de {n} cociente: {otro_factor}")
    #         return f"El número {n} NO es primo.\n¿Sabes por qué? Porque puede dividirse por {divisor} ({divisor} x {otro_factor} = {n}).\nUn número primo solo puede dividirse por 1 y por sí mismo."
    #     else:
    #         print(f"Divisor de prueba: {divisor} - Cociente: {n//divisor} - Resto: {n%divisor} --- {divisor} No es divisor")
    #     divisor += 1
    #     print(f"\nNUEVO divisor de prueba: {divisor}")
    # return f"El número {n} es primo."
#*****************************************************************************************************************************

#TEST MILLER-RABIN
def es_primo_miller_rabin(n, k=5):
    """
    TEST DE MILLER-RABIN
    --------------------
    Concepto: Una versión sofisticada y más segura del test de Fermat. 
    Analiza las raíces cuadradas de la unidad en aritmética modular.
    
    Fortalezas: Es el estándar de la industria (usado en OpenSSL, Python, etc.).
    Debilidades: Sigue siendo probabilístico, pero con k=40, la probabilidad de 
    error es menor que la de que un rayo golpee tu computadora justo ahora.
    """
    if n <= 1: return False  #Se descarta cualquier número menor o igual a 1
    if n <= 3: return True  #Sumando a la línea 187, se consideran de manera inmediata a 2 y al 3 como números primos
    if n % 2 == 0: return False  #Se descarta todo número que sea PAR

    # Hallar d tal que n-1 = 2^r * d
    r = 0
    d = n - 1
    while d % 2 == 0:  #Mientras d sea par de lo divide por dos y se agrega 1 a "r" que será el exponente de la base
        r += 1  
        d //= 2  
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def explicar_no_primo_MR(n,k=5):
    #mostrar cuando falla el test de miller rabin
    if n <= 1:
        return f"El número {n} no se considera primo por definición (un número primo debe ser mayor que 1)."
    if n <= 3: return True  #Sumando a la línea 187, se consideran de manera inmediata a 2 y al 3 como números primos
    if n % 2 == 0: return f"El número {n} No ES PRIMO por ser número Par."  #Se descarta todo número que sea PAR
    r = 0
    d = n - 1
    while d % 2 == 0:  #Mientras d sea par de lo divide por dos y se agrega 1 a "r" que será el exponente de la base
        r += 1  
        d //= 2  
    
    for i in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        print(f"\nPRIMERA PARTE: Test de evaluación de base\n")
        print(f"Prueba 1: \nNúmero (n) = {n}\nNúmero par anterior (n-1) = {n-1}\nExponente de 2 en la descomposición (r) = {r}\nFactor impar de la descomposición (d) = {d}\nbase (a) = {a}")
        
        print(f"Tenemos que: {a}^{d} mod {n}={x}")
        
        if x == 1 or x == (n-1):
            return f"El número {n} ES PRIMO."
        if x != 1 and x != (n - 1):
            print(f"\n x = {x} No pasa la primer prueba. ¡Cuidado! puede ser un primo escondido")
            
        print(f"\nSEGUNDA PARTE: Bucle de x^2 sucesiva\n")
        print(f"Buscamos si x se transforma en {n-1} al elevar al cuadrado r-1 veces ({r-1} veces)")
        for i in range(r-1):
            x_anterior = x
            x = pow(x, 2, n)
            print(f"  Prueba {i+1}: ({x_anterior})^2 mod {n} = {x}")
            
            if x == n - 1:
                break
                 
        else:
            print(f"x no logró convertirse en {n-1}")
            return f"El número {n} No ES PRIMO."

def obtener_metodos():
    return {
        "1": {
            "nombre": "División por Ensayo",
            "funcion": es_primo_division_ensayo,
            "fortalezas": "100% exacto (determinista). Ideal para entender el concepto básico.",
            "debilidades": "Se vuelve extremadamente lento con números de muchos dígitos.",
            "descripcion": "Intenta dividir el número por todos los posibles factores menores.",
            "no_primo": explicar_no_primo_DS
        },
        "2": {
            "nombre": "Test de Fermat",
            "funcion": es_primo_fermat,
            "fortalezas": "Extremadamente rápido. Usa matemáticas modulares elegantes.",
            "debilidades": "Probabilístico. Puede dar 'falsos positivos' (números de Carmichael).",
            "descripcion": "Basado en el 'Pequeño Teorema de Fermat'. Si n es primo, entonces para cualquier 'a': a^(n-1) ≡ 1 mod n.",
            "no_primo": explicar_no_primo_TF
        },
        "3": {
            "nombre": "Test de Miller-Rabin",
            "funcion": es_primo_miller_rabin,
            "fortalezas": "El estándar industrial. Muy rápido y altamente confiable.",
            "debilidades": "Teóricamente probabilístico, aunque el riesgo es casi nulo en la práctica.",
            "descripcion": "Una versión sofisticada y más segura del test de Fermat. Analiza las raíces cuadradas de la unidad en aritmética modular.",
            "no_primo": explicar_no_primo_MR
        }
    }






