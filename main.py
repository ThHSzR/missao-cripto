"""Menu interativo para acessar todas as funções da biblioteca matemática."""

from collections.abc import Callable

from aritmetica_modular import aritmetica_modular
from euclides import algoritmo_euclides
from euclides_estendido import euclides_estendido
from euler_phi_lib import euler_phi
from inverso_multiplicativo import inverso_multiplicativo
from mdc import calcular_mdc, coprimos
from modular_exponentiation_lib import exponenciacao_modular
from numeros_primos import eh_primo, listar_primos
from teorema_chines_resto import teorema_chines_resto


def ler_inteiro(mensagem: str) -> int:
    """Lê um número inteiro informado pelo usuário."""
    return int(input(mensagem).strip())


def ler_lista_inteiros(mensagem: str) -> list[int]:
    """Lê inteiros separados por espaços ou vírgulas."""
    texto = input(mensagem).strip().replace(",", " ")
    valores = texto.split()
    if not valores:
        raise ValueError("Informe ao menos um número inteiro.")
    return [int(valor) for valor in valores]


def executar_aritmetica_modular() -> None:
    """Solicita valores e mostra soma, subtração e multiplicação modulares."""
    a = ler_inteiro("Primeiro número (a): ")
    b = ler_inteiro("Segundo número (b): ")
    modulo = ler_inteiro("Módulo: ")
    resultado = aritmetica_modular(a, b, modulo)

    print(f"Soma modular: {resultado['soma']}")
    print(f"Subtração modular: {resultado['subtracao']}")
    print(f"Multiplicação modular: {resultado['multiplicacao']}")


def executar_mdc() -> None:
    """Calcula o máximo divisor comum entre dois inteiros."""
    a = ler_inteiro("Primeiro número: ")
    b = ler_inteiro("Segundo número: ")
    print(f"MDC({a}, {b}) = {calcular_mdc(a, b)}")


def executar_coprimos() -> None:
    """Informa se dois inteiros são coprimos."""
    a = ler_inteiro("Primeiro número: ")
    b = ler_inteiro("Segundo número: ")
    resposta = "Sim" if coprimos(a, b) else "Não"
    print(f"{a} e {b} são coprimos? {resposta}.")


def executar_euclides() -> None:
    """Exibe as divisões produzidas pelo algoritmo de Euclides."""
    a = ler_inteiro("Primeiro número: ")
    b = ler_inteiro("Segundo número: ")
    passos = algoritmo_euclides(a, b)

    if not passos:
        print(f"Nenhuma divisão necessária. MDC = {calcular_mdc(a, b)}")
        return

    print("Passos do algoritmo:")
    for dividendo, divisor, resto in passos:
        print(f"  {dividendo} = {dividendo // divisor} × {divisor} + {resto}")
    print(f"MDC = {calcular_mdc(a, b)}")


def executar_euclides_estendido() -> None:
    """Calcula o MDC e os coeficientes da identidade de Bézout."""
    a = ler_inteiro("Primeiro número não negativo: ")
    b = ler_inteiro("Segundo número não negativo: ")
    if a < 0 or b < 0:
        raise ValueError("Use números não negativos nesta operação.")

    mdc, x, y = euclides_estendido(a, b)
    print(f"MDC = {mdc}, x = {x}, y = {y}")
    print(f"Verificação: {a} × ({x}) + {b} × ({y}) = {mdc}")


def executar_inverso() -> None:
    """Calcula o inverso multiplicativo de um número em um módulo."""
    numero = ler_inteiro("Número: ")
    modulo = ler_inteiro("Módulo maior que 1: ")
    if modulo <= 1:
        raise ValueError("O módulo deve ser maior que 1.")

    inverso = inverso_multiplicativo(numero, modulo)
    print(f"{numero}⁻¹ mod {modulo} = {inverso}")


def executar_teste_primalidade() -> None:
    """Informa se um número é primo."""
    numero = ler_inteiro("Número: ")
    resposta = "Sim" if eh_primo(numero) else "Não"
    print(f"{numero} é primo? {resposta}.")


def executar_listagem_primos() -> None:
    """Lista todos os números primos até um limite informado."""
    limite = ler_inteiro("Listar primos até: ")
    primos = listar_primos(limite)
    print(f"Primos até {limite}: {primos}")


def executar_phi_euler() -> None:
    """Calcula a função totiente de Euler."""
    numero = ler_inteiro("Número positivo (n): ")
    resultado = euler_phi(numero)
    print(f"φ({numero}) = {resultado['phi']}")
    print(f"Fatores primos distintos: {resultado['fatores_primos']}")


def executar_exponenciacao_modular() -> None:
    """Calcula uma potência modular com square-and-multiply."""
    base = ler_inteiro("Base: ")
    expoente = ler_inteiro("Expoente não negativo: ")
    modulo = ler_inteiro("Módulo positivo: ")
    resultado = exponenciacao_modular(base, expoente, modulo)

    print(f"Expoente em binário: {resultado['expoente_binario']}")
    print(f"{base}^{expoente} mod {modulo} = {resultado['resultado']}")


def executar_tcr() -> None:
    """Resolve um sistema pelo Teorema Chinês do Resto."""
    residuos = ler_lista_inteiros("Resíduos, separados por espaços ou vírgulas: ")
    modulos = ler_lista_inteiros("Módulos, separados por espaços ou vírgulas: ")
    solucao, modulo_produto = teorema_chines_resto(residuos, modulos)
    print(f"Solução: x ≡ {solucao} (mod {modulo_produto})")


ACOES: dict[str, tuple[str, Callable[[], None]]] = {
    "1": ("Aritmética modular", executar_aritmetica_modular),
    "2": ("Máximo divisor comum (MDC)", executar_mdc),
    "3": ("Verificar números coprimos", executar_coprimos),
    "4": ("Algoritmo de Euclides", executar_euclides),
    "5": ("Algoritmo estendido de Euclides", executar_euclides_estendido),
    "6": ("Inverso multiplicativo", executar_inverso),
    "7": ("Verificar número primo", executar_teste_primalidade),
    "8": ("Listar números primos", executar_listagem_primos),
    "9": ("Função φ de Euler", executar_phi_euler),
    "10": ("Exponenciação modular", executar_exponenciacao_modular),
    "11": ("Teorema Chinês do Resto", executar_tcr),
}


def exibir_menu() -> None:
    """Mostra as operações disponíveis."""
    print("\n=== MISSÃO CRIPTO — MENU ===")
    for codigo, (descricao, _) in ACOES.items():
        print(f"{codigo:>2} - {descricao}")
    print(" 0 - Sair")


def main() -> None:
    """Mantém o menu em execução até o usuário escolher sair."""
    while True:
        exibir_menu()
        try:
            opcao = input("\nEscolha uma opção: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nPrograma encerrado.")
            break

        if opcao == "0":
            print("Programa encerrado.")
            break

        acao = ACOES.get(opcao)
        if acao is None:
            print("Opção inválida. Escolha um número do menu.")
            continue

        print(f"\n--- {acao[0]} ---")
        try:
            acao[1]()
        except (TypeError, ValueError, ZeroDivisionError) as erro:
            print(f"Erro: {erro}")
        except (EOFError, KeyboardInterrupt):
            print("\nOperação cancelada.")

        try:
            input("\nPressione Enter para voltar ao menu...")
        except (EOFError, KeyboardInterrupt):
            print()


if __name__ == "__main__":
    main()
