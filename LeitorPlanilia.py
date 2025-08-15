import pandas as pd
from pathlib import Path

# Caminho do arquivo Excel ou outro formato ORIGINAL
ARQUIVO_ORIGINAL = Path.home() / ".vscode" / "Analise_Dados_python" / "Dados_Originais.xlsx"
ARQUIVO_EDITADO = Path.home() / ".vscode" / "Analise_Dados_python" / "Dados_Editados.xlsx"

# Função onde lemos o arquivo original
def ler_dados():
    try:
        df = pd.read_excel(ARQUIVO_ORIGINAL)
        print("Dados lidos com sucesso.")
        return df
    except Exception as e:
        print(f"Erro ao ler os dados: {e}")
        return None

# Função na qual os dados serão editados
def editar_dados(df):
    try:
        # Exemplo de edição: renomear colunas, filtrar dados, etc.
        df.columns = [col.strip().lower() for col in df.columns]  # Renomeia colunas para minúsculas e sem espaços
        df = df.dropna()  # Remove linhas com valores ausentes
        print("Dados editados com sucesso.")
        return df
    except Exception as e:
        print(f"Erro ao editar os dados: {e}")
        return None

# Função para salvar o arquivo editado
def salvar_dados(df):
    try:
        df.to_excel(ARQUIVO_EDITADO, index=False)
        print(f"Dados salvos em {ARQUIVO_EDITADO}.")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

# Função principal
def main():
    df = ler_dados()
    if df is not None:
        df_editado = editar_dados(df)
        if df_editado is not None:
            salvar_dados(df_editado)

if __name__ == "__main__":
    main()
