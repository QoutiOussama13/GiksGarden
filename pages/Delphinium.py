import streamlit as st
import streamlit as st
import os
from PIL import Image
from utils import *

st.title("Delphinium Chatbot")
st.image('./Images/Delphinium.png', caption='Delphinium ')

agent_executor = setup_agent()
os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']


api_key = os.environ['OPENAI_API_KEY']



if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Display or clear chat messages
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
