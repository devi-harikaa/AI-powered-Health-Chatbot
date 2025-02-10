import streamlit as st
import google.generativeai as genai

# Set up Streamlit page
st.set_page_config(page_title="AI Chatbot 🤖", layout="centered")

st.title("AI Chatbot 🤖 (Powered by Google Gemini)")
st.write("Ask me anything!")

# Load API key (from Streamlit secrets)
genai.configure(api_key=st.secrets["AIzaSyB5mtrw4UbGBw3VwjKfKZgnfyLZ6BbGiFM"])

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if user_input := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate AI response
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(user_input)

    bot_message = response.text
    st.session_state.messages.append({"role": "assistant", "content": bot_message})

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(bot_message)

