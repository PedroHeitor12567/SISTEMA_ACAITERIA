import streamlit as st
import csv
import os

st.set_page_config(page_title="Home", layout="centered")

st.markdown("""
    <style>
        [data-testid="stSidebar"] { display: none; } 
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

if "sacola" not in st.session_state:
    st.session_state.sacola = []

if st.button("⬅️ Sair da conta"):
    st.set_query_params(page="login")
    st.experimental_rerun()

st.title("Bem-vindo(a) à nossa açaiteria! 🍧")
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
        st.session_state.produto_selecionado = "Guaraçaí"

    if "produto_selecionado" in st.session_state and st.session_state.produto_selecionado == "Guaraçaí":
        arquivo_csv = "pedido.csv"
        st.write("Escolha seu Guaraçaí")
        produtos = {
            "Copo 250 ml": 5.00,
            "Copo 300 ml": 6.00,
            "Copo 400 ml": 8.00,
            "Copo 500 ml": 10.00
        }
        selecionados = []
        for produto, preco in produtos.items():
            key_produto = produto.replace(" ", "_").lower()
            if st.checkbox(f"{produto} ...... R$ {preco:.2f}", key=f"chk_{key_produto}"):
                quantidade = st.number_input(f"Quantos {produto} deseja?", min_value=1, step=1, key=f"qtd_{key_produto}")
                selecionados.append([produto, quantidade, preco])
        total_itens = 0
        for item in selecionados:
            total_itens += item[1]
        if total_itens > 0:
            if st.button("Adicionar à sacola"):
                st.session_state.sacola.extend(selecionados)
                st.success("Itens adicionados à sacola!")

        sacola_container = st.container()
        with sacola_container:
            st.markdown("### 🛒 Sua Sacola")
            if st.session_state.sacola:
                total = 0
                for item in st.session_state.sacola:
                    subtotal = item[1] * item[2]
                    st.write(f"{item[1]}x {item[0]} - R$ {subtotal:.2f}")
                    total += subtotal
                st.write(f"**Total: R$ {total:.2f}**")
            else:
                st.write("Sua sacola está vazia.")
        endereco = st.text_input("Digite seu endereço:", key="endereco_input")
        if st.button("Finalizar Pedido"):
            if endereco.strip() == "":
                st.error("Por favor, insira seu endereço para finalizar o pedido.")
            else:
                if not os.path.exists(arquivo_csv):
                    with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as file:
                        writer = csv.writer(file)
                        writer.writerow(["Produto", "Quantidade", "Preço Unitário", "Subtotal", "Endereço"])
                with open(arquivo_csv, mode="a", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    for item in st.session_state.sacola:
                        writer.writerow([item[0], item[1], item[2], item[1] * item[2], endereco])
                st.success("✅ Pedido finalizado com sucesso! Obrigado pela compra. 🎁")
                sacola_container.empty()  
                st.session_state.sacola = []  