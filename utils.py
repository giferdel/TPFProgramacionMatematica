from colores import VERDE, ROJO, AMARILLO, RESET

def imprimir_encabezado(titulo):
    print("\n" + "*" * 41)
    print(f"{AMARILLO}{titulo.center(41)}{RESET}")
    print("*" * 41)

def pausa(mensaje="\n[Presiona Enter para continuar...]"):
    input(mensaje)

def limpiar_pantalla():
    # Podríamos usar os.system('cls' if os.name == 'nt' else 'clear')
    # Pero para una CLI simple, a veces basta con imprimir saltos de línea
    # o simplemente no hacerlo para mantener el historial. 
    # Por ahora, dejémoslo como un placeholder si se requiere.
    pass

def validacion_entrada_int(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"{ROJO}Error: El valor debe ser al menos {minimo}.{RESET}")
                continue
            if maximo is not None and valor > maximo:
                print(f"{ROJO}Error: El valor debe ser como máximo {maximo}.{RESET}")
                continue
            return valor
        except ValueError:
            print(f"{ROJO}Error: Por favor, introduce un número entero válido.{RESET}")

def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def inverso_modular(e, phi):
    # Usando pow(e, -1, phi) si está disponible en Python 3.8+
    try:
        return pow(e, -1, phi)
    except ValueError:
        return None
