import streamlit as st
from Pages.Chicago import chicago_page
from Pages.Boston import boston_page
from Pages.SanFrancisco import san_francisco_page
from Pages.About import about_page;

def main():
    st.set_page_config(
        page_title="Predictive Analysis in Policing",
        page_icon="🚨",
        layout="wide"
    )
    # st.snow()
    st.title("Predictive Analysis in Policing" )
    st.markdown("<p style='font-size: 10px;'>Pioneering Tomorrow's Policing With The Power of Predictive Analysis</p>" , unsafe_allow_html=True)
    

    st.header("Available Dashboards:" , divider=True)
    boston , chicago , sanFrancisco = st.columns(3);
    with boston:
        st.markdown("<h3><a target='_self' href='/Boston'>Boston</a></h3>" , unsafe_allow_html=True)
        st.write("A City in Massachusetts")
        st.image('https://d13k13wj6adfdf.cloudfront.net/urban_areas/boston-7399414b98.jpg');

    with chicago:
        st.markdown("<h3><a target='_self' href='/Chicago'>Chicago</a></h3>" , unsafe_allow_html=True)
        st.write("A City in Illinois")
        st.image('https://d13k13wj6adfdf.cloudfront.net/urban_areas/chicago-1e610b84c3.jpg');

    with sanFrancisco:
        st.markdown("<h3><a target='_self' href='/SanFrancisco'>San Francisco</a></h3>" , unsafe_allow_html=True)
        st.write("A City in California")
        st.image('https://d13k13wj6adfdf.cloudfront.net/urban_areas/new-york-9cb6cc2ae5.jpg')

    st.write("")
    st.markdown("<a href='/About' target='_self' style='text-decoration: none; color: inherit; border: 2px solid white; border-radius: 10px; padding: 5px 10px; display: inline-block; text-align: left'>Read more about us here</a>" , unsafe_allow_html=True)
if __name__ == "__main__":
    main()
