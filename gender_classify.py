import readdata  # read pkl file from here
import streamlit as st

with st.spinner('Wait for gender model to load ...'):
    gender_model = readdata.read_data_gdrive('gender_classify.pkl', type = 'joblib')
st.success('gender model loaded')

def gender_features(word):
    return {'last_letter': word[-1]}

def gender_classify(gender):
        return gender_model.classify(gender_features(gender))
