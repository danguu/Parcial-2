from mesa import Agent, Model
from mesa.time import BaseScheduler

class OperacionAgent(Agent):
    def __init__(self, unique_id, model, operation):
        super().__init__(unique_id, model)
        self.operation = operation

    def operar(self, a, b):
        if self.operation == 'suma':
            return a + b
        elif self.operation == 'resta':
            return a - b
        elif self.operation == 'multiplicacion':
            return a * b
        elif self.operation == 'division':
            if b != 0:
                return a / b
            else:
                return "Error: No se puede dividir por cero"
        elif self.operation == 'potencia':
            return a ** b

class CalculadoraModel(Model):
    def __init__(self):
        self.schedule = BaseScheduler(self)
        # Crear agentes para cada operación
        self.suma_agent = OperacionAgent(1, self, 'suma')
        self.resta_agent = OperacionAgent(2, self, 'resta')
        self.multiplicacion_agent = OperacionAgent(3, self, 'multiplicacion')
        self.division_agent = OperacionAgent(4, self, 'division')
        self.potencia_agent = OperacionAgent(5, self, 'potencia')
        # Añadir agentes al planificador
        self.schedule.add(self.suma_agent)
        self.schedule.add(self.resta_agent)
        self.schedule.add(self.multiplicacion_agent)
        self.schedule.add(self.division_agent)
        self.schedule.add(self.potencia_agent)

    def calcular(self, operacion, a, b):
        # Determinar el agente según la operación
        if operacion == '+':
            return self.suma_agent.operar(a, b)
        elif operacion == '-':
            return self.resta_agent.operar(a, b)
        elif operacion == '*':
            return self.multiplicacion_agent.operar(a, b)
        elif operacion == '/':
            return self.division_agent.operar(a, b)
        elif operacion == '**':
            return self.potencia_agent.operar(a, b)
        else:
            return "Operación no válida"

# Función principal para interactuar con el usuario
def ejecutar_calculadora():
    calculadora = CalculadoraModel()

    while True:
        expresion = input("Ingresa una operación (formato: a operador b, o 'salir' para terminar): ")
        if expresion.lower() == 'salir':
            break
        
        try:
            a, operacion, b = expresion.split()
            a, b = float(a), float(b)
            resultado = calculadora.calcular(operacion, a, b)
            print(f"Resultado: {resultado}")
        except ValueError:
            print("Error: formato de entrada no válido")
        except Exception as e:
            print(f"Error en la expresión: {e}")

# Ejecutar la calculadora
if __name__ == "__main__":
    ejecutar_calculadora()
