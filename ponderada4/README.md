# Enunciado - Construção de um Chatbot com LLM:

Utilizando um LLM (local ou API externa), crie um chatbot simples com instruções customizadas para ajudar um usuário a pesquisar normas de segurança em ambientes industriais. O sistema deve contar com uma interface gráfica e responder de forma sucinta e clara sobre o que lhe foi perguntado.

# Padrão de entrega:

1. A atividade deve ser feita em um repositório aberto no github. Seu link deve ser fornecido no card da adalove;
2. No README do repositório deve ter instruções claras de como instalar e rodar o sistema criado, comandos em blocos de código e uma expliação sucinta do que fazem;
3. Ainda no README, deve haver um vídeo gravado demonstrando plenamente o funcionamento do nó criado;

# Padrão de qualidade:

1. Utilizar o langchain para criar a interface com o modelo de LLM utilizado (pode ser openAI ou modelos do huggingface/ollama) - até 4,0 pontos;
2. Utilizar o gradio para criar uma interface gráfica simples para o chatbot - até 3,0 pontos;
3. Responder de forma concisa aos prompts do usuário. Para isso, deve-se criar um prompt de sistema que contextualiza todas as respostas do modelo utilizado - até 3,0 pontos.

# Resolução:

## Guia de instalação 

Primeiramente, certifique-se de ter o Conda instalado no seu computador ou crie uma Venv:

```bash
python3 -m venv venv
```

Ative o ambiente virtual:
 1. Linux:
 ```bash
 source venv/bin/activate
 ```

 2. Windows:
 ```bash
 ./venv/Scripts/activate
 ```

 Depois instale as dependências do arquivo "requirements.txt":
 ```bash
 pip install -r requirements.txt
 ```
Depois da instalação do Ollama como dependência, é necessário criar um modelo LLM com o comando: 
```bash
ollama create <nome-do-modelfile> 
```
Nesse caso o Modelfile é o jedibot.

 ## Explicação (jedibot.py):

- **Configuração Inicial:**
  - Importação de bibliotecas essenciais, incluindo `Ollama` e `gradio`.
  - Configuração da conexão com um servidor local onde o modelo 'jedibot' está hospedado.

- **Configuração do Ollama e Prompt:**
  - Utilização da classe `ChatPromptTemplate` para criar um template de conversação, onde o bot atua como Yoda respondendo sobre padrões de segurança em ambientes industriais em português brasileiro.

- **Cadeia de Processamento (Chain of Responsibility):**
  - Definição de uma sequência de processamento (`chain`) que conecta a entrada do usuário à lógica do modelo Ollama, passando pela prompt de conversação e pela entrada de atividade.

- **Função de Execução do Ollama:**
  - `run_ollama` é a função principal que envia solicitações para o Ollama, processa as respostas em um loop e as envia de volta para a interface do usuário. Trata possíveis erros durante o processamento.

- **Configuração da Interface Gráfica:**
  - Utilização do `gr.Interface` para criar uma interface onde os usuários podem digitar texto para interagir com o bot e receber respostas sobre segurança industrial. Configurações de título, descrição e tipo de entrada/saída são definidas.

- **Lançamento da Interface:**
  - No final, a interface é lançada para permitir que os usuários interajam com o bot.

## Vídeo:
<a href="https://youtu.be/iMj63Bhj7tA"> Chatbot com LLM e Gradio Interface</a>