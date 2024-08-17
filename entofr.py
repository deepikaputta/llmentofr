
import streamlit as st
from transformers import pipeline

# Replace with your actual API token
API_TOKEN = ''

# Initialize the Hugging Face translation pipeline with the specific model
@st.cache_resource
def load_translation_pipeline():
    translator = pipeline(
    "translation_en_to_fr",
    model="Helsinki-NLP/opus-mt-en-fr"
    )

    return translator

translator = load_translation_pipeline()

# Streamlit app layout
st.title("Language Translation App")
st.header("Translate English to French")

# Input text box
input_text = st.text_area("Enter text in English:", height=200)

# Translate button
if st.button("Translate"):
    if input_text:
        # Translate text
        translation = translator(input_text)
        translated_text = translation[0]['translation_text']
        # Display translated text
        st.subheader("Translated Text:")
        st.write(translated_text)
    else:
        st.warning("Please enter text to translate.")
