# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import numpy as np

#loading the saved model
loaded_model=pickle.load(open('C:/Users/TAKU/.spyder-py3/Deployment/trained_model.sav','rb'))
input_data=(5849,0.0,146.412162,4.986426,0,1,0,0,0,0,6,1,2)
input_data_as_numpy_array=np.asarray(input_data)
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)


Prediction=loaded_model.predict(input_data_reshaped)
print(Prediction)

if (Prediction[0]==0):
    print('Loan not approved')
    
else:
    print('Loan approved!!')