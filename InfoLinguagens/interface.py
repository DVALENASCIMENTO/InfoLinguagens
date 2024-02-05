# interface.py
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext  # Importe adicionado para um campo de texto com rolagem
from linguagens_de_programacao import linguagens

class InterfaceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("InfoLinguagens App")
        self.root.geometry("600x500")  # Defina as dimensões da janela principal

        # Adicionado um estilo para melhorar a aparência
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#ccc")
        style.configure("TCombobox", fieldbackground="#fff")

        self.label = ttk.Label(root, text="Selecione uma linguagem:", font=("Arial", 12))
        self.label.pack(pady=10)

        self.combo = ttk.Combobox(root, values=list(linguagens.keys()), font=("Arial", 11), state="readonly")
        self.combo.pack(pady=10)

        self.button = ttk.Button(root, text="Obter Informações", command=self.mostrar_informacoes)
        self.button.pack(pady=10)

        # Adicionado um campo de texto com rolagem para melhorar a exibição das informações
        self.resultado_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=30, font=("Arial", 11))
        self.resultado_text.pack(pady=10)

    def mostrar_informacoes(self):
        linguagem_selecionada = self.combo.get()
        if linguagem_selecionada:
            linguagem = linguagens.get(linguagem_selecionada)
            if linguagem:
                informacoes = f"Informações sobre {linguagem_selecionada}:\n"
                for chave, valor in linguagem.obter_informacoes().items():
                    informacoes += f"{chave}: {valor}\n"
                self.resultado_text.delete(1.0, tk.END)  # Limpa o campo de texto antes de adicionar novas informações
                self.resultado_text.insert(tk.END, informacoes)
            else:
                self.resultado_text.delete(1.0, tk.END)
                self.resultado_text.insert(tk.END, "Linguagem não encontrada.")
        else:
            self.resultado_text.delete(1.0, tk.END)
            self.resultado_text.insert(tk.END, "Por favor, selecione uma linguagem.")

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceApp(root)
    root.mainloop()


