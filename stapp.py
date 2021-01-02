import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import pandas as pd
import numpy as np

def func_welcome(): # This message diplays from sub-module stapp
    st.header('Features:')

@st.cache #cache data from dataframe to avoid loading it each time when the function is called
def func_df():
    dataframe = pd.DataFrame(
        np.random.randn(10, 7),
        columns=('Feature%d' % i for i in range(1,8)))
    return dataframe
