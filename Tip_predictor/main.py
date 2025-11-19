import streamlit as st
import pickle
st.title('Tip amount predictor')
st.header('Select your bill amount so that i can predict tip for that')
bill=st.slider('Bill Amount',min_value=0,max_value=5000,step=10)
if st.button('submit'):
    with open('file.pkl','rb') as file:
      model=pickle.load(file)
      out=model.predict([(bill,)])
      st.write(f'Tip amount which you will get is {out}')
      st.header('Thank you for using')
