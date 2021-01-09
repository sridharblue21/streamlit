import streamlit as st
import gender_classify
import readdata
import pandas as pd


def fn_to_userdf(name, passwd, region):
    userdf = readdata.read_user()
    gender = gender_classify.gender_classify(name)
    if name not in userdf.name.values:
        dict = {'sno':len(userdf)+1,'name':name, 'pswd':passwd, 'gender':gender, 'region':region}
        df = pd.DataFrame.from_dict(dict,orient='index').T
        userdf = userdf.reset_index().append(df).set_index('sno')
        userdf.to_csv('userdf.csv', mode='w')
        return 'Registration successful'
    else:
        return 'Thank you! You have registered with us already. Please login!'


def register():
    st.header('User Registration')
    region = st.selectbox('region', options=['IN', 'US', '/N'], index=2)
    name = st.text_input('name', max_chars=20, key=33)
    passwd = st.text_input('passcode', max_chars=8, type="password", key=44)
    # .__hash__() hashed password field to be added
    bt=st.button('Click here to submit')
    if name and passwd and region and bt:
        ret_val = fn_to_userdf(name, passwd, region)
        return ret_val
    else:
        ret_val = 'Change region, enter name and passcode'
        return ret_val
