# ============================================================
# Relatório comparativo de desempenho
#
# Desenvolvido por Filipe Fernandes
# ============================================================

import matplotlib.pyplot as plt


class Relatorio:
    """
    Classe responsável por apresentar informações de ambiente,
    relatórios de desempenho e gráficos comparativos entre
    simulação quântica (Grover) e busca linear clássica.
    """

    # --------------------------------------------------
    # Informações do ambiente
    # --------------------------------------------------
    def ambiente(self, simulacao):
        env = simulacao.get_env_info()

        print("\n================ AMBIENTE DE EXECUÇÃO ================\n")

        sys = env["system_info"]
        print("💻 Sistema")
        print(f"- Sistema Operacional: {sys['sistema_operacional']}")
        print(f"- Arquitetura: {sys['arquitetura']}")
        print(f"- Processador: {sys['processador']}")
        print(f"- Núcleos físicos: {sys['nucleos_fisicos']}")
        print(f"- Núcleos lógicos: {sys['nucleos_logicos']}")
        print(f"- Memória RAM: {sys['memoria_ram_gb']} GB")

        print("\n🔧 Backend Quântico")
        print(f"- Backend: {env['backend_name']}")
        print(f"- GPU disponível: {'SIM' if env['gpu_available'] else 'NÃO'}")
        print(f"- Execução usando GPU: {'SIM' if env['using_gpu'] else 'NÃO'}")

        if env["gpu_available"]:
            print("- Backends GPU detectados:")
            for b in env["gpu_backends"]:
                print(f"  • {b}")

        print("\n======================================================\n")


    def relatorio(self, simulacao, classica):
        print("\n================ RELATÓRIO DE DESEMPENHO ================\n")

        # ======================================================
        # ALGORITMO DE GROVER (SIMULAÇÃO QUÂNTICA)
        # ======================================================
        print("⚛️ ALGORITMO DE GROVER (SIMULAÇÃO QUÂNTICA)\n")

        num_qubits = simulacao.get_num_qubits()
        espaco_busca = 2 ** num_qubits
        env = simulacao.get_env_info()

        print(f"- Número de qubits: {num_qubits}")
        print(f"- Espaço de busca: {espaco_busca}")

        for execucao in simulacao.get_execucoes():
            shots = execucao["shots"]
            tempo = execucao["execution_time"]
            counts = execucao["counts"]

            estado_alvo = max(counts, key=counts.get)

            # Indicadores estruturais do circuito
            # (assumindo circuito de Grover fixo por execução)
            total_portas = "N/A (não armazenado)"
            profundidade = "N/A (não armazenado)"
            num_iteracoes = "k (definido na construção do circuito)"

            print("\nExecução:")
            print(f"  • Estado alvo: {estado_alvo}")
            print(f"  • Shots: {shots}")
            print(f"  • Tempo (s): {tempo:.6f}")
            print(f"  • Número de iterações (Grover): {num_iteracoes}")
            print(f"  • Total de portas: {total_portas}")
            print(f"  • Profundidade do circuito: {profundidade}")

        print("\n- Backend:", env["backend_name"])
        print(f"- Uso de GPU: {'SIM' if env['using_gpu'] else 'NÃO'}")

        # ======================================================
        # BUSCA LINEAR CLÁSSICA
        # ======================================================
        print("\n🖥️ BUSCA LINEAR CLÁSSICA\n")

        r = classica.get_resultado()

        print(f"- Número de bits: {r['num_bits']}")
        print(f"- Espaço de busca: {r['espaco_busca']}")
        print(f"- Estado alvo: {r['alvo_bits']}")
        print(f"- Tempo (s): {r['execution_time']:.6f}")
        print(f"- Número de iterações: {r['iteracoes']}")

        print("\n=========================================================\n")

    # --------------------------------------------------
    # Gráficos comparativos
    # --------------------------------------------------
    def graficos(self, simulacao, classico):
        execucoes = simulacao.get_execucoes()

        shots = [e["shots"] for e in execucoes]
        tempos_quanticos = [e["execution_time"] for e in execucoes]

        tempo_classico = classico.get_execution_time()

        # ---------- Gráfico 1: Tempo x Shots (Quântico) ----------
        plt.figure()
        plt.plot(shots, tempos_quanticos, marker="o")
        plt.xlabel("Número de shots")
        plt.ylabel("Tempo de execução (s)")
        plt.title("Desempenho da Simulação Quântica (Grover)")
        plt.grid(True)
        plt.show()

        # ---------- Gráfico 2: Comparação Clássico x Quântico ----------
        plt.figure()

        plt.bar(
            ["Busca Clássica", "Grover (Simulado)"],
            [tempo_classico, min(tempos_quanticos)],
        )

        plt.ylabel("Tempo de execução (s)")
        plt.title("Comparação de Desempenho: Clássico × Quântico")
        plt.grid(axis="y")
        plt.show()