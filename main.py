import streamlit as st
import stapp #import sub-module stapp
from load_css import local_css
import login
import authenticate

local_css("style.css")

def print_hi(name):
    st.title('Welcome to Group 4-Capstone Project')
    welcome_head=f"<div>Hi <span class='highlight blue'>{name}</span> here is your data</div>"
    st.markdown(welcome_head,unsafe_allow_html=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    yourname,yourpass=login.login() #get login field values
    message=authenticate.authenticate(yourname,yourpass) # authenticate with name,passcode not empty and passcode matching
    if message == 'authenticated': #display blocks below if yourname is not empty
        print_hi(yourname)
        stapp.func_welcome()# call welcome function from the sub-module
        df = stapp.func_df()# call data load function from the sub-module
        st.table(df)
        #Multi-select features
        features=st.multiselect('Please choose your features to plot here',options=df.columns)
        if features:
            st.line_chart(df[features])#plot line chart based on themulti-select
    else:
        st.sidebar.markdown(message,unsafe_allow_html=True)
