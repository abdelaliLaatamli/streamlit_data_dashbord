import streamlit as st
import pandas as pd



from sections.home import set_metrics , set_area_plot , set_funnel
from sections import set_servers_and_domain_charts,set_sidebar,set_dates_range,set_pie_charts

st.set_page_config(page_title="Dashbord" , page_icon="🌍" , layout="wide")
st.subheader("📧 Email Marketing analytics platform ")
st.markdown("##")


set_sidebar(st)

connection = st.experimental_connection("mysql")

 
start_date , end_date = set_dates_range(st)

if start_date or end_date:
    query = f"SELECT * FROM logs_table WHERE date BETWEEN '{start_date}' AND '{end_date}'"
    data_logs = connection.query(query)

if start_date or end_date:
    query = f"SELECT * FROM actions_table WHERE date BETWEEN '{start_date}' AND '{end_date}'"
    data_actions = connection.query(query)

# st.dataframe(data_actions)


set_metrics(st,data_logs , data_actions)

set_funnel(st,data_logs,data_actions)

set_area_plot(st , data_actions)

set_servers_and_domain_charts(st,data_logs)


set_pie_charts(st,data_logs)



