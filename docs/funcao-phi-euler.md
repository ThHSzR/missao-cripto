# Função φ de Euler

Responsável: Marini (@mariniluzia98)

Implementação: [`euler_phi_lib.py`](../euler_phi_lib.py)

## Conceito

A função totiente de Euler `φ(n)` conta quantos inteiros positivos menores ou iguais a `n` são coprimos com `n`. Para a fatoração em primos distintos

```text
n = p₁^e₁ · p₂^e₂ · ... · pₖ^eₖ,
```

vale

```text
φ(n) = n · (1 - 1/p₁) · (1 - 1/p₂) · ... · (1 - 1/pₖ).
```

## Interface

```python
def euler_phi(n: int) -> dict:
    ...
```

A função usa fatoração por tentativa e retorna:

```python
{
    "n": n,
    "phi": resultado,
    "fatores_primos": fatores_primos_distintos,
}
```

`n` deve ser maior que zero; caso contrário, a função lança `ValueError`.

## Exemplo

```python
from euler_phi_lib import euler_phi

euler_phi(36)
# {"n": 36, "phi": 12, "fatores_primos": [2, 3]}
```

Para dois primos distintos `p` e `q`, `φ(pq) = (p - 1)(q - 1)`. Assim, `φ(35) = 24`.

## Relação com criptografia

O totiente aparece na formulação clássica do RSA e no teorema de Euler. Ele ajuda a definir expoentes que permitem que as operações de cifração e decifração sejam inversas.

## Limitações atuais

- A fatoração por tentativa não é adequada para inteiros criptograficamente grandes.
- Não há validação explícita de tipo.
- A função retorna metadados em um dicionário, não apenas o valor de `φ(n)`.
