import streamlit as st
from googletrans import Translator

st.title("Language Translation Tool")

translator = Translator()

text = st.text_area("Enter text to translate")

source = st.selectbox(
    "Source Language",
    ["auto", "English", "Hindi", "Marathi", "French"]
)

target = st.selectbox(
    "Target Language",
    ["English", "Hindi", "Marathi", "French"]
)

if st.button("Translate"):
    translation = translator.translate(text, src=source, dest=target)
    st.success("Translated Text:")
    st.write(translation.text)
