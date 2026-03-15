import streamlit as st
from googletrans import Translator

st.title("Language Translation Tool")

translator = Translator()

text = st.text_area("Enter text to translate")

source = st.selectbox(
    "Source Language",
    ["auto", "en", "hi", "mr", "fr", "de"]
)

target = st.selectbox(
    "Target Language",
    ["en", "hi", "mr", "fr", "de"]
)

if st.button("Translate"):
    translation = translator.translate(text, src=source, dest=target)
    st.success("Translated Text:")
    st.write(translation.text)