import streamlit as st

# Configurações da página
st.set_page_config(page_title="Para Meu Amor", page_icon="❤️")

st.title("Validação de Acesso ❤️")
st.write("Somente a pessoa certa pode entrar aqui.")

# Campos de entrada
nome = st.text_input("Digite seu nome:")
senha = st.text_input("Qual a nossa data de namoro? (DDMMYY)", type="password")

if st.button("Verificar"):
    # Ajuste aqui os valores se precisar
    if nome == "Estefane" and senha == "190325":
        st.balloons() # Faz balões subirem na tela
        st.success(f"Que bom que você acertou, {nome}! ❤️")
        st.write("### Eu te amo muito!")
        
        # Opcional: Você pode colocar um link para uma foto de vocês aqui
        st.image("lv_7283941053110045957_20260217044534.mp4") 
    else:
        st.error("Ops! O nome ou a data estão incorretos. Tente de novo.")
