import pickle
import joblib
import pandas as pd
import numpy as np
import streamlit as st
import base64

filename = 'final_model_fraud.pkl'
model = pickle.load(open(filename, 'rb'))

st.set_page_config(page_title='Fraud Detection', page_icon="🔎", layout="wide")


html_temp = """
<div style="background-color:MediumSeaGreen;padding:10px">
<h1 style="color:white;text-align:center;">FRAUD DETECTION</h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)

st.image("fraud.jpg")
st.write('\n')


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
  
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

#set_background('background.jpg')

html_temp2 = """
<div style="background-color:Gray;padding:10px">
<h3 style="color:white;text-align:center;">Input Values </h3>
</div><br>"""
st.markdown(html_temp2,unsafe_allow_html=True)
 
column_1, column_2 = st.columns((3,3))

with column_1:
    V10=st.slider("V10", -24.588, 23.745, -7.0, step=0.05)
    st.write('\n')
    V11=st.slider("V11", -4.797, 12.019, 11.0, step=0.05)
    st.write('\n')
    V12=st.slider("V12", -18.684, 7.848, -4.0, step=0.05)
    
with column_2:
    V14=st.slider("V14", -19.214, 10.527, -7.0, step=0.05)
    st.write('\n')
    V16=st.slider("V16", -14.130, 17.315, -4.0, step=0.05)
    st.write('\n')
    V17=st.slider("V17", -25.163, 9.254, -20.0, step=0.05)
 
ColorMinMax = st.markdown(''' <style> div.stSlider > div[data-baseweb = "slider"] > div[data-testid="stTickBar"] > div { background: white; } </style>''', unsafe_allow_html = True)
Slider_Cursor = st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"]{ background-color: rgb(187, 43, 130); box-shadow: rgb(251 92 92 / 20%) 0px 0px 0px 0.3rem;} </style>''', unsafe_allow_html = True)
Slider_Number = st.markdown(''' <style> div.stSlider > div[data-baseweb="Square"] > div > div > div > div { color: rgb(14, 38, 74); } </style>''', unsafe_allow_html = True)

col = f''' <style> div.stSlider > div[data-baseweb = "slider"] > div > div {{ background: linear-gradient(to right, rgb(1, 183, 158) 0%, 
                    rgb(187, 213, 145), 
                    rgba(96, 164, 149, 0.75), 
                    rgba(14, 38, 74, 0.75) 100%); }} </style>'''

ColorSlider = st.markdown(col, unsafe_allow_html = True)   





my_dict = {'V10':V10,
         'V11':V11,
             'V12':V12,
             'V14':V14,
         'V16':V16,
             'V17': V17
            }

columns = ['V10',
       'V11',
           'V12',
           'V14',
       'V16',
           'V17'
          ]

button_style = """ 
<style> div.stButton > button:first-child { 
display: block;
width: 100%;
border: none;
background-color: #a62440;
color: white;
padding: 14px 28px;
font-size: 24px;
cursor: pointer;
text-align: center; 
}
.button span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
}
.button span:after {
  content: '\00bb';
  position: absolute;
  opacity: 0;
  top: 0;
  right: -20px;
  transition: 0.5s;
}
.button:hover span {
  padding-right: 25px;
}
.button:hover span:after {
  opacity: 1;
  right: 0;
  }
</style>
"""
st.markdown(button_style, unsafe_allow_html=True) 

df = pd.DataFrame.from_dict([my_dict])
prediction = model.predict(df)


c1, c2, c3,c4,c5= st.columns((1,1,3,1,1)) 
with c3:
    if c3.button("CHECK"):
      
      if prediction == 1:
          st.error('  🚨 ATTENTION FRAUD DETECTED 🚨')
      elif prediction == 0:
          st.success('  ✅ NO FRAUD DETECTED')


      
