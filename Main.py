import streamlit as st
from Pages.Chicago import chicago_page
from Pages.Boston import boston_page
from Pages.SanFrancisco import san_francisco_page
from Pages.About import about_page;

def main():
    st.set_page_config(
        page_title="Advanced Policing",
        page_icon="🚨"
    )

    st.sidebar.title("Select a City")
    selected_page = st.sidebar.radio("Cities", ["About", "Chicago", "Boston", "San Francisco"])

    if selected_page == "About":
        about_page()
    elif selected_page == "Chicago":
        chicago_page()
    elif selected_page == "Boston":
        boston_page()
    elif selected_page == "San Francisco":
        san_francisco_page()

if __name__ == "__main__":
    main()
