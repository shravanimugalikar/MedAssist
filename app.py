import streamlit as st
from healthcare_bot import ask_bot

st.set_page_config(page_title="MedAssist AI", page_icon="🩺")
st.title("MedAssist")
st.subheader("AI Healthcare Assistant")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("Describe your symptoms...")

if prompt:

    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # Get bot response
    response = ask_bot(prompt)

    # Show bot message
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )