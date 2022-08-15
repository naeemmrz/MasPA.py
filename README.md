
![Logo](https://github.com/naeemmrz/MasPA.py/blob/main/MasPA_logo.png?raw=true)

    
# MasPA.py

MasPA.py is a ML-based Web App that can predict the **Risk of Mastitis** in cattle from simple easy-to-obtain cost-effective sensor data.

## Authors

Abdul Ghafoor N.¹² & Sitkowska B.²
###### ¹Mugla Sitki Kocman University, Faculty of Science, Department of Molecular Biology and Genetics, Mugla, Turkey.
###### ²University of Science and Technology Bydgoszcz, Department of Biotechnology and Animal Genetics, Bydgoszcz, Poland.
###### [Click Here For The Corresponding Article](https://doi.org/10.3390/agriengineering3030037)

 
### Notice: 
#### The online version of MasPA is deprecated and will no longer be available in the online-version after 31.12.2022. Please use the offline version by following the "Run Locally" section. 

  
## Usage
## [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/naeemmrz/maspa.py/main/MasPA.py)
- Click on the "Open in Streamlit" badge above. 
- Download the example input and upload your input files accordingly, the abbreviations as follows: 
- Front left udder inhale limit (IUFL) front left udder exhale limit (EUFL), front right udder inhale limit (IUFR), front right udder exhale limit (EUFR), rear left udder inhale limit (IURL) rear left udder exhale limit (EURL), rear right udder inhale limit (IURR), rear right udder exhale limit (EURR), temperature of the cattle.
- The results will automatically show up, a download link will also be provided.

  
## Run Locally

Download the project

```bash
  wget https://github.com/naeemmrz/MasPA.py.git
```

Unzip and go to the project directory

```bash
  unzip MasPA.py-main.zip
  cd MasPA.py-main
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the application

```bash
  streamlit run MasPA.py
```

#### The Application will open in your default browser with the same interface as the online version.

  
## Acknowledgements
If you find our work useful, please cite us as:\
**Abdul Ghafoor N, Sitkowska B. MasPA: A Machine Learning Application to Predict Risk of Mastitis in Cattle from AMS Sensor Data. AgriEngineering. 2021; 3(3):575-583. https://doi.org/10.3390/agriengineering3030037**

###### Data used to train the model for this app was obtained from *K, ANKITHA; D H, MANJAIAH ; M, Kartik (2020) “Clinical Mastitis in Cows based on Udder Parameter using Internet of Things (IoT)”, Mendeley Data, V2 (doi: 10.17632/kbvcdw5b4m.2)*, consider citing them as well if you use this app.

MasPA.py is distributed under CC BY 4.0 without any guarantee, you may use it for almost any purpose (unless stated otherwise) and/or modify and adapt it for your own use as long as the proper credits and citations are provided.
