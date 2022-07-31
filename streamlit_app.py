import pandas as pd
import numpy as np
#import altair as alt
import streamlit as st
#import plotly.figure_factory as ff
import plotly.express as px
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

#st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

st.title("How many animals are slaughtered per year?",)
st.text("The data is part of the FAOSTAT database from the Food and Agriculture Organization (FAO) of the United Nations. We have the yearly comsumption of meat from 1961 to 2020 ")

sheet_id = st.secrets["sheet_id"]
sheet_name = st.secrets["sheet_name"]
sheet_region = st.secrets["sheet_region"]
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
url_regions=f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_region}"

df=pd.read_csv(url)

df['Area']=df['Area'].replace({'China, mainland': 'China', 'T?rkiye': 'Turkey', 'Syrian Arab Republic': 'Syria',
                               'Iran (Islamic Republic of)': 'Iran', 'Bolivia (Plurinational State of)': 'Bolivia', 'United States of America': 'United States',
                               'China, Taiwan Province of': 'China', 'Viet Nam': 'Vietnam', 'Brunei Darussalam': 'Brunei',
                               'United Republic of Tanzania': 'Tanzania', 'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom', 'Venezuela (Bolivarian Republic of)': 'Venezuela',
                               'China, Macao SAR': 'China', 'Sudan (former)': 'Sudan', 'China, Hong Kong SAR': 'China',
                               "C?te d'Ivoire": "Cote d'Ivoire", 'Russian Federation': 'Russia', 'Republic of Moldova': 'Moldova'})

df_regions=pd.read_csv(url_regions)

df_total=df.merge(df_regions, left_on='Area', right_on='Entity', how='left')\
.rename({'World Region according to the World Bank':'Region'},axis=1)\
.drop(columns='Year_y')\
.dropna(subset=['Region'])



#df_nan=df_total[df_total['Region'].isnull()]
#df_nan['Area'].value_counts()
#df_total['Region'].value_counts()
#lst = ['Meat, chicken', 'Meat, cattle','Meat, pig','Meat, sheep']
#df['Domain Code'].value_counts()
#components.html("<html><body><h1 style='color:white;font-size:10px'>The data is part of the FAOSTAT database from the Food and Agriculture Organization (FAO) of the United Nations. We have the yearly comsumption of meat from 1961 to 2020 </h1></body></html>")
#components.html("<html><body><a href='https://www.fao.org'>FAO</a></body></html>")


source=df.query('Area == "Chile"')\
.query('Item in @lst ')
source.Year = pd.to_datetime(source.Year, format='%Y')
