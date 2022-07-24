import streamlit as st
import pandas as pd


st.write("""
# App for Substraction

This app substracts the second number from the first number
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    num1 = st.number_input("NUM1")
    num2 = st.number_input("NUM2")

    data = {"NUM1":num1,
            "NUM2":num2
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df.to_dict())

result = df.iloc[0,0]-df.iloc[0,1]
st.subheader('Result')
st.write(result)
