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
#sheet_region = st.secrets["sheet_region"]
sheet_region = "all"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
url_regions=f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_region}"

df=pd.read_csv(url)

df['Area']=df['Area'].replace({'China, mainland': 'China', 'T?rkiye': 'Turkey',
                               'China, Taiwan Province of': 'China', 'Viet Nam': 'Vietnam', 'Brunei Darussalam': 'Brunei',
                               'China, Macao SAR': 'China', 'Sudan (former)': 'Sudan', 'China, Hong Kong SAR': 'China',
                               "C?te d'Ivoire": "Côte d'Ivoire",  'Republic of Moldova': 'Moldova'})

df_regions=pd.read_csv(url_regions)


df_total_pigs=df.merge(df_regions, left_on='Area', right_on='name', how='left')\
.dropna(subset=['sub-region'])\
.query('Item == "Meat, pig"')

df_total_pigs['sub-region']=df_total_pigs['intermediate-region'].where(df_total_pigs['sub-region'].eq('Latin America and the Caribbean'),df_total_pigs['sub-region'])
df_total_pigs_last=df_total_pigs[df_total_pigs['Year']==2019]
#df_nan=df_total_pigs[df_total_pigs['sub-region'].isnull()]
#df_nan['Area'].value_counts()
#df_total['Region'].value_counts()

#df_nan=df_total_pigs[df_total_pigs['sub-region'].isnull()]
#df_nan['Area'].value_counts()

#world_region = st.selectbox("Select the Job", pd.unique(df_total_pigs["sub-region"]))

#df_world_region=df_total_pigs[df_total_pigs['sub-region']==world_region]

country = st.multiselect(
     'Select a Country',
      pd.unique(df_total_pigs["Area"]))

source=df_total_pigs\
.query('Area in @country ')

lst = ['Meat, chicken', 'Meat, cattle','Meat, pig','Meat, sheep']


# source=df.query('Area == "Chile"')\
# .query('Item in @lst ')
# source.Year = pd.to_datetime(source.Year, format='%Y')


st.header('Idiom Test with Plotly')
fig = px.line(source, x="Year", y="Value", color='Area',
                 labels={
                     "Value": "Pigs Slaughtered in the thousands",
                     "Item": "Species"
                 },
                title="How many pigs are slaughtered per year in Chile?")
st.plotly_chart(fig, use_container_width=True)

sub_regions= st.multiselect(
     'Select a Region',
      pd.unique(df_total_pigs_last["sub-region"]))

source_tree=df_total_pigs_last\
.query('`sub-region` in @sub_regions ')

fig_tree = px.treemap(source_tree, path=['sub-region', 'Area'],
                 values='Value')

st.plotly_chart(fig_tree, use_container_width=True)

