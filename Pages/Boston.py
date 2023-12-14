import streamlit as st
import pandas as pd
import numpy as np

colsForYearWiseDataFrame = ['OFFENSE_CODE' , 'OFFENSE_DESCRIPTION' , 'OCCURRED_ON_DATE' , 'Location'];
colsForOffenseWiseDataFrame = ['OFFENSE_DESCRIPTION' , 'OCCURRED_ON_DATE' , 'Location'];

def getData():
    # Files and Data/Boston Crime.csv
    path = 'Files and Data/Boston Crime.csv'
    crime_df = pd.read_csv(path , encoding='unicode_escape')
    crime_df = crime_df.dropna(how='any',axis=0) 
    return crime_df

def getYears(crime_df):
    years = list(crime_df['YEAR'].unique());
    # years.insert(0 , 'All Years')
    return years

def getOffense(crime_df):
    offenses = list(crime_df['OFFENSE_CODE_GROUP'].unique());
    offenses.insert(0 , 'All Offenses')
    return offenses

def getYearWiseDataFrame(crime_df , startYear , endYear):
    # if yearOption == 'All Years': return crime_df[colsForYearWiseDataFrame];
    return crime_df[(crime_df['YEAR'] >= startYear) & (crime_df['YEAR'] <= endYear)][colsForYearWiseDataFrame];

def getOffenseWiseDataframe(crime_df , offenseOption):
    if offenseOption == 'All Offenses': return crime_df[colsForOffenseWiseDataFrame]
    return crime_df[(crime_df['OFFENSE_CODE_GROUP'] == offenseOption)][colsForOffenseWiseDataFrame]    

def boston_page():
    st.title("Boston Page")
    st.write("Welcome to the Boston page!")

    df = getData();
    st.map(df , latitude='Lat', longitude='Long')

    st.title("Boston Crime Report");

    st.subheader("Year-Wise Classification of Crime")
    years = getYears(df);

    values = st.slider(
        'Select the Year Range: ',
        max(years) , min(years) , (min(years) , max(years)))

    yearWiseData = getYearWiseDataFrame(df , values[0] , values[-1]);
    st.write(f'{yearWiseData.size} Records Found For Years: ' , values)
    st.dataframe(yearWiseData, use_container_width=True , hide_index=True)
    
    st.subheader("Offense-Wise Classification of Crime")
    offenses = getOffense(df);
    offenseOption = st.selectbox(
        f"Offense-Wise Data related to the Crimes in Boston",
        offenses,
        index=0,
        placeholder="Select An Offense...",
    )
    
    st.dataframe(getOffenseWiseDataframe(df , offenseOption), use_container_width=True , hide_index=True)
    st.write('Showing Results for year: ', offenseOption)

if __name__ == "__main__":
    boston_page()
