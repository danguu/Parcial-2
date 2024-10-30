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

class Mesa:
    def _init_(self):
        # Crear los "agentes" que harán las operaciones
        self.agentes = {
            '+': SumaAgent(),
            '-': RestaAgent(),
            '*': MultiplicacionAgent(),
            '/': DivisionAgent(),
            '**': PotenciaAgent()
        }

    def delegar_operacion(self, operador, a, b):
        if operador in self.agentes:
            return self.agentes[operador].operar(a, b)
        else:
            return "Operador no soportado"

class Calculadora:
    def _init_(self):
        # Crear la mesa para delegar las operaciones
        self.mesa = Mesa()

    def calcular(self, expresion):
        try:
            # Dividir la expresión en operandos y operador
            elementos = expresion.split()
            if len(elementos) == 3:
                a = float(elementos[0])
                operador = elementos[1]
                b = float(elementos[2])
                
                # Delegar la operación en la mesa
                resultado = self.mesa.delegar_operacion(operador, a, b)
                return resultado
            else:
                return "Error: Expresión inválida. Usa el formato 'a operador b'"
        except ValueError:
            return "Error: Entrada inválida. Asegúrate de usar números."
        except Exception as e:
            return f"Error en la expresión: {e}"

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
if _name_ == "_main_":
    ejecutar_calculadora()
