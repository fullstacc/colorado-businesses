import streamlit as st

# df is filtered via radio button before being passed to this function
def show_foreign_investment(df):
    st.title("Foreign Investment in Colorado")
    st.write("This section is under construction")

    # Radio button for entity status
    entity_status = st.radio("Entity Status", ["Only Show Business Entities still in Existence", "Include all Businesses (including defunct)"])
    if entity_status == "Only Show Business Entities still in Existence":
        df_exists = df[df['entitystatus'].isin(['Good Standing', 'Exists'])]
    else:
        df_exists = df

    # filter dataset to only foreign entities
    foreign_entity_types = df_exists[df_exists['entitytype'].str.contains('foreign', case=False)]['entitytype'].unique()
    foreign_entity_df = df_exists[df_exists['entitytype'].isin(foreign_entity_types)]

    # Radio button for foreign entity type
    foreign_entity_type = st.radio("Foreign Entity Type", ["Show me only foreign country", "Show me only foreign state", "Show me everything"], index=2)
    if foreign_entity_type == "Show me only foreign country":
        foreign_entity_df = foreign_entity_df[foreign_entity_df['principalcountry'] != 'US']
    elif foreign_entity_type == "Show me only foreign state":
        foreign_entity_df = foreign_entity_df[foreign_entity_df['principalcountry'] == 'US']

    # Calculate total foreign investment
    st.subheader(f"Viewing Data for {len(foreign_entity_df)} Foreign Business Entities")
    proportion = len(foreign_entity_df) / len(df_exists)
    st.write(f"*{proportion:.2%} of total business entities*")


    # Table for principal country counts
    principal_country_counts = foreign_entity_df['principalcountry'].value_counts().reset_index()
    principal_country_counts.columns = ['Principal Country', 'Count']
    # Calculate percentage
    principal_country_counts['Percentage'] = round(principal_country_counts['Count'] / principal_country_counts['Count'].sum() * 100, 2)
    principal_country_counts['Percentage'] = principal_country_counts['Percentage'].map("{:.2f}%".format)
    st.dataframe(principal_country_counts, use_container_width=True, hide_index=True)