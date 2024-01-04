import streamlit as st
# page config
st.set_page_config(page_title="Colorado Business Data Dashboard", page_icon="static/co-favicon.png")

from views import state, about
# from utils import data_loader  # Import utility functions


# data science
import pandas as pd
import numpy as npx

# import dataframe for the rest of the app to use
# based on the st docs, this will load df into memory and the rest of the pages can use it
df = pd.read_csv('Business.csv')

# visualization
from visualizations.foreign_investment import show_foreign_investment
from visualizations.business_entity_types import show_business_entity_types
from visualizations.state_overview import show_state_overview


# flag
st.sidebar.image('static/colorado_flag.svg', width=100)

top_level = st.sidebar.selectbox("Choose a category", ["Home", "State-Level Analytics", "County-Level Analytics"])


if top_level == "State-Level Analytics":
    second_level = st.sidebar.selectbox("Choose a sub-category", ["Overview", "Business Entity Types","Foreign Investment", "Trend Analysis"], index=0)
    if second_level == "Business Entity Types":
        show_business_entity_types(df)
    elif second_level == "Foreign Investment":
        show_foreign_investment(df)
    elif second_level == "Trend Analysis":
        state.show_trend_analysis(df)
    else:
        show_state_overview(df)
elif top_level == "County-Level Analytics":
    st.title("Coming Soon!")
elif top_level == "Home":
    st.title("Colorado Business Data Dashboard")
    st.write("Welcome to the Colorado Business Data Dashboard!")
    st.write("This dashboard provides an interactive way to explore business data in Colorado.")
    st.write("Use the sidebar to navigate between pages.")
else:
    st.write("Please select a category from the sidebar.")




# # Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )

# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )