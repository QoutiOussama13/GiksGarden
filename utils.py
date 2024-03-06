import streamlit as st
def display_chatbot(page_title, chat_prefix=""):
    st.title(page_title)
    # Initialize chat history for each chatbot page separately
    if f"messages_{chat_prefix}" not in st.session_state:
        st.session_state[f"messages_{chat_prefix}"] = []
    # Display chat messages from history on app rerun
    for message in st.session_state[f"messages_{chat_prefix}"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state[f"messages_{chat_prefix}"].append({"role": "user", "content": prompt})
        response = f"Echo: {prompt}"
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state[f"messages_{chat_prefix}"].append({"role": "assistant", "content": response})