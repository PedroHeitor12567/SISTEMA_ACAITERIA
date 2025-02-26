import streamlit as st

st.set_page_config(page_title="Home", layout="centered")

st.html("""
    <style>
        [data-testid="stSidebar"] { display: none; }
            
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
    </style>
""")

if st.button("⬅️ Sair da conta"):
    st.switch_page("pages/login.py")

st.title(f"Bem-vindo(a) à nossa açaiteria! 🍧")

st.markdown("### Escolha qual produto deseja pedir!")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🍨 Açaí"):
        st.write("Você escolheu Açaí!")

with col2:
    if st.button("🍦 Sorvete"):
        st.write("Você escolheu Sorvete!")

with col3:
    if st.button("🥤 Guraçaí"):
        st.switch_page("pages/pedir_guaracai.py")


