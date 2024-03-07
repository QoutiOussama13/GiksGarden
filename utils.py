
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
import os 
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ["OPENAI_API_KEY"]
tavily_key = os.environ["OPENAI_API_KEY"]

model = 'gpt-3.5-turbo'
llm = ChatOpenAI(temperature=0, model=model)

def general_llm(input_user, llm):
    sys_template = "Pretend you're a proficient horticulturist capable of analyzing the condition of a plant, identifying its species, and outlining the necessary steps for optimal growth"

    prompt = ChatPromptTemplate.from_messages([
        ("system", sys_template),
        ("user", "{input}")
    ])
    chain = prompt | llm
    return chain.invoke({"input": input_user})


def display_chatbot(page_title, chat_prefix=""):
    st.title(page_title)
    #client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    if "general_text_model" not in st.session_state:
        st.session_state["general_text_model"] = llm

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response=general_llm(prompt,llm)      
        st.session_state.messages.append({"role": "assistant", "content": response})