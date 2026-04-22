'''Módulo responsável pela seleção de arquivos via interface gráfica'''

from tkinter import filedialog, Tk


def selecionar_arquivos(titulo, tipo):
    root = Tk()
    root.withdraw()
    arquivo = filedialog.askopenfilename(
        title=titulo,
        filetypes=tipo
    )

    root.destroy()
    return arquivo


def selecionar_excel():
    arquivo = selecionar_arquivos(
        "Selecione a planilha Excel",
        [("Arquivos Excel", "*.xlsx *.xls *.csv")]
    )
    if not arquivo:
        raise ValueError("Nenhum arquivo Excel selecionado.")
    return arquivo


def selecionar_pdf():
    arquivo = selecionar_arquivos(
        "Selecione o PDF",
        [("Arquivo PDF", "*.pdf")]
    )
    if not arquivo:
        raise ValueError("Nenhum arquivo PDF selecionado.")
    return arquivo

