import streamlit as st
import csv
import os

st.set_page_config(page_title="Login", layout="centered")

st.html("""
    <style>
        [data-testid="stSidebar"] { display: none; }
            
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
    </style>
""")

st.title("🔐 Login")

arquivo = "lista_de_usuario.csv"
email = st.text_input("Email")
senha = st.text_input("Senha", type="password")


if st.button("Entrar"):
    usuario_encontrado = False
    try:
        with open(arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                if len(linha) == 4:
                    email_salvo, senha_salva, _, apelido = linha
                    if email == email_salvo and senha == senha_salva:
                        usuario_encontrado = True
                        st.success(f"✅ Bem-vindo(a), {apelido}!")
                        st.switch_page("pages/home.py")
                        break
    except FileNotFoundError:
        st.error("🚨 O arquivo de usuários não foi encontrado! Cadastre-se primeiro.")
    if not usuario_encontrado:
        st.error("❌ E-mail ou senha incorretos. Tente novamente.")

if st.button("⬅️ Voltar"):
    st.switch_page("app.py")
