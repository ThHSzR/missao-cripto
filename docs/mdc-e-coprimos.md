# MDC e números coprimos

Responsável: Mateus Afonso (@IsMateusReal)

Implementação: [`mdc.py`](../mdc.py)

## Conceitos

O máximo divisor comum de `a` e `b`, escrito `mdc(a, b)`, é o maior inteiro positivo que divide os dois números. Dois inteiros são **coprimos** ou **primos entre si** quando o MDC entre eles é `1`.

Isso não significa que cada número seja primo. Por exemplo, `8` e `15` são compostos, mas são coprimos porque `mdc(8, 15) = 1`.

## Interfaces

```python
def calcular_mdc(a: int, b: int) -> int:
    ...


def coprimos(a: int, b: int) -> bool:
    ...
```

`calcular_mdc` usa o algoritmo de Euclides e normaliza entradas negativas com `abs`. `coprimos` reutiliza o resultado do MDC.

## Exemplo

```python
from mdc import calcular_mdc, coprimos

calcular_mdc(48, 18)  # 6
coprimos(14, 15)      # True
coprimos(14, 21)      # False
```

## Relação com criptografia

A coprimalidade determina quando um inverso modular existe. Ela é usada na geração de parâmetros do RSA, no Teorema Chinês do Resto e em vários algoritmos baseados em grupos multiplicativos.

## Casos importantes

- `mdc(a, 0) = |a|`.
- `mdc(0, 0) = 0` por convenção da implementação.
- `coprimos(a, b)` é equivalente a `calcular_mdc(a, b) == 1`.

## Limitações atuais

- Não há validação explícita de tipo.
- Os exemplos no bloco principal não substituem uma suíte de testes automatizados.
