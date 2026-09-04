"""Módulo para cálculo de divisores comuns.

Criador: Mateus Afonso Miranda de Oliveira
"""

__all__ = ["calcular_mdc"]


def calcular_mdc(a: int, b: int) -> int:
    """Calcula o Máximo Divisor Comum (MDC) entre dois inteiro utilizando Euclides"""
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


# Teste do módulo
if __name__ == "__main__":
    num1 = 3
    num2 = 1
    resultado = calcular_mdc(num1, num2)
    print(f"O MDC de {num1} e {num2} é: {resultado}")