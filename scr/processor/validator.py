'''Módulo responsável pela validação e processamento dos arquivos pós seleção via interface gráfica.
Regra de negócio é imposta aqui.'''

import tkinter
import pdfplumber
import pandas as pd
import re
from tkinter import Tk, filedialog


def extrair_texto_pdf(caminho_pdf):
    texto = ""

    with pdfplumber.open(caminho_pdf) as pdf:
        for pagina in pdf.pages:
            t = pagina.extract_text()
            if t:
                texto += t + "\n"


    texto = texto.replace("\n", " ")

    return texto



def extrair_ccbs(texto):
    padrao = r'\b\d{10}\b'
    return set(re.findall(padrao,texto))


def ler_planilha(caminho_excel):
    df = pd.read_excel(caminho_excel)

    ccbs = (
        df["codigo_da_operacao"]
        .astype(str)
        .str.replace(r'\D', '',regex=True)
    )


    return set(ccbs)


'''
def selecionar_arquivos(titulo, tipo):
    root = Tk()
    root.withdraw()
    arquivo = filedialog.askopenfilename(
        title=titulo,
        filetypes=tipo
    )

    root.destroy()
    return arquivo


def selecionar_pdf():
    arquivo = selecionar_arquivos(
        "Selecione o PDF",
        [("Arquivo PDF", "*.pdf")]
    )
    if not arquivo:
        raise ValueError("Nenhum arquivo PDF selecionado.")
    return arquivo



def extrair_texto_pdf(caminho_pdf):
    texto = ""

    with pdfplumber.open(caminho_pdf) as pdf:
        for pagina in pdf.pages:
            t = pagina.extract_text()
            if t:
                texto += t + "\n"

        
    texto = texto.replace("\n", " ")

    return texto



if __name__ == "__main__":
    try:
        caminho = selecionar_pdf()
        texto = extrair_texto_pdf(caminho)
        print(texto)
    except Exception as e:
        print("Erro", e)


        
        if "tiago".upper() in texto:
            print("Contém o nome.")
        else:
            print("Nome não encontrado")

'''