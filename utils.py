import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
import os, time
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ["OPENAI_API_KEY"]
llm = ChatOpenAI(openai_api_key=api_key)

sys_template = "Pretend you're a proficient horticulturist capable of analyzing the condition of a plant, identifying its species, and outlining the necessary steps for optimal growth"


def general_llm(input_user, llm):
    prompt = ChatPromptTemplate.from_messages(
        [("system", sys_template), ("user", "{input}")]
    )
    chain = prompt | llm
    return chain.invoke({"input": input_user})


def response_generator(prompt):
    response = general_llm(prompt, llm)
    print(response)
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


def display_chatbot(chat_prefix=""):
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            response = st.write_stream(response_generator(prompt))
            # st.markdown(response)
            print(response)

        st.session_state.messages.append({"role": "assistant", "content": response})
