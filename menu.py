import streamlit as st

def menu():
    st.write('\n')
    menu_choice = st.sidebar.radio("Choose your Menu", ('Artist Choice', 'Features plot'),index=0,key=1)
    return menu_choice


