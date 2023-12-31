# colorado-businesses
Data Engineering &amp; Analysis project using publicly available data

## Technical

### Dependencies
- streamlit
- plotly

### Setup
`streamlit run main.py`


### Data Sources
- [Colorado Information Marketplace: Business Entities in Colorado](https://data.colorado.gov/Business/Business-Entities-in-Colorado/4ykn-tg5h/about_data)


## Main Dev Trajectory
1. Get all the things in place to answer all of the key questions using one datasource
2. Get all the things in place to answer all of the key questions using derived or multiple datasources
3. Deploy production system with updating data
4. Get feedback


## Log

### 12/31/2023 

DONE:
- ✅ Business Enttiy data (State Level)
- Foreign Investment (basic)

TODO: 
- Foreign Investment geoplot
- Refactor visualizations to be in their own modules (simplifies code)
- Business Entity geoplot
- Business Entity Industry discovery (possible NLP)

### 12/30/2023
Current emphasis (given available data):
1. Which counties in Colorado have the highest number of business filings?
    (assuming principal/mailing addresses can be used to determine the county)
2. Is there an increasing trend in the number of business filings in Colorado over the past 5 years?
(`entityformdate`)
3. What has been the trend in business filings over the past 10 years? (`entityformdate`)
4. How have business filings varied month-over-month in the last 12 months? (`entityformdate`)
5. Is there foreign investment in Colorado? If so, which countries are investing and where?

Additional Data Needed:
- **At the state level, which types of businesses or industries are most prevalent?**
  - *(Not Answerable with Current Data: don’t have direct industry classification data.)*
- **On a county basis, which types of businesses or industries are most common?**
  - *(Not Answerable with Current Data: Similar to the state-level question, lack industry classification.)*
- **In different regions, what are the most common types of businesses or industries?**
  - *(Not Answerable with Current Data: Requires industry data which is not present.)*
- **What business types are most prevalent? Was this always the case?**

### 12/28/2023
- Do I have the data required to group by type or by industry? 
    - No, not with the current dataset



