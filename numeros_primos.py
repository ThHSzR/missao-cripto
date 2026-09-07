"""Teste e enumeração de números primos.

Responsável pelo tópico: Mateus Afonso (@IsMateusReal).
"""

from math import isqrt

__all__ = ["eh_primo", "listar_primos"]


def _validar_inteiro(nome: str, valor: object) -> None:
    """Garante que ``valor`` seja um inteiro, sem aceitar booleanos."""
    if isinstance(valor, bool) or not isinstance(valor, int):
        raise TypeError(f"{nome} deve ser um número inteiro.")


def eh_primo(n: int) -> bool:
    """Retorna se ``n`` é primo usando divisão por tentativa otimizada.

    Depois de tratar 2 e 3, basta testar divisores da forma ``6k - 1`` e
    ``6k + 1`` até a raiz quadrada inteira de ``n``.

    Args:
        n: Número inteiro que será verificado.

    Returns:
        ``True`` se ``n`` for primo; caso contrário, ``False``.

    Raises:
        TypeError: Se ``n`` não for um inteiro.
    """
    _validar_inteiro("n", n)

    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    limite = isqrt(n)
    candidato = 5
    while candidato <= limite:
        if n % candidato == 0 or n % (candidato + 2) == 0:
            return False
        candidato += 6

    return True


def listar_primos(limite: int) -> list[int]:
    """Lista os números primos menores ou iguais a ``limite``.

    A implementação usa o Crivo de Eratóstenes e começa a eliminar múltiplos
    de cada primo a partir de seu quadrado.

    Args:
        limite: Maior valor que poderá aparecer na lista.

    Returns:
        Lista crescente com todos os primos no intervalo ``[2, limite]``.

    Raises:
        TypeError: Se ``limite`` não for um inteiro.
    """
    _validar_inteiro("limite", limite)

    if limite < 2:
        return []

    crivo = bytearray(b"\x01") * (limite + 1)
    crivo[0:2] = b"\x00\x00"

    for primo in range(2, isqrt(limite) + 1):
        if crivo[primo]:
            inicio = primo * primo
            quantidade = ((limite - inicio) // primo) + 1
            crivo[inicio : limite + 1 : primo] = b"\x00" * quantidade

    return [numero for numero, marcado in enumerate(crivo) if marcado]


if __name__ == "__main__":
    exemplos = [1, 2, 17, 25, 97]

    print("=== NÚMEROS PRIMOS ===")
    for numero in exemplos:
        print(f"{numero} é primo? {eh_primo(numero)}")
    print(f"\nPrimos até 50: {listar_primos(50)}")
