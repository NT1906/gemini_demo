import PIL.Image
import streamlit as st
import google.generativeai as genai
from config import GOOGLE_API_KEY

st.title("Image to text generator")
st.divider()


uploaded_file = st.file_uploader("Choose a file")


if uploaded_file is not None:
    # Read the uploaded file as an image
    img = PIL.Image.open(uploaded_file)
    st.image(uploaded_file)
    # Setup your API key
    genai.configure(api_key=GOOGLE_API_KEY)

    # Use the gemini-pro model for text generation
    model = genai.GenerativeModel('gemini-pro-vision')

    # Generate text from the converted image text
    response = model.generate_content(img)
    st.write(response.text)
    

   
    
