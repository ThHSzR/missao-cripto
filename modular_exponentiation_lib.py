def exponenciacao_modular(base: int, expoente: int, m: int) -> dict:
    """Criadora: Marini Luzia"""
    """Calcula a exponenciação modular (base^expoente) mod m
    utilizando o algoritmo Square-and-Multiply.

    Args:
        base: Número inteiro da base.
        expoente: Inteiro não-negativo representando o expoente.
        m: Módulo, que deve ser maior que zero.

    Returns:
        Um dicionário contendo os parâmetros de entrada, a representação
        binária do expoente e o resultado final da operação modular.
    """
    # Valida as condições básicas da exponenciação modular.
    if m <= 0:
        raise ValueError("O módulo deve ser maior que zero.")
    if expoente < 0:
        raise ValueError("O expoente deve ser um inteiro não-negativo.")

    # Todo inteiro é congruente a zero módulo 1.
    if m == 1:
        return {
            "base": base,
            "expoente": expoente,
            "modulo": m,
            "expoente_binario": bin(expoente)[2:],
            "resultado": 0
        }

    # Reduz a base antes de iniciar o método square-and-multiply.
    resultado = 1
    base_atual = base % m
    exp = expoente

    while exp > 0:
        # Se o bit menos significativo for 1, multiplica
        if exp & 1:
            resultado = (resultado * base_atual) % m

        # Eleva a base ao quadrado para o próximo bit
        base_atual = (base_atual * base_atual) % m
        exp >>= 1

    # Preserva os dados da operação junto com o resultado.
    return {
        "base": base,
        "expoente": expoente,
        "modulo": m,
        "expoente_binario": bin(expoente)[2:],
        "resultado": resultado
    }


if __name__ == "__main__":

    print("=== TESTES DE EXPONENCIAÇÃO MODULAR ===")

    # Teste 1: Caso clássico
    base = 7
    expoente = 11
    m = 13

    res = exponenciacao_modular(base, expoente, m)

    print(f"\nValores: base = {base}, expoente = {expoente}, m = {m}")
    print(f"Expoente em binário:           {res['expoente_binario']}")
    print(f"({base}^{expoente}) mod {m} =               {res['resultado']}")

    # Teste 2: Números grandes (demonstrando eficiência)
    b_grande = 12345
    e_grande = 6789
    m_grande = 10007

    res_grande = exponenciacao_modular(b_grande, e_grande, m_grande)

    print(f"\nValores grandes: base = {b_grande}, expoente = {e_grande}, m = {m_grande}")
    print(f"Resultado computado:           {res_grande['resultado']}")
    print(f"Verificação Python nativo:     {pow(b_grande, e_grande, m_grande)}")
