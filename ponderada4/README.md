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