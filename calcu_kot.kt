import kotlin.math.*

open class Calculadora {
    // Métodos para operaciones básicas
    open fun suma(a: Double, b: Double): Double {
        return a + b
    }

    open fun resta(a: Double, b: Double): Double {
        return a - b
    }

    open fun multiplicacion(a: Double, b: Double): Double {
        return a * b
    }

    open fun division(a: Double, b: Double): Double {
        if (b == 0.0) throw IllegalArgumentException("No se puede dividir por cero.")
        return a / b
    }
}

class CalculadoraCientifica : Calculadora() {
    // Propiedad para la memoria
    private var memoria: Double = 0.0

    // Métodos para operaciones científicas
    fun seno(x: Double): Double {
        return sin(Math.toRadians(x))
    }

    fun coseno(x: Double): Double {
        return cos(Math.toRadians(x))
    }

    fun tangente(x: Double): Double {
        return tan(Math.toRadians(x))
    }

    fun potencia(base: Double, exponente: Double): Double {
        return base.pow(exponente)
    }

    fun raizCuadrada(x: Double): Double {
        if (x < 0) throw IllegalArgumentException("No se puede calcular la raíz cuadrada de un número negativo.")
        return sqrt(x)
    }

    fun logaritmoBase10(x: Double): Double {
        if (x <= 0) throw IllegalArgumentException("El logaritmo no está definido para números menores o iguales a cero.")
        return log10(x)
    }

    fun logaritmoNatural(x: Double): Double {
        if (x <= 0) throw IllegalArgumentException("El logaritmo no está definido para números menores o iguales a cero.")
        return ln(x)
    }

    fun exponencial(x: Double): Double {
        return exp(x)
    }

    fun gradosARadianes(grados: Double): Double {
        return Math.toRadians(grados)
    }

    fun radianesAGrados(radianes: Double): Double {
        return Math.toDegrees(radianes)
    }

    // Métodos de memoria
    fun memoriaSumar(valor: Double) {
        memoria += valor
    }

    fun memoriaRestar(valor: Double) {
        memoria -= valor
    }

    fun memoriaRecuperar(): Double {
        return memoria
    }

    fun memoriaLimpiar() {
        memoria = 0.0
    }
}

// Funciones de prueba
fun main() {
    val calculadora = CalculadoraCientifica()

    // Ejemplo de uso
    println("Suma: ${calculadora.suma(5.0, 3.0)}")
    println("Resta: ${calculadora.resta(5.0, 3.0)}")
    println("Multiplicación: ${calculadora.multiplicacion(5.0, 3.0)}")
    println("División: ${calculadora.division(5.0, 2.0)}") // Lanza excepción
    println("Seno: ${calculadora.seno(45.0)}")
    println("Coseno: ${calculadora.coseno(45.0)}")
    println("Tangente: ${calculadora.tangente(45.0)}")
    println("Potencia: ${calculadora.potencia(2.0, 3.0)}")
    println("Raíz cuadrada: ${calculadora.raizCuadrada(16.0)}")
    println("Logaritmo base 10: ${calculadora.logaritmoBase10(100.0)}")
    println("Exponencial: ${calculadora.exponencial(2.0)}")

    // Uso de memoria
    calculadora.memoriaSumar(10.0)
    println("Memoria: ${calculadora.memoriaRecuperar()}")
    calculadora.memoriaRestar(5.0)
    println("Memoria: ${calculadora.memoriaRecuperar()}")
    calculadora.memoriaLimpiar()
    println("Memoria: ${calculadora.memoriaRecuperar()}")
}
