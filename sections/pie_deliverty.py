import plotly.express as px

def set_pie_charts(st,data):
    col1, col2 = st.columns(2)
    with col1:
        data_types =  data.groupby('type')['total_count'].sum().reset_index()
        fig = px.pie( data_types , values='total_count', names='type', title='Deliverity Tracking')
        st.plotly_chart(fig)

    with col2:
        data_types =  data[data['type'] == 'bounce'].groupby('bounce_type')['total_count'].sum().reset_index()
        fig = px.pie(data_types, values='total_count', names='bounce_type', title='Bounce stats')
        st.plotly_chart(fig)