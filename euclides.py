def algoritmo_euclides(a: int, b: int) -> list:
    """Executa o Algoritmo de Euclides e registra seus passos.
        Retorna uma lista no formato (a, b, resto) para cada passo do algoritmo.
    """
    # Normaliza os sinais e prepara o registro das divisões.
    a, b = abs(a), abs(b)
    passos = []

    # Guarda cada divisão antes de avançar para o próximo resto.
    while b != 0:
        resto = a % b
        passos.append((a, b, resto))
        a, b = b, resto

    # A última divisão registrada termina com resto zero.
    return passos


# ---------------------------------------------------------
# Testes
# ---------------------------------------------------------

if __name__ == "__main__":

    print("\n=== TESTE DO ALGORITMO DE EUCLIDES ===")

    a = 48
    b = 18

    passos = algoritmo_euclides(a, b)

    print(f"\nCalculando o MDC de {a} e {b}:")

    for x, y, resto in passos:
        print(f"{x} mod {y} = {resto}")

    print(f"\nÚltimo divisor diferente de zero: "
          f"{passos[-2][2] if len(passos) > 1 else passos[0][1]}")
