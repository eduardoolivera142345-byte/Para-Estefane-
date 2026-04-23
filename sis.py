import streamlit as st
import time

# Configuração da página (Título que aparece na aba do navegador)
st.set_page_config(page_title="Dindin da Cristina - Delivery", page_icon="🍦", layout="centered")

# Estilo para deixar o site bonito e profissional
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .header-box {
        background-color: #ff4b4b;
        padding: 20px;
        border-radius: 0px 0px 20px 20px;
        color: white;
        text-align: center;
        margin-bottom: 20px;
    }
    .category-title {
        background-color: #eee;
        padding: 10px;
        border-radius: 10px;
        font-weight: bold;
        color: #333;
        margin: 20px 0px 10px 0px;
    }
    .product-card {
        background-color: white;
        padding: 15px;
        border-radius: 15px;
        border-left: 5px solid #ff4b4b;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 10px;
    }
    .price-tag { color: #28a745; font-weight: bold; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

# Cabeçalho do Site
st.markdown("""
    <div class="header-box">
        <h1>🍦 Dindin da Cristina</h1>
        <p>📍 Travessa Nossa Senhora da Conceição</p>
        <p>🕒 Aberto agora • Pedido mínimo: R$ 10,00</p>
    </div>
    """, unsafe_allow_html=True)

st.write("### 📜 Nosso Cardápio")
st.info("Faça sua seleção abaixo e finalize o pedido no final da página.")

# --- CATEGORIA GOURMET ---
st.markdown('<div class="category-title">✨ DINDIN GOURMET - R$ 2,50</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="product-card"><b>🍫 Ninho com Nutella</b><br><span class="price-tag">R$ 2,50</span></div>', unsafe_allow_html=True)
    if st.button("Adicionar Ninho + Nutella"):
        st.toast("Ninho com Nutella adicionado!")

    st.markdown('<div class="product-card"><b>🍪 Oreo Especial</b><br><span class="price-tag">R$ 2,50</span></div>', unsafe_allow_html=True)
    if st.button("Adicionar Oreo"):
        st.toast("Oreo adicionado!")

with col2:
    st.markdown('<div class="product-card"><b>🍓 Morango Gourmet</b><br><span class="price-tag">R$ 2,50</span></div>', unsafe_allow_html=True)
    if st.button("Adicionar Morango"):
        st.toast("Morango Gourmet adicionado!")

    st.markdown('<div class="product-card"><b>🥥 Prestígio Cremoso</b><br><span class="price-tag">R$ 2,50</span></div>', unsafe_allow_html=True)
    if st.button("Adicionar Prestígio"):
        st.toast("Prestígio adicionado!")

# --- CATEGORIA TRADICIONAL ---
st.markdown('<div class="category-title">🍦 DINDIN TRADICIONAL - R$ 2,00</div>', unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown('<div class="product-card"><b>🥭 Manga</b><br><span class="price-tag">R$ 2,00</span></div>', unsafe_allow_html=True)
    if st.button("Adicionar Manga"):
        st.toast("Manga adicionada!")

    st.markdown('<div class="product-card"><b>🥥 Coco</b><br><span class="price-tag">R$ 2,00</span></div>', unsafe_allow_html=True)
    if st.button("Adicionar Coco"):
        st.toast("Coco adicionado!")

with col4:
    st.markdown('<div class="product-card"><b>🍇 Uva</b><br><span class="price-tag">R$ 2,00</span></div>', unsafe_allow_html=True)
    if st.button("Adicionar Uva"):
        st.toast("Uva adicionada!")

    st.markdown('<div class="product-card"><b>🍍 Abacaxi</b><br><span class="price-tag">R$ 2,00</span></div>', unsafe_allow_html=True)
    if st.button("Adicionar Abacaxi"):
        st.toast("Abacaxi adicionado!")

# --- CARRINHO E FINALIZAÇÃO ---
st.markdown("---")
st.write("### 🛍️ Finalizar Pedido")

nome_cliente = st.text_input("Seu Nome:")
forma_pagamento = st.selectbox("Como deseja pagar?", ["Pix", "Dinheiro (Levar troco)", "Cartão na Entrega"])

if st.button("🚀 ENVIAR PEDIDO AGORA"):
    if nome_cliente:
        with st.status("Enviando pedido para a Cristina...", expanded=True) as status:
            time.sleep(1)
            st.write("Organizando sacola...")
            time.sleep(1)
            st.write("Calculando rota de entrega...")
            time.sleep(1)
            status.update(label="Pedido Confirmado!", state="complete", expanded=False)
        
        st.balloons()
        st.success(f"Parabéns **{nome_cliente}**! Seu pedido foi enviado para a **Travessa Nossa Senhora da Conceição**.")
        st.warning("Aguarde o contato da Cristina para confirmar a entrega!")
    else:
        st.error("Por favor, digite seu nome para que possamos te identificar!")
