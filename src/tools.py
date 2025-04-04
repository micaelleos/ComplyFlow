from typing import Optional, Type, List
from pydantic import  Field
from pydantic import BaseModel
from langchain_core.tools import BaseTool
from langchain.agents import tool
import streamlit as st
from typing import Literal

from pydantic import BaseModel, Field
from typing import List, Optional, Union
from uuid import uuid4, UUID
from datetime import datetime


class Params(BaseModel):
    regulatory_summary: str = Field(description="Regulatory summary ")
    impact_analysis: str = Field(description="Impact Analysis")
    action_plan: str = Field(description="Action plan ")
    final_recommendations: str = Field(description="final recommendations ")

class ActionItem(BaseModel):
    action: str = Field(description="Descrição da ação a ser tomada")
    responsible: str = Field(description="Equipe responsável pela ação")
    area: str = Field(description="Área envolvida na execução da ação")
    priority: str = Field(description="Prioridade da ação (Alta, Média, Baixa)")
    deadline: Optional[Union[datetime, str]] = Field(None, description="Prazo para conclusão da ação ou 'Ongoing' se contínuo")
    status: str = Field(default="Pendente", description="Status atual da ação")
    comments: Optional[str] = Field(None, description="Comentários adicionais sobre a ação")

class RiskMitigation(BaseModel):
    risk: str = Field(description="Descrição do risco identificado")
    impact: str = Field(description="Impacto potencial do risco")
    probability: str = Field(description="Probabilidade de ocorrência (Alta, Média, Baixa)")
    mitigation_action: str = Field(description="Ação para mitigar o risco")

class ActionPlan(BaseModel):
    id: UUID = Field(default_factory=uuid4, description="Identificador único do plano de ação")
    regulation_title: str = Field(description="Título da regulação relacionada")
    compliance_deadline: Optional[Union[datetime, str]] = Field(description="Prazo final para conformidade")
    objective: str = Field(description="Objetivo do plano de ação e resumo da regulação")
    affected_areas: List[str] = Field(description="Áreas impactadas pela regulação")
    risks: List[RiskMitigation] = Field(description="Lista de riscos identificados e ações de mitigação")
    action_plan: Optional[Union[List[ActionItem], str]] = Field(description="Lista de ações a serem executadas")

class Policy(BaseModel):
    title: str = Field(description="Title of the policy")
    objective: str = Field(description="Objective of the policy")
    scope: str = Field(description="Scope of the policy")
    legal_basis: List[str] = Field(description="List of legal bases applicable to the policy")
    regulatory_bodies: List[str] = Field(description="List of regulatory bodies overseeing compliance")
    requirements: str = Field(description="Detailed compliance requirements")
    application_process: str = Field(description="Steps for policy application and approval")
    monitoring: str = Field(description="Monitoring and compliance enforcement measures")
    training: str = Field(description="Training requirements for employees")
    penalties: str = Field(description="Consequences of non-compliance")

@tool(args_schema=Params)
def show_analisys_to_user(**document):
    """Use this action to show to the user the Regulatory Impact Analysis Document
    """
    st.session_state.current_regulation["docs"]['impact_analysis']["document"] = document
    return "The document was shown with success."

@tool(args_schema=ActionPlan)
def show_action_plan_to_user(**document):
    """Use this action to show to the user the Regulatory Action Plan Document
    """
    st.session_state.current_regulation["docs"]['action_plan']["document"] = document
    return "The document was shown with success."
    

@tool(args_schema=Policy)
def show_policy_update_to_user(**document):
    """Use this action to show to the user the Policy
    """
    st.session_state.current_regulation["docs"]['policy_update']["document"] = document
    return "The document was shown with success."

