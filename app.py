
import streamlit as st
import plotly.express as px

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
    st.dataframe(data)


# fig = px.bar(data, x=x_column, y=y_column, title=f"{x_column} vs {y_column}")
# fig = px.pie(df2, valeus='total_count', names='index', hole=0.5)
col1, col2 = st.columns(2)
with col1:
    data_types =  data.groupby('type')['total_count'].sum().reset_index()
    fig = px.pie( data_types , values='total_count', names='type', title='Delivered')
    st.plotly_chart(fig)

with col2:
    data_types =  data[data['type'] == 'bounce'].groupby('bounce_type')['total_count'].sum().reset_index()
    fig = px.pie(data_types, values='total_count', names='bounce_type', title='Distribution by Type')
    st.plotly_chart(fig)