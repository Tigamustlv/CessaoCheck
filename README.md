# Cessão Check

Sistema automatizado de validação de termos de cessão, desenvolvido para comparar informações entre documentos PDF e planilhas Excel, identificando inconsistências em dados operacionais de forma rápida e estruturada.

---

## Problemas que o projeto resolve:

• Em processos de cessão com grande volume de clientes, a validação manual de termos é demorada e suscetível a erros.
• Em alguns casos, inconsistências em operações só são identificadas semanas após a geração do termo, gerando risco operacional.
• Este sistema foi desenvolvido para automatizar essa conferência e permitir validação no mesmo dia da geração do documento.

---

## Solução:

O sistema realiza automaticamente:

- Extração de dados de arquivos PDF
- Extração de CCBs (Cédulas de Crédito Bancário)
- Leitura de planilhas Excel com base operacional
- Comparação entre as duas fontes de dados
- Geração de relatório final com divergências encontradas

---

## Como funciona

1. O usuário seleciona o arquivo PDF do termo de cessão
2. Seleciona a planilha Excel com a base de operações
3. O sistema extrai as CCBs de ambas as fontes
4. Realiza a comparação entre os conjuntos de dados
5. Gera um relatório em Excel com:
   - CCBs presentes em ambas as fontes
   - CCBs ausentes no PDF
   - CCBs ausentes na planilha

---

## Estrutura do projeto

src/
│
├── reader/
│ └── reader.py # Seleção de arquivos via interface gráfica
│
├── processor/
│ └── validator.py # Extração e processamento de dados (regras de negócio)
│
├── report/
│ └── report_generator.py # Geração do relatório final em Excel
│
└── main.py # Orquestração do fluxo do sistema


---

## Tecnologias utilizadas

- Python
- pdfplumber (extração de texto de PDFs)
- pandas (manipulação de dados)
- openpyxl (exportação para Excel)
- tkinter (interface gráfica para seleção de arquivos)

---

## ▶Como executar

### 1. Instale as dependências:

pip install -r requirements.txt

### 2. Execute o projeto:

python main.py


## Saída gerada

O sistema gera um arquivo Excel contendo:

CCB analisada
Presença no PDF
Presença na planilha
Status da validação (OK ou divergência)


## Objetivo

Automatizar a conferência de termos de cessão, reduzindo esforço manual e aumentando a confiabilidade na validação de dados operacionais.

## Observação

Este projeto foi desenvolvido com foco em automação de processos internos e validação de integridade de dados em operações financeiras.
