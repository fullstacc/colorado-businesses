import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px


# # this is random numbers for now
map_data = pd.DataFrame(np.random.uniform(low=36.9, high=41.1, size=(100, 1)), columns=['lat'])
map_data['lon'] = np.random.uniform(low=-109.1, high=-102.0, size=(100, 1))


def show_state_overview(df):
    st.title("Colorado State-Level Analytics")    

    # Radio button for entity status
    entity_status = st.radio("Entity Status", ["Show me Current Business Data", "Show me All-Time Business Data"])
    if entity_status == "Show me Current Business Data":
        df_exists = df[df['entitystatus'].isin(['Good Standing', 'Exists'])]

        # Display the total number of businesses
        total_businesses = len(df_exists)
        formatted_total_businesses = "{:,}".format(total_businesses)
        st.write(f"There are {formatted_total_businesses} active businesses in Colorado")


    else:
        df_exists = df

        # TODO: Fix this logic. Inconsistent number of businesses formed in 2023. Earliest date shows 1975 but should be earlier.
        # Display the total number of businesses
        total_businesses = len(df_exists)
        formatted_total_businesses = "{:,}".format(total_businesses)
        earliest_entityformdate = df_exists['entityformdate'].min()
        latest_entityformdate = df_exists['entityformdate'].max()
        st.write(f"There have been {formatted_total_businesses} businesses in Colorado from {earliest_entityformdate} to {latest_entityformdate}")
    
    
    

    # Line chart showing the count of businesses formed over the last 5 years
    st.title("Total Number of Businesses Formed in Last 5 Years")  # Add title
    df_exists['year'] = pd.to_datetime(df_exists['entityformdate']).dt.year
    df_last_5_years = df_exists[df_exists['year'] >= df_exists['year'].max() - 5]
    business_count_by_year = df_last_5_years.groupby('year').size().reset_index(name='count')
    fig1 = px.line(business_count_by_year, x='year', y='count')
    st.plotly_chart(fig1)
    

    # Bar chart showing the count of businesses over the last 5 years
    fig2 = px.bar(business_count_by_year, x='year', y='count')
    st.plotly_chart(fig2)

    # trend analysis: how have business filings varied month-over-month in the last 12 months?

    