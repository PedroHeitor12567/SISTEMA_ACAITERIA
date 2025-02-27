import streamlit as st
import csv
import os
import uuid

st.title("O que deseja consumir?")
st.write("Selecione um produto para continuar.")

if "sacola" not in st.session_state:
    st.session_state.sacola = []

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🥤 Guaraçaí"):
        st.session_state.produto_selecionado = "Guaraçaí"
with col2:
    if st.button("🍨 Açaí"):
        st.session_state.produto_selecionado = "Açaí"
with col3:
    if st.button("🍦 Sorvete"):
        st.session_state.produto_selecionado = "Sorvete"

if "produto_selecionado" in st.session_state:
    produto_nome = st.session_state.produto_selecionado
    arquivo_csv = "pedido.csv"
    
    st.write(f"Escolha seu {produto_nome}")
    produtos = {
        "Copo 250 ml": 5.00,
        "Copo 300 ml": 6.00,
        "Copo 400 ml": 8.00,
        "Copo 500 ml": 10.00
    }
    
    selecionados = []
    for produto, preco in produtos.items():
        key_produto = produto.replace(" ", "_").lower()
        if st.checkbox(f"{produto}", key=f"chk_{key_produto}"):
            quantidade = st.number_input(f"Quantos {produto} deseja?", min_value=1, step=1, key=f"qtd_{key_produto}")
            selecionados.append([produto, quantidade, preco])
    
    adicionais_selecionados = []
    adicionais = [
        "Granulado De Chocolate", "Tubet's Tradicional", "Cereal De Chocolate", "Castanha Triturado",
        "Amendoim Em Banda", "Abacaxi Ao Vinho", "Choco Leitinho", "Creme De Paçoca", "Aveia Em Flocos",
        "Creme De Valsa", "Creme De Avelã", "Choco Waffer", "Marshmallow", "Bis Original",
        "Chocotrufa", "Coco Ralado", "Morango", "Paçoca", "Jujuba", "Óreo", "Kiwi",
        "Amendoim Triturado", "Granulado Colorido", "Granulado Em Flocos", "Recheio De Morango",
        "Tubet's Recheado", "Choco Bueníssimo", "Chocolate Branco", "Choco Pão De Mel", "Farinha Láctea",
        "Flocos De Arroz", "Ovomaltine", "Chocotine", "Leite Em Pó", "Bis Branco", "Oro Negro",
        "Granola", "Confete", "Banana", "Cereal", "Cereja", "Uva"
    ]
    
    if produto_nome in ["Açaí", "Sorvete"]:
        st.write("### Escolha seus adicionais (opcional)")
        for adicional in adicionais:
            if st.checkbox(adicional, key=f"chk_{adicional}"):
                adicionais_selecionados.append(adicional)
    
    if selecionados:
        if st.button("Adicionar à sacola"):
            for item in selecionados:
                st.session_state.sacola.append([item[0], item[1], item[2], adicionais_selecionados])
            st.success("Itens adicionados à sacola!")
    
    sacola_container = st.container()
    with sacola_container:
        st.markdown("### 🛒 Sua Sacola")
        if st.session_state.sacola:
            total = 0
            for item in st.session_state.sacola:
                subtotal = item[1] * item[2]
                adicionais_txt = ", ".join(item[3]) if item[3] else "Sem adicionais"
                st.write(f"{item[1]}x {item[0]} - R$ {subtotal:.2f} ({adicionais_txt})")
                total += subtotal
            st.write(f"**Total: R$ {total:.2f}**")
        else:
            st.write("Sua sacola está vazia.")
    
    nome_cliente = st.text_input("Digite seu nome:", key="nome_cliente_input")
    endereco = st.text_input("Digite seu endereço:", key="endereco_input")
    
    if st.button("Finalizar Pedido"):
        if not nome_cliente.strip():
            st.error("Por favor, insira seu nome para finalizar o pedido.")
        elif not endereco.strip():
            st.error("Por favor, insira seu endereço para finalizar o pedido.")
        else:
            file_exists = os.path.exists(arquivo_csv)
            with open(arquivo_csv, mode="a", newline="", encoding="utf-8") as file:
                fieldnames = ["id", "nome_cliente", "endereco", "produto", "itens", "preco_total", "adicionais", "status"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                if not file_exists:
                    writer.writeheader()
                
                pedido_id = str(uuid.uuid4())[:8]
                itens_formatados = "; ".join([f"{item[1]}x {item[0]}" for item in st.session_state.sacola])
                preco_total = sum(item[1] * item[2] for item in st.session_state.sacola)
                adicionais_txt = "; ".join(set([adicional for item in st.session_state.sacola for adicional in item[3]]))
                
                writer.writerow({
                    "id": pedido_id,
                    "nome_cliente": nome_cliente,
                    "endereco": endereco,
                    "produto": produto_nome,
                    "itens": itens_formatados,
                    "preco_total": f"R$ {preco_total:.2f}",
                    "adicionais": adicionais_txt,
                    "status": "Pendente"
                })
            
            st.success("✅ Pedido finalizado com sucesso! Obrigado pela compra. 🎁")
            sacola_container.empty()
            st.session_state.sacola = []
