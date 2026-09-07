# Exponenciação modular

Responsável: Marini (@mariniluzia98)

Implementação: [`modular_exponentiation_lib.py`](../modular_exponentiation_lib.py)

## Conceito

A exponenciação modular calcula

```text
base^expoente mod m
```

sem construir primeiro a potência completa. O algoritmo *square-and-multiply* lê os bits do expoente, realiza quadraturas sucessivas e reduz os resultados módulo `m` em cada etapa.

## Interface

```python
def exponenciacao_modular(base: int, expoente: int, m: int) -> dict:
    ...
```

A função retorna as entradas, a representação binária do expoente e o resultado:

```python
{
    "base": base,
    "expoente": expoente,
    "modulo": m,
    "expoente_binario": bin(expoente)[2:],
    "resultado": resultado,
}
```

O módulo deve ser positivo e o expoente não pode ser negativo. Entradas fora dessas condições produzem `ValueError`.

## Exemplo

```python
from modular_exponentiation_lib import exponenciacao_modular

resultado = exponenciacao_modular(7, 11, 13)
assert resultado["resultado"] == 2
```

## Complexidade

O algoritmo realiza `O(log expoente)` iterações e mantém os valores intermediários reduzidos módulo `m`.

## Relação com criptografia

Exponenciação modular é a operação central do RSA, do Diffie-Hellman e de vários esquemas de assinatura. Sua execução eficiente é essencial quando expoentes e módulos têm centenas ou milhares de bits.

## Limitações atuais

- Expoentes negativos não são suportados.
- Não há validação explícita de tipo.
- A implementação é didática e não protege contra canais laterais de tempo ou consumo de energia.
