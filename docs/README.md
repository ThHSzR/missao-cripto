# Documentação da biblioteca

Esta pasta reúne a fundamentação e o uso dos nove tópicos matemáticos da Missão 1.

| Tópico | Módulo | Documentação |
| --- | --- | --- |
| Aritmética modular | `aritmetica_modular.py` | [Aritmética modular](aritmetica-modular.md) |
| MDC e coprimalidade | `mdc.py` | [MDC e coprimos](mdc-e-coprimos.md) |
| Algoritmo de Euclides | `euclides.py` | [Algoritmo de Euclides](algoritmo-euclides.md) |
| Algoritmo estendido de Euclides | `euclides_estendido.py` | [Euclides estendido](euclides-estendido.md) |
| Inverso multiplicativo | `inverso_multiplicativo.py` | [Inverso multiplicativo](inverso-multiplicativo.md) |
| Números primos | `numeros_primos.py` | [Números primos](numeros-primos.md) |
| Função φ de Euler | `euler_phi_lib.py` | [Função φ de Euler](funcao-phi-euler.md) |
| Exponenciação modular | `modular_exponentiation_lib.py` | [Exponenciação modular](exponenciacao-modular.md) |
| Teorema Chinês do Resto | `teorema_chines_resto.py` | [Teorema Chinês do Resto](thiago-teorema-chines-resto.md) |

## Execução

Os módulos usam somente a biblioteca padrão do Python. Execute uma demonstração com:

```bash
python3 nome_do_modulo.py
```

Execute todos os testes automatizados com:

```bash
python3 -m unittest discover -v
```

As implementações são didáticas. Para sistemas reais, devem ser usadas bibliotecas criptográficas consolidadas, auditadas e adequadas ao modelo de ameaça da aplicação.
