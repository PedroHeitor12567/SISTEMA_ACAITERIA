import streamlit as st
import os
import csv

st.set_page_config(page_title="Painel do Administrador", layout="wide")
st.title("Painel do Administrador - Loja de Açaí")

arquivo = "pedido.csv"

if st.button("🔄 Atualizar Pedidos"):
    st.rerun()

if os.path.exists(arquivo):
    pedidos = []
    with open(arquivo, mode="r", newline="", encoding="utf-8") as file:
        leitor = csv.DictReader(file)
        pedidos = [dict(linha) for linha in leitor]

    if not pedidos:
        st.info("Nenhum pedido encontrado.")
    else:
        st.subheader("📦 Pedidos Recebidos")

        pedidos_restantes = pedidos.copy()

        for pedido in pedidos:
            with st.expander(f"🆔 Pedido {pedido.get('id', 'Desconhecido')} - {pedido.get('nome_cliente', 'Cliente')}"):
                st.write(f"📍 **Endereço:** {pedido.get('endereco', 'Não informado')}")
                st.write(f"🍹 **Produto:** {pedido.get('produto', 'Desconhecido')}")
                st.write(f"🛍 **Itens:** {pedido.get('itens', 'Sem itens')}")
                st.write(f"💰 **Preço Total:** {pedido.get('preco_total', 'R$ 0,00')}")
                st.write(f"🔖 **Status:** {pedido.get('status', 'Pendente')}")

                col1, col2 = st.columns(2)

                with col1:
                    if st.button(f"✅ Aceitar {pedido.get('id', 'Desconhecido')}", key=f"aceitar_{pedido.get('id', 'Desconhecido')}"):
                        pedido["status"] = "Aceito"
                        with open("pedidos_aceitos.csv", mode="a", newline="", encoding="utf-8") as file_aceito:
                            writer = csv.DictWriter(file_aceito, fieldnames=pedido.keys())
                            if not os.path.exists("pedidos_aceitos.csv"):
                                writer.writeheader()
                            writer.writerow(pedido)
                        st.success(f"Pedido {pedido.get('id', 'Desconhecido')} aceito!")

                with col2:
                    if st.button(f"❌ Recusar {pedido.get('id', 'Desconhecido')}", key=f"recusar_{pedido.get('id', 'Desconhecido')}"):
                        pedidos_restantes.remove(pedido) 

                        with open(arquivo, mode="w", newline="", encoding="utf-8") as file:
                            fieldnames = pedidos[0].keys() if pedidos else ["id", "nome_cliente", "produto", "itens", "preco_total", "endereco", "adicionais"]
                            writer = csv.DictWriter(file, fieldnames=fieldnames)
                            writer.writeheader()
                            writer.writerows(pedidos_restantes)

                        st.warning(f"Pedido {pedido.get('id', 'Desconhecido')} recusado e removido!")
                        st.rerun()  

else:
    st.error("Não há pedidos.")
