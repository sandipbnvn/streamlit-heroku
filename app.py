import streamlit as st

st.write('''
#App for Substracting 2 Numbers
''')

#Get input

st.header('Number input:')
first_num = st.number_input('FIRST_NUMBER')
second_num = st.number_input('SECOND_NUMBER')
  

result = first_num-second_num

st.subheader('Result')
st.write(result)
