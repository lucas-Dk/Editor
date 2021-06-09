# Script de manipulação de imagem com pillow
# autor: lucas-Dk
# Atualmente contém 3 funções
# meu whatsapp copie e cole no navegador: https://wa.me/5531986802198

import os
import re
import rich
from time import sleep as wait
from PIL import Image
from rich.console import Console
from pathlib import Path

def trocar(extensao):
	valid = re.search(r"\.[a-zA-Z]{3}",extensao)
	if valid:
		return extensao

os.makedirs("FotosDoScript",exist_ok=True)
os.system("clear")
console = Console()
local = str(input("Informe o caminho das imagens: ")).strip()
console.print("\nEfeitos disponíveis por enquanto\n",style="red bold")
console.print("[1] Deixar a imagem em preto e branco",style="green bold")
console.print("[2] Deixar a imagem em preto e branco com 'tremida'",style="green bold")
console.print("[3] Redimensionar uma imagem\n",style="green bold")


escolha = str(input("[+] O que deseja fazer: ")).lower()

if escolha.isnumeric():
	escolha = int(escolha)
	if escolha == 1:

		for imagem in os.listdir(str(local)):
			if imagem.endswith(".jpg"):
				image = Image.open(imagem)
				print("Tamanho original: {}".format(image.size))
				wait(1)
				os.system("clear")
				console.print("Adicionando efeito...",style="red bold")
				redimensionar = image.convert("L",palette=Image.ADAPTIVE).resize((image.size),Image.LANCZOS)
				os.chdir("FotosDoScript")
				final_imagem = trocar(extensao=imagem)
				trocar_extensao = final_imagem.replace(final_imagem,".png")
				nome_imagem = imagem.replace(imagem,"PretoEbranco"+trocar_extensao)
				os.path.join("FotosDoScript" + "/" +str(redimensionar.save(nome_imagem)))
				console.print("Imagem com efeito adicionada na pasta!",style="green bold")
	elif escolha == 2:
		for fotos in os.listdir(str(local)):
			if fotos.endswith(".jpg"):
				foto = Image.open(fotos)
				print("Tamanho original: {}".format(foto.size))
				wait(1)
				os.system("clear")
				console.print("Adicionando efeito na foto...",style="red bold")
				efeito = foto.convert("1",palette=Image.ADAPTIVE).resize((foto.size),Image.LANCZOS)
				console.print("Efeito adicionado com sucesso!",style="green bold")
				os.chdir("FotosDoScript")
				os.path.join("FotosDoScript" + "/" + str(efeito.save("FotoTremida.png")))
	elif escolha == 3:
		for imagens in os.listdir(str(local)):
			if imagens.endswith(".jpg"):
				sua_foto = Image.open(imagens)
				print()
				altura_nova = int(input("Informe a altura nova: "))
				largura_nova = int(input("Informe a largura nova: "))
				novo = altura_nova,largura_nova
				os.system("clear")
				print("""
============================
Dados originais:

Altura: {}
Largura: {}
============================
Novos dados:

Altura nova: {}
Largura nova: {}
============================\n""".format(sua_foto.size[1],sua_foto.size[0],altura_nova,largura_nova))
				wait(1)
				console.print("Redimensionando sua imagem...",style="red bold")
				foto_nova = altura_nova, largura_nova
				redimensionamento = sua_foto.convert("P",palette=Image.ADAPTIVE,colors=256).resize((foto_nova),Image.LANCZOS)
				console.print("Imagem redimensionada!",style="green bold")
				os.chdir("FotosDoScript")
				os.path.join("FotosDoScript" + "/" + str(redimensionamento.save("Nova_imagem.png")))

# FIM
