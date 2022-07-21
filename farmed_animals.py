import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

sheet_id = st.secrets["sheet_id"]
sheet_name = st.secrets["sheet_name"]
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

df=pd.read_csv(url)
df['Item'].value_counts()
st.title("Haciendo gráficos con altair en streamlit")


#df=pd.read_csv('FAOSTAT_data_7-20-2022.csv') 
lst = ['Meat, chicken', 'Meat, cattle','Meat, pig','Meat, sheep']

source=df.query('Area == "Chile"')\
.query('Item in @lst ')


st.write(source.head(5))

highlight = alt.selection(type='single', on='mouseover',
                          fields=['symbol'], nearest=True)

base = alt.Chart(source).encode(
    x='Year',
    y='Value:Q',
    color='Item:N'
)

points = base.mark_circle().encode(
    opacity=alt.value(0)
).add_selection(
    highlight
).properties(
    width=600
)

lines = base.mark_line().encode(
    size=alt.condition(~highlight, alt.value(1), alt.value(3))
)

c = points + lines

# c = alt.Chart(df).mark_circle().encode(
#      x='a', y='b', color='c', tooltip=['a', 'b', 'c'])
# 
st.altair_chart(c, use_container_width=True)
