import streamlit as st
import pandas as pd
import numpy as np

def getLatLong():
    # Files and Data/Boston Crime.csv
    path = 'Files and Data/Boston Crime.csv'
    crime_df = pd.read_csv(path , encoding='unicode_escape')
    crime_df = crime_df.dropna(how='any',axis=0) 
    # crime_df = crime_df
    crime_df['OFFENSE_CODE'] = "#" + crime_df['OFFENSE_CODE'].astype(str)
    # print(crime_df['OFFENSE_CODE'][0])
    filtered_df = crime_df[['Lat', 'Long', 'OFFENSE_CODE']]
    filtered_df.columns = ['latitude', 'longitude', 'offense_code']

    # TODO: Try making a different color segmnet for different colors

    return filtered_df


def boston_page():
    st.title("Boston Page")
    st.write("Welcome to the Boston page!")

    df = getLatLong();
    st.map(df , latitude='latitude', longitude='longitude')

    # st.dataframe(df) 

if __name__ == "__main__":
    boston_page()
