import streamlit as st
import urllib.parse

# Configuração da página
st.set_page_config(page_title="Dindin da Cristina", page_icon="🍦", layout="centered")

# --- ESTILO PROFISSIONAL (CSS) ---
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { background-color: #ffffff; }
    .product-box {
        display: flex;
        align-items: center;
        background-color: #f9f9f9;
        padding: 10px;
        border-radius: 15px;
        margin-bottom: 15px;
        border: 1px solid #eee;
    }
    .product-img {
        width: 80px;
        height: 80px;
        border-radius: 10px;
        object-fit: cover;
        margin-right: 15px;
    }
    .product-info { flex-grow: 1; }
    .product-name { font-weight: bold; font-size: 16px; margin: 0; }
    .product-price { color: #28a745; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# Cabeçalho
st.image("https://images.unsplash.com/photo-1551024601-bec78aea704b?w=800&q=80", use_container_width=True) # Foto de capa
st.title("🍦 Dindin da Cristina")
st.caption("📍 Travessa Nossa Senhora da Conceição | 🛵 Entrega Rápida")

if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

def add(n, p):
    st.session_state.carrinho.append({"n": n, "p": p})
    st.toast(f"Adicionado: {n}")

# --- FUNÇÃO PARA CRIAR ITEM COM FOTO ---
def criar_item(nome, preco, img_url):
    col_foto, col_info, col_btn = st.columns([1, 2, 1])
    with col_foto:
        st.image(img_url, width=80)
    with col_info:
        st.markdown(f"**{nome}**")
        st.markdown(f"<span style='color:green'>R$ {preco:.2f}</span>", unsafe_allow_html=True)
    with col_btn:
        if st.button("Add", key=nome):
            add(nome, preco)
    st.divider()

# --- SEÇÃO GOURMET ---
st.subheader("✨ Linha Gourmet - R$ 2,50")
criar_item("Ninho com Nutella", 2.50, "https://cdn.pixabay.com/photo/2017/04/19/20/03/ice-cream-2243402_1280.jpg")
criar_item("Oreo Especial", 2.50, "https://cdn.pixabay.com/photo/2016/03/31/21/53/ice-cream-1296707_1280.png")

# --- SEÇÃO TRADICIONAL ---
st.subheader("🍦 Linha Tradicional - R$ 2,00")
criar_item("Manga Natural", 2.00, "https://cdn.pixabay.com/photo/2016/03/31/18/07/fruit-1294125_1280.png")
criar_item("Coco Cremoso", 2.00, "https://cdn.pixabay.com/photo/2014/12/21/23/34/coconut-575510_1280.png")

# --- FINALIZAÇÃO ---
if st.session_state.carrinho:
    st.sidebar.header("🛒 Seu Carrinho")
    total = 0
    resumo = ""
    for i in st.session_state.carrinho:
        st.sidebar.write(f"{i['n']} - R$ {i['p']:.2f}")
        total += i['p']
        resumo += f"- {i['n']} (R$ {i['p']:.2f})\n"
    
    st.sidebar.write(f"### Total: R$ {total:.2f}")
    
    with st.expander("Finalizar Pedido"):
        nome = st.text_input("Seu Nome")
        cpf = st.text_input("CPF")
        endereco = st.text_input("Endereço completo")
        cel = st.text_input("Celular")
        
        if st.button("Enviar para o WhatsApp"):
            msg = f"Dindin da Cristina!\n\nPedido:\n{resumo}\nTotal: R$ {total:.2f}\n\nCliente: {nome}\nCPF: {cpf}\nEnd: {endereco}\nCel: {cel}"
            link = f"https://wa.me/5583993856238?text={urllib.parse.quote(msg)}"
            st.link_button("📲 Confirmar no WhatsApp", link)
            
