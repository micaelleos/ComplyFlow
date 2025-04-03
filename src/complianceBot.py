
import os
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools.render import render_text_description_and_args
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

from langchain.agents import AgentExecutor
from langchain.schema.runnable import RunnablePassthrough
from langchain.agents.format_scratchpad import format_to_openai_functions
from langchain.prompts import MessagesPlaceholder
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.memory import ConversationBufferMemory
from langchain_core.utils.function_calling import convert_to_openai_function
from langchain.prompts import ChatPromptTemplate

from dotenv import load_dotenv
import streamlit as st
from src.tools import generate_tools_for_user
from src.prompts import impact_analysis_prompt
from langchain_core.messages import AIMessage
from typing import Literal


load_dotenv()

@st.cache_resource()
def memory(id):
    memory = ConversationBufferMemory(return_messages=True,memory_key="chat_history")
    return memory

class ComplianceAgent:
    def __init__(self, params, hash, workflow:Literal["impact_analysis", "action_plan", "policy_update"]):
        self.params =  params
        self.OPENAI_API_KEY=os.environ["OPEN_API_KEY"]

        self.model = ChatOpenAI(model="gpt-4o",api_key=self.OPENAI_API_KEY)

        self.tools = generate_tools_for_user(workflow=workflow)
        self.memory = memory(hash)
        self.model_with_tool = self.model.bind(functions=[convert_to_openai_function(self.tools)])
        

        if workflow == 'impact_analysis':
            self.system_prompt = impact_analysis_prompt
        elif workflow == 'action_plan':
            self.system_prompt = impact_analysis_prompt
        elif workflow == 'policy_update':
            self.system_prompt = impact_analysis_prompt


        self.prompt = ChatPromptTemplate.from_messages([
            ("system", f"{self.system_prompt}"),
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ])

        self.agent_chain = RunnablePassthrough.assign(
            agent_scratchpad= lambda x: format_to_openai_functions(x["intermediate_steps"])
        ) | self.prompt | self.model_with_tool | OpenAIFunctionsAgentOutputParser()

        self.agent_executor = AgentExecutor(agent=self.agent_chain, tools=[self.tools], verbose=True, memory=self.memory,handle_parsing_errors=True)


    def chat(self,query:str):  
        response=self.agent_executor.invoke({'input':query})
        return response['output']
    
    def initial_analysis(self,regulation):
        task = f"""
            ## Analise the following regulation:

            {str(regulation)}
            """
        response=self.agent_executor.invoke({'input':task})
        return response['output']