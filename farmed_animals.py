import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

uploaded_file = st.file_uploader('FAOSTAT_data_7-20-2022.csv')

st.title("Haciendo gráficos con altair en streamlit")


df=pd.read_csv('FAOSTAT_data_7-20-2022.csv') 

source=df.query('Area == "Chile"')
st.write(source.head(5))

# c = alt.Chart(df).mark_circle().encode(
#      x='a', y='b', color='c', tooltip=['a', 'b', 'c'])
# 
# st.altair_chart(c, use_container_width=True)
