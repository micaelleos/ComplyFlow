
import os
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools.render import render_text_description_and_args
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

from dotenv import load_dotenv
import streamlit as st
from src.tools import tools
from src.prompts import prompt
from langchain_core.messages import AIMessage


load_dotenv()

@st.cache_resource()
def memory(id):
    memory = MemorySaver() 
    return memory

class ComplianceAgent:
    def __init__(self, params, hash):
        self.params =  params
        self.OPENAI_API_KEY=os.environ["OPEN_API_KEY"]

        self.model = ChatOpenAI(model="gpt-4o",api_key=self.OPENAI_API_KEY)

        self.tools = tools
        self.memory = memory(hash)
        self.config = {"configurable": {"thread_id": "def234"}}

        self.agent_executor = create_react_agent(self.model, self.tools, checkpointer=self.memory, state_modifier=prompt)


    def chat(self,query:str):
        menssage = None
        for event in self.agent_executor.stream(
            {"messages": [{"role": "user", "content": query}]},
            stream_mode="values",
            config=self.config,
        ):
            event["messages"][-1].pretty_print()
            if isinstance(event["messages"][-1], AIMessage):
                menssage = event["messages"][-1]
        return menssage.content
    
    def initial_analysis(self,regulation):
        task = f"""
            ## Analise the following regulation:

            {regulation}
            """
        for event in self.agent_executor.stream(
            {"messages": [{"role": "user", "content": task}]},
            stream_mode="values",
            config=self.config,
        ):
            event["messages"][-1].pretty_print()