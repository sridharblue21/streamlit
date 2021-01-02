import streamlit as st
#pass login field values
def login():
    st.sidebar.header('Login to access the App')
    yourname=st.sidebar.text_input('name',max_chars=20)
    yourpass=st.sidebar.text_input('passcode',max_chars=8,type="password").__hash__() #hashed password field
    return yourname,yourpass
