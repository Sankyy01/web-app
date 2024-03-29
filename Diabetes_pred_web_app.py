# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 23:39:34 2024

@author: gurav
"""

import numpy as np
import pickle
import streamlit as st

#load the save model
loaded_model = pickle.load(open('D:/Diabetes pred api/trained_model.sav','rb'))

#creating function for prediction

def diabetes_prediction(input_data):
    
    #changing input data to numpy array
    input_data_as_numpy_array=np.asarray(input_data)
    
    #reshaping the array as we are predecting one instance
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if(prediction[0]==0):
      return'the person is not diabetic'
    else:
      return'the person is diabetic'


def main():
    
    
    #give title
    st.title('Diabetes Prediction System')
    
    #getting input from user
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure Value')
    SkinThickness = st.text_input('Skin Thickness Value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI Vlue')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    Age = st.text_input('Age of the person')
    
    #code for prediction
    diagnosis = ''
    
    #creting button for prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
    st.success(diagnosis)
    
if __name__== '__main__':
    main()