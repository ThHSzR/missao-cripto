# Esboço — Teorema Chinês do Resto

Responsável: Thiago (@ThHSzR)

Status: implementação concluída e validada na Missão 1.

## 1. Objetivo

Pesquisar, explicar e implementar o Teorema Chinês do Resto (TCR) para sistemas de congruências cujos módulos sejam coprimos dois a dois. A entrega deve mostrar não apenas o resultado, mas também as condições de validade, a construção da solução, os testes e uma aplicação em criptografia.

## 2. Conhecimentos necessários

Esta parte integra resultados produzidos nos demais tópicos da missão:

- congruência e aritmética modular;
- máximo divisor comum;
- algoritmo de Euclides;
- algoritmo estendido de Euclides;
- inverso multiplicativo modular.

O algoritmo do TCR usará o MDC para validar os módulos e o algoritmo estendido de Euclides para calcular os inversos modulares.

## 3. Fundamentação matemática

Considere o sistema

```text
x ≡ a₁ (mod m₁)
x ≡ a₂ (mod m₂)
⋮
x ≡ aₖ (mod mₖ)
```

Se todos os módulos forem maiores que 1 e coprimos dois a dois, isto é,

```text
mdc(mᵢ, mⱼ) = 1, para todo i ≠ j,
```

então existe uma única solução módulo

```text
M = m₁ · m₂ · ... · mₖ.
```

"Única módulo M" significa que existem infinitas soluções inteiras, todas da forma `x + tM`, mas apenas um representante no intervalo `0 ≤ x < M`.

### Ideia da demonstração

- **Existência:** construir parcelas que valem `1` no próprio módulo e `0` nos demais módulos; a soma dessas parcelas, ponderada pelos resíduos, satisfaz todas as congruências.
- **Unicidade:** se `x` e `y` satisfazem o sistema, cada `mᵢ` divide `x - y`. Como os módulos são coprimos dois a dois, o produto `M` também divide `x - y`; portanto, `x ≡ y (mod M)`.

## 4. Algoritmo construtivo

Para cada congruência `x ≡ aᵢ (mod mᵢ)`:

1. Calcular `M`, o produto de todos os módulos.
2. Calcular `Mᵢ = M / mᵢ`.
3. Calcular o inverso `yᵢ = Mᵢ⁻¹ mod mᵢ`.
4. Somar as contribuições `aᵢ · Mᵢ · yᵢ`.
5. Normalizar o resultado no intervalo canônico com módulo `M`.

Assim,

```text
x = (Σ aᵢ · Mᵢ · yᵢ) mod M.
```

O inverso `yᵢ` existe porque `Mᵢ` e `mᵢ` são coprimos.

### Pseudocódigo

```text
função tcr(resíduos, módulos):
    validar entradas
    validar se os módulos são coprimos dois a dois

    M ← produto(módulos)
    soma ← 0

    para cada (aᵢ, mᵢ):
        Mᵢ ← M // mᵢ
        yᵢ ← inverso_modular(Mᵢ, mᵢ)
        soma ← soma + aᵢ · Mᵢ · yᵢ

    retornar (soma mod M, M)
```

A função deve retornar tanto o menor representante não negativo quanto o módulo da classe de soluções. Por exemplo, `(23, 105)` representa `x ≡ 23 (mod 105)`.

## 5. Exemplo manual

Resolver:

```text
x ≡ 2 (mod 3)
x ≡ 3 (mod 5)
x ≡ 2 (mod 7)
```

Os módulos `3`, `5` e `7` são coprimos dois a dois e `M = 3 · 5 · 7 = 105`.

| i | aᵢ | mᵢ | Mᵢ | yᵢ = Mᵢ⁻¹ mod mᵢ | Contribuição |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 2 | 3 | 35 | 2 | 140 |
| 2 | 3 | 5 | 21 | 1 | 63 |
| 3 | 2 | 7 | 15 | 1 | 30 |

```text
x = (140 + 63 + 30) mod 105
x = 233 mod 105
x = 23
```

Verificação:

```text
23 mod 3 = 2
23 mod 5 = 3
23 mod 7 = 2
```

Logo, `x ≡ 23 (mod 105)`.

## 6. Esboço da implementação em Python

### Interface implementada

```python
from collections.abc import Sequence


def teorema_chines_resto(
    residuos: Sequence[int],
    modulos: Sequence[int],
) -> tuple[int, int]:
    """Retorna (solução, módulo_produto) para módulos coprimos dois a dois."""
```

### Regras de entrada

