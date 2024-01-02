import streamlit as st

import plotly.graph_objects as go


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
        