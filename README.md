# Missão Cripto

Projeto acadêmico colaborativo para investigar e aplicar fundamentos matemáticos e criptográficos na evolução do **SecureDocs**, um sistema fictício de troca e armazenamento de documentos confidenciais.

## Contexto

O SecureDocs foi inicialmente desenvolvido sem mecanismos adequados de proteção: mensagens trafegam em texto claro, documentos são armazenados sem criptografia e senhas são mantidas diretamente no banco de dados.

O projeto busca construir gradualmente uma arquitetura capaz de garantir:

- confidencialidade;
- integridade;
- autenticidade;
- não repúdio.

## Missão 1 — Precisamos de matemática

A primeira etapa consiste em estudar e implementar os fundamentos de teoria dos números usados em criptografia:

- aritmética modular; (Nicole)
- máximo divisor comum (MDC); (Mateus)
- algoritmo de Euclides; (Nicole)
- algoritmo estendido de Euclides; (Guilherme)
- inverso multiplicativo; (Guilherme)
- números primos; (Mateus)
- função φ de Euler; (Marini)
- exponenciação modular; (Marini)
- teorema Chinês do Resto para módulos coprimos. (Thiago)

### Entregáveis

- Biblioteca com as implementações dos algoritmos estudados, preferencialmente em Python.
- Apresentação de 10 minutos com os artefatos produzidos.

### Equipe e responsabilidades

Cada integrante será responsável por pesquisar, implementar, testar e documentar os tópicos atribuídos:

| Integrante | Responsabilidades |
| --- | --- |
| Nicole Noleto (@Nickolliye) | Aritmética modular e algoritmo de Euclides |
| Mateus Afonso (@IsMateusReal) | Máximo divisor comum (MDC) e números primos |
| Guilherme (@GuilhermeAgu1ar) | Algoritmo estendido de Euclides e inverso multiplicativo |
| Marini (@mariniluzia98) | Função φ de Euler e exponenciação modular |
| Thiago (@ThHSzR) | [Teorema Chinês do Resto para módulos coprimos](docs/thiago-teorema-chines-resto.md) |

### Exemplo: Teorema Chinês do Resto

```python
from teorema_chines_resto import teorema_chines_resto

solucao, modulo = teorema_chines_resto(
    residuos=[2, 3, 2],
    modulos=[3, 5, 7],
)

print(f"x ≡ {solucao} (mod {modulo})")  # x ≡ 23 (mod 105)
```

Para executar a demonstração e os testes:

```bash
python3 teorema_chines_resto.py
python3 -m unittest -v test_teorema_chines_resto.py
```

## Colaboração

1. Crie uma branch a partir da `main`.
2. Faça alterações pequenas e bem documentadas.
3. Inclua testes para toda implementação.
4. Abra um pull request para revisão antes de integrar as mudanças.

## Status

🚧 Em desenvolvimento.
