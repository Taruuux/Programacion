"""
calculadora_ocp.py

Calculadora extensible siguiendo el Principio de Abierto/Cerrado (OCP).
- El núcleo (Calculator + OperationRegistry + interfaz Operation) NO se modifica para añadir nuevas operaciones.
- Las operaciones se registran externamente (plugins/clases nuevas).
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Callable


# === 1) Contrato de operación (estable y cerrado a cambios) ===

class Operation(ABC):
    """Contrato estable para cualquier operación binaria a ∘ b."""

    @property
    @abstractmethod
    def symbol(self) -> str:
        """Símbolo textual de la operación, p.ej. '+', '-', '*', '/'."""
        raise NotImplementedError

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        """Aplica la operación sobre a y b y devuelve el resultado."""
        raise NotImplementedError


# === 2) Implementaciones concretas (clases abiertas a extensión) ===

@dataclass(frozen=True)
class Add(Operation):
    symbol: str = "+"
    def execute(self, a: float, b: float) -> float:
        return a + b

@dataclass(frozen=True)
class Subtract(Operation):
    symbol: str = "-"
    def execute(self, a: float, b: float) -> float:
        return a - b

@dataclass(frozen=True)
class Multiply(Operation):
    symbol: str = "*"
    def execute(self, a: float, b: float) -> float:
        return a * b

@dataclass(frozen=True)
class Divide(Operation):
    symbol: str = "/"
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("División por cero no permitida")
        return a / b


# === 3) Infraestructura de registro (permite extender sin tocar la calculadora) ===

class OperationRegistry:
    """Registro de operaciones disponibles."""

    def __init__(self) -> None:
        self._ops: Dict[str, Operation] = {}

    def register(self, op: Operation) -> None:
        if op.symbol in self._ops:
            raise ValueError(f"Ya existe una operación registrada con símbolo '{op.symbol}'")
        self._ops[op.symbol] = op

    def get(self, symbol: str) -> Operation:
        try:
            return self._ops[symbol]
        except KeyError:
            raise KeyError(f"Operación '{symbol}' no encontrada. Registradas: {', '.join(self._ops)}")

    def list_symbols(self) -> str:
        return ", ".join(sorted(self._ops.keys()))


# === 4) Núcleo de la calculadora (cerrado a modificaciones) ===

class Calculator:
    """Calculadora que delega en el registro. No necesita cambios para nuevas operaciones."""

    def __init__(self, registry: OperationRegistry) -> None:
        self.registry = registry

    def calculate(self, symbol: str, a: float, b: float) -> float:
        op = self.registry.get(symbol)
        return op.execute(a, b)


# === 5) Registro por defecto con las 4 operaciones requeridas ===

def default_registry() -> OperationRegistry:
    reg = OperationRegistry()
    reg.register(Add())
    reg.register(Subtract())
    reg.register(Multiply())
    reg.register(Divide())
    return reg


# === 6) Quinta operación (potencia) añadida SIN tocar la calculadora ===

@dataclass(frozen=True)
class Power(Operation):
    symbol: str = "^"  # podrías elegir "**" si prefieres
    def execute(self, a: float, b: float) -> float:
        return a ** b


# === 7) Pequeña batería de pruebas / demo ===

def _assert_equal(actual, expected) -> None:
    # Aserciones sencillas para verificación rápida
    if isinstance(actual, float) or isinstance(expected, float):
        assert abs(actual - expected) < 1e-9, f"Esperado {expected}, obtuve {actual}"
    else:
        assert actual == expected, f"Esperado {expected}, obtuve {actual}"

def run_demo() -> None:
    print("== DEMO CALCULADORA OCP ==")

    # 1) Crear calculadora con 4 operaciones
    reg = default_registry()
    calc = Calculator(registry=reg)

    # 2) Comprobaciones de funcionamiento básicas
    print("Operaciones disponibles inicialmente:", reg.list_symbols())
    _assert_equal(calc.calculate("+", 2, 3), 5)
    _assert_equal(calc.calculate("-", 10, 4), 6)
    _assert_equal(calc.calculate("*", 7, 6), 42)
    _assert_equal(calc.calculate("/", 8, 2), 4)
    print("✔ Pruebas básicas superadas.")

    # 3) Agregar la quinta operación (potencia) SIN modificar la calculadora
    reg.register(Power())  # extensión por registro
    print("Operaciones tras añadir potencia:", reg.list_symbols())
    _assert_equal(calc.calculate("^", 2, 10), 1024)
    print("✔ Potencia funcionando.")

    # 4) Comprobación de OCP (evidencia práctica)
    print("\nComprobación OCP:")
    print("- No hemos cambiado NADA en Calculator ni en OperationRegistry para añadir Power.")
    print("- Únicamente hemos definido una nueva clase Power y la hemos 'register()' en tiempo de ejecución.")
    print("- Por lo tanto, el sistema está ABIERTO a extensión y CERRADO a modificación. ✔")

    # 5) Prueba de error controlado (división por cero)
    try:
        calc.calculate("/", 1, 0)
    except ValueError as e:
        print("✔ Error controlado:", e)

    print("\nTodas las comprobaciones han finalizado correctamente.")

if __name__ == "__main__":
    run_demo()
