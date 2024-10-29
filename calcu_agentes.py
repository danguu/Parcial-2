class SumaAgent:
    def operar(self, a, b):
        return a + b

class RestaAgent:
    def operar(self, a, b):
        return a - b

class MultiplicacionAgent:
    def operar(self, a, b):
        return a * b

class DivisionAgent:
    def operar(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: No se puede dividir por cero"

class PotenciaAgent:
    def operar(self, a, b):
        return a ** b

class Calculadora:
    def __init__(self):
        # Crear los "agentes" que harán las operaciones
        self.suma_agent = SumaAgent()
        self.resta_agent = RestaAgent()
        self.multiplicacion_agent = MultiplicacionAgent()
        self.division_agent = DivisionAgent()
        self.potencia_agent = PotenciaAgent()

    def calcular(self, expresion):
        try:
            # Evalúa la expresión matemática ingresada
            resultado = eval(expresion)
            return resultado
        except Exception as e:
            return "Error en la expresión"

# Función principal que interactúa con el usuario
def ejecutar_calculadora():
    calculadora = Calculadora()

    while True:
        expresion = input("Ingresa una operación (o 'salir' para terminar): ")
        if expresion.lower() == 'salir':
            break
        
        # La calculadora resuelve la expresión matemática
        resultado = calculadora.calcular(expresion)
        print(f"Resultado: {resultado}")

# Ejecutar la calculadora
if __name__ == "__main__":
    ejecutar_calculadora()
