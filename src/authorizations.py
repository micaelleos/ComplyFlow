import streamlit as st
import uuid 
from typing import Literal
roles =  ["Compliance","Legal","Operations","Risk"]

@st.dialog("Role configuration")
def modal(type:Literal["impact_analysis_role","action_plan_role","policy_update_role"]):
        
        selectec_roles = [roles[i] for i in range(len(st.session_state.system_params[type])) if st.session_state.system_params[type][i]]
        index = selectec_roles .index(st.session_state.system_params["role"])
        st.markdown("## Role")
        role = st.radio(
            "Select the role",
            selectec_roles , 
            horizontal=True,
            index=index  
        )
        if st.button("Salvar"):
            st.session_state.system_params["role"] = role
            st.rerun()

def checkbox_approvall(v,type):
    compliance = st.checkbox("Compliance",value=v[0],key=f'{type}C')
    legal = st.checkbox("Legal",value=v[1],key=f'{type}L')
    operations = st.checkbox("Operations",value=v[2],key=f'{type}O')
    risk = st.checkbox("Risk",value=v[3],key=f'{type}R')
    return [compliance,legal,operations,risk]

@st.dialog("Configure Approval Flow",width='large')
def config_approvall():
    cols = st.columns(3)
    with cols[0]:
        st.markdown("#### Regulatory Impact Analysis")
        a = checkbox_approvall(st.session_state.system_params["impact_analysis_role"],"impact")
    with cols[1]:
        st.markdown("#### Regulatory Action Plan")
        p = checkbox_approvall(st.session_state.system_params["action_plan_role"],'action')
    with cols[2]:
        st.markdown("#### Internal policy_update and Procedures")
        r = checkbox_approvall(st.session_state.system_params["policy_update_role"],'policy')
    
    if st.button("Save",type='primary'):
        st.session_state.system_params["impact_analysis_role"] = a
        st.session_state.system_params["action_plan_role"] = p
        st.session_state.system_params["policy_update_role"] = r
        st.rerun()
    