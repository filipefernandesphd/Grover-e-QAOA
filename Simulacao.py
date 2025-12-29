# ============================================================
# Execução simulada de circuito quântico
# 
# Desenvolvido por Filipe Fernandes [filipe.fernandes@ifsudestemg.edu.br]
# ============================================================
from qiskit import transpile
from qiskit_aer import AerSimulator, Aer
import platform
import psutil
import time
from typing import List, Dict, Any


class Simulacao:
    """
    Executa um circuito quântico em ambiente simulado para
    diferentes valores de shots e armazena os dados de desempenho.
    """

    def __init__(self):
        self._num_qubits: int | None = None
        self._execucoes: List[Dict[str, Any]] = []
        self._env_info: Dict[str, Any] | None = None

    # --------------------------------------------------
    # Execução das simulações
    # --------------------------------------------------
    def executar(self, qc, lista_shots: List[int]) -> None:
        """
        Executa o circuito quântico para cada valor de shots
        fornecido e armazena os resultados.
        """
        self._num_qubits = qc.num_qubits
        simulator = AerSimulator()
        self._env_info = self._coletar_info_ambiente(simulator)

        for shots in lista_shots:
            # qc_transpiled = transpile(qc, simulator)
            start_time = time.perf_counter()
            job = simulator.run(qc, shots=shots)
            result = job.result()
            end_time = time.perf_counter()

            self._execucoes.append({
                "shots": shots,
                "execution_time": end_time - start_time,
                "counts": result.get_counts(),
                "backend_name": simulator.name
            })

    # --------------------------------------------------
    # Coleta de informações do ambiente
    # --------------------------------------------------
    def _coletar_info_ambiente(self, simulator: AerSimulator) -> Dict[str, Any]:
        backend_name = simulator.name

        gpu_backends = [
            backend.name for backend in Aer.backends()
            if "gpu" in backend.name.lower()
        ]

        return {
            "backend_name": backend_name,
            "gpu_available": len(gpu_backends) > 0,
            "using_gpu": getattr(simulator.options, "device", "CPU") == "GPU",
            "gpu_backends": gpu_backends,
            "system_info": {
                "sistema_operacional": platform.system(),
                "arquitetura": platform.machine(),
                "processador": platform.processor(),
                "nucleos_fisicos": psutil.cpu_count(logical=False),
                "nucleos_logicos": psutil.cpu_count(logical=True),
                "memoria_ram_gb": round(psutil.virtual_memory().total / (1024**3), 2),
            }
        }

    # --------------------------------------------------
    # Getters (para Relatorio)
    # --------------------------------------------------
    def get_num_qubits(self) -> int:
        return self._num_qubits

    def get_execucoes(self) -> List[Dict[str, Any]]:
        return self._execucoes

    def get_env_info(self) -> Dict[str, Any]:
        return self._env_info