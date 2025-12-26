import streamlit as st

with open("product.md", "r", encoding="utf-8") as f:
    context = f.read()

st.title("Local Culture AI")

question = st.text_input("Ask about local culture:")

if question:
    st.write("Answer based on local context:")
    st.write(context)
