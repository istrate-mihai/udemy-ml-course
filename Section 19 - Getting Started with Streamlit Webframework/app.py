import numpy as np
import pandas as pd
import streamlit as st

st.title('Hello Streamlit')
st.write('This is a simple text')

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})

st.write('Here is the dataframe')
st.write(df)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ['a', 'b', 'c']
)

st.write(chart_data)
st.line_chart(chart_data)
