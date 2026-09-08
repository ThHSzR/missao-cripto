"""Teorema Chinês do Resto para módulos coprimos dois a dois.

Criador: Thiago H. S. Rodrigues
"""

from collections.abc import Sequence
from itertools import combinations
from math import prod

from inverso_multiplicativo import inverso_multiplicativo
from mdc import coprimos

__all__ = ["teorema_chines_resto"]


def _validar_sequencia(nome: str, valores: object) -> None:
    """Valida se ``valores`` é uma sequência formada apenas por inteiros."""
    # Impede o uso de textos ou valores que não possam ser percorridos.
    if isinstance(valores, (str, bytes)) or not isinstance(valores, Sequence):
        raise TypeError(f"{nome} devem ser uma sequência de inteiros.")

    # Booleanos são rejeitados porque, em Python, também são considerados inteiros.
    if any(isinstance(valor, bool) or not isinstance(valor, int) for valor in valores):
        raise TypeError(f"{nome} devem conter apenas números inteiros.")


def teorema_chines_resto(
    residuos: Sequence[int],
    modulos: Sequence[int],
) -> tuple[int, int]:
    """Resolve um sistema de congruências com módulos coprimos dois a dois.

    Para congruências da forma ``x ≡ residuos[i] (mod modulos[i])``, retorna
    ``(solucao, modulo_produto)``. A solução é o único representante no
    intervalo ``0 <= solucao < modulo_produto``; todas as demais soluções são
    congruentes a ela módulo ``modulo_produto``.

    Args:
        residuos: Resíduos inteiros das congruências.
        modulos: Módulos inteiros, maiores que 1 e coprimos dois a dois.

    Returns:
        Uma tupla contendo a solução canônica e o produto dos módulos.

    Raises:
        TypeError: Se as entradas não forem sequências de inteiros.
        ValueError: Se as sequências forem vazias, tiverem tamanhos diferentes,
            contiverem módulos menores ou iguais a 1, ou se algum par de
            módulos não for coprimo.
    """
    # Confere os tipos antes de realizar qualquer operação matemática.
    _validar_sequencia("Resíduos", residuos)
    _validar_sequencia("Módulos", modulos)

    # Cada resíduo precisa ter um módulo correspondente e válido.
    if not residuos:
        raise ValueError("O sistema deve conter ao menos uma congruência.")

    if len(residuos) != len(modulos):
        raise ValueError("As quantidades de resíduos e módulos devem ser iguais.")

    if any(modulo <= 1 for modulo in modulos):
        raise ValueError("Todos os módulos devem ser maiores que 1.")

    # O TCR desta implementação exige módulos coprimos dois a dois.
    for (indice_a, modulo_a), (indice_b, modulo_b) in combinations(
        enumerate(modulos), 2
    ):
        if not coprimos(modulo_a, modulo_b):
            raise ValueError(
                "Os módulos devem ser coprimos dois a dois; "
                f"posições {indice_a} e {indice_b}: "
                f"mdc({modulo_a}, {modulo_b}) != 1."
            )

    # M é o produto dos módulos e define a classe da solução final.
    modulo_produto = prod(modulos)
    soma = 0

    # Constrói e acumula a contribuição de cada congruência.
    for residuo, modulo in zip(residuos, modulos):
        modulo_parcial = modulo_produto // modulo
        inverso = inverso_multiplicativo(modulo_parcial, modulo)
        soma += (residuo % modulo) * modulo_parcial * inverso

    # Normaliza a resposta para o intervalo de zero até M - 1.
    return soma % modulo_produto, modulo_produto


if __name__ == "__main__":
    residuos_exemplo = [2, 3, 2]
    modulos_exemplo = [3, 5, 7]
    solucao, modulo = teorema_chines_resto(residuos_exemplo, modulos_exemplo)

    print("=== TEOREMA CHINÊS DO RESTO ===")
    for residuo, modulo_atual in zip(residuos_exemplo, modulos_exemplo):
        print(f"x ≡ {residuo} (mod {modulo_atual})")
    print(f"\nSolução: x ≡ {solucao} (mod {modulo})")
