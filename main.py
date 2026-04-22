from tkinter import Tk, messagebox
from scr.reader.reader import selecionar_arquivos, selecionar_excel, selecionar_pdf
from scr.processor.validator import extrair_texto_pdf, extrair_ccbs, ler_planilha
from scr.report.report_generator import gerar_relatorio, selecionar_saida



def main():
    root = Tk()
    root.withdraw()

    try:
        pdf_path = selecionar_arquivos(
            "Selecione o termo (PDF)",
            [("Arquivos PDF", "*.pdf")]
        )

        if not pdf_path:
            return
        
        excel_path = selecionar_arquivos(
            "Selecione a Planilha",
            [("Arquivos Excel", "*.xlsx")]
        )

        if not excel_path:
            return
        
        saida = selecionar_saida()

        if not saida:
            return

        texto = extrair_texto_pdf(pdf_path)

        ccbs_pdf = extrair_ccbs(texto)
        ccbs_planilha = ler_planilha(excel_path)

        gerar_relatorio(ccbs_pdf, ccbs_planilha, saida)

        messagebox.showinfo("Sucesso", "Auditoria concluída!")

    except Exception as e:
        messagebox.showerror("Erro", str(e))

if __name__ == "__main__":
    main()

