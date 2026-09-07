# Números primos

Responsável pelo tópico: Mateus Afonso (@IsMateusReal)

Implementação: [`numeros_primos.py`](../numeros_primos.py)

## Conceito

Um número primo é um inteiro maior que `1` com exatamente dois divisores positivos: `1` e ele mesmo. Números maiores que `1` que não são primos são chamados compostos.

Primalidade é uma propriedade de um número individual. Ela não deve ser confundida com coprimalidade, que compara dois números pelo MDC.

## Teste de primalidade

```python
def eh_primo(n: int) -> bool:
    ...
```

A função trata inicialmente números menores que `2`, os primos `2` e `3`, e múltiplos de `2` ou `3`. Depois testa apenas candidatos da forma `6k - 1` e `6k + 1` até `isqrt(n)`.

### Exemplo

```python
from numeros_primos import eh_primo

eh_primo(2)   # True
eh_primo(17)  # True
eh_primo(25)  # False
eh_primo(1)   # False
```

### Complexidade

- Tempo: `O(√n)` no pior caso.
- Memória adicional: `O(1)`.

## Enumeração com o Crivo de Eratóstenes

```python
def listar_primos(limite: int) -> list[int]:
    ...
```

O crivo marca números compostos a partir do quadrado de cada primo encontrado e retorna todos os primos no intervalo fechado `[2, limite]`.

### Exemplo

```python
from numeros_primos import listar_primos

listar_primos(20)  # [2, 3, 5, 7, 11, 13, 17, 19]
```

### Complexidade

- Tempo: `O(n log log n)`.
- Memória: `O(n)`.

## Entradas e erros

- Números negativos, `0` e `1` não são primos.
- Limites menores que `2` produzem uma lista vazia.
- Valores não inteiros, inclusive booleanos, produzem `TypeError`.

## Relação com criptografia

Primos grandes são fundamentais no RSA e em outros sistemas baseados em problemas aritméticos difíceis. Este módulo ensina os conceitos com algoritmos determinísticos simples.

## Limitações de segurança

O teste por divisão e o crivo não são apropriados para gerar chaves criptográficas reais. Sistemas de produção precisam de geração aleatória segura, testes probabilísticos adequados para inteiros grandes e bibliotecas criptográficas auditadas.

## Verificação local

```bash
python3 numeros_primos.py
```

O bloco principal demonstra a classificação de números primos e compostos e lista os primos até `50`.
