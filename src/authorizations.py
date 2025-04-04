import streamlit as st

roles =  ["Compliance","Legal","Operations"] #"Risk"

@st.dialog("Role configuration")
def modal():
        index = roles.index(st.session_state.system_params["role"])
        st.markdown("## Role")
        role = st.radio(
            "Select the role",
            roles, #Compliance, Legal, Risk, Operations, IT, (T), Internal Audit (A), Corporate Governance (G)
            horizontal=True,
            index=index  # mantém o valor anterior
        )
        if st.button("Salvar"):
            st.session_state.system_params["role"] = role
            st.rerun()

def checkbox_approvall(status):
    compliance = st.checkbox("Compliance",status[0])
    legal = st.checkbox("Legal",status[1])
    operations = st.checkbox("Operations",status[3])
    risk = st.checkbox("Risk",status[4])
    return [compliance,legal,operations,risk]

@st.dialog("Configure Approvall Flow")
def config_approvall():
    st.markdown("#### Regulatory Impact Analysis")
    impact_analysis_role = checkbox_approvall(st.session_state.system_params["impact_analysis_role"])
    st.markdown("#### Regulatory Action Plan")
    action_plan_role = checkbox_approvall(st.session_state.system_params["action_plan_role"])
    st.markdown("#### Internal Policies and Procedures")
    policies_role = checkbox_approvall(st.session_state.system_params["policies_role"])

    if st.button('Save'):
        st.session_state.system_params["impact_analysis_role"] = impact_analysis_role
        st.session_state.system_params["action_plan_role"] = action_plan_role
        st.session_state.system_params["policies_role"] = policies_role
        print(st.session_state.system_params)
        st.rerun()
