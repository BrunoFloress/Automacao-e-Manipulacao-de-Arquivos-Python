import os

def renomear_arquivos(diretorio, prefixo = "", sufixo = "", subistituir = None, por = None):
    try:
        for nome_do_arquivo in os.listdir(diretorio):
            camoinho_completo = os.path.join(diretorio, nome_do_arquivo)
            if os.path.isfile(camoinho_completo):
                novo_nome = nome_do_arquivo
                
                if prefixo:
                    novo_nome = prefixo + novo_nome
                if sufixo:
                    nome, extensao = os.path.splitext(novo_nome)
                    novo_nome = nome + sufixo + extensao
                
                if subistituir and por:
                    novo_nome = novo_nome.replace(subistituir, por)
                
                novo_camoinho_completo = os.path.join(diretorio, novo_nome)
                
                os.rename(camoinho_completo, novo_camoinho_completo)
                print(f"Arquivo renomeado: {nome_do_arquivo} -> {novo_nome}")
    except Exception as e:
        print(f"Erro ao renomear arquivos: {e}")

def main():
    diretorio = input("Digite o caminho do diretório: ")
    if not os.path.isdir(diretorio):
        print("Diretório inválido.")
        return
    
    prefixo = input("Digite o prefixo (deixe em branco para não adicionar): ")
    sufixo = input("Digite o sufixo (deixe em branco para não adicionar): ")
    subistituir = input("Digite a parte do nome a ser substituída (deixe em branco para não substituir): ")
    por = input("Digite o que substituirá (deixe em branco se não quiser substituir): ")
    
    renomear_arquivos(diretorio, prefixo, sufixo, subistituir, por)
if __name__ == "__main__":
    main()      