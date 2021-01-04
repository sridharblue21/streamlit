import streamlit as st


def artist_choice():
    artist_choice = st.multiselect("Who's your favorite artist?", ('Dwight Yoakam', 'Kings Of Leon', 'Alliance Ethnik'))

    return artist_choice


