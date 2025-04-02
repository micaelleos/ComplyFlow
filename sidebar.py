import streamlit as st
import time
from PIL import Image

def side_bar():
    s = st.sidebar
    with s:
        image = Image.open("logoComplyFlow.png")
        image = image.resize((1000, 155))  # Ajuste conforme necessário

        st.logo(image,size="large")
        #s.image("logoComplyFlow.png")
        #st.markdown("# ComplyFlow")
    s.page_link("directory.py", label="Regulation Directory", icon="📂")
    with s:
        if "current_regulation" in st.session_state:
            if st.session_state.current_regulation['regulation']:
                with st.container(border=True):
                    st.write(f"**Regulation in Analisys :** *{st.session_state.current_regulation['regulation']['title']}*")
        st.write("Workflow")
        impact_analisys = st.session_state.current_regulation['impact_analisys']
        action_plan = st.session_state.current_regulation['action_plan']
        policies = st.session_state.current_regulation['policies']

    s.page_link("pages/impact_analisys.py", label="Regulatory Impact Analysis", icon="1️⃣", disabled= impact_analisys)
    s.page_link("pages/action_plan.py", label="Regulatory Action Plan", icon="2️⃣", disabled= action_plan)
    s.page_link("pages/policies.py", label="Internal Policies and Procedures", icon="3️⃣", disabled = policies)