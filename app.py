
import streamlit as st

from sections import set_metrics,set_sidebar,set_dates_range,set_pie_charts

st.set_page_config(page_title="Dashbord" , page_icon="🌍" , layout="wide")
st.subheader("📧 Email Marketing analytics platform ")
st.markdown("##")


set_sidebar(st)

connection = st.experimental_connection("mysql")

 
start_date , end_date = set_dates_range(st)

if start_date or end_date:
    query = f"SELECT * FROM logs_table WHERE date BETWEEN '{start_date}' AND '{end_date}'"
    data = connection.query(query)


set_metrics(st,data)


set_pie_charts(st,data)

