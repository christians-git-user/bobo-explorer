import streamlit as st

def site_config():
    st.subheader('Configuration')
    site_id = st.text_area('Enter site ID')
    bearer_token = st.text_area('Enter bearer token')
    date_input = st.date_input('Date input')
    num_clusters = st.number_input('Number of clusters')