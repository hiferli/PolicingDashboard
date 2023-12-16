import streamlit as st
import pandas as pd
import numpy as np
import random
import plotly.express as px

colsForYearWiseDataFrame = ['OFFENSE_CODE' , 'OFFENSE_DESCRIPTION' , 'OCCURRED_ON_DATE' , 'STREET' , 'Lat' , 'Long'];
colsForOffenseWiseDataFrame = ['OFFENSE_DESCRIPTION' , 'OCCURRED_ON_DATE' , 'STREET' , 'Lat' , 'Long'];

def getData():
    # Files and Data/Boston Crime.csv
    path = 'Files and Data/Boston Crime.csv'
    crime_df = pd.read_csv(path , encoding='unicode_escape')
    crime_df = crime_df.dropna(how='any',axis=0) 
    return crime_df

def getYears(crime_df):
    years = list(crime_df['YEAR'].unique());
    # years.insert(0 , 'All Years')
    years.sort();
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

def getColor():
    red = random.randint(180, 255)
    green = random.randint(180, 255)
    blue = random.randint(180, 255)
    hex_color = "#{:02X}{:02X}{:02X}".format(red, green, blue)
    return hex_color


def boston_page():
    st.title("Boston Page")
    st.write("Welcome to the Boston page!")

    df = getData();
    st.map(df , latitude='Lat', longitude='Long' , color=getColor())

    st.title("Boston Crime Report");

    st.subheader("Year-Wise Classification of Crime")
    years = getYears(df);

    values = st.slider(
        'Select the Year Range: ',
        max(years) , min(years) , (min(years) , max(years)))
    
    col1, col2 = st.columns(2)

    with col1: 
        yearWiseData = getYearWiseDataFrame(df , values[0] , values[-1]);
        st.write(f'{yearWiseData.size} Records Found For Years: ' , values)
        st.dataframe(yearWiseData, use_container_width=True , hide_index=True)

    with col2:
        st.map(yearWiseData , latitude='Lat', longitude='Long' , color=getColor())
    
    st.subheader("Offense-Wise Classification of Crime")

    offenses = getOffense(df);
    offenseOption = st.selectbox(
        f"Offense-Wise Data related to the Crimes in Boston",
        offenses,
        index=0,
        placeholder="Select An Offense...",
    )
    
    offenseWiseData = getOffenseWiseDataframe(df , offenseOption);
    st.write(f'{offenseWiseData.size} Records Found For' , offenseOption)
    tab1, tab2 = st.tabs(['Chart' , 'Data']);
    
    with tab1:
        if(offenseOption == 'All Offenses'):
            allFrequencyDataFrame = df.groupby('OFFENSE_CODE_GROUP')['OFFENSE_CODE_GROUP'].count().reset_index(name='values');
            # st.dataframe(allFrequencyDataFrame);
            fig = px.pie(allFrequencyDataFrame, values='values' , names='OFFENSE_CODE_GROUP', title='Offense Classification')
            # fig.show()
            st.plotly_chart(fig, theme="streamlit")

        else:
            frequencyDataframe = df[df['OFFENSE_CODE_GROUP'] == offenseOption]['YEAR'].value_counts().sort_index();
            st.bar_chart(frequencyDataframe , color=getColor() , use_container_width=True)

    with tab2:
        st.dataframe(offenseWiseData, use_container_width=True , hide_index=True)


if __name__ == "__main__":
    boston_page()
