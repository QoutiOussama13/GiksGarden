import streamlit as st

def display_welcome_page():
    st.title("Welcome to GiksGarden 🌱")
    st.image("./Images/GiksGarden.png", width=200)
    st.subheader("Overview")
    st.write("""
    GiksGarden is your conversational companion for gardening. Navigate through the app to:
    - Have a general conversation with a chatbot.
    - Register your plant and have personalized chats. 
    - Explore example chats with different plants.
    """)
    st.subheader("How to Use")
    st.write("""
    - Use the sidebar to navigate through the app.
    - Enter the chat sections to interact with the bot.
    - Fill out the form to add your plant's information.
    """)
