import streamlit as st
import time

# Configuração da página
st.set_page_config(page_title="Dindin do Amor - Cardápio", page_icon="🍦", layout="centered")

# Estilo personalizado para os cards e títulos
st.markdown("""
    <style>
    .main {
        background-color: #fff5f8;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #ff4b4b;
        color: white;
    }
    .flavor-card {
        padding: 15px;
        border-radius: 15px;
        background-color: white;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🍦 Dindin Gourmet & Cia")
st.write("Escolha seus sabores favoritos e faça seu pedido!")

# --- SEÇÃO GOURMET ---
st.markdown("## ✨ Linha Gourmet (R$ 5,00)")
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="flavor-card"><b>🍫 Ninho com Nutella</b><br>R$ 5,00</div>', unsafe_allow_html=True)
    if st.button("Adicionar Nutella"):
        st.toast("Adicionado ao carrinho!")

    st.markdown('<div class="flavor-card"><b>🍓 Morango com Nutella</b><br>R$ 5,00</div>', unsafe_allow_html=True)
    if st.button("Adicionar Morango Gourmet"):
        st.toast("Adicionado ao carrinho!")

with col2:
    st.markdown('<div class="flavor-card"><b>🍪 Oreo</b><br>R$ 5,00</div>', unsafe_allow_html=True)
    if st.button("Adicionar Oreo"):
        st.toast("Adicionado ao carrinho!")

    st.markdown('<div class="flavor-card"><b>🥥 Prestígio</b><br>R$ 5,00</div>', unsafe_allow_html=True)
    if st.button("Adicionar Prestígio"):
        st.toast("Adicionado ao carrinho!")

# --- SEÇÃO NORMAL ---
st.markdown("---")
st.markdown("## 🍦 Linha Tradicional (R$ 3,00)")
col3, col4 = st.columns(2)

with col3:
    st.markdown('<div class="flavor-card"><b>🥭 Manga</b><br>R$ 3,00</div>', unsafe_allow_html=True)
    if st.button("Adicionar Manga"):
        st.toast("Adicionado!")

    st.markdown('<div class="flavor-card"><b>🍍 Abacaxi</b><br>R$ 3,00</div>', unsafe_allow_html=True)
    if st.button("Adicionar Abacaxi"):
        st.toast("Adicionado!")

with col4:
    st.markdown('<div class="flavor-card"><b>🥥 Coco</b><br>R$ 3,00</div>', unsafe_allow_html=True)
    if st.button("Adicionar Coco"):
        st.toast("Adicionado!")

    st.markdown('<div class="flavor-card"><b>🍇 Uva</b><br>R$ 3,00</div>', unsafe_allow_html=True)
    if st.button("Adicionar Uva"):
        st.toast("Adicionado!")

# --- FINALIZAÇÃO ---
st.markdown("---")
st.write("### 🛒 Finalizar Pedido")
endereco = st.text_input("Digite seu endereço para entrega:")
forma_pagamento = st.selectbox("Forma de Pagamento", ["Pix", "Dinheiro", "Cartão"])

if st.button("ENVIAR PEDIDO 🚀"):
    if endereco:
        # Efeito de carregamento bonito
        with st.status("Processando seu pedido...", expanded=True) as status:
            st.write("Verificando estoque...")
            time.sleep(1.5)
            st.write("Preparando embalagem térmica...")
            time.sleep(1.5)
            st.write("Chamando o entregador...")
            time.sleep(1)
            status.update(label="Pedido Enviado com Sucesso!", state="complete", expanded=False)
        
        st.balloons()
        st.success(f"Tudo pronto! Seu Dindin será entregue em: **{endereco}**")
        st.info(f"Pagamento selecionado: {forma_pagamento}")
    else:
        st.error("Por favor, preencha o endereço antes de enviar.")
        
                 
