import streamlit as st
from utils import read_disclaimer

st.set_page_config(page_title="MamaMind", page_icon=":female-doctor:")

# Apply custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles.css")

logo_path = "static/image1-removebg-preview.png"
st.image(logo_path, width=150)

st.markdown("<div style='text-align: center; font-size: 32px; font-weight: bold;'>👩‍⚕️ MamaMind</div>".format(logo_path), unsafe_allow_html=True)
st.markdown("<div style='text-align: center; font-size: 24px;'>Gentle Guidance for New Beginnings</div", unsafe_allow_html=True)
st.divider()
st.write("""<div style='text-align: center; font-size: 20px;'>
    Hello and welcome to MamaMind, your supportive companion through the journey of motherhood. 
    We understand that pregnancy and the postpartum period can be filled with a mix of emotions, 
    and we're here to provide you with the mental health support you deserve.</div""", unsafe_allow_html=True)
st.divider()

st.subheader("About")
st.markdown("""<div style='text-align: justify;'>
    As a gentle guidance companion, MamaMind is here to support you through the ups and downs of motherhood, 
    providing a safe and non-judgmental space to explore your emotions and concerns. Our chatbot application is designed specifically for expecting and new mothers, offering personalized mental health recommendations 
    based on cognitive behavioral therapy and knowledge from research articles from PubMed on perinatal depression. We also assess the severity of perinatal depression using the 
    Edinburgh Depression Scale, ensuring our responses are tailored to your unique needs. </div>""", unsafe_allow_html=True)

st.divider()

# Display disclaimer
# File path to the disclaimer markdown file
disclaimer_file_path = 'static/disclaimer.md'
disclaimer_text = read_disclaimer(disclaimer_file_path)
st.subheader("Disclaimer")
st.markdown(f"<div style='text-align: justify;'>{disclaimer_text}</div>", unsafe_allow_html=True)

st.divider()
st.markdown("<div style='text-align: center; font-size: 20px;'>Created with 💖 from the team of 'MamaMind'</div>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; font-size: 20px;'>Contributed and Developed by Foutse, Priyanka N, Rahul Menon and Vaishnavi Mudaliar</div>", unsafe_allow_html=True)