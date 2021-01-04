import streamlit as st
import stapp #import sub-module stapp
from load_css import local_css
import login
import authenticate
import popular_reco
import menu
import numpy as np
local_css("style.css") #include style.css

def print_hi(name):
    #st.header('Welcome to Group 4-Capstone Project')
    welcome_head=f"<div>Hi <span class='highlight blue'>{name}</span></div>"
    st.markdown(welcome_head,unsafe_allow_html=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    yourname,yourpass=login.login() #get login field values
    #st.write(yourpass)
    st.header('Welcome to Top Songs Recommender System ')
    message=authenticate.authenticate(yourname,yourpass) # authenticate with name,passcode not empty and passcode matching
    if message == 'authenticated': #display blocks below if authenticated
        print_hi(yourname)
        st.write ('\n')
        menu_out=menu.menu()

        if menu_out=='Artist Choice':
            pop=popular_reco.artist_choice()
            if pop:
                pop_msg=f"<div>Your favourite(s), <span class='highlight blue'>{pop}</span></div>"
                st.markdown(pop_msg,unsafe_allow_html=True)
            st.write('\n')
        elif menu_out=='Features plot':
            stapp.func_welcome()# call welcome function from the sub-module
            df = stapp.func_df()# call data load function from the sub-module
            if len(df)>10:
                st.table(df[:10])
            else:
                st.table(df)

            st.write('\n')
            #Multi-select features
            features=st.multiselect('Please choose your features to plot here',options=df['artist_name'].head(10))
            if features:
                st.write('Name=>',features[0])#plot line chart based on themulti-select
    else:
        st.sidebar.markdown(message,unsafe_allow_html=True)
