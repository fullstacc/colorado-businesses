import streamlit as st

import plotly.graph_objects as go


def show_trend_analysis(df):
    st.dataframe(df.head(10))
    # TODO: 
    # Is there an increasing trend in the number of business filings in Colorado over the past 5 years? (entityformdate)
    # What has been the trend in business filings over the past 10 years? (entityformdate)
    # How have business filings varied month-over-month in the last 12 months? (entityformdate)
