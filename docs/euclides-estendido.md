# Algoritmo estendido de Euclides

Responsável: Guilherme (@GuilhermeAgu1ar)

Implementação: [`euclides_estendido.py`](../euclides_estendido.py)

## Conceito

Além de calcular o MDC, o algoritmo estendido encontra coeficientes inteiros `x` e `y` que satisfazem a identidade de Bézout:

```text
a · x + b · y = mdc(a, b)
```

## Interface

```python
def euclides_estendido(a: int, b: int) -> tuple[int, int, int]:
    ...
```

O retorno segue a ordem `(mdc, x, y)`. A implementação confere internamente se o MDC calculado coincide com `calcular_mdc(a, b)`.

## Exemplo

```python
from euclides_estendido import euclides_estendido

mdc, x, y = euclides_estendido(101, 13)
# (1, 4, -31)

assert 101 * x + 13 * y == mdc
```

## Relação com criptografia

Quando `mdc(a, m) = 1`, o coeficiente associado a `a` fornece seu inverso módulo `m`. Isso liga diretamente o algoritmo ao RSA e ao Teorema Chinês do Resto.

## Limitações atuais

- A interface foi projetada e demonstrada com inteiros positivos.
- Não há validação explícita de tipo.
- Uma asserção interna é usada para conferir o MDC durante a execução.
