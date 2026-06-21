from utils import imprimir_encabezado, pausa, validacion_entrada_int, AMARILLO, VERDE, ROJO, RESET

def iniciar_practica():
    imprimir_encabezado("MODO PRÁCTICA")
    print("Demuestra lo que has aprendido respondiendo estas preguntas.")
    
    puntaje = 0
    total = 3

    # Nivel 1
    print(f"\n{AMARILLO}Nivel 1: El Módulo{RESET}")
    print("Si elegimos los primos p = 11 y q = 13...")
    respuesta = validacion_entrada_int("¿Cuál es el valor de n (p * q)? ")
    if respuesta == 143:
        print(f"{VERDE}¡Correcto! 11 * 13 = 143.{RESET}")
        puntaje += 1
    else:
        print(f"{ROJO}Incorrecto. 11 * 13 = 143.{RESET}")

    # Nivel 2
    print(f"\n{AMARILLO}Nivel 2: Factorización{RESET}")
    print("Si sabemos que n = 187...")
    respuesta = validacion_entrada_int("¿Cuál es el primo p más pequeño que lo compone? ")
    if respuesta == 11:
        print(f"{VERDE}¡Muy bien! 187 = 11 * 17.{RESET}")
        puntaje += 1
    else:
        print(f"{ROJO}No. 187 es 11 * 17.{RESET}")

    # Nivel 3
    print(f"\n{AMARILLO}Nivel 3: Conceptos{RESET}")
    print("¿Qué llave puedes compartir libremente por Internet?")
    print("1. Clave Privada")
    print("2. Clave Pública")
    respuesta = input("Tu respuesta (1/2): ")
    if respuesta == '2':
        print(f"{VERDE}¡Exacto! La clave pública es para que todos puedan cifrarte mensajes.{RESET}")
        puntaje += 1
    else:
        print(f"{ROJO}Cuidado: La clave privada NUNCA debe compartirse.{RESET}")

    imprimir_encabezado("RESULTADOS")
    print(f"Tu puntaje final es: {puntaje}/{total}")
    if puntaje == total:
        print(f"{VERDE}¡Eres un experto en Cripto-Primos! 🏆{RESET}")
    
    pausa()
