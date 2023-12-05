# Classificação MNIST - Classificação de Dígitos Manuscritos usando Rede Neural Convolucional (CNN)

1. Objetivo

Treinar e utilizar uma rede neural convolucional para classificar corretamente o dataset MNIST.

2. Padrão de qualidade

- O sistema implementa uma arquitetura válida de rede neural convolucional. - até 6,0 pontos;
- O sistema apresenta acurácia maior que 95% no dataset MNIST (conjunto de treino) com apenas 3 épocas. - até 4,0 pontos.

# Solução

Como pedido, foi feito um modelo de Rede Neural Convolucional (CNN) implementando Keras/TensorFlow para classificar dígitos manuscritos do conjunto de dados MNIST.

## Conjunto de dados MNIST

O conjunto de dados MNIST é um conjunto padrão para aprender técnicas de reconhecimento de imagem e é composto por 60.000 imagens de treinamento e 10.000 imagens de teste, cada uma representando dígitos manuscritos de 0 a 9 em imagens grayscale de 28x28 pixels.

## Arquitetura da Rede Neural

A arquitetura da CNN utilizada é composta por:

- Camadas Convolucionais: A rede possui três camadas convolucionais, com 32, 64 e 64 filtros, respectivamente, usando ativação ReLU e tamanho de filtro 3x3.
- Camadas de Pooling: Entre as camadas convolucionais, são aplicadas camadas de max pooling de tamanho 2x2 para reduzir a dimensionalidade.
- Camadas Densas: Após as camadas convolucionais, há uma camada Flatten para transformar os dados em um vetor unidimensional, seguida por duas camadas densas, uma com 64 neurônios e ativação ReLU, e outra com 10 neurônios de saída usando ativação softmax para classificação de 10 classes (dígitos de 0 a 9).

## Funcionalidades do código

### Carregamento e pré-processamento 

- <code>keras.datasets.mnist.load_data()</code>: Carrega o conjunto de dados MNIST, dividindo-o em dados de treinamento e teste.
- <code> reshape() e astype()</code>: Reorganiza as imagens para o formato adequado (28x28 pixels com um canal para imagens em escala de cinza) e normaliza os valores de pixel para o intervalo [0, 1].
- <code> to_categorical()</code>: Converte os rótulos para o formato de categoria one-hot para serem usados na classificação.

### Definição da Arquitetura da Rede Neural

- <code>keras.Sequential()</code>: Cria um modelo sequencial onde as camadas são empilhadas sequencialmente.
- **Camadas Convolutivas e de Pooling**: Define camadas convolucionais com ativação ReLU seguidas por camadas de max pooling para redução de dimensionalidade.
- **Camadas Densas**: Após as camadas convolucionais, há uma camada Flatten para transformar os dados em um vetor unidimensional e duas camadas densas para classificação.

### Compilação e Treinamento do Modelo

- <code>complie()</code>: Configura o modelo para treinamento, especificando o otimizador, a função de perda e as métricas a serem utilizadas.
- <code>fit()</code>: Treina o modelo utilizando os dados de treinamento, especificando o número de épocas, o tamanho do lote e os dados de validação.

### Avaliação do Modelo

- <code>evaluate()</code>: Avalia o modelo usando os dados de teste e retorna a perda e a precisão do modelo.

### Predição e Visualização

- <code>predict()</code>: Realiza a predição das classes para os dados de teste.
- <code>plt.imshow()</code>: Mostra uma imagem do conjunto de teste usando Matplotlib.

## Guia de execução

1. Instale o TensorFlow e Keras
```bash
pip install tensorflow keras
```
2. Abra o Jupyter Notebook ou o Google Colab e execute o código presente na solução

## Vídeo

<a href="https://youtu.be/7m_EJxijA3c"> Aqui está a demonstração do funcionamento do código </a>