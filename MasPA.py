import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64
import sklearn
from PIL import Image
from sklearn.ensemble import RandomForestClassifier

image = Image.open('MasPA_logo.png')
st.image(image, use_column_width=True)

st.write("""
Developed by N. Abdul-Ghafoor¹² and B. Sitkowska²
""")

st.write("""
###### ¹Mugla Sitki Kocman University, Faculty of Science, Department of Molecular Biology and Genetics, Mugla, Turkey.\n 
""")

st.write("""
###### ²University of Science and Technology Bydgoszcz, Department of Biotechnology and Animal Genetics, Bydgoszcz, Poland.
""")

st.write("""
\n
[Click Here For More Details](https://www.google.com)
\n
User Input:
""")


st.sidebar.markdown("""
[Example CSV input file](https://github.com/naeemmrz/MasPA.py/blob/main/example_input_file.csv)
""")

# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])

if uploaded_file is not None:
    input_dff = pd.read_csv(uploaded_file)
    #input_dff.set_index('ID')
    input_df = input_dff.drop(["ID"], axis=1)
    st.write(input_dff)
else:
    st.write("""
    **Awaiting CSV file to be uploaded**.
    """)
    st.stop()

#st.sidebar.markdown("""
###### Data used to train this model was obtained from K, ANKITHA; D H, MANJAIAH ; M, Kartik (2020) “Clinical Mastitis in Cows based on Udder Parameter using Internet of Things (IoT)”, Mendeley Data, V2 (doi: 10.17632/kbvcdw5b4m.2).
#""")
st.sidebar.markdown("""
Please cite this work if you find it useful
"CITATION"
""")


# Reads in saved classification model
load_clf = pickle.load(open('RndmForest_mastistis.pkl', 'rb'))

# Apply model to make predictions
prediction = load_clf.predict(input_df)
prediction_proba = load_clf.predict_proba(input_df)

st.write("""
# Predictions
""")

Health = np.array(['At_Risk_of_Mastitis', 'No_Significant_Mastitis_Risk']) #[0,1] order hence 0=mastitis and 1=Healthy
st.write(Health[prediction])

##Activate this if you're interested in the exact probabilities of each classification
st.subheader("""
Prediction Probability 
##### P(0)= P(Risk of Mastitis) | P(1) = P(No Mastitis Risk) 
""")
pp = prediction_proba
#ppdf = pd.DataFrame(pp)
st.write(pp)

Healthdf = pd.DataFrame(Health[prediction])

out = pd.concat([input_df, input_dff['ID'], Healthdf], axis=1)
output = out.set_axis(['Months_after_giving_birth', 'IUFL', 'EUFL', 'IUFR', 'EUFR', 'IURL', 'EURL', 'IURR', 'EURR', 'Temperature', 'ID', 'Prediction' ], axis=1, inplace=False)
#results = pd.concat([output, input_dff['ID']], axis=1)

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="Prediction_Results.csv">Download csv file</a>'
    return(href)	

st.markdown(get_table_download_link(output), unsafe_allow_html=True)

