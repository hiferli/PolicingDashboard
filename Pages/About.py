import streamlit as st

def about_page():
    st.set_page_config(
        page_title="About - Predictive Analysis in Policing",
        page_icon="🚔",
        layout="wide"
    )

    st.title("About")
    st.markdown("<div style='text-align: justify;'>Significant economic and social changes are being brought about by the steadily rising urbanization of cities, which presents a number of difficulties for service and management providers. Especially in places with greater rates of crime, adequately addressing public safety is an increasingly difficult task. To manage this intricacy, novel technologies are being providing police forces with more access to crime-related data volumes that can be examined in order to identify trends and patterns. These technological advancements could enhance the effective use of police resources within a certain area and eventually encourage more efficient deterrence of crime.</div>" , unsafe_allow_html=True , help="Source: Abstract")
    st.text("")
    st.markdown("<div style='text-align: justify;'>To effectively fill in the gaps in the current detection mechanisms, crime prediction is a complex problem that calls for sophisticated analytical tools. The growing availability of crime data combined with technological advancements has given researchers a unique opportunity to investigate crime detection through the application of machine learning and deep learning techniques.</div>" , unsafe_allow_html=True , help="Source: Introduction")
    st.text("")
    st.text("")
    st.markdown("<div style='text-align: justify;'>The main objective of our project is:<ul><li>Using algorithms and visualization to analyze crime data from multiple sources, including crime reports, social media, and police records, providing a more comprehensive view of criminal activities.</li><li>To work on time series model that analyses the crime data collected to predict the location and type of crime going to occur at a location.</li><li>To compare the performance of different time series for better accuracy and precision.</li><li>Design and Develop Application-Based Solution containing Dashboards which helps personnels in their daily work hence contributing to a safe neighbourhood and data-driven security system</li></ul></div>" , unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'><h3><a href='https://drive.google.com/file/d/1M1qdVG4vZdc1o_ShCvHH6CIZcjU6SIno/view?usp=sharing' target='_blank'>Read more</a></h3></div>" , unsafe_allow_html=True)

if __name__ == "__main__":
    about_page()
