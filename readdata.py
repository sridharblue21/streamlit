import streamlit as st
import pandas as pd
import appconfig #import for data file
staticpath=appconfig.staticpath()
datapath=appconfig.datapath() # data file path

@st.cache(persist=True) #cache data from dataframe to avoid loading it each time when the function is called
def read_song():
    filename='/song_data_with_gender.csv'
    datafile=datapath + filename
    song_data = pd.read_csv(datafile)
    return song_data

@st.cache(persist=True) #cache data from dataframe to avoid loading it each time when the function is called
def read_count():
    filename='/count_data.csv'
    datafile=datapath + filename
    count_data = pd.read_csv(datafile)
    return count_data

@st.cache(persist=True) #cache data from dataframe to avoid loading it each time when the function is called
def read_akas():
    filename='/akas_data.tsv'
    datafile=datapath + filename
    akas_data = pd.read_csv(datafile,sep='\t')
    return akas_data

@st.cache(persist=True) #cache data from dataframe to avoid loading it each time when the function is called
def read_rating():
    filename='/rating_datas.tsv'
    datafile=datapath + filename
    rating_data = pd.read_csv(datafile,sep='\t')
    return rating_data
