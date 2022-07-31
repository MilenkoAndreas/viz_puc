#Librerias
import pandas as pd
import numpy as np
#import altair as alt
import streamlit as st
#import plotly.figure_factory as ff
import plotly.express as px
import streamlit.components.v1 as components
import urllib
import requests
from PIL import Image

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
#session = requests.Session()
#response = session.get(st.secrets["image_pig"], stream = True)

#save_response_content(response,'pigs.png')

@st.cache(suppress_st_warning=True)
def set_image(url):
    session = requests.Session()
    response = session.get(url, stream = True)
    save_response_content(response,'cow.png')
    image = Image.open('cow.png')
    return image
    
st.set_page_config(layout="wide")


st.title("How many cows do we slaugther?")

#image = Image.open('pigs.png')
image = set_image(st.secrets["image_cow"])

fig_col_a, fig_col_b = st.columns(2)

with fig_col_a:
     
     st.image(image, caption='',)
   
with fig_col_b:
     st.header("Meet the individual")
     st.text("Cows lick each other to help remain\n calm in stressful situations")
     st.text("Cows have a complex social structure\n with strong familial bonds")
     st.text("Cows form social grooming partnerships\n similar to chimpanzees")
     st.text("Despite their size, cows love to jump\n and play, especially in sunshine")




#st.markdown("# Plotting Demo")
#st.sidebar.header("Plotting Demo")



sheet_id = st.secrets["sheet_id"]
sheet_name = st.secrets["sheet_name"]

#sheet_region = st.secrets["sheet_region"]
sheet_region = "all"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
url_regions=f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_region}"

df=pd.read_csv(url)
df['Value']=df['Value']*1000

df['Area']=df['Area'].replace({'China, mainland': 'China', 'T?rkiye': 'Turkey',
                               'China, Taiwan Province of': 'China', 'Viet Nam': 'Vietnam', 'Brunei Darussalam': 'Brunei',
                               'China, Macao SAR': 'China', 'Sudan (former)': 'Sudan', 'China, Hong Kong SAR': 'China',
                               "C?te d'Ivoire": "Côte d'Ivoire",  'Republic of Moldova': 'Moldova'})

df_regions=pd.read_csv(url_regions)


df_total_pigs=df.merge(df_regions, left_on='Area', right_on='name', how='left')\
.dropna(subset=['sub-region'])\
.query('Item == "Meat, cattle"')

df_total_pigs['sub-region']=df_total_pigs['intermediate-region'].where(df_total_pigs['sub-region'].eq('Latin America and the Caribbean'),df_total_pigs['sub-region'])
df_total_pigs_last=df_total_pigs[df_total_pigs['Year']==2020]
#df_nan=df_total_pigs[df_total_pigs['sub-region'].isnull()]
#df_nan['Area'].value_counts()
#df_total['Region'].value_counts()

#df_nan=df_total_pigs[df_total_pigs['sub-region'].isnull()]
#df_nan['Area'].value_counts()

#world_region = st.selectbox("Select the Job", pd.unique(df_total_pigs["sub-region"]))

#df_world_region=df_total_pigs[df_total_pigs['sub-region']==world_region]



#lst = ['Meat, chicken', 'Meat, cattle','Meat, pig','Meat, sheep']


# source=df.query('Area == "Chile"')\
# .query('Item in @lst ')
# source.Year = pd.to_datetime(source.Year, format='%Y')


# st.header('Idiom Test with Plotly')
# fig = px.line(source, x="Year", y="Value", color='Area',
#                  labels={
#                      "Value": "Pigs Slaughtered in the thousands",
#                      "Item": "Species"
#                  },
#                 title="How many pigs are slaughtered per year in Chile?")
# st.plotly_chart(fig, use_container_width=True)





# create two columns for charts
fig_col1, fig_col2 = st.columns(2)

with fig_col1:
     country = st.multiselect(
     'Select a Country',
      pd.unique(df_total_pigs["Area"]),default=["Chile"])

     source=df_total_pigs\
      .query('Area in @country ')
  
     fig = px.line(source, x="Year", y="Value", color='Area',
                     labels={
                         "Value": "",
                         "Item": ""
                     },
                    title="How many cows are slaughtered per year?")
     st.plotly_chart(fig, use_container_width=True)
   
with fig_col2:
     sub_regions= st.multiselect(
         'Select a Region',
          pd.unique(df_total_pigs_last["sub-region"]),default=["South America"])
    
     source_tree=df_total_pigs_last\
     .query('`sub-region` in @sub_regions ')
     fig_tree = px.treemap(source_tree, path=['sub-region', 'Area'],
                   values='Value',
                    title="How many cows were slaughtered in 2020?")
  
     st.plotly_chart(fig_tree, use_container_width=True)
