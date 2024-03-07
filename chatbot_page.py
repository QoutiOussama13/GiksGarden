import streamlit as st
from utils import *


# Assuming this function can be extended or modified for specific chatbots
def display_chatbot_page(page_title, chat_prefix=""):
    st.title(page_title)
    display_chatbot()
