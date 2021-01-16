import streamlit as st
import pandas as pd
import appconfig #import for data file
import urllib
import pickle
import joblib

# @st.cache #cache data from dataframe to avoid loading it each time when the function is called
def read_user():
    filename='userdf.csv'
    user=pd.read_csv(filename,sep=',',index_col='sno')
    return user

# read data and picke from gdrive
@st.cache(max_entries=10, ttl=3600)
def read_data_gdrive(file, type='data'):
    file_type = file.split('.')[-1]
    if file_type == 'pkl' and type == 'data':
        pickle_url = appconfig.datapath(file)
        pickle_path = 'https://drive.google.com/uc?export=download&id=' + pickle_url.split('/')[-2]
        pickle_data = pickle.load(urllib.request.urlopen(pickle_path))
        return pickle_data
    elif file_type == 'pkl' and type == 'joblib':
        joblib_url = appconfig.datapath(file)
        joblib_path = 'https://drive.google.com/uc?export=download&id=' + joblib_url.split('/')[-2]
        joblib_data = joblib.load(urllib.request.urlopen(joblib_path))
        return joblib_data
    elif file_type == 'csv':
        csv_url = appconfig.datapath(file)
        csv_path = 'https://drive.google.com/uc?export=download&id=' + csv_url.split('/')[-2]
        csv_data = pd.read_csv(csv_path)
        return csv_data
    elif file_type == 'tsv':
        tsv_url = appconfig.datapath(file)
        tsv_path = 'https://drive.google.com/uc?export=download&id=' + tsv_url.split('/')[-2]
        tsv_data = pd.read_csv(tsv_path, sep='\t')
        return tsv_data
