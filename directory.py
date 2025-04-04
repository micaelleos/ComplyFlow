import streamlit as st
import os
from text import regulation
from sidebar import side_bar
from src.util import save_uploadedfile, init_workflow
from styles import styles_directory
from src.authorizations import config_approvall

styles_directory()


if "current_regulation" not in st.session_state:
    st.session_state.current_regulation = None

side_bar()

cols = st.columns([0.9,0.1])

with cols[0]:
    st.title("Regulation Directory")
with cols[1]:
    if st.button(":gear:",use_container_width=True):
        config_approvall()

if "regulations" not in st.session_state:
    st.session_state.regulations = [] # definir estrutura de dados da regulação, tem que ter tudo aqui, tanto o chat, quanto os documentos processados quanto o status do doc
    #st.session_state.regulations.append(regulation)


if "system_params" not in st.session_state:
    st.session_state.system_params = {}
    st.session_state.system_params["role"] = "Compliance"

    st.session_state.system_params["impact_analysis_role"] = [True,True,False,False]
    st.session_state.system_params["action_plan_role"] = [True,True,True,True]
    st.session_state.system_params["policies_role"] = [False,True,True,True]

if "show_regulation" not in st.session_state:
    st.session_state.show_regulation = None


def call_show_documents_page(regulation):
    st.session_state.show_regulation  = regulation
    st.switch_page("pages/show_documents.py")


uploaded_file = st.file_uploader("Add a new regulation", type=['pdf'], accept_multiple_files=False)

if uploaded_file is not None:
    with st.spinner('Uploading file...'):
        save_uploadedfile(uploaded_file)
        

def reg_bloc(regulation):
    with st.container(height=400):
        with st.container():
            button_init = "init" + regulation['title'].replace(" ", "") 
            button_seedoc = "see" + regulation['title'].replace(" ", "") 
            st.write(f"**Title:** {regulation['title']}")
            st.write(f"**Status:** {regulation['status']}")
            st.write(f"**Text:** {regulation['text'][:200]}...")
            if st.button("Init workflow",key=button_init, use_container_width=True,type="primary"):
                init_workflow(regulation["id"])
            if st.button("See documents",key=button_seedoc, use_container_width= True):
                call_show_documents_page(regulation)

if "regulations" in st.session_state:
    reg = st.session_state.regulations
    cols = st.columns(2)
    i=0
    for r in reg:
        with cols[i]:
            reg_bloc(r)
            i= i + 1
        if i > 1:
            i=0