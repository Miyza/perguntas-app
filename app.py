import streamlit as st

st.title("Perguntas")

nome = st.text_input("Qual seu nome?")
idade = st.text_input("Qual sua idade?")
cor = st.text_input("Qual sua cor favorita?")

if st.button("Enviar"):
    st.write(f"Olá {nome}, você tem {idade} anos e gosta de {cor}.")
