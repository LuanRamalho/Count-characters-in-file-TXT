import tkinter as tk
from tkinter import messagebox
import os

def contar_caracteres_em_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
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

def verificar_arquivo():
    nome = entrada_arquivo.get()
    if not nome:
        messagebox.showwarning("Atenção", "Digite o nome do arquivo!")
        return
    contar_caracteres_em_arquivo(nome)

# Janela principal
janela = tk.Tk()
janela.title("Contador de Caracteres")
janela.geometry("400x250")
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
    width=30,
    bg="#ffffff",
    fg="#000000",
    relief="groove",
    borderwidth=3
)
entrada_arquivo.pack(pady=5)
entrada_arquivo.insert(0, "exemplo.txt")  # valor padrão

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
