import sys,os
import primos
import rsa
import simulador
# import practica
import ataque
from utils import imprimir_encabezado, pausa, ROJO, VERDE, AMARILLO, RESET

def mostrar_menu():
    os.system("cls")
    imprimir_encabezado("CRIPTO-PRIMOS\nAPRENDE CRIPTOGRAFÍA")
    print("1. Introducción a Número Primos")
    print("2. Verificador de Números Primos")
    print("3. Buscar primos en rango")
    print("4. Introducción a RSA")
    print("5. Simulación paso a paso")
    print("6. Generar claves RSA")
    print("7. Cifrar mensaje (Manual)")
    print("8. Descifrar mensaje (Manual)")
    print("9. Cifrar ARCHIVO (texto.txt)")
    print("10. Descifrar ARCHIVO (mensaje_cifrado.txt)")
    print("11. Modo ataque")
    print("12. Ayuda")
    print("0. Salir")

def mostrar_ayuda():
    imprimir_encabezado("AYUDA")
    print("Esta aplicación te permite aprender sobre criptografía RSA.")
    print("Navega por las opciones para descubrir cómo los números primos")
    print("protegen la información en el mundo digital.")
    pausa()

ultimo_numero = None

def verificador_opcion():
    global ultimo_numero
    while True:
        prompt = "\nIntroduce un número para analizar"
        if ultimo_numero is not None:
            prompt += f" [{ultimo_numero}]"
        prompt += " (o 'V' para volver al inicio): "
        
        entrada = input(prompt).strip().upper()
        
        if entrada == 'V':
            return
        
        if entrada == '' and ultimo_numero is not None:
            num = ultimo_numero
        else:
            try:
                num = int(entrada)
                ultimo_numero = num
            except ValueError:
                print(f"{ROJO}Error: Por favor, introduce un número entero válido.{RESET}")
                continue
        
        imprimir_encabezado(f"ANALIZANDO EL NÚMERO: {num}")
        print("Métodos de verificación disponibles:")
        metodos = primos.obtener_metodos()
        for k, v in metodos.items():
            print(f" {k}. {v['nombre' ]}")
        print(" T. Todos los métodos")
        print(" V. Volver")
        
        sel = input("\nSelecciona el método (ej: 1, 3 o T): ").upper()
        
        if sel == 'V':
            continue
        
        seleccionados = []
        if sel == 'T':
            seleccionados = list(metodos.keys())
        else:
            seleccionados = [s.strip() for s in sel.split(',')]

        encontrado = False
        for s in seleccionados:
            if s in metodos:
                encontrado = True
                m = metodos[s]
                print(f"\n--- {AMARILLO}{m['nombre']}{RESET} --- \n{m['descripcion']} \nFortaleza del método: {m['fortalezas']} \nDebilidad del método: {m['debilidades']}\n")
                
                if m['funcion'](num):
                    print(f"{VERDE}¡RESULTADO: El número {num} es PRIMO! 🌟{RESET}")
                else:
                    # mensaje_no_primo = primos.explicar_no_primo(num)
                    mensaje_no_primo= m['no_primo'](num)
                    print(f"{ROJO}RESULTADO: {mensaje_no_primo}{RESET}")
            elif s:
                print(f"{ROJO}Error: El método '{s}' no es válido.{RESET}")
        
        if encontrado:
            pausa()

def buscar_primos_rango(): 
    imprimir_encabezado("BUSCAR PRIMOS EN RANGO")
    try:
        inicio = int(input("Introduce el inicio del rango: "))
        fin = int(input("Introduce el fin del rango: "))
    except ValueError:
        print(f"{ROJO}Error: Por favor, introduce números enteros válidos.{RESET}")
        pausa()
        os.system('cls')
        buscar_primos_rango()
        return

    if inicio > fin:
        print(f"{ROJO}Error: El inicio no puede ser mayor que el fin.{RESET}")
        pausa()
        os.system('cls')
        buscar_primos_rango()
        return

    print("\nMétodos de verificación disponibles:")
    metodos = primos.obtener_metodos()
    for k, v in metodos.items():
        print(f" {k}. {v['nombre']}")
    
    sel = input("\nSelecciona el método (1, 2 o 3): ").strip()
    
    if sel not in metodos:
        print(f"{ROJO}Error: Método no válido.{RESET}")
        pausa()
        return

    m = metodos[sel]
    print(f"\nBuscando primos entre {inicio} y {fin} usando {m['nombre']}...")
    
    primos_encontrados = [] #Crea lista de números primos en el rango dado
    for num in range(inicio, fin + 1):
        if m['funcion'](num):
            primos_encontrados.append(num)
    
    print(f"\n{VERDE}Primos encontrados ({len(primos_encontrados)}):{RESET}")
    print(primos_encontrados)
    
    archivo = "primos_rango.txt"
    try:
        with open(archivo, "w") as f:
            f.write(f"Primos encontrados en el rango [{inicio}, {fin}] usando {m['nombre']}:\n")
            f.write(str(primos_encontrados))
        print(f"\n{VERDE}La lista ha sido guardada en '{archivo}'.{RESET}")
    except Exception as e:
        print(f"{ROJO}Error al guardar el archivo: {e}{RESET}")
    
    pausa()
    # return {primos_encontrados}

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == '1':
            primos.def_primos()
        elif opcion == '2':
            verificador_opcion()
        elif opcion == '3':
            buscar_primos_rango()
        elif opcion == '4':
            rsa.mostrar_introduccion()
        elif opcion == '5':
            simulador.ejecutar_simulacion()
        elif opcion == '6':
            rsa.generar_claves()
        elif opcion == '7':
            rsa.cifrar_mensaje()
        elif opcion == '8':
            rsa.descifrar_mensaje()
        elif opcion == '9':
            rsa.cifrar_archivo()
        elif opcion == '10':
            rsa.descifrar_archivo()
        elif opcion == '11':
            ataque.iniciar_ataque()
        elif opcion == '12':
            mostrar_ayuda()
        elif opcion == '0':
            print("\n¡Gracias por aprender con Cripto-Primos! Hasta pronto.")
            sys.exit()
        else:
            print(f"\n{ROJO}Opción no válida. Por favor, intenta de nuevo.{RESET}")

if __name__ == "__main__":
    main()
