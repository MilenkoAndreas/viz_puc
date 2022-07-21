import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

sheet_id = st.secrets["sheet_id"]
sheet_name = st.secrets["sheet_name"]
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

df=pd.read_csv(url)

st.title("Haciendo gráficos con altair en streamlit")


#df=pd.read_csv('FAOSTAT_data_7-20-2022.csv') 

source=df.query('Area == "Chile"')
st.write(source.head(5))

# c = alt.Chart(df).mark_circle().encode(
#      x='a', y='b', color='c', tooltip=['a', 'b', 'c'])
# 
# st.altair_chart(c, use_container_width=True)
