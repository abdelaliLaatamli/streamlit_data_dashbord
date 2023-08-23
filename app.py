
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
       st.info('Percentile 25 %', icon="⏱")
       st.metric(label='USD', value=f"{np.percentile(data['total_count'], 25):,.2f}")
    with c2:
       st.info('Percentile 50 %', icon="⏱")
       st.metric(label='USD', value=f"{np.percentile(data['total_count'], 50):,.2f}")
    with c3:
       st.info('Percentile 75 %', icon="⏱")
       st.metric(label='USD', value=f"{np.percentile(data['total_count'], 75):,.2f}")
    with c4:
       st.info('Percentile 100 %', icon="⏱")
       st.metric(label='USD', value=f"{np.percentile(data['total_count'], 100):,.2f}")
    with c5:
       st.info('Percentile 0 %', icon="⏱")
       st.metric(label='USD', value=f"{np.percentile(data['total_count'], 0):,.2f}")


col1, col2 = st.columns(2)
with col1:
    data_types =  data.groupby('type')['total_count'].sum().reset_index()
    fig = px.pie( data_types , values='total_count', names='type', title='Deliverity Tracking')
    st.plotly_chart(fig)

with col2:
    data_types =  data[data['type'] == 'bounce'].groupby('bounce_type')['total_count'].sum().reset_index()
    fig = px.pie(data_types, values='total_count', names='bounce_type', title='Bounce stats')
    st.plotly_chart(fig)