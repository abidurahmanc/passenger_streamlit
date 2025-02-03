import streamlit as st
import pickle
import pandas as pd

with open('model.pkl','rb') as file:
    model=pickle.load(file)
# 	Age	Class	Seat_Type	Fare_Paid	Survival_Status	Gender_Male

st.title('Passenger Survival Prediction')
Age=st.number_input('Age',min_value=0)
Class=st.selectbox('Class',['First class','Buisiness','Economy'])
Seat_Type=st.selectbox('seat type',['First class','Buisiness','Economy'])
Fare_Paid=st.number_input('Fare',min_value=0)
Gender=st.selectbox('Gender',['Male','Female'])

input_data={
    'Age':Age,
    'Class':Class,
    'Seat_Type':Seat_Type,
    'Fare_Paid':Fare_Paid,
    'Gender':Gender
    }

# converting it to a df
df=pd.DataFrame([input_data])

# mapping
classes={
    'Economy':0,
    'Business':1,
    'First':2
}
seats={
    'Aisle':0,
    'Middle':1,
    'Window':2
}

df['Seat_Type']=df['Seat_Type'].map(seats)
df['Class']=df['Class'].map(classes)

df=pd.get_dummies(df,columns=['Gender'],drop_first=True)



col=['Age','Class','Seat_Type','Fare_Paid','Gender_Male']

df=df.reindex(columns=col,fill_value=0)


if st.button('Predict'):
    prediction=model.predict(df)[0]
    if prediction==0:
        st.error('Not Survived')
    elif prediction==1:
        st.success('Survived')
