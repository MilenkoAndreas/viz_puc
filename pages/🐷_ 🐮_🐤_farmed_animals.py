import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
#import plotly.figure_factory as ff
import plotly.express as px
import streamlit.components.v1 as components

st.set_page_config(layout="wide")


sheet_id = st.secrets["sheet_id"]
sheet_name = st.secrets["sheet_name"]

#sheet_region = st.secrets["sheet_region"]
sheet_region = "all"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
#url_regions=f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_region}"

df=pd.read_csv(url)
df['Value']=df['Value']*1000

df['Area']=df['Area'].replace({'China, mainland': 'China', 'T?rkiye': 'Turkey',
                               'China, Taiwan Province of': 'China', 'Viet Nam': 'Vietnam', 'Brunei Darussalam': 'Brunei',
                               'China, Macao SAR': 'China', 'Sudan (former)': 'Sudan', 'China, Hong Kong SAR': 'China',
                               "C?te d'Ivoire": "Côte d'Ivoire",  'Republic of Moldova': 'Moldova'})

#df_regions=pd.read_csv(url_regions)

lst = ['Meat, chicken', 'Meat, cattle','Meat, pig']

df_total_pigs=df.query('Item in @lst ')

#df_total_pigs['sub-region']=df_total_pigs['intermediate-region'].where(df_total_pigs['sub-region'].eq('Latin America and the Caribbean'),df_total_pigs['sub-region'])
#df_total_pigs_last=df_total_pigs[df_total_pigs['Year']==2020]

st.title("How many animals are slaughtered ?")
st.text("The data is part of the FAOSTAT database from \nthe Food and Agriculture Organization (FAO) of the United Nations.\n We have the yearly comsumption of meat from 1961 to 2020 ")

# sub_regions= st.multiselect(
#          'Select a Region',
#           pd.unique(df_total_pigs_last["sub-region"]),default=["South America"])
# 
# #df=pd.read_csv('FAOSTAT_data_7-20-2022.csv') 
# source_tree=df_total_pigs_last\
#      .query('`sub-region` in @sub_regions ')

#components.html("<html><body><h1 style='color:white;font-size:10px'>The data is part of the FAOSTAT database from the Food and Agriculture Organization (FAO) of the United Nations. We have the yearly comsumption of meat from 1961 to 2020 </h1></body></html>")
#components.html("<html><body><a href='https://www.fao.org'>FAO</a></body></html>")


#source=df.query('Area == "Chile"')\
#.query('Item in @lst ')
#source.Year = pd.to_datetime(source.Year, format='%Y')
st.text("Data:")
st.write(df_total_pigs.head(8))


st.header('How many animals are slaughtered per year?')

df_total_pigs.Year=pd.to_datetime(df_total_pigs.Year, format='%Y')

country = st.selectbox(
     'Select a Country',
      pd.unique(df_total_pigs["Area"]),index=34)
      
source=df_total_pigs\
      .query('Area == @country ')

fig = px.line(source, x="Year", y="Value", color='Item',
                 labels={
                     "Value": "Animals Slaughtered",
                     "Item": "Species"
                 })
st.plotly_chart(fig, use_container_width=True)
