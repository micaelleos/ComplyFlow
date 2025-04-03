import streamlit as st
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Literal
import pdfplumber
import uuid
from datetime import datetime

load_dotenv()


def doc_approved(role,current_regulation,workflow:Literal["impact_analysis", "action_plan", "policy_update"]):
    
    if role not in st.session_state.current_regulation["docs"][workflow]["approved_by"]:
        st.session_state.current_regulation["docs"][workflow]["approved_by"].append(role)

    if set(st.session_state.current_regulation["docs"][workflow]["approved_by"]) == {'Compliance', 'Legal', 'Operations', 'Risk'}:
        st.session_state.current_regulation["docs"][workflow]["status"] = "Approved"

        if workflow == "impact_analysis":
            st.session_state.current_regulation["docs"]["action_plan"]["status"] = 'Processing'
        elif workflow == "action_plan":
            st.session_state.current_regulation["docs"]["policy_update"]["status"] = 'Processing'
        
    for reg in st.session_state.regulations:
        if reg['id']==current_regulation['id']:
            reg = st.session_state.current_regulation.copy()
    
    st.rerun()
    
    
    


    
def doc_summary(text):
    pass


def save_uploadedfile(uploaded_file):
    with pdfplumber.open(uploaded_file) as pdf:
        text = "\n\n".join(page.extract_text() or "" for page in pdf.pages)
    
    if not search_regulation_title(uploaded_file.name):
        st.session_state.regulations.append(
                    {
            "title": uploaded_file.name,
            "id": uuid.uuid4(),
            "text": text,
            "status": "Not Analyzed",  # Status of the regulation in the workflow
            "created_at": datetime.now(),  # Timestamp for tracking
            "docs": {
                "impact_analysis": {
                    "status": "Pending",  # Status of this phase
                    "document": None,  # Stores the generated document
                    "approved_by": [],  # List of approved users/roles
                    "chatbot_id": uuid.uuid4(),  # Unique ID for the chatbot
                    "messages": []  # Chat history for this phase
                },
                "action_plan": {
                    "status": "Pending",
                    "document": None,
                    "approved_by": [],
                    "chatbot_id": uuid.uuid4(),
                    "messages": []
                },
                "policy_update": {
                    "status": "Pending",
                    "document": None,
                    "approved_by": [],
                    "chatbot_id": uuid.uuid4(),
                    "messages": []
                }
            }
        }
            )
        
        """
                    {"title":uploaded_file.name,
                "id":uuid.uuid4(),
                "text":text,
                "status":"Not Analizes",
                "docs":[{"roles":
                        {"Compliance":"Not approved",
                        "Legal":"Not approved"}},
                        ]

            }
        
        """

def search_regulation(id):
    for reg in st.session_state.regulations:
        if reg['id'] == id:
            return reg
        
def search_regulation_title(title):
    for reg in st.session_state.regulations:
        if reg['title'] == title:
            return True
    return False

 
def init_workflow(id):
    st.session_state.current_regulation = search_regulation(id)
    st.session_state.current_regulation["docs"]["impact_analysis"]["status"] = 'Processing'
    st.switch_page("pages/impact_analisys.py")
