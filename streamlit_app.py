import streamlit as st
import pandas as pd

st.sidebar.radio(
    'Select an Option',
    ('Medal Tally','Overall Analysis','Countrywise Analysis', 'Athele-Wise Analysis')
)

