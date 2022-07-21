import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

uploaded_file = st.file_uploader('FAOSTAT_data_7-20-2022.csv')
if uploaded_file is not None:
     # # To read file as bytes:
     # bytes_data = uploaded_file.getvalue()
     # st.write(bytes_data)
     # 
     # # To convert to a string based IO:
     # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
     # st.write(stringio)
     # 
     # # To read file as string:
     # string_data = stringio.read()
     # st.write(string_data)

     # Can be used wherever a "file-like" object is accepted:
     df = pd.read_csv(uploaded_file)
     st.write(df.head(5))



st.title("Haciendo gráficos con altair en streamlit")


#df=pd.read_csv('FAOSTAT_data_7-20-2022.csv') 

source=df.query('Area == "Chile"')
st.write(source.head(5))

# c = alt.Chart(df).mark_circle().encode(
#      x='a', y='b', color='c', tooltip=['a', 'b', 'c'])
# 
# st.altair_chart(c, use_container_width=True)
