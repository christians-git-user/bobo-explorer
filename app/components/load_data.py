import pyarrow.parquet as pq
import pandas as pd
import boto3
import streamlit as st

def load_data():
    s3client = boto3.client(
        's3',
        region_name='us-east-1'
    )
    
    bucketname = "boboserverstack-boboserviceboboa67afcbb-1vv76sne2db6j" 
    file_to_read = "fileout.txt/part-00000-82ce6fe5-7109-4971-85b9-ce448ad5bc42-c000.snappy.parquet"

    #Create a file object using the bucket and object key. 
    fileobj = s3client.get_object(
        Bucket=bucketname,
        Key=file_to_read
        ) 
    st.write(fileobj)
    # open the file object and read it into the variable filedata. 
    filedata = fileobj['Body'].read()
    st.write(filedata)

    arrow_dataset = pq.ParquetDataset('fileobj')
    arrow_table = arrow_dataset.read()
    temp = arrow_table.to_pandas()

    st.write(temp)
    
    # # file data will be a binary stream.  We have to decode it 
    # contents = filedata.decode('utf-8') 

    # # Once decoded, you can treat the file as plain text if appropriate 
    # print(contents)

    # create day col
    temp['date'] = temp['on'].apply(lambda x: x.split('T')[0])

    # groupby
    df_daily = temp.groupby(by='date').count()