import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
#import plotly.figure_factory as ff
import plotly.express as px
import streamlit.components.v1 as components




sheet_id = st.secrets["sheet_id"]
sheet_name = st.secrets["sheet_name"]
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

df=pd.read_csv(url)
df['Item'].value_counts()
st.title("How many animals are slaughtered per year?",)
st.text("The data is part of the FAOSTAT database from the Food and Agriculture Organization (FAO) of the United Nations. We have the yearly comsumption of meat from 1961 to 2020 ")

#df=pd.read_csv('FAOSTAT_data_7-20-2022.csv') 
lst = ['Meat, chicken', 'Meat, cattle','Meat, pig','Meat, sheep']

#components.html("<html><body><h1 style='color:white;font-size:10px'>The data is part of the FAOSTAT database from the Food and Agriculture Organization (FAO) of the United Nations. We have the yearly comsumption of meat from 1961 to 2020 </h1></body></html>")
#components.html("<html><body><a href='https://www.fao.org'>FAO</a></body></html>")


source=df.query('Area == "Chile"')\
.query('Item in @lst ')
source.Year = pd.to_datetime(source.Year, format='%Y')
st.text("Sample:")
st.write(source.head(5))

st.header('Idiom Test with Altair')
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

st.header('Idiom Test with Plotly')
fig = px.line(source, x="Year", y="Value", color='Item',
                 labels={
                     "Value": "Animals Slaughtered in the thousands",
                     "Item": "Species"
                 },
                title="How many animals are slaughtered per year in Chile?"))
st.plotly_chart(fig, use_container_width=True)
