import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as pt

st.title('Netflix show Rating Analysis')
st.sidebar.title('Netflix show Rating Analysis')
st.sidebar.markdown('This application is a Streamlit dashboard to analyse the netflix ratings')
st.markdown('This application is a Streamlit dashboard to analyse the netflix ratings')
st.subheader('Guidelines')
st.markdown('PG-13 --> A film contains material deemed unsuitable for children under the age of 13')
st.markdown('R --> Restricted - Under 17 requires accompanying parent or adult guardian')
st.markdown('TV-14 --> A film contains material deemed unsuitable for children under the age of 14')
st.markdown('TV-MA --> A film suitable for mature audiences only')
st.markdown('TV-PG --> Parental guideline suggested')

@st.cache(persist=True)
def load():
    df=pd.read_csv('netf.csv')
    df1=df.drop_duplicates(subset='title',keep='first',inplace=True)
    return df
df=load()

st.sidebar.subheader('Show random shows')
ran_show=st.sidebar.radio('Shows',('PG-13','R','TV-14','TV-MA','TV-PG'))
st.sidebar.markdown(df.query('rating==@ran_show')[['title']].sample(n=1).iat[0,0])

st.sidebar.markdown('### Number of shows released in particular year')
sel=st.sidebar.selectbox('Visualization type',['Histogram'],key='1')

s_count=df['release_year'].value_counts()
s_count=pd.DataFrame({'Release_Year':s_count.index,'Count':s_count.values})

if not st.sidebar.checkbox('Hide',True):
    st.markdown('### Number of shows released')
    if sel=='Histogram':
        fig=pt.bar(s_count,x='Release_Year',y='Count',color='Release_Year',height=400)
        st.plotly_chart(fig)


res=df.sort_values(by='user_rating_score',ascending=False)
st.sidebar.subheader('Top rated netflix shows')
if st.sidebar.checkbox('Show data',False):
    st.subheader('Top 20 shows')
    st.write(res.head(20))

st.sidebar.subheader('Shows based on release year')
choice=st.sidebar.multiselect('Choose a Year',('2017','2016','2015','2014','2013','2012'),key=0)
if len(choice)>0:
    c_data=df[df.release_year.isin(choice)]
    st.subheader('Shows based on best rating')
    res=c_data.sort_values(by='user_rating_score',ascending=False)
    st.write(res)

st.sidebar.subheader('Shows based on Category')
c1=st.sidebar.multiselect('Choose a Category',('TV-14','R','PG-13','TV-MA','TV-PG'),key=0)
if len(c1)>0:
    c1_data=df[df.rating.isin(c1)]
    st.subheader('Shows based on best rating')
    res1=c1_data.sort_values(by='user_rating_score',ascending=False)
    st.write(res1)
