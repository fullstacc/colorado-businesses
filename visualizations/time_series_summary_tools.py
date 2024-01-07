import pandas as pd
import numpy as np
import streamlit as st

import plotly.express as px

def show_total_businesses(df, active=True):
    # Display the total number of current businesses
    total_businesses = len(df)
    formatted_total_businesses = "{:,}".format(total_businesses)
    earliest_entityformdate = df['entityformdate'].min().strftime('%Y-%m-%d')
    latest_entityformdate = df['entityformdate'].max().strftime('%Y-%m-%d')
    if active:
        st.write(f"- There are **{formatted_total_businesses}** active businesses in Colorado.")
        st.write(f"- The oldest business in this selection is from {earliest_entityformdate} and the newest is from {latest_entityformdate}")

    else:
        st.write(f"There have been {formatted_total_businesses} businesses in Colorado from {earliest_entityformdate} to {latest_entityformdate}")


      

# def  show_line_graph(df):
                  
#             # Line chart showing the count of businesses formed over the last 5 years
#             st.title("Total Number of Businesses Formed in Last 5 Years")  # Add title
#             df_exists.loc[:, 'year'] = pd.to_datetime(df_exists['entityformdate']).dt.year
#             df_last_5_years = df_exists[df_exists['year'] >= df_exists['year'].max() - 5]
#             business_count_by_year = df_last_5_years.groupby('year').size().reset_index(name='count')
#             fig1 = px.line(business_count_by_year, x='year', y='count')
#             st.plotly_chart(fig1)

#             # Calculate the total number of businesses formed for the previous 5 years
#             current_year = pd.to_datetime('today').year
#             previous_5_years = range(current_year - 5, current_year)
#             business_count_by_year = df_exists[df_exists['year'].isin(previous_5_years)].groupby('year').size().reset_index(name='count')

#             # Generate a markdown table
#             markdown_table = "| Year | Total Businesses Formed | Percentage Change |\n"
#             markdown_table += "|------|------------------------|------------------|\n"
#             previous_count = None
#             total_change = 0
#             for index, row in business_count_by_year.iterrows():
#                 percentage_change = ""
#                 if previous_count is not None:
#                     change = row['count'] - previous_count
#                     total_change += change
#                     percentage_change = f"{(change / previous_count) * 100:.2f}%"
#                 else:
#                     percentage_change = "-"
#                 count_with_commas = "{:,}".format(row['count'])
#                 markdown_table += f"| {row['year']} | {count_with_commas} | {percentage_change} |\n"
#                 previous_count = row['count']
            
#             # Calculate the total 5-year change
#             total_change_percentage = (total_change / previous_count) * 100
#             total_change_formatted = f"{total_change_percentage:.2f}%"
#             if total_change_percentage > 0:
#                 total_change_formatted = "+" + total_change_formatted

#             # Display the markdown table
#             st.write(f"Total 5 Year Change: {total_change_formatted}")
#             st.markdown(markdown_table)