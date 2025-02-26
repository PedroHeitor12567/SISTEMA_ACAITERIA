import streamlit as st

st.set_page_config(page_title="Guaraçaí", layout="centered")

st.html("""
    <style>
        [data-testid="stSidebar"] { display: none; }
            
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
    </style>
""")

st.title("Escolha seu guaraçaí")
st.checkbox("Copo 250 ml......R$ 5,00")
st.checkbox("Copo 300 ml......R$ 6,00")
st.checkbox("Copo 400 ml......R$ 8,00")
st.checkbox("Copo 500 ml......R$ 10,00")