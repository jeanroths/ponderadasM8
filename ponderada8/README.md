# Ponderada 8 - Tradutor Speech-to-text e Text-to-speech

Crie uma ferramenta de terminal capaz de receber como argumento o caminho para um arquivo de áudio contendo a fala de uma pessoa. Após ler o arquivo fornecido, a sua aplicação deve ser capaz de transformar o áudio em texto corretamente, usar esse texto gerado para alimentar um tradutor de texto (e.g. transforma um texto do português para o inglês) e, por fim, transforma o texto traduzido em áudio novamente e reproduz para o usuário.

# Solução:

# Transcrição de Áudio e Tradução com Python

Este é um script que utiliza bibliotecas como `speech_recognition`, `googletrans` e `gtts` para realizar a transcrição de áudio, tradução do texto resultante e reprodução do texto traduzido como áudio.

## Funcionalidades do Script

### `transcribe_translate_speak(audio_path)`

Esta é a função principal do script, responsável por coordenar todo o processo de transcrição, tradução e reprodução.

#### `transcribe_audio(audio_path)`

Função interna que utiliza a biblioteca `speech_recognition` para realizar a transcrição de áudio em texto. Caso o arquivo de áudio seja legível e contenha fala, o texto reconhecido é retornado. Caso contrário, mensagens de erro apropriadas são retornadas.

#### `translate_text(text)`

Função que utiliza a biblioteca `googletrans` para traduzir o texto reconhecido de português para inglês.

#### `speak_text(text)`

Função que utiliza a biblioteca `gtts` para converter o texto traduzido em áudio (voz) no idioma inglês e reproduzi-lo para o usuário.

### Execução do Script

### Instalação:

Certifique-se de ter instalado as dependencias do `requirements.txt` com o comando `pip install -r requirements.txt`

### Execução:

O script pode ser executado a partir do terminal, fornecendo o caminho para o arquivo de áudio como argumento:
```bash
python3 TTS_translator.py caminho_para_o_arquivo_de_audio
```

O script verificará se o arquivo de áudio está presente e seguirá com o processo de transcrição, tradução e reprodução.

Caso o arquivo fornecido não seja legível ou não contenha fala, mensagens indicativas serão exibidas.

## Vídeo:
