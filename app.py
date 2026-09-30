import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI API KEY")
client = genai.Client(api_key=api_key)

st.set_page_config(
    page_title="Gemini AI Chatbot",
    layout="centered"
)

st.markdown("""
<style>

.stApp {
    background-color: #000000;
}

h1 {
    color: #c49a6c;
    text-align: center;
}

.stTextArea label {
    color: #ffffff;
    font-weight: bold;
}

.stTextArea textarea {
    background-color: #1a1a1a;
    color: #ffffff;
    border: 2px solid #38bdf8;
    border-radius: 10px;
}

.stButton button {
    background-color: #5c3a21;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 25px;
    font-weight: bold;
}

.stButton button:hover {
    background-color: #38bdf8;
    color: white;
}

.stAlert {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

st.title("Gemini AI Chatbot")
st.write("Ask Gemini anything!")

prompt = st.text_area(
    "Enter your prompt:",
    placeholder="Explain AI in simple words"
)

if st.button("Generate Response"):
    if prompt:
        with st.spinner("Gemini is thinking....."):
            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )
            st.success("Response generated!")
            st.write(response.text)
    else:
        st.warning("Please enter a prompt.")