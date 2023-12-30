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

    
    percentage_entity_types = df_exists['entitytype'].value_counts(normalize=True).head(10) * 100

    percentage_entity_figure = go.Figure(data=[go.Bar(
        x=percentage_entity_types.index,
        y=percentage_entity_types.values,
        hovertemplate=
            "<b>%{x}</b><br><br>" +
            "Percentage: %{y:.2f}%<br>",
        hoverinfo='text'
    )])

    percentage_entity_figure.update_layout(
        title='Distribution of Top 10 Entity Types in df_exists (with percentage)',
        xaxis=dict(title='Entity Type'),
        yaxis=dict(title='Percentage'),
        xaxis_tickangle=-45
    )

    st.plotly_chart(percentage_entity_figure, use_container_width=True)



    # Expander window for business entity definitions
    with st.expander("What is a Business Entity?"):
        st.write("A business entity is an organization that is formed and administered as per commercial law in order to engage in business activities, charitable work, or other activities allowable. Common types of business entities include:")
        st.write("- Limited Liability Company (LLC): A type of business structure that combines the pass-through taxation of a partnership or sole proprietorship with the limited liability of a corporation.")
        st.write("- DBA (Doing Business As): A legal term used to refer to a business that operates under a name different from its legal name.")
        st.write("- Corporation: A legal entity that is separate and distinct from its owners. It has rights and liabilities separate from its owners and can enter into contracts, sue and be sued, and own property.")
        st.write("See [Colorado Secretary of State](https://www.sos.state.co.us/pubs/business/forms_main.html) for a complete list.")
        

    
   



