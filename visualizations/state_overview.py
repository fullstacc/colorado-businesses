import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px

from . import time_series_summary_tools


def show_state_overview(df):
    df.loc[:, 'year'] = pd.to_datetime(df['entityformdate']).dt.year
    full_data = df
    df_alltime = full_data
    st.title("Colorado State-Level Analytics") 

    

    # Radio button for entity status
    entity_status_help = '''"Current" businesses are businesses listed as 'In good standing' or 'Exists' '''.strip()
    entity_status = st.radio("Entity Status", ["Show me Current Business Data", "Show me All-Time Business Data"], help=entity_status_help)
    

    
    if entity_status == "Show me Current Business Data":
        # CURRENT BUSINESS DATA
        # ---------------------
        df_exists = df.copy(deep=True)
        df_exists = df_exists[df_exists['entitystatus'].isin(['Good Standing', 'Exists'])]
        
        summary_options = ["Show 5 Year Summary", "Show 10 Year Summary", "Show Past Year Summary", "Show Custom Summary"]
        selected_option = st.radio("Summary Options", summary_options)
    
        if selected_option == "Show 5 Year Summary":
            # Display the total number of current businesses
            total_businesses = len(df_exists)
            
            # summary
            time_series_summary_tools.show_total_businesses(df_exists)

            # line graph and table for 5 year summary
            time_series_summary_tools.show_line_graph(df_exists, "5 Year")   

            
        elif selected_option == "Show 10 Year Summary":
            
            # summary
            time_series_summary_tools.show_total_businesses(df_exists)

            time_series_summary_tools.show_line_graph(df_exists, "10 Year")   

        elif selected_option == "Show Past Year Summary":
            st.write("Coming Soon!")

            time_series_summary_tools.show_past_year_graph(df_exists)

            # # Display the markdown table
            # st.markdown(markdown_table)


        elif selected_option == "Show Custom Summary":
            st.write("Coming Soon!")
        
        

    else:
        # show all-time data
        # ------------------
        df_alltime = full_data

        # summary
        time_series_summary_tools.show_total_businesses(full_data, active=False)
    
# trend analysis: how have business filings varied month-over-month in the last 12 months?

    