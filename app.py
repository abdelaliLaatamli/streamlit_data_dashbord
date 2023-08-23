
import streamlit as st
import plotly.express as px
import numpy as np

st.set_page_config(page_title="Dashbord" , page_icon="🌍" , layout="wide")
st.subheader("📧 Email Marketing analytics platform ")
st.markdown("##")

st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 200px !important; # Set the width to your desired value
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.image("./assets/img/pls.png" , caption="Online Analytics")

st.sidebar.header("Choose your filter")


connection = st.experimental_connection("mysql")


col1, col2 = st.columns(2)

with col1 :
    start_date = st.date_input("Select start date:")

with col2:
    end_date = st.date_input("Select end date:")

if start_date and end_date:
    query = f"SELECT * FROM logs_table WHERE date BETWEEN '{start_date}' AND '{end_date}'"
    data = connection.query(query)
    # st.dataframe(data)

# print(data.empty)
if not data.empty :
    c1,c2,c3,c4,c5=st.columns(5)
    with c1:
       st.info('Queued', icon="📤")
       st.metric(label='Message', value=f"{data['total_count'].sum() }")
    with c2:
       st.info('Delivered', icon="🚚")
       st.metric(label='Message', value=f"{data[data['type'] == 'delivered']['total_count'].sum()}")
    with c3:
       st.info('Bounce', icon="⛔")
       st.metric(label='Message', value=f"{data[data['type'] == 'bounce']['total_count'].sum()}")
    with c4:
       st.info('Soft Bounce', icon="⚠")
       st.metric(label='Message', value=f"{data[(data['type'] == 'bounce') & (data['bounce_type'] == 'soft')]['total_count'].sum()}")
    with c5:
       st.info('Hard Bounce', icon="🚫")
       st.metric(label='Message', value=f"{data[(data['type'] == 'bounce') & (data['bounce_type'] == 'hard')]['total_count'].sum()}")


col1, col2 = st.columns(2)
with col1:
    data_types =  data.groupby('type')['total_count'].sum().reset_index()
    fig = px.pie( data_types , values='total_count', names='type', title='Deliverity Tracking')
    st.plotly_chart(fig)

with col2:
    data_types =  data[data['type'] == 'bounce'].groupby('bounce_type')['total_count'].sum().reset_index()
    fig = px.pie(data_types, values='total_count', names='bounce_type', title='Bounce stats')
    st.plotly_chart(fig)