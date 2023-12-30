import streamlit as st
import pandas as pd
import numpy as np

# visualization
import plotly.graph_objects as go

# STATE LEVEL analytics
# -----------------------------------
# df already loaded from main.py and imported


# this is random numbers for now
map_data = pd.DataFrame(np.random.uniform(low=36.9, high=41.1, size=(100, 1)), columns=['lat'])
map_data['lon'] = np.random.uniform(low=-109.1, high=-102.0, size=(100, 1))


# Presentation
# -----------------------------------
st.title("Colorado State-Level Analytics")
st.map(map_data)


def show_overview():
    st.write("This is the overview page")
    st.map(map_data)
    

def show_business_entity_types(df):
    df_exists = df[df['entitystatus'].isin(['Good Standing', 'Exists'])]
    top_10_entity_types = df_exists['entitytype'].value_counts(normalize=True).head(10) * 100

    fig = go.Figure(data=[go.Bar(
        x=top_10_entity_types.index,
        y=top_10_entity_types.values,
        hovertext=top_10_entity_types.values.round(2).astype(str),
        hoverinfo='text'
    )])

    fig.update_layout(
        title='Distribution of Top 10 Entity Types in df_exists',
        xaxis=dict(title='Entity Type'),
        yaxis=dict(title='Percentage'),
        xaxis_tickangle=-45
    )

    fig2 = go.Figure(data=[go.Bar(
        x=top_10_entity_types.index,
        y=top_10_entity_types.values,
        hovertemplate=
            "<b>%{x}</b><br><br>" +
            "Percentage: %{y:.2f}%<br>",
        hoverinfo='text'
    )])

    fig2.update_layout(
        title='Distribution of Top 10 Entity Types in df_exists (with percentage)',
        xaxis=dict(title='Entity Type'),
        yaxis=dict(title='Percentage'),
        xaxis_tickangle=-45
    )

    st.plotly_chart(fig, use_container_width=True)
    st.plotly_chart(fig2, use_container_width=True)
    st.write(df_exists.head())
   



