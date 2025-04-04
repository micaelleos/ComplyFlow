
from fpdf import FPDF
import io
import re

def remove_caracteres_incompativeis(texto):
    texto.replace('\u2014', '-')
    return re.sub(r'[‘’]', "'", texto)  # Substitui os apóstrofos curvos por simples

def limpar_caracteres(dict):
    dict_limpo = {}
    for item in dict.keys():
        dict_limpo[item] = remove_caracteres_incompativeis(dict[item])
    return dict_limpo

def impressão_a4(Doc,title):
    doc = limpar_caracteres(Doc)
    # Cria um objeto PDF
    pdf = FPDF(format="A4")
    pdf.set_creator(creator="ComplyFlow")

    # Adiciona uma página ao PDF
    pdf.add_page()

    # Define a fonte (Arial, estilo normal, tamanho 12)
    pdf.set_font('Arial', 'B', 16)

    # Adiciona um título
    pdf.cell(0, 10, txt=title, ln=True, align='C')
    pdf.ln(h = '15')
    # Define uma nova fonte para o corpo do texto
    pdf.set_font('Helvetica', '', 12)

    # Adiciona outro parágrafo
    pdf.write(5,doc)

    nome = "title" + ".pdf"
    # Salva o arquivo PDF
    # Criar um buffer em memória
    buffer = io.BytesIO()

    # Salvar o PDF no buffer diretamente como bytes
    pdf_output = pdf.output(dest='S').encode('latin1')
    
    # Escrever no buffer
    buffer.write(pdf_output)

    # Retornar ao início do buffer
    buffer.seek(0)

    return buffer, nome

