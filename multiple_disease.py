# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the models
diabetes_model = pickle.load(open('C:/Users/Admin/Desktop/multiple_disease/saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('C:/Users/Admin/Desktop/multiple_disease/saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('C:/Users/Admin/Desktop/multiple_disease/saved_models/parkinsons_model.sav', 'rb'))

# Creating side bars for navigation, using option_menu
# after giving heading, we have to create a list of different web pages we want
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System', 
                           ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                           icons = ['activity', 'hearts', 'person'],
                           default_index = 0)
    
# Diabetes Prediction Page
if(selected == 'Diabetes Prediction'):
    #page title
    st.title('Diabetes Prediction using ML')
    
#Creating Columns for input fields:
    col1, col2, col3 = st.columns(3)
    
    with col1:
       Pregancies = st.text_input('Number of pregancies')
       
    with col2:
        Glucose = st.text_input('Glucose Level')
        
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
        
    with col2:
        Insulin = st.text_input('Insulin Level')
        
    with col3:
        BMI = st.text_input('BMI value')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    
    with col2:
        Age = st.text_input ('Age of person')
    
# Code for prediction
    diab_diagnosis = ''
    
    
# Creating a button
    if st.button('Diabetes Prediction Result'):
        diab_prediction = diabetes_model.predict([[Pregancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
    st.success(diab_diagnosis)
        
    
    
    
    
if (selected == 'Heart Disease Prediction'):
    st.title('Heart disease using ML')
    
if (selected == 'Parkinsons Prediction'):
    st.title('Parkinsons Prediction using ML')