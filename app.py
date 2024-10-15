import os
from langchain_community.llms import Ollama
from langchain_groq import ChatGroq
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

# os.environ["LANGCHAIN_API_KEY"] = os.getenv("langchain_api_key")
# st.secrets["langchain_api_key"]
api_key=st.sidebar.text_input("Enter your Groq API Key:",type="password")

#prompt template
prompt =  ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the question asked."),
        ("user", "Question:{question}")
    ]
)

#streamlit framework

st.title("Langchain Demo")
input_text = st.text_input("What question you have in mind?")

#ollama llama 2 model
# llm = Ollama(model = "llama2")
llm=ChatGroq(groq_api_key=api_key,model_name="Llama3-8b-8192",streaming=True)
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))