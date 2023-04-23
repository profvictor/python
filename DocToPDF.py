import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from docx2pdf import convert

# Crie a janela raiz do tkinter
root = tk.Tk()

# Oculte a janela raiz
root.withdraw()

messagebox.showinfo(title="Diretório", message="Selecione a pasta contendo os arquivos :)")

# Abra a janela de diálogo para escolher o diretório
diretorio_escolhido = filedialog.askdirectory()

diretorio = diretorio_escolhido

for arquivo in os.listdir(diretorio):
    if arquivo.endswith('.docx'):
        caminho_arquivo = os.path.join(diretorio, arquivo)
        convert(caminho_arquivo)
print("Todos os arquivos foram gerados :)")
messagebox.showinfo(title="Fim do código", message="Todos os arquivos foram gerados :)")

# Encerre a janela raiz
root.destroy()
