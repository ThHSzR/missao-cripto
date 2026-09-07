def euler_phi(n: int) -> dict:
    """Criadora: Marini Luzia"""
    """Calcula a função Totiente de Euler phi(n) usando fatoração prima.

    Conta quantos inteiros positivos até n são coprimos com n.

    Args:
        n: Inteiro positivo maior que zero.

    Returns:
        Um dicionário contendo o valor de n, a quantidade de coprimos (phi)
        e a lista dos fatores primos únicos identificados.
    """
    if n <= 0:
        raise ValueError("O valor de n deve ser maior que zero.")

    resultado = n
    fatores_primos = []
    temp = n
    p = 2

    while p * p <= temp:
        if temp % p == 0:
            fatores_primos.append(p)
            while temp % p == 0:
                temp //= p
            resultado -= resultado // p
        p += 1

    if temp > 1:
        fatores_primos.append(temp)
        resultado -= resultado // temp

    return {
        "n": n,
        "phi": resultado,
        "fatores_primos": fatores_primos
    }


if __name__ == "__main__":

    print("=== TESTES DA FUNÇÃO PHI DE EULER ===")

    # Teste 1: Número composto
    n1 = 36
    res1 = euler_phi(n1)
    print(f"\nValor: n = {n1}")
    print(f"Fatores primos distintos: {res1['fatores_primos']}")
    print(f"phi({n1}) = {res1['phi']}")

    # Teste 2: Número primo (phi(p) = p - 1)
    n2 = 13
    res2 = euler_phi(n2)
    print(f"\nValor (Primo): n = {n2}")
    print(f"Fatores primos distintos: {res2['fatores_primos']}")
    print(f"phi({n2}) = {res2['phi']}")

    # Teste 3: Produto de dois primos (Caso RSA: n = p * q)
    p, q = 5, 7
    n3 = p * q
    res3 = euler_phi(n3)
    print(f"\nCaso RSA (n = {p} * {q} = {n3}):")
    print(f"phi({n3}) calculado: {res3['phi']}")
    print(f"Fórmula (p-1)*(q-1): ({p}-1) * ({q}-1) = {(p - 1) * (q - 1)}")