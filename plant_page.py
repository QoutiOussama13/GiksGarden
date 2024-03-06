import streamlit as st
from utils import *

def display_plant_page():
    st.title("Add Your Plant 🌿")
    with st.form(key='plant_form'):
        plant_name = st.text_input("Plant name")
        planting_date = st.date_input("Date of Planting")
        plant_desc = st.text_area("Description")
        plant_image = st.file_uploader("Upload an image of the plant", type=["jpg", "jpeg", "png"])
        if plant_image:
            st.image(plant_image, caption=plant_name)
        submit_button = st.form_submit_button("Submit")
    
    if submit_button and plant_name:
        if submit_button and plant_name:
            st.session_state.plant_added = True
            st.session_state.plant_name = plant_name
            # The rest of your submission logic
            st.success(f"Plant '{plant_name}' added successfully!")
            st.info("Now let's chat with your plant! Use the sidebar to navigate to your plant chat.")
            # Potentially automatically redirect or provide a link/button to go to the chat page