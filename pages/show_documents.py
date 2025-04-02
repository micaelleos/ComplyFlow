from sidebar import side_bar
import streamlit as st

side_bar()

st.title("Documents Details")

if st.button("Back"):
    st.switch_page("directory.py")

regulation = st.session_state.show_regulation 


for reg in regulation["docs"]:
    with st.container(border=True, height= 500):
        if reg["title"] == 'Regulatory Impact Analysis':    
            st.markdown(f"#### {reg['title']}")
            st.markdown(f"##### Summary")
            st.markdown(reg['text']['regulatory_summary'])

            st.markdown(f"##### Impact Analysis")
            st.markdown(reg['text']['impact_analysis'])

            st.markdown(f"##### Action Plan")
            st.markdown(reg['text']['action_plan'])

            st.markdown(f"##### Final Recomendation")
            st.markdown(reg['text']['final_recommendations'])
            st.markdown(f"**Document Status**: {reg['status']}")
            for r,s in reg['roles'].items():
                st.markdown(f"**{r}**: {s}")
