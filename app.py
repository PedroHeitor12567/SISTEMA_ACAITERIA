import streamlit as st
import re

st.set_page_config(page_title="Início", layout="centered")

arquivo = "listas_de_usuarios.csv"

st.html("""
    <style>
        [data-testid="stSidebar"] { display: none; }
        
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
    </style>
""")

st.title("Bem-vindo! 👋")

st.markdown('<h2>Escolha uma das opções abaixo:</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("🔐 Fazer Login"):
        st.switch_page("pages/login.py")

with col2:
    if st.button("📝 Criar Cadastro"):
        st.switch_page("pages/cadastro.py")