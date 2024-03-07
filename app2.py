import streamlit as st

# Assuming these imports are bringing in functions that display different pages
from welcome_page import display_welcome_page
from plant_page import display_plant_page
from chatbot_page import display_chatbot_page
from utils import * 

st.set_page_config(
    page_title="GiksGarden is Here 🟩",
    page_icon="🟩")

# Check if a plant has been added
if 'plant_added' not in st.session_state:
    st.session_state.plant_added = False
if 'plant_name' not in st.session_state:
    st.session_state.plant_name = ""

# Sidebar Navigation
st.sidebar.title("GiksGarden Navigation 🌻")
if st.sidebar.button("Welcome"):
    st.session_state.plant_added = False
    display_welcome_page()

if st.sidebar.button("General Chatbot"):
    st.session_state.plant_added = False
    display_chatbot_page("General Chatbot")

# This button shows conditionally depending on the state of plant addition
if not st.session_state.plant_added:
    if st.sidebar.button("Add Your Plant"):
        display_plant_page()
else:
    if st.sidebar.button(f"{st.session_state.plant_name} Chat"):
        display_chatbot_page(f"Chat for {st.session_state.plant_name}", chat_prefix=st.session_state.plant_name.replace(" ", "_"))

if st.sidebar.button("Example Chat 1"):
    st.session_state.plant_added = False
    display_chatbot_page("Rosa Example")
if st.sidebar.button("Example Chat 2"):
    st.session_state.plant_added = False
    display_chatbot_page("Delphinium Eample")