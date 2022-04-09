import pyarrow.parquet as pq
import pandas as pd
import streamlit as st
import s3fs
import altair as alt

def load_data():
    bucketname = "boboserverstack-boboserviceboboa67afcbb-1vv76sne2db6j" 
    file_to_read = "fileout.txt/part-00000-82ce6fe5-7109-4971-85b9-ce448ad5bc42-c000.snappy.parquet"

    s3 = s3fs.S3FileSystem()
    temp = pq.read_table(f"s3://{bucketname}/{file_to_read}", filesystem=s3).to_pandas()
    
    # # file data will be a binary stream.  We have to decode it 
    # contents = filedata.decode('utf-8') 

    # # Once decoded, you can treat the file as plain text if appropriate 
    # print(contents)

    # create day col
    temp['date'] = temp['on'].apply(lambda x: x.split('T')[0])

    # groupby
    df_daily = temp.groupby(by='date').count()

    st.subheader('Visualizations')
    st.altair_chart(alt.Chart(df_daily.reset_index()).mark_bar().encode(
        x='date',
        y='on'
    ))

    st.subheader('Explore Daily Counts')
    st.write(df_daily)