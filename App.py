# %%writefile app6.py

# Import required libraries
import google.generativeai as genai
from PIL import Image
import streamlit as st

# Configure API key for generative AI
api_key = "AIzaSyA1OHmASnpSH03l3jw6zVmDrWlgXUo4cxk"
genai.configure(api_key=api_key)

# Streamlit app setup
st.set_page_config(
    page_title="PixelPerfect AI: Image Insight & Exploration",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for enhanced styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(45deg, #ff7b72, #ff3e30);
        font-family: 'Verdana', sans-serif;
        color: #fff;
        margin: 0;
        padding: 0;
        text-align: center;
    }
    .stButton button {
        background-color: #ff3e30;
        color: white;
        font-size: 18px;
        padding: 14px 28px;
        border-radius: 30px;
        border: none;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.15);
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        background-color: #ff2a1e;
        transform: scale(1.05);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
    }
    h1 {
        font-size: 56px;
        color: #fefefe;
        font-weight: bold;
        margin-top: 60px;
        letter-spacing: 3px;
        text-transform: uppercase;
    }
    h2 {
        color: #fff;
        font-size: 32px;
        margin-bottom: 30px;
    }
    .stTextInput input {
        font-size: 18px;
        border-radius: 10px;
        padding: 12px;
        border: 2px solid #ff3e30;
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
    }
    .stTextInput input:focus {
        border-color: #ff2a1e;
    }
    .stImage img {
        border-radius: 20px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .stImage img:hover {
        transform: scale(1.05);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.4);
    }
    .stMarkdown {
        font-size: 20px;
        color: #fefefe;
        padding: 12px 0;
    }
    .header {
        background-color: #ff3e30;
        color: white;
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }
    .footer {
        background-color: #2d3e50;
        color: white;
        padding: 25px 0;
        text-align: center;
        margin-top: 40px;
        font-size: 18px;
        border-radius: 10px;
    }
    .footer a {
        color: #fefefe;
        text-decoration: none;
        font-weight: bold;
    }
    .footer a:hover {
        color: #ff3e30;
    }
    </style>
""", unsafe_allow_html=True)

# Page Header
st.title("🎨 PixelPerfect AI")
st.subheader("Unlocking Visual Intelligence")

st.write(
    """
    **PixelPerfect AI** is your personal assistant for analyzing and exploring images.
    Upload an image and ask any question about it. Get powerful, AI-generated insights in seconds.

    **Upload an image or ask anything about it, and I will provide you with a comprehensive analysis!**
    """
)

# Upload File Section
st.header("📂 Upload Your Image")
uploaded_file = st.file_uploader(
    "Choose an image file (JPG, PNG, JPEG):", 
    type=['jpg', 'png', 'jpeg']
)

# Display uploaded image
if uploaded_file is not None:
    st.image(Image.open(uploaded_file), caption="Uploaded Image", use_column_width=True)

# Input for user prompt
st.header("💡 Ask Your Question")
prompt = st.text_input("Enter your prompt or question about the image:")

# Generate AI response
if st.button("Generate Insight"):
    if uploaded_file is not None and prompt.strip():
        img = Image.open(uploaded_file)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content([prompt, img])
        st.success("Here's your AI-powered response:")
        st.write(response.text)
    else:
        st.error("Please upload an image and enter a valid prompt.")

# Footer Section
st.markdown(
    """
    <div class="footer">
        <p>Developed by <strong>Abhinish Tiwari</strong></p>
        <p>Powered by Streamlit & Google Generative AI</p>
        <a href="https://github.com/abhinishtiwari" target="_blank">Visit my GitHub</a>
    </div>
    """, unsafe_allow_html=True
)
