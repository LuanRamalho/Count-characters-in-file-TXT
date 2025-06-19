import tkinter as tk
from tkinter import messagebox, filedialog
import os

def contar_caracteres_em_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='latin-1') as arquivo:
            conteudo = arquivo.read()
            quantidade = len(conteudo)
            resultado_label.config(
                text=f"Total de caracteres: {quantidade}",
                fg="#ffffff",
                bg="#32a852"
            )
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo não encontrado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def selecionar_arquivo():
    caminho = filedialog.askopenfilename(
        title="Selecione um arquivo de texto",
        filetypes=[("Arquivos de texto", "*.txt")]
    )
    if caminho:
        entrada_arquivo.delete(0, tk.END)
        entrada_arquivo.insert(0, caminho)

def verificar_arquivo():
    nome = entrada_arquivo.get()
    if not nome or not os.path.isfile(nome):
        messagebox.showwarning("Atenção", "Selecione um arquivo válido!")
        return
    contar_caracteres_em_arquivo(nome)

# Janela principal
janela = tk.Tk()
janela.title("Contador de Caracteres")
janela.geometry("500x280")
janela.configure(bg="#282c34")

# Título
titulo = tk.Label(
    janela,
    text="CONTADOR DE CARACTERES EM TXT",
    font=("Arial", 14, "bold"),
    bg="#282c34",
    fg="#61dafb"
)
titulo.pack(pady=10)

# Entrada do nome do arquivo
entrada_arquivo = tk.Entry(
    janela,
    font=("Arial", 12),
    width=40,
    bg="#ffffff",
    fg="#000000",
    relief="groove",
    borderwidth=3
)
entrada_arquivo.pack(pady=5)

# Botão para selecionar arquivo
botao_selecionar = tk.Button(
    janela,
    text="Selecionar Arquivo",
    font=("Arial", 10, "bold"),
    bg="#f0ad4e",
    fg="#000000",
    command=selecionar_arquivo
)
botao_selecionar.pack(pady=5)

# Botão para contar
botao = tk.Button(
    janela,
    text="Contar Caracteres",
    font=("Arial", 12, "bold"),
    bg="#61dafb",
    fg="#000000",
    activebackground="#21a1f1",
    relief="raised",
    command=verificar_arquivo
)
botao.pack(pady=10)

# Resultado
resultado_label = tk.Label(
    janela,
    text="",
    font=("Arial", 12, "bold"),
    bg="#282c34",
    fg="#ffffff"
)
resultado_label.pack(pady=20)

# Executa a interface
janela.mainloop()
