import pathlib
import streamlit as st
STREAMLIT_STATIC_PATH = pathlib.Path(st.__path__[0]) / 'static'

def staticpath():
    return STREAMLIT_STATIC_PATH

def datapath():
    return '/Users/vrln/Prediction_Algorithms/greatlearning/capstone_project'
