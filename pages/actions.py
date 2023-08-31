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

    query = f"SELECT * FROM drive_stats WHERE date BETWEEN '{start_date}' AND '{end_date}'"
    data_devices = connection.query(query)

# st.dataframe(data_devices)
    
set_map_plot(st,data)

col1, col2 = st.columns(2)
with col1:
    device_type = data_devices[['device_type' , 'total_count']].groupby(['device_type'])['total_count'].sum().reset_index().head(10).sort_values(by=["total_count"],ascending=True)
    fig = px.pie(device_type, names='device_type', values='total_count' )
    fig.update_layout(title='Device type')
    st.plotly_chart(fig)

with col2:
    device_type = data_devices[['os_family' , 'total_count']].groupby(['os_family'])['total_count'].sum().reset_index().head(10).sort_values(by=["total_count"],ascending=False)
    fig = px.bar( device_type, x='os_family', y='total_count'  )
    fig.update_layout(title='Operating System')
    st.plotly_chart(fig)



col1, col2 = st.columns(2)


with col1:
    device_type = data_devices[['browser_family' , 'total_count']].groupby(['browser_family'])['total_count'].sum().reset_index().head(10).sort_values(by=["total_count"],ascending=True)
    fig = px.pie(device_type, names='browser_family', values='total_count' , hole=0.4 )
    fig.update_layout(title='Browser')
    st.plotly_chart(fig)


with col2:
    touch_capable = data_devices[['device_touch_capable' , 'total_count']]
    touch_capable['device_touch_capable'] = touch_capable['device_touch_capable'].apply(lambda x: True if x == 1 else False)
    touch_capable = touch_capable[['device_touch_capable' , 'total_count']].groupby(['device_touch_capable'])['total_count'].sum().reset_index().head(10).sort_values(by=["total_count"],ascending=True)
    fig = px.pie(touch_capable, names='device_touch_capable', values='total_count' , hole=0.8 , color_discrete_sequence=px.colors.sequential.RdBu )
    fig.update_layout(title='Touch Capable')
    st.plotly_chart(fig)