import seaborn as sns
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# Set Page Layout
st.set_page_config(layout='wide')

#-----------------------------------------------------------------------
# Load the Dataset
df = sns.load_dataset('titanic')

#-----------------------------------------------------------------------

# SIDEBAR
# Let's add some functionalities in a sidebar

st.sidebar.subheader('Select to Filter the data')

# By Sex
st.sidebar.text('By Sex')
filter_sex = st.sidebar.radio('Filter By Sex', options=['Both', 'female', 'male'])
if filter_sex == 'Both':
    pass
else:
    df = df[df['sex']==filter_sex]

# By City
st.sidebar.text('By embarked')
filter_embarked = st.sidebar.multiselect('Filter By embarked', options=['S', 'C','Q'])
df = df[df['embarked'].isin(filter_embarked)]

# Title
st.title('Titanic Dashboard')

# Subheader
st.subheader('Titanic statistics.')

#Separator
st.markdown('---')

# #-----------------------------------------------------------------------

# Columns Summary

st.subheader('| QUICK SUMMARY')

col1, col2, col3, col4 = st.columns(4)

with col1:
    mean_fare = f'{df.fare.mean()}'
    st.title('Mean fare')
    st.text(mean_fare)

with col2:
    st.title('Age')
    st.text(f'Age max: {df.age.max()}')
    st.text(f'Age min: {df.age.min()}')

with col3:
    st.title('Survived')
    st.text(df.survived.value_counts())

with col4:
    st.title('Class')
    st.text(df.pclass.value_counts())

# #-----------------------------------------------------------------------

# Graphics
col1, col2, col3 = st.columns(3)

with col1:
    ind1 = pd.DataFrame(df.groupby('sex').sex.count()).rename(columns={'sex':'count'}).reset_index()
    g1 = px.pie(ind1,
                values='count',
                names='sex',
                color='sex',
                color_discrete_map={'male': 'royalblue','female': 'pink'},
                title='| GENDER')
    g1.update_traces(textposition='inside',
                     textinfo='percent+label',
                     showlegend=False)
    st.plotly_chart(g1, use_container_width=True)

with col2:
    ind3 = pd.DataFrame(df.groupby('embark_town').embark_town.count()).rename(columns={'embark_town':'count'}).reset_index()
    g3 = px.bar(ind3,
                x='embark_town',
                y='count',
                title='| Embark town')
    st.plotly_chart(g3, use_container_width=True)

with col3:
    ind2 = pd.DataFrame(df.groupby('alone').alone.count()).rename(columns={'alone':'count'}).reset_index()
    g2 = px.pie(ind2,
                values='count',
                names='alone',
                color='alone',
                color_discrete_map={False: 'royalblue',True: 'darkblue'},
                title='| Alone')
    g2.update_traces(textposition='inside',
                     textinfo='percent+label',
                     showlegend=False)
    st.plotly_chart(g2, use_container_width=True)
