# Algoritmo de Euclides

Responsável: Nicole Noleto (@Nickolliye)

Implementação: [`euclides.py`](../euclides.py)

## Conceito

O algoritmo de Euclides calcula o MDC por divisões sucessivas. Ele usa a identidade

```text
mdc(a, b) = mdc(b, a mod b)
```

até que o segundo valor seja zero. O último divisor não nulo é o MDC.

## Interface

```python
def algoritmo_euclides(a: int, b: int) -> list:
    ...
```

A função retorna uma lista de tuplas `(dividendo, divisor, resto)` e, portanto, preserva o passo a passo do algoritmo em vez de retornar diretamente o MDC.

## Exemplo

```python
from euclides import algoritmo_euclides

algoritmo_euclides(48, 18)
# [(48, 18, 12), (18, 12, 6), (12, 6, 0)]
```

O MDC pode ser identificado como o divisor da última tupla: `6`.

## Relação com criptografia

O algoritmo permite verificar coprimalidade de maneira eficiente e é a base do algoritmo estendido de Euclides, usado para encontrar inversos modulares.

## Limitações atuais

- A função retorna os passos, não o MDC isoladamente; para obter diretamente o MDC, use `calcular_mdc` de `mdc.py`.
- Não há validação explícita de tipo.
- Para `(0, 0)`, a lista retornada é vazia.
