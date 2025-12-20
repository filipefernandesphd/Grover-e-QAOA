# ============================================================
# Contrução do circuito quântico do algoritmo Grover
# 
# Desenvolvido por Filipe Fernandes [filipe.fernandes@ifsudestemg.edu.br]
# ============================================================

from qiskit import QuantumCircuit

class Grover:
    def __init__(self, target:str, reversebits: bool = False):        
        # String do bit alvo a ser encontrado pelo Grover
        self.__target = target 

        # Retorna a quantidade de qubits
        self.__n_qubits = len(self.__target)

        # Se inverterá os bits para melhorar a leitura
        self.__reversebits = reversebits

    def circuit(self):
        self.__criar_circuito()
        self.__oraculo()
        self.__difusor()
        self.__medir()
        return self.__qc

    def __criar_circuito(self):
        # Cria o circuito quantico
        self.__qc = QuantumCircuit(self.__n_qubits, self.__n_qubits)

        # Aplica hadamard
        for i in range(self.__n_qubits):
            self.__qc.h(i)
        
        self.__qc.barrier()

    def __oraculo(self):
        """
        Implementa o oráculo de Grover para um único estado alvo.
        """
        # 1. Aplicar X nos qubits cujo alvo é '0'
        for i, bit in enumerate(self.__target):
            if bit == '0':
                self.__qc.x(i)

        # 2. Aplicar Z controlado (caso geral)
        if self.__n_qubits == 1:
            self.__qc.z(0)
        elif self.__n_qubits == 2:
            self.__qc.cz(0, 1)
        else:
            # multi-controlled Z usando H + MCX + H
            self.__qc.h(self.__n_qubits - 1)
            self.__qc.mcx(list(range(self.__n_qubits - 1)), self.__n_qubits - 1)
            self.__qc.h(self.__n_qubits - 1)

        # 3. Desfazer os X
        for i, bit in enumerate(self.__target):
            if bit == '0':
                self.__qc.x(i) 

        self.__qc.barrier()    

    def __difusor(self):
        """
        Aplica o operador difusor de Grover no circuito self.__qc,
        adaptado automaticamente ao número de qubits self.__n_qubits.
        """

        n = self.__n_qubits

        # 1. Hadamard em todos os qubits
        self.__qc.h(range(self.__n_qubits))

        # 2. X em todos os qubits
        self.__qc.x(range(self.__n_qubits))

        # 3. Inversão de fase do estado |11...1>
        if self.__n_qubits == 1:
            self.__qc.z(0)

        elif self.__n_qubits == 2:
            self.__qc.cz(0, 1)

        else:
            # Multi-controlled Z:
            # H no último qubit + MCX + H
            self.__qc.h(self.__n_qubits - 1)
            self.__qc.mcx(list(range(n - 1)), self.__n_qubits - 1)
            self.__qc.h(self.__n_qubits - 1)

        # 4. X em todos os qubits
        self.__qc.x(range(self.__n_qubits))

        # 5. Hadamard em todos os qubits
        self.__qc.h(range(self.__n_qubits))

        self.__qc.barrier()

    def __medir(self):
        if(self.__reversebits):
            """
            Função com o obejtivo de medir e inverter a ordem os bits clássicos para facilitar a leitura

            :param qc: circuito quântico
            """
            # Mapeamento manual na medição para simular Big-Endian
            for i in range(self.__n_qubits):
                self.__qc.measure(i, self.__n_qubits - 1 - i)
        else:
            self.__qc.measure_all()