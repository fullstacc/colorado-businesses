import streamlit as st
import pandas as pd
import numpy as np

# visualization
import plotly.graph_objects as go


# STATE LEVEL analytics
# -----------------------------------
# df already loaded from main.py and imported


# # this is random numbers for now
map_data = pd.DataFrame(np.random.uniform(low=36.9, high=41.1, size=(100, 1)), columns=['lat'])
map_data['lon'] = np.random.uniform(low=-109.1, high=-102.0, size=(100, 1))


# Presentation
# -----------------------------------
st.title("Colorado State-Level Analytics")

st.map(map_data)


def show_overview():
    st.write("This is the overview page")
    st.map(map_data)
    

        



