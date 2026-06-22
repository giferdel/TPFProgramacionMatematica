# Cripto-Primos: Aprende Criptografía RSA

**Cripto-Primos** es una herramienta educativa interactiva diseñada para enseñar los fundamentos de la teoría de números y la criptografía RSA. A través de simulaciones, juegos y herramientas de análisis, podrás entender cómo los números primos se convierten en el fundamento que protege la información en el mundo digital.

---

## Características Principales

### 1. Analizador de Números Primos
Verifica si un número es primo utilizando diferentes algoritmos:
* **División por Ensayo:** El método tradicional y determinista.
* **Test de Fermat:** Un método probabilístico rápido basado en el pequeño teorema de Fermat.
* **Test de Miller-Rabin:** El estándar de la industria, altamente confiable y eficiente para números grandes.

### 2. Sistema Criptográfico RSA
* **Generación de Claves:** Elige tus propios primos $p$ y $q$, y observa cómo se calculan $n$, $\phi(n)$, $e$ y $d$.
* **Cifrado y Descifrado:**
  * **Manual:** Introduce mensajes de texto y observa la conversión a ASCII y su transformación matemática.
  * **Archivos:** Cifra el contenido de `texto.txt` y recupéralo desde `mensaje_cifrado.txt`.
* **Exportación:** Guarda tu sesión de claves para usarla más tarde.

### 3. Modos Educativos
* **Simulación Paso a Paso:** Un recorrido guiado por todo el proceso de RSA con ejemplos claros.
* **Modo Ataque (Factorización):** Intenta "romper" RSA mediante fuerza bruta y descubre por qué la seguridad depende del tamaño de los números.
* **Modo Práctica:** Desafía tus conocimientos con preguntas interactivas.

---

## Instalación y Uso

### Requisitos
* Python 3.10 o superior.

### Configuración
1. Clona este repositorio o descarga los archivos.
2. *(Opcional)* Crea y activa un entorno virtual:

```bash
# Crear el entorno
python -m venv env

# Activar en Linux/macOS
source env/bin/activate  

# Activar en Windows
env\Scripts\activate

#Ejecución del Proyecto

python main.py