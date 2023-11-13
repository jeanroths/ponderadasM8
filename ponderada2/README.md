# Ponderada 2 - Navegação com o turtlebot

## 1. Objetivo:

Interagir de forma programática com o stack de navegação do ROS

## 2. Enunciado:

Desenvolva um pacote em ROS com as funcionalidades de mapeamento e navegação utilizando o turtlebot 3 (simulado ou real)

## 3. Padrão de entrega:

Esses são os critérios mínimos para que eu considere a atividade como entregue. Fique atento, pois o não cumprimento de qualquer um desses critérios pode, no melhor dos casos, gerar um desconto de nota e, no pior deles, invalidar a atividade.

- A atividade deve ser feita em um repositório aberto no github. Seu link deve ser fornecido no card da adalove;
    
- O repositório deve contar com um workspace ROS2 com pelo menos um pacote configurado. Deverá haver ao menos dois lançadores: um que lança todo o necessário para o mapeamento e outro que lança todo o necessário para navegação;

- No README do repositório deve ter instruções claras de como instalar e rodar o pacote criado, com comandos em blocos de código e uma explicação sucinta do que fazem;

- Ainda no README, deve haver um vídeo gravado demonstrando plenamente o funcionamento do sistema completo, mostrando tanto o mapeamento quanto a navegação.

## 4. Padrão de qualidade:

O sistema desenvolvido deve:

1. Comprovadamente ser capaz de mapear de forma fidedigna um ambiente (simulado ou real) - até 3,0 pontos;

2. Ser capaz de navegar em um ambiente pré-mapeado de forma programática - até 3,0 pontos;

3. Ser capaz de desviar de obstáculos de forma dinâmica (obstáculos não mapeados) - até 3,0 pontos;

4. O sistema deve ser idempotente. Isso significa, na prática, que mesmo rodando várias vezes o navegador, ele vai passar pelos mesmos pontos (sem tentar inicializar a pose duas vezes) - até 1,0 ponto;

## 5. Solução:

Este é um pacote ROS2 que integra o Turtlebot3 com o Gazebo, RViz e o Cartographer para mapeamento. Além disso, inclui um script Python para navegação programática do robô.

### Instalação:

```bash
# Clone o repositório
git clone https://github.com/jeanroths/ponderadasM8 

# Navegue até o diretório do pacote 
cd /ponderada2/ws_pond2/src/my_turtlebot3_mapping

# Instale as dependencias
rosdep install -i --from-path src --rosdistro humble -y

# Compile o pacote usando 
colcon build

# Para rodar o pacote é necessário dar source no script de configuração do workspace
source install/setup.bash #se estiver usando zsh, mudar para setup.zsh

```

### Como rodar:

Execute o primeiro lançador de Mapeamento dentro do pacote no diretorio launch:
```bash
cd /ponderada2/ws_pond2/src/my_turtlebot3_mapping/launch
ros2 launch turtlebot3_mapping.launch.py
```

Após isso, o RViz, Gazebo e o Teleop serão executados para que o mapeamento seja feito, e após o fechamento do terminal com o teleop, o mapa criado será salvo localmente no diretório launch.

Após isso, execute o segundo lançador de Navegação dentro do pacote no diretório launch:
```bash
ros2 launch turtlebot3_navigation.launch.py
```
Feito isso, o RViz, Gazebo e o nó com o script de navegação do pacote serão ativados e o robô irá passar do seu ponto inicial (0.0, 0.0, 0.0), para os pontos programados (4.0, 1.25, -0.00143).

### Vídeos:
<a href='https://youtu.be/THB993_EkHQ'>Vídeo do Launcher Mapeamento</a>

<a href='https://youtu.be/p_pt2SLE6_E'>Vídeo do Launcher Navegação</a>

