def algoritmo_euclides(a: int, b: int) -> int:
    """Calcula o MDC de dois números usando o Algoritmo de Euclides."""

    a, b = abs(a), abs(b)

    while b != 0:
        a, b = b, a % b
    return a
          f"{passos[-2][2] if len(passos) > 1 else passos[0][1]}")
