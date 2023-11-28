# Perceptron e portas lógicas

1. Objetivo:
- Implementação de um perceptron capaz de ser treinado para reproduzir o comportamento das seguintes portas lógicas:
    1. AND
    2. OR
    3. NAND
    4. XOR

## Funcionamento do código

### Estrutura da Rede Neural
- A rede neural é um Perceptron simples com uma função de ativação degrau.
- Utiliza a biblioteca NumPy para manipulação de matrizes e cálculos vetoriais.

### Parâmetros do Perceptron
- **Pesos (`self.weights`):** Inicializados como um vetor de zeros.
- **Limiar (`self.threshold`):** Determina o ponto de ativação da função degrau.
- **Taxa de Aprendizado (`learning_rate`):** Controla o ajuste dos pesos durante o treinamento.
- **Viés (`self.bias`):** Utilizado para ajustar a saída da rede.

### Métodos Principais

#### `activation_function(self, x)`
- Implementa a função de ativação degrau, retornando 1 se o valor for maior ou igual ao limiar (`self.threshold`), caso contrário, retorna 0.

#### `predict(self, inputs)`
- Realiza a predição para um conjunto de entradas (`inputs`) calculando a combinação linear das entradas e pesos.
- Aplica a função de ativação para gerar a saída prevista.

#### `train(self, X, y)`
- Método de treinamento do Perceptron.
- Ajusta os pesos iterativamente com base nos erros entre a saída prevista e os resultados esperados (`y`) para o conjunto de dados de entrada (`X`).

## Testes das Portas Lógicas

O código realiza o treinamento do Perceptron para cada porta lógica (OR, AND, NAND, XOR) separadamente, utilizando conjuntos de dados de entrada e saída previstos para cada operação lógica.

## Teste da Porta Lógica XOR

Como o Perceptron é uma rede neural de uma única camada que utiliza da função de ativação simples, como a função degrau, para realização da separação linear entre a classe dos dados, não é possível ter um retorno como o esperado para a porta lógica XOR, pois esta não é linearmente separável, ou seja, não é possível separar as entradas usando uma linha reta. Dessa forma, ao tentar treinar o perceptron para aprender a porta lógica XOR, a separação linear da rede neural não é suficiente para alcançar os resultados esperados.

### Exemplo de Uso
- O Perceptron é treinado para cada operação lógica individualmente.
- Após o treinamento, são realizados testes para verificar as previsões do Perceptron para diferentes combinações de entradas.

## Como Utilizar
1. Execute o código Python.
2. Os resultados serão impressos no console, mostrando as saídas previstas para cada porta lógica e suas respectivas entradas.

## Vídeo:

