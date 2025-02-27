import streamlit as st
import os
import csv

st.title("Painel do Administrador - Loja de Açaí")


if st.button("Receber Pedidos"):

    if os.path.exists("usuario_logado.csv"):
        pedidos = []
        with open("usuario_logado.csv", mode="r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                pedidos.append(linha)
        
        if not pedidos:
            st.info("Nenhum pedido encontrado.")
        else:
            st.subheader("Pedidos Recebidos")

            st.table(pedidos)
            

            for pedido in pedidos:
                with st.expander(f"Pedido {pedido['id']} - {pedido['nome_cliente']}"):
                    st.write(f"*Itens:* {pedido['itens']}")
                    st.write(f"*Status:* {pedido['status']}")
    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        if st.button("Aceitar", key=f"aceitar_{pedido['id']}"):
                            # Verifica se o arquivo de pedidos aceitos já existe
                            file_exists = os.path.exists("pedidos_aceitos.csv")
                            
                            # Abre o arquivo em modo de append para adicionar o pedido aceito
                            with open("pedidos_aceitos.csv", mode="a", newline="", encoding="utf-8") as arquivo_aceito:
                                writer = csv.DictWriter(arquivo_aceito, fieldnames=pedido.keys())
                                # Se o arquivo não existir, escreve o cabeçalho
                                if not file_exists:
                                    writer.writeheader()
                                writer.writerow(pedido)
                            
                            st.success("Pedido aceito!")
                    
                    with col2:
                        if st.button("Recusar", key=f"recusar_{pedido['id']}"):
                            st.info("Pedido recusado!")
    else:
        st.error("Arquivo 'pedidos.csv' não foi encontrado.")