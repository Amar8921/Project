import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.header("""
#SALES PREDICTION
This app predicts the **sales turnover**!
""")
st.write('---')
data=pd.read_csv('pred_data.csv')
x=data.drop('Sales',axis=1)
y=data['Sales']
st.sidebar.header('INPUTS')

def user_input_features():
    DayOfWeek_options=['monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    DayOfWeek = st.sidebar.selectbox('Day Of Week',DayOfWeek_options, index=1)
    DayOfWeek_mapping= {'monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6,'Sunday':7}
    DayOfWeek = DayOfWeek_mapping[DayOfWeek]
    Month_option=['Janvary','Februvary','March','April','May','June','July','August','September','October','November','December']
    Month = st.sidebar.selectbox('Month',Month_option, index=1)
    Month_mapping={'Janvary':1,'Februvary':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
    Month=Month_mapping[Month]
    Customers = st.sidebar.number_input('Customers', min_value=int(x['Customers'].min()))
    Assortment_options = ['Basic', 'Normal', 'Extra']
    Assortment = st.sidebar.selectbox('Assortment', Assortment_options, index=1)
    Assortment_mapping = {'Basic': 0, 'Normal': 1, 'Extra': 2}
    Assortment = Assortment_mapping[Assortment]
    Promo = st.sidebar.number_input('Promo',min_value=0, max_value=1)
    StateHoliday = st.sidebar.number_input('StateHoliday', min_value=0, max_value=1)
    SchoolHoliday = st.sidebar.number_input('SchoolHoliday', min_value=0, max_value=1)
    CompetitionOpen= st.sidebar.number_input('Competition Open',min_value=int(x['CompetitionOpen'].min()))
    CompetitionDistance= st.sidebar.number_input('Competition Distance',min_value=int(x['CompetitionDistance'].min()))
    Promo2 = st.sidebar.number_input('Promo2', min_value=0, max_value=1)
    data1 = {'DayOfWeek': DayOfWeek, 'Customers': Customers, 'Promo': Promo, 'StateHoliday': StateHoliday,'SchoolHoliday': SchoolHoliday, 'Assortment': Assortment, 'CompetitionDistance': CompetitionDistance,'Promo2': Promo2, 'Month': Month, 'CompetitionOpen': CompetitionOpen}
    features = pd.DataFrame(data1, index=[0])
    return features

df=user_input_features()

st.header('Speacified Input parameters')
st.write(df)
st.write('---')

model = LinearRegression()
model.fit(x, y)
prediction = model.predict(df)    
st.header('Prediction of Sales')

# Apply CSS to increase font size
st.markdown(
    f"""
    <style>
    .large-font {{
        font-size: 24px !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.write(f"<div class='large-font'>The predicted sales value is: {prediction[0]:.2f}</div>", unsafe_allow_html=True)
st.write('---')
