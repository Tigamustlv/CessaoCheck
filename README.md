# PDF-Excel Reconciliation Tool

Protótipo em Python desenvolvido para automatizar a validação entre documentos PDF e bases estruturadas (Excel), identificando inconsistências em operações de forma rápida e confiável.

---

## Contexto

Este projeto foi criado a partir de um problema real, onde inconsistências em documentos financeiros eram detectadas apenas semanas após sua geração, gerando risco operacional.

O objetivo é permitir a validação de grandes volumes de dados no mesmo dia, por meio da automação da comparação entre fontes.

---

## Problema

- Validação manual de grandes volumes de dados é demorada e suscetível a erros  
- Inconsistências podem passar despercebidas por longos períodos  
- A detecção tardia aumenta o risco operacional  

---

## Solução

O protótipo automatiza:

- Extração de dados de arquivos PDF  
- Extração de identificadores únicos (ex: IDs de contratos)  
- Leitura de bases estruturadas em Excel  
- Comparação entre as duas fontes  
- Geração de relatório com divergências  

---

## Como funciona

1. O usuário seleciona o arquivo PDF  
2. Seleciona a planilha Excel  
3. O sistema extrai os identificadores de ambas as fontes  
4. Realiza a comparação dos dados  
5. Gera um relatório em Excel com:

- Correspondências  
- Registros ausentes no PDF  
- Registros ausentes na base  

---

## Estrutura do projeto

src/
├── reader/
├── processor/
├── report/
└── main.py


---

## Tecnologias

- Python  
- pdfplumber  
- pandas  
- openpyxl  
- tkinter  

---

## Como executar

pip install -r requirements.txt
python main.py

## Saída gerada

O sistema gera um arquivo Excel contendo:

Identificador analisado
Presença no PDF
Presença na base
Status da validação


## Impacto esperado
Redução do tempo de validação de horas para minutos
Possibilidade de validação no mesmo dia
Redução de risco operacional


## Melhorias futuras
Integração com banco de dados
Interface web
Execução automatizada (pipeline)




## Demonstração

Exemplo de saída gerada pelo sistema:


<img width="430" height="109" alt="f93bd620-dd53-4dc6-b36a-6c524bbdd8a1" src="https://github.com/user-attachments/assets/5a2a0446-71a9-4115-aa85-2453e183a0e6" />


[adicione aqui um print do Excel]
