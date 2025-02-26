import streamlit as st
import csv
import os
import datetime
import re

st.set_page_config(page_title="Cadastro", layout="centered")

st.html("""
    <style>
        [data-testid="stSidebar"] { display: none; }
            
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
    </style>
""")

arquivo = "lista_de_usuario.csv"

hoje = datetime.date.today()
min_data = hoje.replace(year=hoje.year - 117)

def validar_email(email):
    padrao = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(padrao, email)

st.title("📝 Criar Cadastro")

email = st.text_input("Email")
senha = st.text_input("Senha", type="password")
confirmar_senha = st.text_input("Confirme sua senha", type="password")
data_nascimento = st.date_input("Data de nascimento", min_value=min_data, max_value=hoje)
apelido = st.text_input("Apelido")

if st.button("Registrar"):
    if not validar_email(email):
        st.error("Formato de e-mail inválido")
    elif senha != confirmar_senha:
        st.error("As senhas não coincidem!")
    else:
        if not os.path.exists(arquivo):
            with open(arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerow(["E-mail", "Senha", "Data de nascimento", "Apelido"])
        with open(arquivo, mode="a", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([email, senha, data_nascimento, apelido])
        st.success("Cadastro realizado com sucesso!")
        

if st.button("⬅️ Voltar"):
    st.switch_page("app.py")  
