# Missão Cripto

Biblioteca acadêmica em Python para estudar os fundamentos matemáticos usados em criptografia. O projeto faz parte da evolução do **SecureDocs**, um sistema fictício de troca e armazenamento de documentos confidenciais.

## Objetivo

A Missão 1, **Precisamos de matemática**, investiga como a teoria dos números permite construir sistemas criptográficos. A biblioteca reúne pequenas implementações didáticas dos algoritmos estudados e servirá como base para as próximas missões de segurança do SecureDocs.

O projeto busca contribuir, gradualmente, para uma arquitetura que ofereça:

- confidencialidade;
- integridade;
- autenticidade;
- não repúdio.

## Escopo implementado

Considerando o escopo da biblioteca matemática, os nove tópicos da Missão 1 possuem implementação própria em Python:

| Tópico | Responsável | Implementação | Situação |
| --- | --- | --- | --- |
| Aritmética modular | Nicole Noleto (@Nickolliye) | [`aritmetica_modular.py`](aritmetica_modular.py) | ✅ Implementado |
| Máximo divisor comum (MDC) | Mateus Afonso (@IsMateusReal) | [`mdc.py`](mdc.py) | ✅ Implementado |
| Algoritmo de Euclides | Nicole Noleto (@Nickolliye) | [`euclides.py`](euclides.py) | ✅ Implementado |
| Algoritmo estendido de Euclides | Guilherme (@GuilhermeAgu1ar) | [`euclides_estendido.py`](euclides_estendido.py) | ✅ Implementado |
| Inverso multiplicativo | Guilherme (@GuilhermeAgu1ar) | [`inverso_multiplicativo.py`](inverso_multiplicativo.py) | ✅ Implementado |
| Números primos | Mateus Afonso (@IsMateusReal) | [`numeros_primos.py`](numeros_primos.py) | ✅ Implementado |
| Função φ de Euler | Marini (@mariniluzia98) | [`euler_phi_lib.py`](euler_phi_lib.py) | ✅ Implementado |
| Exponenciação modular | Marini (@mariniluzia98) | [`modular_exponentiation_lib.py`](modular_exponentiation_lib.py) | ✅ Implementado |
| Teorema Chinês do Resto para módulos coprimos | Thiago (@ThHSzR) | [`teorema_chines_resto.py`](teorema_chines_resto.py) | ✅ Implementado |

`mdc.py` verifica coprimalidade entre dois inteiros. Já `numeros_primos.py` implementa o teste de primalidade de um número individual e o Crivo de Eratóstenes para enumerar primos até um limite.

A documentação completa dos métodos está disponível no [índice de documentação](docs/README.md).

## Requisitos

- Python 3.10 ou superior.
- Nenhuma dependência externa.

## Como executar

Cada módulo implementado possui uma demonstração que pode ser executada diretamente. Por exemplo:

```bash
python3 mdc.py
python3 inverso_multiplicativo.py
python3 teorema_chines_resto.py
```

Os exemplos e verificações locais ficam nos respectivos blocos `if __name__ == "__main__"`.

## Exemplo: Teorema Chinês do Resto

```python
from teorema_chines_resto import teorema_chines_resto

solucao, modulo = teorema_chines_resto(
    residuos=[2, 3, 2],
    modulos=[3, 5, 7],
)

print(f"x ≡ {solucao} (mod {modulo})")  # x ≡ 23 (mod 105)
```

A função valida se os módulos são coprimos dois a dois, normaliza os resíduos e retorna a solução canônica junto com o produto dos módulos. A [documentação do Teorema Chinês do Resto](docs/thiago-teorema-chines-resto.md) apresenta a fundamentação, o algoritmo, um exemplo manual, o plano de testes e sua relação com o RSA.

## Organização

```text
.
├── aritmetica_modular.py
├── euclides.py
├── euclides_estendido.py
├── euler_phi_lib.py
├── inverso_multiplicativo.py
├── mdc.py
├── modular_exponentiation_lib.py
├── numeros_primos.py
├── teorema_chines_resto.py
└── docs/
    ├── README.md
    ├── algoritmo-euclides.md
    ├── aritmetica-modular.md
    ├── euclides-estendido.md
    ├── exponenciacao-modular.md
    ├── funcao-phi-euler.md
    ├── inverso-multiplicativo.md
    ├── mdc-e-coprimos.md
    ├── numeros-primos.md
    └── thiago-teorema-chines-resto.md
```

## Critérios atendidos

- [x] Os nove tópicos matemáticos possuem implementação própria.
- [x] Números primos e coprimalidade são tratados como conceitos distintos.
- [x] Todos os módulos possuem documentação em `docs/`.
- [x] Os módulos compilam e suas demonstrações executam sem erro.

## Colaboração

1. Crie uma branch a partir da `main` atualizada.
2. Faça alterações pequenas e documentadas.
3. Execute os módulos afetados antes de enviar sua contribuição.
4. Abra um pull request para revisão antes de integrar as mudanças.

## Status

✅ **Biblioteca matemática da Missão 1 concluída e documentada.**
