#Librerias
import pandas as pd
import numpy as np
#import altair as alt
import streamlit as st
#import plotly.figure_factory as ff
import plotly.express as px
import streamlit.components.v1 as components


st.set_page_config(page_title="Plotting Demo", page_icon="📈")

#st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")


sheet_id = st.secrets["sheet_id"]
sheet_name = st.secrets["sheet_name"]
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

df=pd.read_csv(url)

lst = ['Meat, chicken', 'Meat, cattle','Meat, pig','Meat, sheep']

#components.html("<html><body><h1 style='color:white;font-size:10px'>The data is part of the FAOSTAT database from the Food and Agriculture Organization (FAO) of the United Nations. We have the yearly comsumption of meat from 1961 to 2020 </h1></body></html>")
#components.html("<html><body><a href='https://www.fao.org'>FAO</a></body></html>")


source=df.query('Area == "Chile"')\
.query('Item in @lst ')
source.Year = pd.to_datetime(source.Year, format='%Y')


st.header('Idiom Test with Plotly')
fig = px.line(source, x="Year", y="Value", color='Item',
                 labels={
                     "Value": "Animals Slaughtered in the thousands",
                     "Item": "Species"
                 },
                title="How many animals are slaughtered per year in Chile?")
st.plotly_chart(fig, use_container_width=True)
