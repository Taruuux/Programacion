# https://github.com/Taruuux/Programacion
# Clase estática con métodos útiles: es_primo, factorial, es_palindromo y suma_digitos.

class Utilidades:
    """Clase estática con operaciones matemáticas y de texto útiles."""

    @staticmethod
    def es_primo(n):
        """Devuelve True si n es primo, False en caso contrario."""
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def factorial(n):
        """Devuelve el factorial de n."""
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos.")
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

    @staticmethod
    def es_palindromo(cadena):
        """Devuelve True si la cadena es un palíndromo, False si no."""
        cadena = str(cadena).replace(" ", "").lower()
        return cadena == cadena[::-1]

    @staticmethod
    def suma_digitos(n):
        """Devuelve la suma de los dígitos del número n."""
        return sum(int(digito) for digito in str(abs(n)))


# =====================
# PRUEBAS DE FUNCIONAMIENTO
# =====================
if __name__ == "__main__":
    print("=== PRUEBAS DE LA CLASE UTILIDADES ===\n")

    print("¿7 es primo?", Utilidades.es_primo(7))            # True
    print("¿10 es primo?", Utilidades.es_primo(10))          # False

    print("\nFactorial de 5:", Utilidades.factorial(5))      # 120
    print("Factorial de 0:", Utilidades.factorial(0))        # 1

    print("\n¿'Anita lava la tina' es palíndromo?",
          Utilidades.es_palindromo("Anita lava la tina"))    # True
    print("¿'Python' es palíndromo?",
          Utilidades.es_palindromo("Python"))                # False

    print("\nSuma de dígitos de 12345:",
          Utilidades.suma_digitos(12345))                    # 15
    print("Suma de dígitos de -987:",
          Utilidades.suma_digitos(-987))                     # 24
