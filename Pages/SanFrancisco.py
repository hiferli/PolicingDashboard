import streamlit as st
import pandas as pd
import random
import plotly.express as px

colsForYearWiseDataFrame = ['Dates' , 'Category' , 'Descript' , 'Resolution' , 'Address' , 'Long' , 'Lat' , 'Year'];
colsForOffenseWiseDataFrame = ['Dates' , 'Category' , 'Descript' , 'Resolution' , 'Address' , 'Long' , 'Lat' , 'Year'];

def getData():
    # Files and Data/Boston Crime.csv
    path = 'Files and Data/San Francisco.csv'
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
    st.set_page_config(
        page_title="San Francisco - Dashboard",
        page_icon="chart_with_upwards_trend",
        layout="wide",
    )

    df = getData();
    offenses = getOffense(df);

    st.title("San Francisco")

    # Details
    imageColumn , textColumn = st.columns(2);
    with imageColumn:
        st.image('https://e1.pxfuel.com/desktop-wallpaper/427/284/desktop-wallpaper-golden-gate-bridge-san-francisco-bay-iphone-golden-gate-bridge-phone-thumbnail.jpg' , caption='San Francisco')
    
    with textColumn:
        st.header('City in California')
        st.markdown(
            '<div style="text-align: justify;"><b><u><a href=https://www.google.com/search?q=San+Francisco>San Francisco</a></u></b>, officially the City and County of San Francisco, is the commercial, financial, and cultural center of Northern California. The city proper is the fourth most populous city in California, <i>with 808,437 residents</i>, and the 17th most populous city in the United States as of 2022'
            , unsafe_allow_html=True)
        st.header('Population')
        st.write('8.15 lakhs (2021)');
    
        st.header("Crime Metrics")
        col1, col2 = st.columns(2)
        col1.metric("Reported Crimes", df.shape[0])
        col2.metric("Offenses Reported", len(offenses))

    st.map(df.head(2000) , latitude='Lat' , longitude='Long' , color=getColor() , use_container_width=True);

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

    offenseOption = st.selectbox(
        f"Offense-Wise Data related to the Crimes in Chicagos",
        offenses,
        index=0,
        placeholder="Select An Offense...",
    )
    offenseWiseData = getOffenseWiseDataframe(df , offenseOption);
    st.write(f'{offenseWiseData.shape[0]} Records Found For' , offenseOption)
    tab1 , tab2 , tab3 = st.tabs(['Chart' , 'Map' , 'Data']);
    
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
        st.map(offenseWiseData.head(1000) , latitude='Lat' , longitude='Long' , color=getColor() , use_container_width=True);
    
    with tab3:
        st.dataframe(offenseWiseData, use_container_width=True , hide_index=True)


if __name__ == "__main__":
    san_francisco_page()
