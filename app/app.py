import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import time

from components.load_data import load_data

# pd.set_option('display.max_columns', None)

st.title('Bobo Explorer')
st.warning('EXPERIMENTAL')

st.header('Event Data')
st.subheader('Raw Table')

load_data()

# st.write(temp)

# st.subheader('Daily Counts')
# st.write(df_daily)

# st.subheader('Visualizations')
# st.altair_chart(alt.Chart(df_daily.reset_index()).mark_bar().encode(
#     x='date',
#     y='on'
# ))



