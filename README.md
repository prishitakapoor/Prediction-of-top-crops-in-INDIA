# Prediction-of-top-crops-in-INDIA

<h2>Description</h2>
  <p>Predict the top 3 crops that can be grown in India based on the input parameters like state, district and season.</p>
  <p>This file has a Flask web app which functions like an api. The input parameters can be given through a call to the local host link</p>
  <p>The output can be obtained as a JSON response</p>

<h2>ML model details</h2>
  <p>
    This problem uses a multi-class classification approach. The model is a label powerset model imported from Scikit-Learn. 
    The label_pst.pkl file contains the trained weights for this problem. It returns a scipy-sparse-matrix which is processed and the top
    3 crops that can be grown in the region are returned as a JSON response.
  </p>
  
<h2>Data</h2>
  <p>
    The data was downloaded from data.gov.in website.
  </p>
