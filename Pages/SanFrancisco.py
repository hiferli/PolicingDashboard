import streamlit as st
import pandas as pd
import random
import plotly.express as px

colsForYearWiseDataFrame = ['Dates' , 'Category' , 'Descript' , 'Resolution' , 'Address' , 'Long' , 'Lat' , 'Year'];
colsForOffenseWiseDataFrame = ['Dates' , 'Category' , 'Descript' , 'Resolution' , 'Address' , 'Long' , 'Lat' , 'Year'];

def getData():
    # Files and Data/Boston Crime.csv
    path = 'Files and Data/mydata.csv'
    crime_df = pd.read_csv(path , encoding='unicode_escape')
    crime_df = crime_df.dropna(how='any',axis=0) 
    return crime_df

def getColor():
    red = random.randint(180, 255)
    green = random.randint(180, 255)
    blue = random.randint(180, 255)
    hex_color = "#{:02X}{:02X}{:02X}".format(red, green, blue)
    return hex_color

def getYears(crime_df):
    years = list(crime_df['Year'].unique());
    years.sort();
    # print(years)
    return years

def getYearWiseDataFrame(crime_df , startYear , endYear):
    # if yearOption == 'All Years': return crime_df[colsForYearWiseDataFrame];
    return crime_df[(crime_df['Year'] >= startYear) & (crime_df['Year'] <= endYear)][colsForYearWiseDataFrame]

def getOffense(crime_df):
    offenses = list(crime_df['Category'].unique());
    offenses.insert(0 , 'All Offenses')
    return offenses

def getOffenseWiseDataframe(crime_df , offenseOption):
    if offenseOption == 'All Offenses': return crime_df[colsForOffenseWiseDataFrame]
    return crime_df[(crime_df['Category'] == offenseOption)][colsForOffenseWiseDataFrame]

def san_francisco_page():
    st.title("San Francisco Page")
    st.write("Welcome to the San Francisco page!")

    df = getData();
    st.map(df.head(1000) , latitude='Lat' , longitude='Long' , color=getColor());

    st.title("San Francisco Crime Report");

    st.subheader("Year-Wise Classification of Crime")
    years = getYears(df);

    values = st.slider(
        'Select the Year Range: ',
        max(years) , min(years) , (min(years) , max(years)))
    
    col1, col2 = st.columns(2)

    with col1: 
        yearWiseData = getYearWiseDataFrame(df , values[0] , values[-1]);
        st.write(f'{yearWiseData.shape[0]} Records Found For Years: ' , values)
        st.write(f'Rate Limiting Analysis for only {1000} Data Points')
        st.dataframe(yearWiseData, use_container_width=True , hide_index=True)

    with col2:
        st.map(yearWiseData.head(1000) , latitude='Lat', longitude='Long' , color=getColor())

    st.subheader("Offense-Wise Classification of Crime")

    offenses = getOffense(df);
    offenseOption = st.selectbox(
        f"Offense-Wise Data related to the Crimes in Chicagos",
        offenses,
        index=0,
        placeholder="Select An Offense...",
    )
    offenseWiseData = getOffenseWiseDataframe(df , offenseOption);
    st.write(f'{offenseWiseData.shape[0]} Records Found For' , offenseOption)
    tab1, tab2 = st.tabs(['Chart' , 'Data']);
    
    with tab1:
        if(offenseOption == 'All Offenses'):
            allFrequencyDataFrame = df.groupby('Category')['Category'].count().reset_index(name='values');
            # st.dataframe(allFrequencyDataFrame);
            fig = px.pie(allFrequencyDataFrame, values='values' , names='Category', title='Offense Classification')
            # fig.show()
            st.plotly_chart(fig, theme="streamlit")

        else:
            frequencyDataframe = df[df['Category'] == offenseOption]['Year'].value_counts().sort_index();
            st.bar_chart(frequencyDataframe , color=getColor() , use_container_width=True)

    with tab2:
        st.dataframe(offenseWiseData, use_container_width=True , hide_index=True)


if __name__ == "__main__":
    san_francisco_page()
