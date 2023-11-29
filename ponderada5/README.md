# Construção de um chatbot com LLM e RAG

1. Objetivo
Melhoria do chatbot desenvolvido na ponderada anterior, agora utilizando técnicas de leitura de documentos.

2. Enunciado
Utilizando um LLM (local ou API externa), crie um chatbot simples com instruções customizadas para ajudar um usuário a pesquisar normas de segurança em ambientes industriais. O sisema deve contar com uma interface gráfica e responder de forma sucinta e clara sobre o que lhe foi perguntado. O sistema ainda deve ser capaz de contextualizar suas respostas a partir do seguinte documento:

<a href= "https://www.deakin.edu.au/students/study-support/faculties/sebe/abe/workshop/rules-safety"> Workshop rules and safety considerations </a>

# Solução

## Guia de Instalação

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

 Depois certifique-se de ter instalados as dependências da ponderada 4, e instale o Chroma:
 ```bash
 pip install Chroma
 ```
Depois da instalação do Ollama como dependência, instalar um modelo de Ollama específico: 
```bash
ollama run llama2 
```
Nesse caso o modelo é o `llama2` mas poderia ser também outro modelo como o `mistral`. (O modelo `llama2` exigiu uma capacidade de processamento muito alta para devolver a resposta na aplicação).

### Explicação (jedibot_txt_reader)

1. Função load_archive_and_vectorize()

Esta função realiza várias etapas:

- Carregamento de Documentos: Carrega documentos a partir de um arquivo de texto (text.txt).
- Divisão de Texto: Divide os documentos em trechos menores usando CharacterTextSplitter.
- Extração de Embeddings: Usa SentenceTransformerEmbeddings para extrair embeddings dos documentos.
- Criação do Vector Store: Utiliza chroma.Chroma para criar um vetor de armazenamento com base nos embeddings extraídos.
- Criação do Retriever: Configura um RetrievalQA com base no tipo de cadeia (chain_type="stuff") e no vetor de armazenamento.

2. Função run_ollama(input_text)

Esta função é a peça central do bot:

- Configuração do Prompt: Cria um prompt de chat específico para Yoda em português para interagir com o usuário.
- Chamada da Função load_archive_and_vectorize(): Carrega e prepara os dados necessários para o bot responder às consultas.
- Criação da Cadeia de Processamento: Define uma cadeia de processamento que consiste em recuperar a atividade do retriever e passar para o prompt e, em seguida, para o Ollama.
- Processamento do Texto de Entrada: Envia o texto de entrada para a cadeia de processamento, capturando as respostas e exibindo-as ao usuário.

3. Configuração da Interface Gráfica

Usa o gr.Interface para configurar a interface do usuário com a função run_ollama.

## Vídeo 

<a href ="https://youtu.be/YJ7B9SUD4bA"> Vídeo do funcionamento do chatbot </a>