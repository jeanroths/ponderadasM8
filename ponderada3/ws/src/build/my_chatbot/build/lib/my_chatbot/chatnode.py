#! /bin/env python3
import rclpy
import re

class Chatbot():
    def __init__(self):
        super().__init__('chatbot')
        # Dicionário de intenções para enviar o robô para um ponto
        self.intent_dict = {
            r"\b(?:(?:[Vv][aá])|(?:[Mm]e leve at[eé]))\s(.+)": "move_to_point",
            r"\b(?:[Vv][aá] para a)\s(.+)": "move_to_point",
            r"\b(?:[Ee]ncaminhe-se para)\s(.+)": "move_to_point",
            r"\b(?:[Dd]irecione-se para)\s(.+)": "move_to_point",
            r"\b(?:[Dd]irija-se para)\s(.+)": "move_to_point",  
            r"([Tt]chau|[Aa]té logo|[Aa]té mais|[Aa]deus)": "turn_off",  
        }

        # Dicionário de ações do robô
        self.action_dict = {
            "move_to_point": lambda point: point,
        }

        self.destiny = None
        self.action = None


    def go_to(self):
        print(f'dirijindo-se {self.destiny}')

    def chatbot_prompt(self):
        while True:
            comando = input("Digite para onde deseja que o robô vá: ").lower().strip()
            self.action = self.chatbot_action(comando)
            if self.action == 'move_to_point':
                self.chat_responses(self.action, comando)
            else:
                self.chat_responses(self.action, None)

    def chat_responses(self, intent, command):
        if intent:
            if intent == 'move_to_point':
                for pattern, action in self.intent_dict.items():
                    match = re.search(pattern, command, re.IGNORECASE)
                    if match:
                        point = match.group(1)
                        self.destiny = self.action_dict[intent](point)
                        self.go_to()
                        return  # Sai da função após o movimento

            elif intent == 'turn_off':
                print('Até logo')
                exit()

        else:
            print('Desculpe mestre, não entendi o que disse')


    def chatbot_action(self, command):
        for pattern, action in self.intent_dict.items():
            match = re.search(pattern, command, re.IGNORECASE)
            if match:
                return action
        return None

def main(args=None):
    # rclpy.init(args=args)

    chatbot = Chatbot()
    chatbot.chatbot_prompt()
    # rclpy.spin(chatbot)

    # rclpy.shutdown()

if __name__ == '__main__':
    main()
