from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image
from tkinter import messagebox

# Abre a janela de diálogo para selecionar o arquivo
Tk().withdraw() # Oculta a janela principal do Tkinter

messagebox.showinfo(title="Diretório", message="Selecione uma imagem para eu converter :)")
caminho_arquivo_jpg = askopenfilename(title='Selecione uma imagem em JPG', filetypes=[('JPEG', '*.jpg')])

# Abre a imagem e converte para PDF
if caminho_arquivo_jpg:
    imagem = Image.open(caminho_arquivo_jpg)
    caminho_arquivo_pdf = caminho_arquivo_jpg.replace('.jpg', '.pdf')
    imagem.save(caminho_arquivo_pdf, 'PDF', resolution=100.0)
    print('Arquivo convertido com sucesso para PDF.')

messagebox.showinfo(title="Fim", message="Acabou! :)")



