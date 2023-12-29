import streamlit as st
import pandas as pd
import numpy as np

# visualization
import plotly.graph_objects as go

df = pd.read_csv('Business.csv')
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





def show():
    st.title("Home Page")
    st.write("Welcome to the Colorado Business Data Dashboard!")
    st.write("This dashboard provides an interactive way to explore business data in Colorado.")
    st.write("Use the sidebar to navigate between pages.")

    map_data = pd.DataFrame(np.random.uniform(low=36.9, high=41.1, size=(100, 1)), columns=['lat'])
    map_data['lon'] = np.random.uniform(low=-109.1, high=-102.0, size=(100, 1))

    st.map(map_data)

    st.plotly_chart(fig, use_container_width=True)
    st.plotly_chart(fig2, use_container_width=True)
    st.write(df_exists.head())


"""
## Refactored Key Questions
- Which **counties** in Colorado have the highest number of business filings?
- What specific **regions** in Colorado show the highest number of business filings? *(Note: Define "regions" if it refers to specific geographical/administrative areas.)*
- At the state level, which **types of businesses** or **industries** are most prevalent?
- Is there foreign investment in Colorado? If so, which countries are investing and where?
- What business types are most prevalent? Was this always the case?
- On a county basis, which **types of businesses** or **industries** are most common?
- In different regions, what are the most common **types of businesses** or **industries**?
- **Trend Analysis:** Is there an increasing trend in the number of business filings in Colorado over the past 5 years?
- **Trend Analysis:** What has been the trend in business filings over the past 10 years?
- **Trend Analysis:** How have business filings varied month-over-month in the last 12 months?
"""
   

"""
# 12/28/2023: Do I have the data required to group by type or by industry? - No, not with the current dataset

"""

