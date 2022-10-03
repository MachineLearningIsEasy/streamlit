import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# Шаг 1
#-----------------------------------------
# st.title('Hello World! This is a Title')

# # Шаг 2
##-----------------------------------------

# st.subheader('Here, a subheader')

# st.text('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum.')

# st.write('This is can be used for text and other features.')

# # Шаг 3
#-----------------------------------------

# df = sns.load_dataset('iris')

# st.title('Some Examples')

# st.write('Hello :sunglasses: :heart: ')

# st.write(1+1)

# a = 2**2
# st.write(a)

# st.write(df.head())


# Шаг 4
#-----------------------------------------
image = Image.open('BDS.png')
st.image(image)


# Шаг 5
#-----------------------------------------
# latlong = {'London': {'lat': 51.509865,'lon': -0.118092},
#            'Paris': {'lat': 48.864716, 'lon':2.349014},
#            'Rome': {'lat': 41.902782,'lon': 12.496366},
#            'Moscow': {'lat': 56.216336,'lon': 38.10921}
#            }

# city = ['London', 'Paris','Rome', 'Moscow']
# df = pd.DataFrame()
# df['lat'] = [latlong[x]['lat'] for x in city]
# df['lon'] = [latlong[x]['lon'] for x in city]
# # Map
# map_df = df[['lat', 'lon']]
# st.map(map_df, zoom=1)

# Шаг 6
#-----------------------------------------
st.radio('Choose your option', options=('Option 1', 'Option 2', 'Option 3'))


st.slider('<-- Slide to the sides -->', min_value=0, max_value=10, value=5, step=1)

st.text('Checkbox')
st.multiselect('What are your favorite colors',
            ['Green', 'Yellow', 'Red', 'Blue'],
            ['Blue', 'Green'])

st.selectbox('Select Box',options=('Option 1', 'Option 2', 'Option 3'))

title = st.text_input('My App Text Input', 'Write Something...')
st.write('You wrote:  ', title)