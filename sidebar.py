import streamlit as st
import time
from PIL import Image

def side_bar():
    s = st.sidebar
    with s:
        image = Image.open("logoComplyFlow.png")
        image = image.resize((1000, 155))  # Ajuste conforme necessário

        st.logo(image,size="large")

    
    s.page_link("directory.py", label="Regulation Directory", icon="📂")
    with s:
        if "current_regulation" in st.session_state:
            if st.session_state.current_regulation:
                with st.container(border=True):
                    st.write(f"**Regulation in Analisys :** *{st.session_state.current_regulation['title']}*")
                st.write("Workflow")
                impact_analisys = [False if st.session_state.current_regulation["docs"]["impact_analysis"]["status"] != "Pending" else True][0]
                action_plan = [False if st.session_state.current_regulation["docs"]['action_plan']["status"] != "Pending" else True][0]
                policies = [False if st.session_state.current_regulation["docs"]['policy_update']["status"]  != "Pending" else True][0]
            else:
                st.write("Workflow")
                impact_analisys = True
                action_plan = True
                policies = True

    s.page_link("pages/impact_analisys.py", label="Regulatory Impact Analysis", icon="1️⃣", disabled= impact_analisys)
    s.page_link("pages/action_plan.py", label="Regulatory Action Plan", icon="2️⃣", disabled= action_plan)
    s.page_link("pages/policies.py", label="Internal Policies and Procedures", icon="3️⃣", disabled = policies)

    # with s:
    #     st.write("Resources")
    #     s.page_link("pages/about.py", label="About") 