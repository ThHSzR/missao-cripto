# Aritmética modular

Responsável: Nicole Noleto (@Nickolliye)

Implementação: [`aritmetica_modular.py`](../aritmetica_modular.py)

## Conceito

Na aritmética modular, inteiros são agrupados pelo resto da divisão por um módulo positivo `m`. A congruência

```text
a ≡ b (mod m)
```

significa que `m` divide `a - b`. Soma, subtração e multiplicação preservam congruências, permitindo reduzir resultados intermediários módulo `m`.

## Interface

```python
def aritmetica_modular(a: int, b: int, m: int) -> dict:
    ...
```

A função retorna:

```python
{
    "soma": (a + b) % m,
    "subtracao": (a - b) % m,
    "multiplicacao": (a * b) % m,
}
```

O módulo deve ser maior que zero; caso contrário, a função lança `ValueError`.

## Exemplo

```python
from aritmetica_modular import aritmetica_modular

resultado = aritmetica_modular(17, 8, 5)
# {"soma": 0, "subtracao": 4, "multiplicacao": 1}
```

## Relação com criptografia

Operações modulares aparecem em RSA, Diffie-Hellman, curvas elípticas e assinaturas digitais. A redução modular mantém os valores dentro de um conjunto finito, mesmo quando as operações envolvem inteiros grandes.

## Limitações atuais

- A função reúne três operações em um dicionário; não há funções separadas.
- Não há validação explícita de tipo para `a`, `b` e `m`.
- A implementação é educacional e não oferece garantias de tempo constante.
