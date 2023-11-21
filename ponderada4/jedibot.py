from langchain.llms import Ollama
import gradio as gr

ollama = Ollama(base_url='http://localhost:11434', model='jedibot')

def run_ollama(input_text, chat_history):
    response = ollama(input_text)
    chat_history.append((input_text, response))
    return "", chat_history


interface = gr.Blocks()

with interface:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])
    msg.submit(run_ollama, inputs=[msg, chatbot], outputs=[msg, chatbot])

print("Master Yoda wants to talk to you...")
interface.launch()

