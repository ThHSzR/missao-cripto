# Inverso multiplicativo modular

Responsável: Guilherme (@GuilhermeAgu1ar)

Implementação: [`inverso_multiplicativo.py`](../inverso_multiplicativo.py)

## Conceito

O inverso multiplicativo de `a` módulo `m` é um inteiro `x` tal que

```text
a · x ≡ 1 (mod m)
```

Esse inverso existe se, e somente se, `mdc(a, m) = 1`.

## Interface

```python
def inverso_multiplicativo(a: int, m: int) -> int:
    ...
```

A função usa `euclides_estendido(a, m)` para obter um coeficiente de Bézout e normaliza o resultado para o intervalo `0 <= x < m`. Se o MDC não for `1`, lança `ValueError`.

## Exemplo

```python
from inverso_multiplicativo import inverso_multiplicativo

inverso = inverso_multiplicativo(23, 60)  # 47
assert (23 * inverso) % 60 == 1
```

O inverso de `8` módulo `12` não existe porque `mdc(8, 12) = 4`.

## Relação com criptografia

Inversos modulares são usados para calcular a chave privada do RSA, resolver congruências, produzir assinaturas e construir a solução do Teorema Chinês do Resto.

## Limitações atuais

- O módulo deve ser maior que `1` para que a operação tenha a interpretação usual, embora isso não seja validado explicitamente.
- Não há validação explícita de tipo.
- A implementação é didática e não foi projetada para execução em tempo constante.
