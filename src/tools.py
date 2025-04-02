from typing import Optional, Type, List
from pydantic import  Field
from pydantic import BaseModel
from langchain_core.tools import BaseTool
from langchain.agents import tool
import streamlit as st
from typing import Literal


class Params(BaseModel):
    regulatory_summary: str = Field(description="Regulatory summary ")
    impact_analysis: str = Field(description="Impact Analysis")
    action_plan: str = Field(description="Action plan ")
    final_recommendations: str = Field(description="final recommendations ")

def generate_tools_for_user(workflow:Literal["impact_analysis", "action_plan", "policy_update"]) -> List[BaseTool]:
    """Generate a set of tools that have a user id associated with them."""

    @tool(args_schema=Params)
    def show_analisys_to_user(**document):
        """Use this action to show to the user the Regulatory Impact Analysis Document
        """
        st.session_state.current_regulation["docs"][workflow]["document"] = document
        return "The document was shown with success."
        
    return show_analisys_to_user

