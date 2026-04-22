''' Aqui iremos gerar o report dos processamentos definidos em validator.py'''

import pandas as pd
import tkinter as tk
from tkinter import filedialog
    
def gerar_relatorio(ccbs_pdf, ccbs_planilha, caminho_saida):

    all_ccbs = sorted(ccbs_pdf.union(ccbs_planilha))

    dados = []

    for ccb in all_ccbs:
        dados.append({
            "CCB": ccb,
            "No_PDF": ccb in ccbs_pdf,
            "Na_Planliha": ccb in ccbs_planilha,
            "Status": (
                "OK" if ccb in ccbs_pdf and ccb in ccbs_planilha
                else "Faltando no PDF" if ccb in ccbs_planilha
                else "Faltando na Planilha"
            )
        })

    df = pd.DataFrame(dados)
    df.to_excel(caminho_saida, index=False)



def selecionar_saida():
    return filedialog.asksaveasfilename(
        title="Salvar relatório como",
        defaultextension=".xlsx",
        filetypes=[("Excel files", "*.xlsx")]
    )