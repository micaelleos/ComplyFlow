from sidebar import side_bar
import streamlit as st
from src.util import display_action_plan

side_bar()

st.title("Documents Details")

if st.button("Back"):
    st.switch_page("directory.py")

regulation = st.session_state.show_regulation 

for reg in regulation["docs"]:
    if regulation["docs"][reg]['document']:
        with st.container(border=True, height= 500):
            if reg == 'impact_analysis':    
                st.markdown("### Regulatory Impact Analysis ")
                for i,c in regulation["docs"][reg]['document'].items():
                    st.markdown(f'**{i.replace("_", " ").title()}**')
                    st.markdown(c)
                st.markdown("**Approved by:**")
                for r in regulation["docs"][reg]['approved_by']:
                    st.markdown(f'{r}')
            
            if reg == 'action_plan':    
                display_action_plan(regulation["docs"][reg]['document'])
                st.markdown("**Approved by:**")
                for r in regulation["docs"][reg]['approved_by']:
                    st.markdown(f'{r}')

