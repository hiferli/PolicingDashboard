import streamlit as st
import pandas as pd;
import random;
import plotly.express as px

colsForYearWiseDataFrame = ['Block' , 'Primary Type' , 'Description' , 'Year' , 'Latitude' , 'Longitude'];
colsForOffenseWiseDataFrame = ['Block' , 'Primary Type' , 'Description' , 'Year' , 'Latitude' , 'Longitude'];

def getData():
    # API = 'https://data.cityofchicago.org/resource/ijzp-q8t2.json?$query=SELECT%20id%2C%20case_number%2C%20date%2C%20block%2C%20iucr%2C%20primary_type%2C%20description%2C%20location_description%2C%20arrest%2C%20domestic%2C%20beat%2C%20district%2C%20ward%2C%20community_area%2C%20fbi_code%2C%20x_coordinate%2C%20y_coordinate%2C%20year%2C%20updated_on%2C%20latitude%2C%20longitude%2C%20location%20ORDER%20BY%20date%20DESC';
    # crime_df = pd.read_json(API);

    path = 'Files and Data/Chicago.csv'
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
    return years

def getYearWiseDataFrame(crime_df , startYear , endYear):
    # if yearOption == 'All Years': return crime_df[colsForYearWiseDataFrame];
    return crime_df[(crime_df['Year'] >= startYear) & (crime_df['Year'] <= endYear)][colsForYearWiseDataFrame]

def getOffense(crime_df):
    offenses = list(crime_df['Primary Type'].unique());
    offenses.insert(0 , 'All Offenses')
    return offenses

def getOffenseWiseDataframe(crime_df , offenseOption):
    if offenseOption == 'All Offenses': return crime_df[colsForOffenseWiseDataFrame]
    return crime_df[(crime_df['Primary Type'] == offenseOption)][colsForOffenseWiseDataFrame]    

def chicago_page():
    st.set_page_config(
        page_title="Chicago - Dashboard",
        page_icon="chart_with_upwards_trend",
        layout="wide",
    )

    df = getData();
    offenses = getOffense(df);

    st.title("Chicago")

    # Details
    imageColumn , textColumn = st.columns(2);
    with imageColumn:
        st.image('https://d13k13wj6adfdf.cloudfront.net/urban_areas/chicago-1e610b84c3.jpg' , caption='Chicago');
    with textColumn:
        st.header('City in Illinois')
        st.markdown(
            '<div style="text-align: justify;"><b><u><a href=https://www.google.com/search?q=Chicago>Chicago</a></u></b>, on Lake Michigan in Illinois, is among the largest cities in the U.S. Famed for its bold architecture, it has a skyline punctuated by skyscrapers such as the iconic John Hancock Center, 1,451-ft. Willis Tower (formerly the Sears Tower) and the neo-Gothic Tribune Tower. The city is also renowned for its museums, including the Art Institute of Chicago with its noted Impressionist and Post-Impressionist works.</div>' , unsafe_allow_html=True)
        st.header('Population')
        st.write('27 lakhs (2021)');
        
        st.header("Crime Metrics")
        col1, col2 = st.columns(2)
        col1.metric("Reported Crimes", df.shape[0])
        col2.metric("Offenses Reported", len(offenses))

    st.map(df.head(1000) , latitude='Latitude' , longitude='Longitude' , color=getColor());
    # st.dataframe(df)
    st.title("Chicago Crime Report");
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
        st.map(yearWiseData.head(1000) , latitude='Latitude', longitude='Longitude' , color=getColor() , use_container_width=True)

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
            allFrequencyDataFrame = df.groupby('Primary Type')['Primary Type'].count().reset_index(name='values');
            # st.dataframe(allFrequencyDataFrame);
            fig = px.pie(allFrequencyDataFrame, values='values' , names='Primary Type', title='Offense Classification')
            # fig.show()
            st.plotly_chart(fig, theme="streamlit")

        else:
            frequencyDataframe = df[df['Primary Type'] == offenseOption]['Year'].value_counts().sort_index();
            st.bar_chart(frequencyDataframe , color=getColor() , use_container_width=True)
    with tab2:
        st.map(offenseWiseData.head(1000) , latitude='Latitude', longitude='Longitude' , color=getColor() , use_container_width=True)
    
    with tab3:
        st.dataframe(offenseWiseData, use_container_width=True , hide_index=True)

if __name__ == "__main__":
    chicago_page()
