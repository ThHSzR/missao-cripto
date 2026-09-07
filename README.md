# Missão Cripto

Biblioteca acadêmica em Python para estudar os fundamentos matemáticos usados em criptografia. O projeto faz parte da evolução do **SecureDocs**, um sistema fictício de troca e armazenamento de documentos confidenciais.

## Objetivo

A Missão 1, **Precisamos de matemática**, investiga como a teoria dos números permite construir sistemas criptográficos. A biblioteca reúne pequenas implementações didáticas dos algoritmos estudados e servirá como base para as próximas missões de segurança do SecureDocs.

O projeto busca contribuir, gradualmente, para uma arquitetura que ofereça:

- confidencialidade;
- integridade;
- autenticidade;
- não repúdio.

## Conformidade com a Missão 1

O enunciado solicita dois produtos. O estado atual é:

| Produto solicitado | Situação | Evidência |
| --- | --- | --- |
| Biblioteca com os algoritmos estudados, preferencialmente em Python | 🚧 Parcial | 8 dos 9 tópicos possuem implementação própria |
| Apresentação de 10 minutos com os artefatos produzidos | ⏳ Pendente | Ainda não há apresentação versionada no repositório |

### Implementações

| Tópico | Responsável | Implementação | Situação |
| --- | --- | --- | --- |
| Aritmética modular | Nicole Noleto (@Nickolliye) | [`aritmetica_modular.py`](aritmetica_modular.py) | ✅ Implementado |
| Máximo divisor comum (MDC) | Mateus Afonso (@IsMateusReal) | [`mdc.py`](mdc.py) | ✅ Implementado |
| Algoritmo de Euclides | Nicole Noleto (@Nickolliye) | [`euclides.py`](euclides.py) | ✅ Implementado |
| Algoritmo estendido de Euclides | Guilherme (@GuilhermeAgu1ar) | [`euclides_estendido.py`](euclides_estendido.py) | ✅ Implementado |
| Inverso multiplicativo | Guilherme (@GuilhermeAgu1ar) | [`inverso_multiplicativo.py`](inverso_multiplicativo.py) | ✅ Implementado |
| Números primos | Mateus Afonso (@IsMateusReal) | — | ⚠️ Pendente |
| Função φ de Euler | Marini (@mariniluzia98) | [`euler_phi_lib.py`](euler_phi_lib.py) | ✅ Implementado |
| Exponenciação modular | Marini (@mariniluzia98) | [`modular_exponentiation_lib.py`](modular_exponentiation_lib.py) | ✅ Implementado |
| Teorema Chinês do Resto para módulos coprimos | Thiago (@ThHSzR) | [`teorema_chines_resto.py`](teorema_chines_resto.py) | ✅ Implementado |

> `mdc.py` implementa `coprimos(a, b)`, que verifica se dois inteiros são primos entre si. Isso é diferente de determinar se um número isolado é primo. Embora `euler_phi_lib.py` faça fatoração internamente para calcular φ(n), o repositório ainda não possui uma implementação própria e documentada para teste ou geração de números primos.

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

Para executar os testes automatizados disponíveis:

```bash
python3 -m unittest discover -v
```

Atualmente, a suíte automatizada contém 14 testes do Teorema Chinês do Resto. Os demais módulos possuem exemplos e verificações locais executados por seus respectivos blocos `if __name__ == "__main__"`.

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
├── teorema_chines_resto.py
├── test_teorema_chines_resto.py
└── docs/
    └── thiago-teorema-chines-resto.md
```

## Pendências para concluir a missão

- [ ] Implementar e documentar o tópico de números primos.
- [ ] Adicionar testes automatizados para os demais módulos.
- [ ] Preparar e versionar a apresentação de 10 minutos.
- [ ] Revisar a integração e os exemplos como grupo.

## Colaboração

1. Crie uma branch a partir da `main` atualizada.
2. Faça alterações pequenas, documentadas e acompanhadas de testes.
3. Execute a suíte antes de enviar sua contribuição.
4. Abra um pull request para revisão antes de integrar as mudanças.

## Status

🚧 **Missão 1 em desenvolvimento:** biblioteca funcional, com uma implementação e a apresentação ainda pendentes.
