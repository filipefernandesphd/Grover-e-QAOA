# **Algoritmo de Grover**

Um dos problemas mais básicos em ciências da computação é a busca em base não estruturada. Basicamente o problema consiste em procurar um elemento em uma lista não ordenada. Classicamente a complexidade desse problema é dado em Big O notation por O(N). O algoritmo de Grover é capaz de reduzir essa complexidade para O(√N).

O algoritmo de Grover, ou pelo menos sua estrutura básica, é utilizado como sub-rotina de vários outros algoritmos quânticos, como por exemplo: amplitude amplification e amplitude estimation. Vale a pena entender a lógica de funcionamento e como construí-lo.

## Passo a Passo do Algoritmo

### 1. Superposição



## OBJETIVOS DE APRENDIZAGEM

- Implementar o código do algoritmo de Grover em Python;
- Explicar o papel do oráculo no algoritmo de Grover;
- Explicar limitações e aspectos de escalabilidade do algoritmo.

## Implementação

Implementar o algoritmo de Grover em **4 contextos distintos**, realizando medições e registros relevantes.

**CENÁRIO 1**: *2 qubits e 1 alvo*. Verificar se o estado alvo aparece com alta probabilidade nas medições

**CENÁRIO 2**: *16 qubits e 1 alvo*. Implementar também a busca clássica linear, percorrendo todos os estados de $0$ até $2^{16}-1$ $(65535)$ e comparar o tempo de execução

**CENÁRIO 3**: *maior número de qubits viável no seu ambiente*, com apenas um alvo. O objetivo aqui é observar os limites da simulação, verificando se ocorrem erros, lentidão ou travamentos.

**CENÁRIO 4**: *5 qubits e múltiplos alvos* (ex: os estados 3, 7 e 11). Avalie o impacto de múltiplas soluções sobre a fidelidade e a distribuição das medições. Calcule o número ideal de iterações ajustando a fórmula para $k > 1$
