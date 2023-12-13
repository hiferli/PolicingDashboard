import streamlit as st
import pandas as pd
import numpy as np

def getData():
    # Files and Data/Boston Crime.csv
    path = 'Files and Data/Boston Crime.csv'
    crime_df = pd.read_csv(path , encoding='unicode_escape')
    crime_df = crime_df.dropna(how='any',axis=0) 
    return crime_df

def getYears(crime_df):
    years = list(crime_df['YEAR'].unique());
    years.insert(0 , 'All Years')
    return years

def getYearWiseDataFrame(crime_df , yearOption):
    returnCols = ['OFFENSE_CODE' , 'OFFENSE_DESCRIPTION' , 'OCCURRED_ON_DATE' , 'Location'];
    if yearOption == 'All Years': return crime_df[returnCols];
    return crime_df[(crime_df['YEAR'] == yearOption)][returnCols];



def boston_page():
    st.title("Boston Page")
    st.write("Welcome to the Boston page!")

    df = getData();
    st.map(df , latitude='Lat', longitude='Long')

    st.title("Boston Crime Report");

    st.subheader("Year-Wise Classification of Crime")
    years = getYears(df);
    yearOption = st.selectbox(
        f"Data related to the Crimes in Boston",
        years,
        index=0,
        placeholder="Select contact method...",
    )

    st.dataframe(getYearWiseDataFrame(df , yearOption), use_container_width=True , hide_index=True)
    st.write('Showing Results for year: ', yearOption)

if __name__ == "__main__":
    boston_page()
