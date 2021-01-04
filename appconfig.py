import pathlib
import streamlit as st

def staticpath():
    STREAMLIT_STATIC_PATH = pathlib.Path(st.__path__[0]) / 'static'
    return STREAMLIT_STATIC_PATH

def datapath():
    return '/Users/vrln/Prediction_Algorithms/greatlearning/capstone_project'
