
import streamlit as st
import plotly.express as px
import numpy as np
import datetime
from sections import set_metrics,set_sidebar

st.set_page_config(page_title="Dashbord" , page_icon="🌍" , layout="wide")
st.subheader("📧 Email Marketing analytics platform ")
st.markdown("##")


set_sidebar(st)

connection = st.experimental_connection("mysql")

date_range = st.date_input(
    "Select your vacation for next year",
    (datetime.datetime.now(), datetime.datetime.now()),
    format="MM.DD.YYYY",
)
# print(date_range)
# print(len(date_range))

# col1, col2 = st.columns(2)

# with col1 :
#     start_date = st.date_input("Select start date:")

# with col2:
#     end_date = st.date_input("Select end date:")
 
if date_range:
    if len(date_range) > 0 :
        start_date = date_range[0]
        end_date = date_range[1] if len(date_range) > 1 else date_range[0]


    query = f"SELECT * FROM logs_table WHERE date BETWEEN '{start_date}' AND '{end_date}'"
    data = connection.query(query)


set_metrics(st,data)


# col1, col2 = st.columns(2)
# with col1:
#     data_types =  data.groupby('type')['total_count'].sum().reset_index()
#     fig = px.pie( data_types , values='total_count', names='type', title='Deliverity Tracking')
#     st.plotly_chart(fig)

# with col2:
#     data_types =  data[data['type'] == 'bounce'].groupby('bounce_type')['total_count'].sum().reset_index()
#     fig = px.pie(data_types, values='total_count', names='bounce_type', title='Bounce stats')
#     st.plotly_chart(fig)