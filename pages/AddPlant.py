import streamlit as st
from utils import *
import os
from PIL import Image
from utils import *


agent_executor = setup_agent()
api_key = os.environ['OPENAI_API_KEY']

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
        st.success(f"Plant '{plant_name}' added successfully!")
        st.info("Now let's chat with your plant! ")
        if "messages" not in st.session_state.keys():
            st.session_state.messages = [{"role": "assistant", "content": f"How may assist you today on : '{plant_name}?"}]
    for message in st.session_state.messages:
        if message["role"] == "user" :
            with st.chat_message(message["role"]):
                st.write(message["content"])
        else : 
            with st.chat_message(message["role"] ):
                st.write(message["content"])

# User-provided prompt
    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

    uploaded_file = st.file_uploader("Choose an image file", type="jpg")

# Generate a new response if last message is not from assistant
    if st.session_state.messages[-1]["role"] != "assistant":
        result = ' '
        if uploaded_file is not None :
            image = Image.open(uploaded_file)
            result = encode_and_query_api(image, api_key)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
        #st.write(result)
                content = result + str(st.session_state.messages[-1]["content"])
                response = agent_executor.invoke(content)
            placeholder = st.empty()
            full_response = ''
        for item in response['output']:
            full_response += item
            placeholder.markdown(full_response)
        placeholder.markdown(full_response)
        message = {"role": "assistant", "content": full_response + result}  
        st.session_state.messages.append(message)
        uploaded_file = None