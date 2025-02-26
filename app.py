import streamlit as st
import re

st.set_page_config(page_title="Início", layout="centered")

arquivo = "listas_de_usuarios.csv"

st.html("""
    <style>
        .stApp {
            background-color: #A020F0;
        }
        [data-testid="stSidebar"] { display: none; }
        
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }

        .container {
            text-align: center;
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        }

        /* Títulos */
        .title {
            font-size: 32px;
            font-weight: bold;
            text-align: center;
            color: #4CAF50;
        }

        /* Inputs personalizados */
        input {
            border: 2px solid #4CAF50 !important;
            border-radius: 5px !important;
            padding: 10px !important;
        }

        /* Botões personalizados */
        div[data-testid="stButton"] button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px;
            transition: 0.3s;
        }

        /* Efeito hover nos botões */
        div[data-testid="stButton"] button:hover {
            background-color: #388E3C;
            color: #ffffff
        }
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