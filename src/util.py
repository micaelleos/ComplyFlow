import streamlit as st
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Literal
import pdfplumber
import uuid
from datetime import datetime
from src.tools import ActionPlan
from src.authorizations import roles

load_dotenv()


def doc_approved(role,current_regulation,workflow:Literal["impact_analysis", "action_plan", "policy_update"]):
    
    selectec_roles = [roles[i] for i in range(len(st.session_state.system_params[f'{workflow}_role'])) if st.session_state.system_params[f'{workflow}_role'][i]]

    if role not in st.session_state.current_regulation["docs"][workflow]["approved_by"]:
        st.session_state.current_regulation["docs"][workflow]["approved_by"].append(role)

    if set(st.session_state.current_regulation["docs"][workflow]["approved_by"]) == set(selectec_roles):
        st.session_state.current_regulation["docs"][workflow]["status"] = "Approved"

        if workflow == "impact_analysis":
            st.session_state.current_regulation["docs"]["action_plan"]["status"] = 'Processing'
        elif workflow == "action_plan":
            st.session_state.current_regulation["docs"]["policy_update"]["status"] = 'Processing'
        
    for reg in st.session_state.regulations:
        if reg['id']==current_regulation['id']:
            reg = st.session_state.current_regulation.copy()
    
    st.rerun()
    
def display_action_plan(action_plan: dict):
    st.markdown(f"#### Regulation: {action_plan['regulation_title']}")
    st.markdown(f"**Receipt Date:** {action_plan['received_date']}")
    st.markdown(f"**Compliance Deadline:** {action_plan['compliance_deadline']}")
    st.markdown(f"**Objective:** {action_plan['objective']}")
    
    st.markdown("#### Affected Areas")
    st.markdown(", ".join(action_plan['affected_areas']))
    
    st.markdown("#### Risks and Mitigation")
    for risk in action_plan['risks']:
        st.markdown(f"**{risk.risk}**")
        st.markdown(f"**Impact:** {risk.impact}")
        st.markdown(f"**Probability:** {risk.probability}")
        st.markdown(f"**Mitigation Action:** {risk.mitigation_action}")
    
    st.markdown("#### Planned Actions")
    for action in action_plan['actions']:
        st.markdown(f"**{action.action}**")
        st.markdown(f"**Responsible:** {action.responsible}")
        st.markdown(f"**Area:** {action.area}")
        st.markdown(f"**Priority:** {action.priority}")
        st.markdown(f"**Deadline:** {action.deadline}")
        st.markdown(f"**Status:** {action.status}")
        if action.comments:
            st.markdown(f"**Comments:** {action.comments}")
    
    st.markdown("#### Monitoring")
    st.markdown(action_plan['monitoring_process'])


    
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
