import os
import shutil
import pathlib 
from pathlib import Path

DOWNLOAD_DIR = Path.home() / "Downloads"

CATEGORIAS = {
    "Imagens": ["jpg", "jpeg", "png", "gif", "bmp"],
    "Videos": ["mp4", "mkv", "avi", "mov", "flv"],
    "Documentos":["pdf", "docx", "txt", "xlsx", "pptx"],
    "Musicas": ["mp3", "wav", "flac", "aac"],
    "Arquivos": ["zip", "rar", "tar", "gz"],
    "outros": []
}

def criar_pastas():
    for categoria in CATEGORIAS.keys():
        pasta = DOWNLOAD_DIR / categoria
        if not pasta.exists():
            pasta.mkdir(parents=True, exist_ok=True)
            print(f"Pasta criada: {pasta}")

def mover_arquivos():
    for arquivo in DOWNLOAD_DIR.iterdir():
        if arquivo.is_file():
            movido = False
            for categoria, extensoes in CATEGORIAS.items():
                if arquivo.suffix[1:].lower() in extensoes:
                    destino = DOWNLOAD_DIR / categoria / arquivo.name
                    shutil.move(arquivo, destino)
                    print(f"Arquivo movido: {arquivo.name} -> {categoria}")
                    movido = True
                    break
            if not movido:
                destino = DOWNLOAD_DIR / "outros" / arquivo.name
                shutil.move(arquivo, destino)
                print(f"Arquivo movido: {arquivo.name} -> outros")

def main():
    criar_pastas()
    mover_arquivos()
    print("Organização de downloads concluída.")

if __name__ == "__main__":
    main()   