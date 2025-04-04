
from fpdf import FPDF
import io
import re


def impressão_a4(reg,regulation):
    
    # Cria um objeto PDF
    pdf = FPDF(format="A4")
    pdf.set_creator(creator="ComplyFlow")

    # Adiciona uma página ao PDF
    pdf.add_page()
    # Define uma nova fonte para o corpo do texto
    pdf.set_font('Arial', '', 24)
    pdf.ln(h = '50')
    if reg == 'impact_analysis':    
            # Adiciona outro parágrafo
        pdf.write(10,"Regulatory Impact Analysis")
        pdf.ln(h = '50')
        for i,c in regulation["docs"][reg]['document'].items():
            pdf.set_font('Arial', 'B', 14)
            pdf.write(5,f'{i.replace("_", " ").title()}')
            pdf.ln(h = '34')
            pdf.set_font('Arial', '', 12)
            pdf.write(5,c)
            pdf.ln(h = '34')

    # if reg == 'action_plan':   
    #     text = "### Regulatory Action Plan "
    #     text =+ f"#### Regulation: {regulation['docs'][reg]['document']['regulation_title']}"
    #     text =+ f"**Compliance Deadline:** {regulation['docs'][reg]['document']['compliance_deadline']}"
    #     text =+ f"**Objective:** {regulation['docs'][reg]['document']['objective']}"
        
    #     text =+ "#### Affected Areas"
    #     text =+ ", ".join(regulation['docs'][reg]['document']['affected_areas'])
        
    #     text =+ "#### Risks and Mitigation"
    #     for risk in regulation['docs'][reg]['document']['risks']:
    #         text =+ f"**{risk.risk}**"
    #         text =+ f"**Impact:** {risk.impact}"
    #         text =+ f"**Probability:** {risk.probability}"
    #         text =+ f"**Mitigation Action:** {risk.mitigation_action}"


    # if reg == 'policy_update':    
    #     text = "### Policies and Procedures "
    #     for i,c in regulation['docs"'][reg]['document'].items():
    #         text =+ f'**{i.replace("_", " ").title()}**'
    #         text =+ c



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

