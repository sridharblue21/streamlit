import streamlit as st

def menu():
    st.write('\n')
    menu_choice = st.sidebar.radio("Main Pages>>>>>", ('User Choices', 'Popular Titles', 'Search songs', 'User Registration'),index=0,key=1)
    return menu_choice

def submenu_1():
    st.write('\n')
    menu_choice = st.sidebar.radio("Sub Pages>>>>>", ('Most Played', 'Most Rated'),index=0,key=2)
    return menu_choice
