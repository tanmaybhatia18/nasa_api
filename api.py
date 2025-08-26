import requests
import streamlit as st

api_key='3ONz7BlikvezeLz6AvetYdRcTiuLOCZAQFsftZxN'
url=f'https://api.nasa.gov/planetary/apod?api_key={api_key}'
response=requests.get(url).json()

st.title('Hope you are not gonna say because NASA got the picture of the DAYY')
st.subheader(response['title'])

if response['media_type']=='image':
    st.image(response['url'],caption=response['title'])
else:
    st.video(response['url'])

st.write(response['explanation'])

#running on terminal as streamlit run api.py gives program