import streamlit as st
from PIL import Image
import base64

# Set page configuration
st.set_page_config(
    page_title="Resource Mapping and Analysis",
    layout="wide"
)

# Set background image function
def set_background(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background image directly
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1920&q=80");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set title with white font color
st.markdown(
    """
    <h1 style='color: white;'>Resource Mapping and Analysis Using Satellite Imagery from Remote Sensing High Resolution Data using AI/ML</h1>
    """,
    unsafe_allow_html=True
)

# Add content with white font color
st.markdown(
    """
    <p style='color: white;'>Welcome to our resource mapping and analysis tool.</p>
    """,
    unsafe_allow_html=True
)

# Add buttons
if st.button("Upload Your Image"):
    st.write("Button 'Upload Your Image' clicked.")

if st.button("Search from Map"):
    st.write("Button 'Search from Map' clicked.")

# You can add more Streamlit components here as needed
