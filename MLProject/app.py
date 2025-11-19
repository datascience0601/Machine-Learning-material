import pandas as pd 
import streamlit as st 
import pickle 
st.set_page_config(page_title='Home_proce_prediction',page_icon='home_icon.jpg')
st.header('Welcome to bengaluru home price predictor:')
df=pd.read_csv('copied_dataset.csv')
with open('RFmodel.pkl','rb') as file:
    model=pickle.load(file)
with st.container(border=True):
    col1,col2=st.columns(2)
    loc=col1.selectbox("Location:",options=df['location'].unique())
    sqft=col1.number_input('sqft',min_value=300)
    bath=col2.number_input('No_of_bathrooms',min_value=1)
    bhk=col2.number_input('No_of_bedrooms',min_value=1)
    encoded_loc=list(df['location'])
    encoded_loc.sort()
    input_values=[(encoded_loc.index(loc),sqft,bath,bhk)]
    c1,c2,c3=st.columns([1.6,1.5,1])

    if c2.button('predict price'):
        out=model.predict(input_values)
        st.subheader(f'price💰: {out[0]*100000}')