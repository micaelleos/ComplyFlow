import streamlit as st
from src.complianceBot import ComplianceAgent
from styles import *
import os
from src.util import doc_approved
from src.authorizations import modal
from sidebar import side_bar
import uuid


side_bar()

styles()

@st.fragment
def atualizar_chat(chat_container,prompt=None):
    with chat_container:
        if not prompt:
            initial_message = st.chat_message("assistant")
            initial_message.write("Hi, how can I assist you today?")
        messages = st.session_state.current_regulation["docs"]['policy_update']["messages"]

        for i in range(0,len(messages)):
            message = messages[i]       
                                
            if message['role'] == "assistant":
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])
            else:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])    

        if prompt:
            with st.chat_message("assistant"):
                with st.spinner(""): 
                    response=chat.chat(prompt)
                st.markdown(response)

            st.session_state.current_regulation["docs"]['policy_update']["messages"].append({"role": "assistant", "content": response})


hash = st.session_state.current_regulation["docs"]['policy_update']["chatbot_id"]

chat = ComplianceAgent(st.session_state.system_params,hash,workflow='policy_update')

if not st.session_state.current_regulation["docs"]['policy_update']["document"]:
    chat.initial_analysis(st.session_state.current_regulation)


with st.container():
    
    with st.container():
        col1, col2 = st.columns([0.8,0.2])
        with col1:
            st.title("Internal Polices and Procedures Agent")
        with col2:
            if st.button("Role: " + st.session_state.system_params["role"],use_container_width=True): #:information_source: :receipt:
                modal()

    
    col11, col22 = st.columns([0.5,0.5])
    with col22:
        with st.container(border=False):
            chat_container = st.container(height=400,border=False)
            atualizar_chat(chat_container)

            if prompt:= st.chat_input("Make a question...",key="user_input"):
        
                st.session_state.current_regulation["docs"]['policy_update']["messages"].append({"role": "user", "content": prompt})
                atualizar_chat(chat_container,prompt)
                
    with col11:   
        if st.session_state.current_regulation["docs"]['policy_update']["document"]:
            with st.expander("Document",expanded=True):
                for i in st.session_state.current_regulation["docs"]['policy_update']["document"]:
                    st.markdown(f'**{i.replace("_"," ").title()}**')
                    st.markdown(st.session_state.current_regulation["docs"]['policy_update']["document"][i])
                    
        else:
            with st.expander("Document",expanded=False):
                st.markdown("__Document__")

        with st.container(border=False):
            colsx = st.columns([0.3,0.3,0.3])
            with colsx[0]:
                pass
            with colsx[1]:
                if st.session_state.current_regulation["docs"]['policy_update']["document"]:
                    if st.button(label="Approve",
                                       type="primary",
                                       use_container_width=True):
                        doc_approved(role=st.session_state.system_params["role"], current_regulation=st.session_state.current_regulation,workflow='policy_update')
                        
