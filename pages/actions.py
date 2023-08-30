import streamlit as st
import plotly.express as px
import os 
from pathlib import Path
import pandas as pd





from sections import set_sidebar,set_dates_range
from sections.actions import set_map_plot

st.set_page_config(page_title="Dashbord" , page_icon="🌍" , layout="wide")
st.subheader("📧 Email Marketing analytics platform ")
st.markdown("### Actions")

set_sidebar(st)


connection = st.experimental_connection("mysql")

start_date , end_date = set_dates_range(st)

if start_date or end_date:
    query = f"SELECT * FROM actions_table WHERE date BETWEEN '{start_date}' AND '{end_date}'"
    data = connection.query(query)
    
set_map_plot(st,data)