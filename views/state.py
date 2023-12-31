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

    st.title("Business Entities in Colorado")

    # Radio button for entity status
    entity_status = st.radio("Entity Status", ["Only Show Business Entities still in Existence", "Include all Businesses (including defunct)"])
    if entity_status == "Only Show Business Entities still in Existence":
        df_exists = df[df['entitystatus'].isin(['Good Standing', 'Exists'])]
    else:
        df_exists = df

    
    st.subheader(f"Viewing Data for {len(df_exists)} Business Entities")

    # Table for entity type counts
    entity_type_counts = df_exists['entitytype'].value_counts().reset_index()
    entity_type_counts.columns = ['Entity Type', 'Count']
    # Calculate percentage
    entity_type_counts['Percentage'] = round(entity_type_counts['Count'] / entity_type_counts['Count'].sum() * 100, 2)
    entity_type_counts['Percentage'] = entity_type_counts['Percentage'].map("{:.2f}%".format)
    st.dataframe(entity_type_counts, use_container_width=True, hide_index=True)

    
    entity_type_counts = df_exists['entitytype'].value_counts().head(10)

    entity_type_figure = go.Figure(data=[go.Bar(
        x=entity_type_counts.index,
        y=entity_type_counts.values,
        hovertemplate=
            "<b>%{x}</b><br><br>" +
            "Count: %{y}<br>",
        hoverinfo='text'
    )])

    entity_type_figure.update_layout(
        title=dict(text='Top 10 Entity Types in Colorado (Total Count)', x=0.5),
        xaxis=dict(title='Entity Type'),
        yaxis=dict(title='Count'),
        xaxis_tickangle=-45
    )

    st.plotly_chart(entity_type_figure, use_container_width=True)



    # Expander window for business entity definitions
    with st.expander("What is a Business Entity?"):
        st.write("A business entity is an organization that is formed and administered as per commercial law in order to engage in business activities, charitable work, or other activities allowable. Common types of business entities include:")
        st.write("- Limited Liability Company (LLC): A type of business structure that combines the pass-through taxation of a partnership or sole proprietorship with the limited liability of a corporation.")
        st.write("- DBA (Doing Business As): A legal term used to refer to a business that operates under a name different from its legal name.")
        st.write("- Corporation: A legal entity that is separate and distinct from its owners. It has rights and liabilities separate from its owners and can enter into contracts, sue and be sued, and own property.")
        st.write("See [Colorado Secretary of State](https://www.sos.state.co.us/pubs/business/forms_main.html) for a complete list.")
        
# TODO: Break into separate module
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


        



