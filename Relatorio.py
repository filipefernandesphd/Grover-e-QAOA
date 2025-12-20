from qiskit import transpile
from qiskit_aer import AerSimulator, Aer
import platform
import psutil
import time

class Relatorio:
    def __init__(self):
        pass
    
    def executar_circuito(qc, shots=1024):
        """
        Executa o circuito quântico e mede o tempo de execução.
        Retorna o resultado e o tempo total.
        """
        simulator = AerSimulator()

        qc_transpiled = transpile(qc, simulator)

        start_time = time.perf_counter()
        job = simulator.run(qc_transpiled, shots=shots)
        result = job.result()
        end_time = time.perf_counter()

        execution_time = end_time - start_time

        return {
            "result": result,
            "execution_time": execution_time,
            "backend": simulator
        }

    def coletar_info_ambiente(simulator):
        """
        Coleta informações do backend e do ambiente de execução.
        """
        backend_name = simulator.name

        gpu_backends = [
            backend.name for backend in Aer.backends()
            if "gpu" in backend.name.lower()
        ]

        gpu_available = len(gpu_backends) > 0
        using_gpu = getattr(simulator.options, "device", "CPU") == "GPU"

        system_info = {
            "Sistema Operacional": platform.system(),
            "Arquitetura": platform.machine(),
            "Processador": platform.processor(),
            "Núcleos físicos": psutil.cpu_count(logical=False),
            "Núcleos lógicos": psutil.cpu_count(logical=True),
            "Memória RAM (GB)": round(psutil.virtual_memory().total / (1024**3), 2),
        }

        return {
            "backend_name": backend_name,
            "gpu_available": gpu_available,
            "using_gpu": using_gpu,
            "gpu_backends": gpu_backends,
            "system_info": system_info
        }
    
    def gerar_relatorio_desempenho(
        num_qubits,
        shots,
        execution_time,
        env_info
    ):
        print("\n================ RELATÓRIO DE DESEMPENHO ================\n")

        print("⚛️ Circuito Quântico")
        print(f"- Número de qubits: {num_qubits}")
        print(f"- Shots: {shots}")

        print("\n⏱️ Tempo de Execução")
        print(f"- Tempo total: {execution_time:.6f} segundos")

        print("\n🔧 Backend Qiskit")
        print(f"- Backend em uso: {env_info['backend_name']}")
        print(f"- GPU disponível no sistema: {'SIM' if env_info['gpu_available'] else 'NÃO'}")
        print(f"- Execução usando GPU: {'SIM' if env_info['using_gpu'] else 'NÃO'}")

        if env_info["gpu_available"]:
            print("- Backends GPU detectados:")
            for b in env_info["gpu_backends"]:
                print(f"  • {b}")

        print("\n💻 Ambiente de Execução")
        for k, v in env_info["system_info"].items():
            print(f"- {k}: {v}")

        print("\n=========================================================\n")