- As sequências não podem estar vazias.
- As sequências devem ter o mesmo tamanho.
- Resíduos e módulos devem ser inteiros.
- Todo módulo deve ser maior que 1.
- Os módulos devem ser coprimos dois a dois.
- Resíduos negativos ou maiores que o módulo devem ser normalizados com `%`.

### Erros esperados

- `ValueError` para listas vazias, tamanhos diferentes, módulos inválidos ou módulos não coprimos dois a dois.
- `TypeError` para valores que não sejam inteiros.

### Decisões de integração

- A implementação reutiliza `coprimos`, do módulo `mdc.py`, e `inverso_multiplicativo`, do módulo `inverso_multiplicativo.py`.
- A interface aceita sequências de inteiros e retorna `(solução, módulo_produto)`.
- A versão atual cobre somente módulos coprimos dois a dois, conforme o escopo da missão.
- Entradas inválidas são rejeitadas com `TypeError` ou `ValueError` e mensagens explicativas.

### Execução

```bash
python3 teorema_chines_resto.py
python3 -m unittest -v test_teorema_chines_resto.py
```

## 7. Plano de testes

### Casos válidos

1. Exemplo clássico: `[2, 3, 2]`, `[3, 5, 7]` → `(23, 105)`.
2. Dois módulos: `[1, 3]`, `[4, 5]` → `(13, 20)`.
3. Um único módulo: `[8]`, `[5]` → `(3, 5)`.
4. Resíduo negativo: `[-1, 3]`, `[5, 7]` → solução equivalente e normalizada.
5. Resíduo maior que o módulo: `[20, 10]`, `[3, 7]` → solução equivalente e normalizada.

### Casos inválidos

1. Listas vazias.
2. Quantidades diferentes de resíduos e módulos.
3. Módulo igual a `0`, `1` ou negativo.
4. Módulos repetidos.
5. Módulos não coprimos, como `[6, 8]`.
6. Valores não inteiros.

### Propriedade a verificar

Para toda entrada válida e para cada índice `i`:

```text
solução % módulos[i] == resíduos[i] % módulos[i]
```

Também deve valer:

```text
0 ≤ solução < produto(módulos)
```

## 8. Relação com criptografia

O TCR permite decompor cálculos com números grandes em cálculos menores e depois recombinar os resultados. No RSA, operações privadas podem ser feitas separadamente módulo `p` e módulo `q`, e então reunidas pelo TCR. A RFC 8017 formaliza parâmetros como `dP`, `dQ` e `qInv` e descreve essa recombinação para descriptografia e assinatura.

Essa otimização também introduz uma preocupação de segurança: uma falha durante apenas uma das exponenciações do RSA-CRT pode produzir um resultado incorreto que revele um fator do módulo público por meio de um cálculo de MDC. Portanto, a apresentação deve diferenciar:

- a implementação didática do TCR desta missão;
- o uso criptográfico em produção, que exige bibliotecas auditadas e contramedidas contra falhas e canais laterais.

Não será implementado um RSA próprio como parte deste tópico. O RSA-CRT servirá como aplicação e possível demonstração controlada, não como componente pronto para uso real.

## 9. Roteiro da demonstração

1. Apresentar o problema de congruências simultâneas.
2. Explicar a condição de coprimalidade e a unicidade módulo `M`.
3. Resolver o exemplo `3, 5, 7` manualmente.
4. Executar a mesma entrada na implementação Python.
5. Mostrar um teste que rejeita módulos não coprimos.
6. Conectar o algoritmo ao RSA-CRT e mencionar o risco de ataques por falha.

## 10. Critérios de conclusão

- [ ] Fundamentação revisada pelo grupo.
- [x] Função implementada com documentação e type hints.
- [x] Integração com MDC e inverso modular concluída.
- [x] Casos válidos e inválidos cobertos por testes automatizados.
- [x] Exemplo manual confere com a saída da biblioteca.
- [ ] Demonstração curta preparada para a apresentação.
- [x] Limitações de segurança documentadas.

## Fontes

- [MIT OpenCourseWare — Linear Congruences, Chinese Remainder Theorem, Algorithms](https://ocw.mit.edu/courses/18-781-theory-of-numbers-spring-2012/7b36e2ada32c5ed0638783d4e66af60c_MIT18_781S12_lec5.pdf)
- [MIT OpenCourseWare — Mathematics for Computer Science, capítulo 8](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf)
- [RFC 8017 — PKCS #1: RSA Cryptography Specifications Version 2.2](https://www.rfc-editor.org/rfc/rfc8017)
- [IACR ePrint 2012/172 — Attacking RSA-CRT Signatures](https://eprint.iacr.org/2012/172)
