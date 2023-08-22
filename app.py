
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Dashbord" , page_icon="🌍" , layout="wide")
st.subheader("📧 Email Marketing analytics platform ")
st.markdown("##")

st.sidebar.image("./assets/img/pls.png" , caption="Online Analytics")

st.sidebar.header("Choose your filter")


connection = st.experimental_connection("mysql")

# pet_owners = connection.query('SELECT * FROM logs_table limit 1000')
# st.dataframe(pet_owners)



# Get user input for date range
start_date = st.date_input("Select start date:")
end_date = st.date_input("Select end date:")

if start_date and end_date:
    query = f"SELECT * FROM logs_table WHERE date BETWEEN '{start_date}' AND '{end_date}'"
    data = connection.query(query)
    # print( data )
    st.dataframe(data)

# print( data )
df2 =  data.groupby('type')['total_count'].sum().reset_index()

# for col in df2.index:
#     print(col)
# print(df2)
# print(df2.describe())

# fig = px.bar(data, x=x_column, y=y_column, title=f"{x_column} vs {y_column}")
# fig = px.pie(df2, valeus='total_count', names='index', hole=0.5)
fig = px.pie(df2, values='total_count', names='type', title='Distribution by Type')
st.plotly_chart(fig)