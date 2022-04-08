import streamlit as st
<<<<<<< HEAD
import os, json
import pandas as pd
import numpy as np
import glob
import altair as alt
import time
=======
from site_config import site_config
>>>>>>> c5733ca22e9dc31bd98bfa8063230eb9e36e2b68

pd.set_option('display.max_columns', None)

path_to_json = './data' 

<<<<<<< HEAD
json_pattern = os.path.join(path_to_json,'*.json')
file_list = glob.glob(json_pattern)
=======
site_config()
>>>>>>> c5733ca22e9dc31bd98bfa8063230eb9e36e2b68

dfs = [] # an empty list to store the data frames
for file in file_list:
    data = pd.read_json(file, lines=True) # read data frame from json file
    dfs.append(data) # append the data frame to the list

temp = pd.concat(dfs, ignore_index=True) # concatenate all the data frames in the list.

# create day col
temp['date'] = temp['on'].apply(lambda x: x.split('T')[0])

# groupby
df_daily = temp.groupby(by='date').count()

st.title('Bobo Explorer')
st.warning('EXPERIMENTAL')

st.header('Event Data')
st.subheader('Raw Table')
st.write(temp)

st.subheader('Daily Counts')
st.write(df_daily)

st.subheader('Visualizations')
st.altair_chart(alt.Chart(df_daily.reset_index()).mark_bar().encode(
    x='date',
    y='on'
))



