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