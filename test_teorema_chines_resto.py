"""Testes da implementação do Teorema Chinês do Resto."""

import unittest

from teorema_chines_resto import teorema_chines_resto


class TestTeoremaChinesResto(unittest.TestCase):
    """Valida resultados, normalização e tratamento de entradas inválidas."""

    def test_exemplo_classico(self) -> None:
        self.assertEqual(
            teorema_chines_resto([2, 3, 2], [3, 5, 7]),
            (23, 105),
        )

    def test_dois_modulos(self) -> None:
        self.assertEqual(teorema_chines_resto([1, 3], [4, 5]), (13, 20))

    def test_um_modulo(self) -> None:
        self.assertEqual(teorema_chines_resto([8], [5]), (3, 5))

    def test_aceita_tuplas(self) -> None:
        self.assertEqual(teorema_chines_resto((2, 3, 2), (3, 5, 7)), (23, 105))

    def test_normaliza_residuo_negativo(self) -> None:
        solucao, modulo = teorema_chines_resto([-1, 3], [5, 7])
        self.assertEqual((solucao, modulo), (24, 35))

    def test_normaliza_residuo_maior_que_modulo(self) -> None:
        solucao, modulo = teorema_chines_resto([20, 10], [3, 7])
        self.assertEqual((solucao, modulo), (17, 21))

    def test_resultado_satisfaz_todas_as_congruencias(self) -> None:
        casos = [
            ([2, 3, 2], [3, 5, 7]),
            ([0, 4, 6], [5, 7, 11]),
            ([-20, 100], [9, 16]),
        ]

        for residuos, modulos in casos:
            with self.subTest(residuos=residuos, modulos=modulos):
                solucao, modulo_produto = teorema_chines_resto(residuos, modulos)
                self.assertGreaterEqual(solucao, 0)
                self.assertLess(solucao, modulo_produto)
                for residuo, modulo in zip(residuos, modulos):
                    self.assertEqual(solucao % modulo, residuo % modulo)

    def test_rejeita_sistema_vazio(self) -> None:
        with self.assertRaisesRegex(ValueError, "ao menos uma congruência"):
            teorema_chines_resto([], [])

    def test_rejeita_tamanhos_diferentes(self) -> None:
        with self.assertRaisesRegex(ValueError, "devem ser iguais"):
            teorema_chines_resto([1], [3, 5])

    def test_rejeita_modulos_invalidos(self) -> None:
        for modulo in (0, 1, -5):
            with self.subTest(modulo=modulo):
                with self.assertRaisesRegex(ValueError, "maiores que 1"):
                    teorema_chines_resto([1], [modulo])

    def test_rejeita_modulos_nao_coprimos(self) -> None:
        with self.assertRaisesRegex(ValueError, "coprimos dois a dois"):
            teorema_chines_resto([1, 2], [6, 8])

    def test_rejeita_modulos_repetidos(self) -> None:
        with self.assertRaisesRegex(ValueError, "coprimos dois a dois"):
            teorema_chines_resto([1, 2], [5, 5])

    def test_rejeita_entradas_que_nao_sao_sequencias(self) -> None:
        with self.assertRaisesRegex(TypeError, "sequência de inteiros"):
            teorema_chines_resto(2, [3])  # type: ignore[arg-type]

    def test_rejeita_valores_que_nao_sao_inteiros(self) -> None:
        entradas_invalidas = [
            ([1.5], [3]),
            ([1], [3.5]),
            ([True], [3]),
            ([1], [False]),
        ]

        for residuos, modulos in entradas_invalidas:
            with self.subTest(residuos=residuos, modulos=modulos):
                with self.assertRaisesRegex(TypeError, "apenas números inteiros"):
                    teorema_chines_resto(residuos, modulos)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
