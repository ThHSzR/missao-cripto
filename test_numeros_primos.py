"""Testes das operações com números primos."""

import unittest

from numeros_primos import eh_primo, listar_primos


class TestEhPrimo(unittest.TestCase):
    """Testa a classificação de números primos e compostos."""

    def test_numeros_menores_que_dois_nao_sao_primos(self) -> None:
        for numero in (-100, -1, 0, 1):
            with self.subTest(numero=numero):
                self.assertFalse(eh_primo(numero))

    def test_primos(self) -> None:
        for numero in (2, 3, 5, 7, 17, 97, 104729):
            with self.subTest(numero=numero):
                self.assertTrue(eh_primo(numero))

    def test_compostos(self) -> None:
        for numero in (4, 6, 9, 15, 25, 49, 121, 104730):
            with self.subTest(numero=numero):
                self.assertFalse(eh_primo(numero))

    def test_rejeita_valores_que_nao_sao_inteiros(self) -> None:
        for valor in (2.0, "2", None, True):
            with self.subTest(valor=valor):
                with self.assertRaisesRegex(TypeError, "número inteiro"):
                    eh_primo(valor)  # type: ignore[arg-type]


class TestListarPrimos(unittest.TestCase):
    """Testa a enumeração pelo Crivo de Eratóstenes."""

    def test_limite_menor_que_dois_retorna_lista_vazia(self) -> None:
        for limite in (-10, 0, 1):
            with self.subTest(limite=limite):
                self.assertEqual(listar_primos(limite), [])

    def test_limite_dois(self) -> None:
        self.assertEqual(listar_primos(2), [2])

    def test_primos_ate_trinta(self) -> None:
        self.assertEqual(
            listar_primos(30),
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
        )

    def test_lista_consistente_com_teste_de_primalidade(self) -> None:
        primos = set(listar_primos(200))
        for numero in range(201):
            with self.subTest(numero=numero):
                self.assertEqual(numero in primos, eh_primo(numero))

    def test_rejeita_valores_que_nao_sao_inteiros(self) -> None:
        for valor in (30.0, "30", None, False):
            with self.subTest(valor=valor):
                with self.assertRaisesRegex(TypeError, "número inteiro"):
                    listar_primos(valor)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
