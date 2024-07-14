import streamlit as st
from utils import read_disclaimer

st.set_page_config(page_title="MamaMind", page_icon=":male-doctor:")

st.markdown("<div style='text-align: center; font-size: 32px; font-weight: bold;'>👨‍⚕️ MamaMind</div>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; font-size: 24px;'>Gentle Guidance for New Beginnings</div", unsafe_allow_html=True)
st.divider()

st.subheader("About the application")
st.markdown("""
    This application helps the people with perinatal depression.
    "Chat with me" is a chat with a AI mental health advisor which is designed to provide the advice 
    using Cognitive Behavioral Therapy (CBT). It is a conversational chatbot designed to be friendly and assess 
    the level of depression using the Edinburgh Prenatal/Postpartum Depression score and provide the advice accordingly.
    The user can choose whether to provide the answers to the EPDS questionnaire. Or choose to simply chat with the advisor. 
""")


# Display disclaimer
# File path to the disclaimer markdown file
disclaimer_file_path = 'static/disclaimer.md'
disclaimer_text = read_disclaimer(disclaimer_file_path)
st.subheader("Disclaimer")
st.markdown(disclaimer_text)