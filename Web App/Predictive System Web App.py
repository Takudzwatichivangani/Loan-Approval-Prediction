# -*- coding: utf-8 -*-
"""
Created on Fri May 20 21:29:33 2022

@author: TAKU
"""


import pickle
import numpy as np
import streamlit as st

#loading the saved model
loaded_model=pickle.load(open('C:/Users/TAKU/.spyder-py3/Deployment/trained_model.sav','rb'))

#creating a function for prediction
def loan_prediction(input_data):

      input_data_as_numpy_array=np.asarray(input_data)
      input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)


      Prediction=loaded_model.predict(input_data_reshaped)
      print(Prediction)

      if (Prediction[0]==0):
         print('Loan not approved')
    
      else:
         print('Loan approved!!')
    
def main():
   
 #giving the title
  st.title('Loan Approval Web App')
    
   #getting the input data from the user
  Loan_ID= st.text_input('Loan-ID')
  Gender =st.text_input('Gender')
  Married=st.text_input('Maritial Status')
  Dependents=st.text_input('Dependents')
  Education=st.text_input('Level of Education')
  Self_Employed=st.text_input('Employement Status')
  ApplicantIncome=st.text_input('Applicant Income')
  CoapplicantIncome =st.text_input('Coapplicant Income')
  LoanAmount=st.text_input('Loan Amount')
  LoanAmount_log=st.text_input('Loan Amount log')
  Loan_Amount_Term=st.text_input('Term of the Loan Amount')
  Credit_History =st.text_input('Credit History')
  Property_Area=st.text_input('Property Area')

       #code for prediction
  Loan_Status=''
  
  
  # Creating a button for Loan Status
    
  if st.button('Loan Status'):
   
      Loan_Status=loan_prediction(np.array([Loan_ID,Gender,Married, Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]))
      
  st.success(Loan_Status)
  
if __name__ == '__main__':
    main()
  
  
  
  
  
       