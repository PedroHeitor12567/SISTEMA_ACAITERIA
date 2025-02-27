import streamlit as st
import os
import csv

# Configuração da página
st.set_page_config(page_title="Guaraçaí", layout="centered")

# Nome do arquivo CSV para armazenar os pedidos
usuario = "usuario_logado"  # Substitua pelo nome real do usuário logado
pedidos_csv = f"{usuario}.csv"

# Inicializa a sacola na sessão se ainda não existir
if "sacola" not in st.session_state:
    st.session_state.sacola = []

# Título
st.title("Escolha seu Guaraçaí")

# Dicionário com os produtos e preços
produtos = {
    "Copo 250 ml": 5.00,
    "Copo 300 ml": 6.00,
    "Copo 400 ml": 8.00,
    "Copo 500 ml": 10.00
}

# Criar checkboxes e capturar a quantidade quando selecionado
selecionados = []
for produto, preco in produtos.items():
    if st.checkbox(f"{produto} ...... R$ {preco:.2f}", key=f"chk_{produto}"):
        quantidade = st.number_input(f"Quantos {produto} deseja?", min_value=1, step=1, key=f"qtd_{produto}")
        selecionados.append({"produto": produto, "quantidade": quantidade, "preco": preco})

# Botão para adicionar os itens à sacola
total_itens = sum(item["quantidade"] for item in selecionados)
if total_itens > 0 and st.button("Adicionar à sacola"):
    st.session_state.sacola.extend(selecionados)
    st.success("Itens adicionados à sacola!")

# Exibir a sacola de compras
st.markdown("### 🛒 Sua Sacola")
if st.session_state.sacola:
    total = 0
    for item in st.session_state.sacola:
        subtotal = item["quantidade"] * item["preco"]
        st.write(f"{item['quantidade']}x {item['produto']} - R$ {subtotal:.2f}")
        total += subtotal
    
    st.write(f"**Total: R$ {total:.2f}**")

    # Botão para finalizar o pedido
    if st.button("Finalizar Pedido"):
        st.success("✅ Pedido finalizado com sucesso! Obrigado pela compra. 🎁")

        # Criar arquivo CSV se não existir
        if not os.path.exists(pedidos_csv):
            with open(pedidos_csv, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Produto", "Quantidade", "Preço Unitário", "Subtotal"])

        # Salvar os pedidos
        with open(pedidos_csv, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for item in st.session_state.sacola:
                writer.writerow([item["produto"], item["quantidade"], item["preco"], item["quantidade"] * item["preco"]])
        
        # Limpar a sacola após finalização do pedido
        st.session_state.sacola.clear()
else:
    st.write("Sua sacola está vazia.")
