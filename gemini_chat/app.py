import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from pathlib import Path

# Load environment variables
load_dotenv()

# Configuration
# We look for GEMINI_API_KEY in .env file
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-3.8-flash" # Updated to requested version

# Configure Google Generative AI
if API_KEY:
    genai.configure(api_key=API_KEY)
else:
    st.error("API Key not found! Please add GEMINI_API_KEY to your .env file.")

# Page setup
st.set_page_config(page_title="Code&Chintan Chatbot", page_icon="🤖", layout="centered")

# Logo integration
logo_path = Path("gemini_chat/logo/1000151908.png")
if logo_path.exists():
    st.image(str(logo_path), width=100)
else:
    st.warning("Logo file not found.")

# Custom CSS for ChatGPT-like look
st.markdown("""
    <style>
    .stChatMessage {
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .stChatInputContainer {
        padding-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 Code&Chintan Chatbot")
st.caption("Powered by Google Gemini 3.8 Flash")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What is on your mind?"):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        # Start a chat session to maintain history
        chat = model.start_chat(history=[
            {"role": m["role"] if m["role"] == "user" else "model", "parts": [m["content"]]}
            for m in st.session_state.messages[:-1]
        ])

        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = ""

            # Use streaming for that ChatGPT feel
            response = chat.send_message(prompt, stream=True)
            for chunk in response:
                full_response += chunk.text
                response_placeholder.markdown(full_response + "▌")

            response_placeholder.markdown(full_response)

        # Add assistant response to history
        st.session_state.messages.append({"role": "assistant", "content": full_response})

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
