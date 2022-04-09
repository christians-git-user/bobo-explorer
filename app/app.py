import streamlit as st
import pandas as pd

from components.load_data import load_data

# pd.set_option('display.max_columns', None)

st.title('Bobo Explorer')
st.warning('EXPERIMENTAL')

st.header('Event Data')
st.subheader('Raw Table')

load_data()



