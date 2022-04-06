import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
  
# loading in the model to predict on the data
pickle_in = open('gym.pkl', 'rb')
g = pickle.load(pickle_in)
  
def welcome():
    return 'welcome all'
  
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(age,height,weight):  
    prediction = g.predict(np.array([age,height,weight]).reshape(1,3))
    print(prediction)
    return prediction
      

 #this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    st.title("GYM PLANNER")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">GYM PLANNER APP </h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    age= st.text_input("AGE", "Type Here")
    height= st.text_input("HEIGHT", "Type Here")
    weight = st.text_input("WEIGHT", "Type Here")
    
    result =""
    r1=""
    r=""
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if st.button("Predict"):
        r1=""
        result = prediction(age,height,weight)
        if(result[0]==0):
            r1="Extremely obese"
            r="Extremely obese--normal exercise+yoga+heavy diet control+TIPS ->Obese"
        elif(result[0]==1):
            r1="Healthy"
            r="Healthy--fitness+protine+simple diet"
        elif(result[0]==2):
            r1="Obese"
            r="Obese--slow lean+protine+full diet ->Overweight"
        elif(result[0]==3):
            r1="Overweight"
            r="Overweight--lean+cardio+protine+normal diet ->Healthy"
        elif(result[0]==4):
            r1="Under Weight"
            r="Under weight--protines+carbs+normal weights ->Healthy"
    st.success('You are {}'.format(r1))
    st.success("Your diet plan is {}".format(r))
     
if __name__=='__main__':
    main()