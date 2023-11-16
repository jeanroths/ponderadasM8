import rclpy
import re

# Dicionário de intenções para enviar o robô para um ponto
intent_dict = {
    r"\b(?:(?:[Vv][aá])|(?:[Mm]e leve at[eé]))\s(.+)": "move_to_point",
    r"\b(?:[Vv][aá] para)\s(.+)": "move_to_point",
    r"\b(?:[Ee]ncaminhe-se para)\s(.+)": "move_to_point",
    r"\b(?:[Dd]irecione-se para)\s(.+)": "move_to_point",
    r"\b(?:[Dd]irija-se para)\s(.+)": "move_to_point",
}

# Dicionário de ações do robô
action_dict = {
    "move_to_point": lambda point: f"dirigindo-se para {point}",
}

comando = input("Digite para onde deseja que o robô vá: ")

def chatbot_prompt(command):
    command = command.lower().strip()
    for pattern, action in intent_dict.items():
        match = re.search(pattern, command, re.IGNORECASE)
        if match:
            result = action_dict[action](match.group(1))
            return result
    return "Desculpe, não entendi. Poderia me dizer para onde devo ir novamente, mestre?"

def main():
    rclpy.init()

    resultado = chatbot_prompt(comando)
    print(resultado)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
