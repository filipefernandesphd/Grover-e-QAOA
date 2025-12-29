# ============================================================
# Implementação da busca linear clássica a partir de uma string de bits
# 
# Desenvolvido por Filipe Fernandes [filipe.fernandes@ifsudestemg.edu.br]
# ============================================================
import time
from typing import Dict, Any, Optional

class BuscaLinearClassica:
    """
    Executa busca clássica não ordenada em um espaço de estados binários,
    utilizando um oráculo clássico f(x).
    """

    def __init__(self):
        self._alvo_bits: Optional[str] = None
        self._alvo_decimal: Optional[int] = None
        self._num_bits: Optional[int] = None
        self._espaco_busca: Optional[int] = None
        self._resultado: Optional[Dict[str, Any]] = None

    # --------------------------------------------------
    # Oráculo clássico (privado)
    # --------------------------------------------------
    def _oraculo(self, x: int) -> int:
        """
        Oráculo clássico:
        retorna 1 se x corresponde ao alvo, 0 caso contrário.
        """
        return 1 if x == self._alvo_decimal else 0

    # --------------------------------------------------
    # Execução da busca clássica não ordenada
    # --------------------------------------------------
    def executar(self, alvo_bits: str) -> None:
        """
        Executa a busca clássica não ordenada.
        O alvo é fornecido como string binária (ex: '01', '1011').
        """
        self._validar_alvo(alvo_bits)

        self._alvo_bits = alvo_bits
        self._num_bits = len(alvo_bits)
        self._espaco_busca = 2 ** self._num_bits
        self._alvo_decimal = int(alvo_bits, 2)

        start_time = time.perf_counter()

        encontrado = False
        posicao = None
        iteracoes = 0

        for x in range(self._espaco_busca):
            iteracoes += 1
            if self._oraculo(x) == 1:
                encontrado = True
                posicao = x
                break

        end_time = time.perf_counter()

        self._resultado = {
            "alvo_bits": self._alvo_bits,
            "alvo_decimal": self._alvo_decimal,
            "num_bits": self._num_bits,
            "espaco_busca": self._espaco_busca,
            "posicao_encontrada": posicao,
            "iteracoes": iteracoes,
            "execution_time": end_time - start_time,
            "encontrado": encontrado,
        }

    # --------------------------------------------------
    # Validação
    # --------------------------------------------------
    def _validar_alvo(self, alvo_bits: str) -> None:
        if not alvo_bits:
            raise ValueError("O alvo não pode ser vazio.")
        if not all(bit in "01" for bit in alvo_bits):
            raise ValueError("O alvo deve ser uma string binária (apenas 0 e 1).")

    # --------------------------------------------------
    # Getters (para Relatorio)
    # --------------------------------------------------
    def get_resultado(self) -> Dict[str, Any]:
        if self._resultado is None:
            raise RuntimeError("Busca clássica ainda não executada.")
        return self._resultado

    def get_execution_time(self) -> float:
        return self.get_resultado()["execution_time"]

    def get_num_bits(self) -> int:
        return self.get_resultado()["num_bits"]

    def get_espaco_busca(self) -> int:
        return self.get_resultado()["espaco_busca"]