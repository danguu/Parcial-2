# Parcial-2

## Punto 1
![image](https://github.com/user-attachments/assets/da33e4fa-658d-4d9d-8c51-c74a790b6c96)

-Codigo: Es el archivo: dan_perse.nlogo

-INFO:

## Funcionamiento del Perceptrón-
El perceptrón se compone de varios elementos importantes:

Entradas y Activaciones: El perceptrón tiene nodos de entrada que reciben información. Cada nodo tiene un valor de activación que puede ser 1 o -1. En mi modelo, configuré dos nodos de entrada.

Bias Node: También incluí un nodo de sesgo cuya activación siempre es 1. Este nodo ayuda a ajustar el modelo y se conecta al nodo de salida.

Nodo de Salida: Este nodo calcula una suma ponderada de las entradas y decide su activación. Si la suma supera un cierto umbral, la activación del nodo de salida se establece en 1; si no, se establece en -1.

Pesos: Cada conexión entre un nodo de entrada y el nodo de salida tiene un peso. Durante el entrenamiento, estos pesos se ajustan para minimizar el error en las predicciones.

Función de Activación: Implementé una función de activación en el nodo de salida que usa la función de signo para determinar la salida del perceptrón.

## Implementación en NetLogo-
Para implementar el perceptrón en NetLogo, seguí estos pasos:

Configuración Inicial: Creé los nodos de entrada y un nodo de salida, colocándolos en posiciones específicas en el espacio de simulación. Inicialicé aleatoriamente las activaciones de los nodos de entrada.

Entrenamiento: Realicé un ciclo de entrenamiento en el que activé aleatoriamente los nodos de entrada y el nodo de salida computó su activación. Utilicé un conjunto de ejemplos para ajustar los pesos de las conexiones, basándome en la diferencia entre la salida real y la esperada. Este proceso se repitió para varios ejemplos en cada época.

Resultados: Al finalizar el entrenamiento, evalué el rendimiento del perceptrón. Determiné si la salida del nodo de salida coincidía con la respuesta correcta para diferentes combinaciones de activación de los nodos de entrada. Se generaron mensajes que indicaban si las predicciones eran correctas o incorrectas, mostrando el valor de salida y el objetivo esperado.

## Resultados Obtenidos

Durante las simulaciones, el perceptrón mostró su capacidad para aprender y clasificar correctamente las entradas después de varias épocas de entrenamiento. Al final del proceso, pude ver que el perceptrón predecía correctamente la salida para varias combinaciones de entradas. Esto demostró que el modelo había encontrado un conjunto de pesos que minimizaban el error.

También noté que los parámetros, como la tasa de aprendizaje y el número de ejemplos por época, afectaban la rapidez con la que el perceptrón aprendía. Un mayor número de ejemplos por época generalmente conducía a un mejor rendimiento, aunque tomaba más tiempo en computarse.

# Punto 2

-Codigo: Es el archivo llamado calcu_agentes.py

-Función:

Agentes de Operación: Se definen cinco clases (SumaAgent, RestaAgent, MultiplicacionAgent, DivisionAgent, PotenciaAgent). Cada clase tiene un método operar que realiza una operación matemática específica.

Clase Calculadora: La clase Calculadora crea instancias de cada agente en su constructor (__init__). Esto permite que la calculadora use estos agentes para realizar operaciones.

Método Calcular: La calculadora tiene un método calcular que evalúa una expresión matemática que el usuario ingresa.

Utiliza eval() para resolver la expresión directamente, aunque esto puede ser riesgoso por razones de seguridad.
Interacción con el Usuario: En la función ejecutar_calculadora, el usuario puede ingresar expresiones repetidamente. La calculadora toma cada expresión, la evalúa y muestra el resultado.

-INFO: 
## Estructura del Sistema-
El sistema tiene tres partes principales:

Agentes: Cada agente es una clase que se encarga de una operación matemática. Por ejemplo, hay un agente para sumar, otro para restar, y así sucesivamente.
Calculadora: Esta clase es la que coordina todo. Crea los agentes y se encarga de recibir la expresión matemática que el usuario ingresa.
Interfaz de Usuario: Un bucle que permite al usuario escribir operaciones y ver los resultados.
## Agentes

Los agentes son clases que tienen un método llamado operar. Este método toma dos números y devuelve el resultado de la operación. Por ejemplo:

SumaAgent: Suma dos números.

RestaAgent: Resta dos números.

MultiplicacionAgent: Multiplica dos números.

DivisionAgent: Divide dos números (previniendo la división por cero).

PotenciaAgent: Calcula un número elevado a otro.

## Clase Calculadora

La clase Calculadora crea los agentes en su constructor. Luego, tiene un método calcular que utiliza la función eval para evaluar la expresión que el usuario ingresa. Si hay un error, muestra un mensaje de error.

## Interacción

La función ejecutar_calculadora permite al usuario ingresar operaciones. La calculadora procesa la operación y devuelve el resultado

Comunicación entre Agentes: Aunque los agentes no son llamados directamente, la calculadora actúa como un intermediario que organiza y ejecuta las operaciones.

# Punto 3

-Codigo: Es el archivo calcu_kot.kt

-INFO:

## Encapsulamiento
El encapsulamiento es cuando escondemos los detalles internos de una clase y solo mostramos lo que es necesario. En mi calculadora:

Clases y Métodos: La clase Calculadora tiene las operaciones básicas como suma, resta, multiplicación y división. Luego, CalculadoraCientifica hereda de esta clase y añade funciones avanzadas como seno y logaritmos. Esto ayuda a que los usuarios solo vean lo que necesitan.

Propiedades Privadas: La variable memoria en CalculadoraCientifica es privada. Solo se puede acceder a ella mediante métodos específicos (como memoriaSumar y memoriaRestar). Esto evita que alguien cambie la memoria sin querer.

Manejo de Excepciones: En los métodos, añadí excepciones para manejar errores, como la división por cero. Así, si el usuario intenta dividir entre cero, recibe un mensaje claro explicando el problema.

## Herencia

La herencia es cuando una clase nueva se basa en una clase existente, lo que nos permite reutilizar código.

Clase Base y Derivada: La clase Calculadora es la base y CalculadoraCientifica es la clase derivada que añade funciones científicas. Esto significa que no tengo que reescribir el código de las operaciones básicas; simplemente las uso en la clase derivada.

## Polimorfismo

El polimorfismo permite que un método funcione de diferentes maneras dependiendo del contexto.

Sobrecarga de Métodos: Aunque no lo implementé en este código, podría hacer que el método suma acepte tanto números enteros como decimales. Así, el usuario puede usar el mismo método sin preocuparse por el tipo de dato.

Flexibilidad en el Uso de Funciones: Los métodos en CalculadoraCientifica permiten a los usuarios hacer cálculos avanzados como seno y logaritmo sin tener que saber cómo funcionan por dentro. Esto hace que la calculadora sea fácil de usar.
