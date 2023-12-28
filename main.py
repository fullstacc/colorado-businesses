import streamlit as st
from pages import home
from utils import data_loader  # Import utility functions

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a page", ["Home", "State-Level Data", "County-Level Data", "About"])

# Display the selected page
if page == "Home":
    home.show()
# elif page == "Page 1":
#     page1.show()
# elif page == "Page 2":
#     page2.show()
