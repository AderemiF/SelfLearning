import streamlit as st
import numpy as np
import pandas as pd

st.title ('Savage, classy and bougie')

st.write("My first attemp at streamlit, leggo! Are you ready?")

df = pd.DataFrame({
'First column': [1,2,3,4],
'Second column': [10,20,30,40]
})

st.write(df)

#Creating a checkbox
if st.checkbox('show dataframe'):
    chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a', 'b', 'c'])

    st.line_chart(chart_data)


#Creating a select box
#option = st.selectbox('what is your favorite season of the year?', ['winter','spring','summer', 'fall'])

#'Did you select: ', option, '?'

#Creating a select box and setting  it as a sidebar
option = st.sidebar.selectbox('what is your favorite season of the year?', ['winter','spring','summer', 'fall'])
'Did you select: ', option, '?'

#side-by-side
left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Yaay!")

expander = st.beta_expander("FAQ")
expander.write("Here you could put in some explanations...")
