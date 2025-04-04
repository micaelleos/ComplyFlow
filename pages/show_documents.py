from sidebar import side_bar
import streamlit as st
from src.util import display_action_plan

side_bar()

st.title("Documents Details")

if st.button("Back"):
    st.switch_page("directory.py")

regulation = st.session_state.show_regulation 

doc_to_show = False

for reg in regulation["docs"]:
    if regulation["docs"][reg]['document']:
        doc_to_show = True
        with st.container(border=True, height= 500):
            col = st.columns([0.8,0.2])
            if reg == 'impact_analysis':    
                with col[0]:
                    st.markdown("### Regulatory Impact Analysis ")
                with col[1]:
                    st.button("Download", type="primary",key=f'db{reg}')
                for i,c in regulation["docs"][reg]['document'].items():
                    st.markdown(f'**{i.replace("_", " ").title()}**')
                    st.markdown(c)
                st.markdown("**Approved by:**")
                for r in regulation["docs"][reg]['approved_by']:
                    st.markdown(f'{r}')
            
            if reg == 'action_plan':   
                with col[0]:
                    st.markdown("### Regulatory Action Plan ")
                with col[1]:
                    st.button("Download", type="primary") 
                display_action_plan(regulation["docs"][reg]['document'])
                st.markdown("**Approved by:**")
                for r in regulation["docs"][reg]['approved_by']:
                    st.markdown(f'{r}')

            if reg == 'policy_update':    
                with col[0]:
                    st.markdown("### Policies and Procedures ")
                with col[1]:
                    st.button("Download", type="primary") 
                for i,c in regulation["docs"][reg]['document'].items():
                    st.markdown(f'**{i.replace("_", " ").title()}**')
                    st.markdown(c)
                st.markdown("**Approved by:**")
                for r in regulation["docs"][reg]['approved_by']:
                    st.markdown(f'{r}')

if not doc_to_show:
    st.info("No documents to show",icon="ℹ️")