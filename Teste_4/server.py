from fastapi import FastAPI, Query
import pandas as pd

app = FastAPI()

# Carregar para DataFrame
CSV_FILE = "../Teste_3/data/processed/Relatorio_cadop.csv"  # Nome do arquivo CSV a ser carregado
df_operadoras = pd.read_csv(CSV_FILE, delimiter=';', encoding='UTF-8', dtype=str)

# Converter para string e remover NaN
df_operadoras.fillna("", inplace=True)

@app.get("/buscar-operadoras/")
def buscar_operadoras(termo: str = Query(..., min_length=2)):
    """buscar operadoras """
    resultado = df_operadoras[
        df_operadoras['Razao_Social'].str.contains(termo, case=False, na=False) |
        df_operadoras['Nome_Fantasia'].str.contains(termo, case=False, na=False)
    ]

    return resultado.to_dict(orient="records")
