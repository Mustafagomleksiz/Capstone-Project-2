import streamlit as st
import pandas as pd
import pickle
import joblib
import base64

df_columns = open("my_columns.pkl","rb")
df_columns = joblib.load(df_columns)

filename = 'final_model_hr.pkl'
model = pickle.load(open(filename, 'rb'))

st.set_page_config(page_title='Employee Churn Analysis', page_icon="👩‍💻", layout="wide")


st.sidebar.title('Configure Employee Churn')
satisfaction_level = st.sidebar.number_input("Satisfaction Level", min_value =0.09, max_value = 1.0, value=0.50)
number_project = st.sidebar.selectbox("Number Project",( "2","3","4","5","6" ,"7"))
time_spend_company = st.sidebar.selectbox("Time Spend Company",( "2","3","4","5","6","7","8","9","10"))
average_montly_hours = st.sidebar.number_input("Average Montly Hours", min_value =96, max_value = 310, value=180)
last_evaluation = st.sidebar.number_input("Last Evaluation", min_value =0.36, max_value = 1.0, value=0.65)


my_dict = {
"satisfaction_level": satisfaction_level,
"number_project" : number_project,
"time_spend_company" : time_spend_company,
"average_montly_hours": average_montly_hours,
"last_evaluation" : last_evaluation}



html_temp = """
<div style="background-color:#3A5874;padding:10px">
<h1 style="color:white;text-align:center;">WILL YOUR EMPLOYEE LEAVE OR STAY ?</h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)

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


set_background('g9.png')

st.image("work.png")

html_temp2 = """
<div style="background-color:#3A5874;padding:10px">
<h3 style="color:white;text-align:center;">Complete the levels left menu and  ease your worries with Employee Churn Analysis</h3>
</div><br>"""
st.markdown(html_temp2,unsafe_allow_html=True)


#predict = st.sidebar.button("P R E D I C T")

df=pd.DataFrame.from_dict([my_dict])
st.table(df)



html_temp = """
<div style="background-color:#6F8EA6;padding:5px">
<h3 style="color:white;text-align:center;">Predict and Learn !</h3>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)

_, _, _,  col, _, _, _ = st.columns([1]*6+[0.30])

button_style = """ 
<style> div.stButton > button:first-child { 
display: block;
width: 100%;
border: none;
background-color: #3A5874;
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
  transition: 1.5s;
}
.button span:after {
  content: '\00bb';
  position: absolute;
  opacity: 0;
  top: 0;
  right: -20px;
  transition: 1.5s;
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

if col.button("Predict"): 
    

    #my_dict = pd.get_dummies(df) 
    #my_dict = my_dict.reindex(columns = df_columns, fill_value=0)
    pred = model.predict(df)
    
    #st.write(pred)
    if pred == 0:
        html_temp = """
        <div style="background-color:MediumSeaGreen">
        <h4 style="color:white;text-align:center;">Employee will stay 👍</h4>
        </div><br>"""
        st.markdown(html_temp,unsafe_allow_html=True)
        
    elif pred == 1:
        html_temp = """
        <div style="background-color:Tomato">
        <h4 style="color:white;text-align:center;">Employee will leave 👎</h4>
        </div><br>"""
        st.markdown(html_temp,unsafe_allow_html=True)
        





