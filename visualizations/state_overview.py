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


            # Line chart showing the count of businesses formed over the last 5 years
            st.title("Total Number of Businesses Formed in Last 5 Years")  # Add title
            df_exists.loc[:, 'year'] = pd.to_datetime(df_exists['entityformdate']).dt.year
            df_last_5_years = df_exists[df_exists['year'] >= df_exists['year'].max() - 5]
            business_count_by_year = df_last_5_years.groupby('year').size().reset_index(name='count')
            fig1 = px.line(business_count_by_year, x='year', y='count')
            st.plotly_chart(fig1)

            # Calculate the total number of businesses formed for the previous 5 years
            current_year = pd.to_datetime('today').year
            previous_5_years = range(current_year - 5, current_year)
            business_count_by_year = df_exists[df_exists['year'].isin(previous_5_years)].groupby('year').size().reset_index(name='count')

            # Generate a markdown table
            markdown_table = "| Year | Total Businesses Formed | Percentage Change |\n"
            markdown_table += "|------|------------------------|------------------|\n"
            previous_count = None
            total_change = 0
            for index, row in business_count_by_year.iterrows():
                percentage_change = ""
                if previous_count is not None:
                    change = row['count'] - previous_count
                    total_change += change
                    percentage_change = f"{(change / previous_count) * 100:.2f}%"
                else:
                    percentage_change = "-"
                count_with_commas = "{:,}".format(row['count'])
                markdown_table += f"| {row['year']} | {count_with_commas} | {percentage_change} |\n"
                previous_count = row['count']
            
            # Calculate the total 5-year change
            total_change_percentage = (total_change / previous_count) * 100
            total_change_formatted = f"{total_change_percentage:.2f}%"
            if total_change_percentage > 0:
                total_change_formatted = "+" + total_change_formatted

            # Display the markdown table
            st.write(f"Total 5 Year Change: {total_change_formatted}")
            st.markdown(markdown_table)
            
        elif selected_option == "Show 10 Year Summary":
            
            # Line chart showing the count of businesses formed over the last 10 years
            st.title("Total Number of Businesses Formed in Last 10 Years")  # Add title
            df_exists.loc[:, 'year'] = pd.to_datetime(df_exists['entityformdate']).dt.year
            df_last_10_years = df_exists[df_exists['year'] >= df_exists['year'].max() - 10]
            business_count_by_year = df_last_10_years.groupby('year').size().reset_index(name='count')
            fig1 = px.line(business_count_by_year, x='year', y='count')
            st.plotly_chart(fig1)

            # Calculate the total number of businesses formed for the previous 10 years
            current_year = pd.to_datetime('today').year
            previous_10_years = range(current_year - 10, current_year)
            business_count_by_year = df_exists[df_exists['year'].isin(previous_10_years)].groupby('year').size().reset_index(name='count')

            # Generate a markdown table
            markdown_table = "| Year | Total Businesses Formed | Percentage Change |\n"
            markdown_table += "|------|------------------------|------------------|\n"
            previous_count = None
            total_change = 0
            for index, row in business_count_by_year.iterrows():
                percentage_change = ""
                if previous_count is not None:
                    change = row['count'] - previous_count
                    total_change += change
                    percentage_change = f"{(change / previous_count) * 100:.2f}%"
                else:
                    percentage_change = "-"
                count_with_commas = "{:,}".format(row['count'])
                markdown_table += f"| {row['year']} | {count_with_commas} | {percentage_change} |\n"
                previous_count = row['count']
    
            # Calculate the total 10-year change
            total_change_percentage = (total_change / previous_count) * 100
            total_change_formatted = f"{total_change_percentage:.2f}%"
            if total_change_percentage > 0:
                total_change_formatted = "+" + total_change_formatted

            # Display the markdown table
            st.write(f"Total 10 Year Change: {total_change_formatted}")
            st.markdown(markdown_table)

        elif selected_option == "Show Past Year Summary":
            st.write("Coming Soon!")

            # Display the markdown table
            st.markdown(markdown_table)


        elif selected_option == "Show Custom Summary":
            st.write("Coming Soon!")
        
        

    else:
        # show all-time data
        # ------------------
        df_alltime = full_data

        # summary
        time_series_summary_tools.show_total_businesses(full_data, active=False)
    
# trend analysis: how have business filings varied month-over-month in the last 12 months?

    