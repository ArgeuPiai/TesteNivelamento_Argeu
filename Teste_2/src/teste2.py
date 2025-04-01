import pandas as pd
import zipfile
import tabula

lista = tabula.read_pdf("../data/input/Anexo_I", pages = "3-181", multiple_tables = True, lattice=True)
print(len(lista))
tabela = pd.concat(lista, ignore_index=True)


legenda = {
            'OD':'Seg. Odontológica',
            'AMB':'Seg. Ambulatorial',
            'HCO':'Seg. Hospitalar Com Obstetrícia',
            'HSO':'Seg. Hospitalar Sem Obstetrícia',
            'REF':'Plano Referência',
            'PAC':'Procedimento de Alta Complexidade',
            'DUT':'Diretriz de Utilização',
           }
tabela.replace(legenda, inplace=True)

csv_path = "../data/output/Rol_Procedimentos.csv"
tabela.to_csv(csv_path, index=False, sep=",", encoding='utf-8-sig')
print(f"Dados salvos em {csv_path}")

zip_path = "../data/output/Teste_Argeu.zip"
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
     zipf.write(csv_path)
print(f"Arquivo compactado em {zip_path}")