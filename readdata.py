import streamlit as st
import pandas as pd
import appconfig #import for data file
import _pickle as cPickle # import compress pickle file
import bz2
#function to compress and decompress pickle files

staticpath=appconfig.staticpath()
datapath=appconfig.datapath() # data file path

def compressed_pickle(title, data):
  with bz2.BZ2File(title + '.pbz2', 'w') as f:
    cPickle.dump(data, f)

def decompress_pickle(file):
  data = bz2.BZ2File(file, 'rb')
  data = cPickle.load(data)
  return data

@st.cache(persist=True) # cache data from dataframe to avoid loading it each time when the function is called
def read_song():
    filename='/song_data_with_gender.csv'
    datafile=datapath + filename
    song_data = pd.read_csv(datafile)
    return song_data

@st.cache(persist=True) # cache data from dataframe to avoid loading it each time when the function is called
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


@st.cache(max_entries=10, ttl=3600)
def read_song_imdb_rating():
    filename = '/song_only_imdb_merge.pkl'
    datafile = datapath + filename
    song_imdb_rating = pd.read_pickle(datafile)
    return song_imdb_rating

# @st.cache #cache data from dataframe to avoid loading it each time when the function is called
def read_user():
    filename='userdf.csv'
    user=pd.read_csv(filename,sep=',',index_col='sno')
    return user

@st.cache(persist=True) #cache data from dataframe to avoid loading it each time when the function is called
def read_song_genre():
    filename='/song_data_with_genre.csv'
    datafile=datapath + filename
    rating_data = pd.read_csv(datafile,sep=',')
    return rating_data

@st.cache(persist=True) #cache data from dataframe to avoid loading it each time when the function is called
def read_song_bowdf():
    filename='/song_data_bow_df.csv'
    datafile=datapath + filename
    senti_data = pd.read_csv(datafile,sep=',')
    return senti_data
