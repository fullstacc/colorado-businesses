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


def show_line_graph(df, selected_option):
    print(f"starting show_line_graph with selected_option = {selected_option}")
    """
    Displays a line graph of the count of businesses formed over the last x years.

    Parameters:
        df (pandas.DataFrame): The DataFrame containing the business data.
        selected_option (str): The selected option indicating the number of years to consider.

    Returns:
        None
    """
    selected_years_back = int(selected_option.split()[0])
    print(f"selected_years_back = {selected_years_back}")
    print("made it here, selected_years_back =", selected_years_back)
    # Line chart showing the count of businesses formed over the last x years
    st.title(f"Total Number of Businesses Formed in Last {selected_years_back} Years") 
    df.loc[:, 'year'] = pd.to_datetime(df['entityformdate']).dt.year

    df_last_x_years = df[df['year'] >= df['year'].max() - selected_years_back]
    business_count_by_year = df_last_x_years.groupby('year').size().reset_index(name='count')
    fig1 = px.line(business_count_by_year, x='year', y='count')
    st.plotly_chart(fig1)

    # Calculate the total number of businesses formed for the previous x years
    current_year = pd.to_datetime('today').year
    selected_years = int(selected_option.split()[0])
    previous_x_years = range(current_year - selected_years, current_year)
    business_count_by_year = df[df['year'].isin(previous_x_years)].groupby('year').size().reset_index(name='count')

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

    # Calculate the total x-year change
    total_change_percentage = (total_change / previous_count) * 100
    total_change_formatted = f"{total_change_percentage:.2f}%"
    if total_change_percentage > 0:
        total_change_formatted = "+" + total_change_formatted

    # Display the markdown table
    st.write(f"Total {selected_years_back} Year Change: {total_change_formatted}")
    st.markdown(markdown_table)
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

        # Calculate the total x-year change
        total_change_percentage = (total_change / previous_count) * 100
        total_change_formatted = f"{total_change_percentage:.2f}%"
        if total_change_percentage > 0:
            total_change_formatted = "+" + total_change_formatted

        # Display the markdown table
        st.write(f"Total {selected_years_back} Year Change: {total_change_formatted}")
        st.markdown(markdown_table)
    
      
def show_past_year_graph(df):
    """
    Displays a line graph of the count of businesses formed over the last 12 months.

    Parameters:
        df (pandas.DataFrame): The DataFrame containing the business data.

    Returns:
        None
    """
    st.title("Total Number of Businesses Formed in the Last 12 Months")
    df.loc[:, 'month'] = df['entityformdate'].dt.strftime('%Y-%m')
    df_last_year = df[df['entityformdate'] >= (pd.to_datetime('today') - pd.DateOffset(months=12))]
    business_count_by_month = df_last_year.groupby('month').size().reset_index(name='count')

    # line graph
    fig2 = px.line(business_count_by_month, x='month', y='count')
    st.plotly_chart(fig2)
