import streamlit as st
from PIL import Image
from sidebar import side_bar
from styles import *

side_bar()

# Título Principal
st.markdown("## 🚀 ComplyFlow: Compliance Inteligente e Automatizado")

# Subtítulo
st.markdown(
    "#### Simplifique a conformidade regulatória com inteligência artificial. Automatize análises, gere planos de ação e reduza riscos!"
)

# Seção de Introdução
st.markdown(
    "A conformidade regulatória pode ser um desafio para instituições financeiras e empresas que lidam com regulamentações complexas e em constante mudança. ComplyFlow é uma solução baseada em inteligência artificial que **automatiza a análise de impacto regulatório**, permitindo que sua empresa se mantenha sempre em conformidade de forma eficiente e sem complicações."
)

st.markdown(
    "Com o ComplyFlow, eliminamos a necessidade de análises manuais demoradas e processos desconectados, oferecendo um sistema integrado que **lê, interpreta e sugere planos de ação automaticamente**, otimizando o fluxo de compliance da sua organização."
)

# Seção de Destaques
st.subheader("🔥 Principais Funcionalidades")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("✅ **Análise Automática de Regulamentos**")
    st.write("A IA lê, interpreta e resume documentos regulatórios em segundos, garantindo que sua equipe sempre tenha acesso rápido às informações essenciais.")
    
with col2:
    st.markdown("✅ **Matriz de Impacto Regulatória**")
    st.write("ComplyFlow identifica automaticamente quais áreas do negócio serão impactadas pelas novas regulamentações e sugere ações para adequação.")
    
with col3:
    st.markdown("✅ **Chatbot Especialista em Compliance**")
    st.write("Tire dúvidas e refine análises com um assistente de IA especializado que oferece respostas em tempo real sobre requisitos regulatórios.")

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("✅ **Fluxo de Aprovações Automatizado**")
    st.write("Facilita a colaboração entre equipes de compliance, jurídico e operações, permitindo um fluxo de validação eficiente e rastreável.")

with col5:
    st.markdown("✅ **Edição e Exportação de Relatórios**")
    st.write("Refine e edite relatórios gerados automaticamente e exporte para diferentes formatos, garantindo documentação completa para auditorias.")

with col6:
    st.markdown("✅ **Integração com Sistemas de Compliance**")
    st.write("Conecte-se diretamente a bancos de dados regulatórios e sistemas de gestão para garantir um fluxo de trabalho contínuo e automatizado.")

# Fluxo de Trabalho
st.subheader("🔄 Como Funciona o ComplyFlow?")

st.markdown(
    "ComplyFlow foi desenvolvido para tornar o processo de conformidade regulatória simples e eficiente. Nossa plataforma orienta você por um fluxo de trabalho estruturado que garante que todas as etapas de análise e adequação sejam realizadas de forma clara e auditável."
)

st.markdown("""
    1️⃣ **Upload do Documento Regulatório** – Faça o upload do regulamento para análise.\n
    2️⃣ **Análise Automática** – A IA extrai pontos-chave e resume os requisitos.\n
    3️⃣ **Avaliação de Impacto** – Identifica áreas de impacto e riscos potenciais.\n
    4️⃣ **Aprovações** – Envie para validação das equipes responsáveis.\n
    5️⃣ **Plano de Ação e Implementação** – Receba um plano estruturado para conformidade.\n
    6️⃣ **Acompanhamento e Auditoria** – Monitore o progresso e gere relatórios completos para inspeções e auditorias.
"""
)

# Seção de Benefícios
st.subheader("🎯 Benefícios do ComplyFlow")
st.markdown(
    "- 📉 **Redução de Custos**: Automatize processos manuais e reduza gastos com conformidade.\n"
    "- 🚀 **Aceleração do Processo**: Deixe a IA fazer o trabalho pesado e obtenha insights regulatórios rapidamente.\n"
    "- 🔍 **Precisão e Segurança**: Elimine erros humanos e tenha rastreabilidade completa.\n"
    "- 🏆 **Conformidade Sempre Atualizada**: Fique à frente das mudanças regulatórias sem esforço extra."
)

# Seção de CTA
st.subheader("💡 Experimente o ComplyFlow Agora")
st.markdown(
    "Quer transformar a conformidade regulatória na sua empresa? **Solicite um teste gratuito** e veja a IA em ação!"
)
