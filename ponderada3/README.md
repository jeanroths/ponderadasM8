# Ponderada 3 - Criação de um chatbot simples

## 1. Enunciado:

Desenvolva um nó de ROS que seja um chatbot capaz de entender comandos escritos em linguagem natural para interagir com um robô de serviço fictício. O chatbot deve fornecer ao usuário a possibilidade de enviar comandos de posição para o robô de forma simples e intuitiva.
Para cada comando registrado, o sistema deve ser capaz de extrair a intenção do usuário a partir de um dicionário de intenções, filtradas por expressões regulares. A partir daí, um segundo dicionário deve ser usado, capaz de vincular intenções à funções que o robô deve executar. Para essa ponderada, o script em Python não precisa se comunicar com o nav2 e nem com o robô, mas é necessário dar um feedback ao usuário de que a ação foi compreendida e está sendo executada.

## 2. Padrão de entrega

Esses são os critérios mínimos para que eu considere a atividade como entregue. Fique atento, pois o não cumprimento de qualquer um desses critérios pode, no melhor dos casos, gerar um desconto de nota e, no pior deles, invalidar a atividade.

1. A atividade deve ser feita em um repositório aberto no github. Seu link deve ser fornecido no card da adalove;
2. O repositório deve contar com um workspace ROS2 com pelo menos um nó configurado: o do chatbot Sugere-se que utilize o mesmo workspace das outras atividades ponderadas.
3. No README do repositório deve ter instruções claras de como instalar e rodar o nó criado, com comandos em blocos de código e uma explicação sucinta do que fazem;
4. Ainda no README, deve haver um vídeo gravado demonstrando plenamente o funcionamento do nó criado;

## 3. Padrão de qualidade:

1. Comprovadamente ser capaz de compreender ao menos uma inteção do usuário: a de mandar o robô para um determinado ponto. Deve haver um dicionário de intenções e a intenção deve ser caputrada através de expressões regulares. Ao menos dois formatos diferentes devem ser considerados para a captura da intenção do usuário (e.g. "Vá para...", "Me leve até...") - até 4,0 pontos;
2. O script deve contar com um dicionário de ações, relacionando cada intenção com uma função a ser executada pelo robô - até 3,0 pontos;
3. O chatbot deve dar feedback ao usuário sobre a compreensão do que foi dito e a ação que será tomada - até 3,0 pontos.

## 4. Solução
Esta é uma aplicação de um nó do ROS 2 que interpreta comandos em linguagem natural fornecidos pelo usuário para controlar um robô. O nó usa expressões regulares para identificar as intenções do usuário e executa ações correspondentes no robô.

### Instalação:

```bash
# Clone o repositório
git clone https://github.com/jeanroths/ponderadasM8 

# Navegue até o diretório do pacote 
cd /ponderada3/ws_pond3/src/my_chatbot

# Instale as dependencias
rosdep install -i --from-path src --rosdistro humble -y

# Compile o pacote usando 
colcon build

# Para rodar o pacote é necessário dar source no script de configuração do workspace
source install/setup.bash #se estiver usando zsh, mudar para setup.zsh

```
#### Uso:
1. Execute o nó do ROS 2 para iniciar o chatbot:

```bash
ros2 run my_chatbot chatnode
```

2. O nó estará pronto para receber comandos do usuário.
3. Os comandos devem seguir as seguintes estruturas:

```bash 
"Vá para o ponto A"
"Me leve até o ponto B"
"Encaminhe-se para o ponto C"
...
```

#### Explicação do script do chat (nó):


- **Inicialização do Chatbot:**

    Define dicionários de intenções (intent_dict) e ações (action_dict) para interpretar comandos de movimento e outras interações.
    Inicializa variáveis para destino (destiny) e ação (action).

- **Método chatbot_prompt:**

    Inicia um loop para capturar os comandos do usuário via input() em lowercase.
    Verifica a ação a ser tomada através do método chatbot_action.
    Se a ação for movimento ('move_to_point'), chama o método chat_responses para lidar com a ação de mover o robô para o ponto especificado.
    Se a ação for 'turn_off', imprime uma despedida e encerra o programa.

- **Método chat_responses:**

    Recebe uma intenção e um comando.
    Se a intenção for movimento ('move_to_point'), utiliza expressões regulares para encontrar o ponto de destino no comando.
    Chama o método go_to() para mover o robô para o ponto específico.
    Se a intenção for desligar ('turn_off'), imprime uma despedida e encerra o programa.

- **Método chatbot_action:**

    Itera pelo dicionário de intenções (intent_dict) para encontrar correspondências entre o comando fornecido e as intenções definidas.
    Usa expressões regulares para verificar se há correspondência entre o comando e as intenções.

- **Método go_to:**

    Simula o movimento do robô para o ponto de destino especificado.

#### Funcionamento Geral:

O programa inicia a classe Chatbot e começa a aguardar comandos do usuário.
O usuário fornece um comando.
O chatbot verifica a intenção desse comando e executa a ação correspondente.
Se for um comando de movimento, o chatbot identifica o ponto de destino e simula o movimento do robô para esse ponto.
Se for um comando de desligamento, o chatbot encerra o programa.

O código utiliza expressões regulares para corresponder padrões nos comandos fornecidos, e as ações são mapeadas por meio de dicionários para responder às intenções específicas do usuário.


### Vídeo:

<a href="https://youtu.be/_LZW9dXkOOI">vídeo do nó chatbot funcionando</a>
