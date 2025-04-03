import os


def converter_para_utf8(arquivos_origem, pasta_destino):
    for arquivo_origem in arquivos_origem:
        try:
            nome_arquivo = os.path.basename(arquivo_origem)
            arquivo_destino = os.path.join(pasta_destino, nome_arquivo)

            with open(arquivo_origem, 'r', encoding='windows-1252', errors='ignore') as f_origem:
                conteudo = f_origem.read()

            with open(arquivo_destino, 'w', encoding='utf-8') as f_destino:
                f_destino.write(conteudo)

            print(f"{nome_arquivo} convertido {arquivo_destino}")

        except Exception as e:
            print(f"Erro {arquivo_origem}: {e}")


arquivos = [
    "1T2024.csv",
    "1T2023.csv",
    "2t2023.csv",
    "2T2024.csv",
    "3T2023.csv",
    "3T2024.csv",
    "4T2023.csv",
    "4T2024.csv",
    "Relatorio_cadop.csv",
]

pasta_destino = "../processed"

converter_para_utf8(arquivos, pasta_destino)
