import pandas as pd
import plotly.express as px

def set_funnel(st,data_logs,data_actions):
    # Sample data (you can replace this with your data)
    delivered = data_logs[data_logs['type'] == 'delivered'].groupby(['type'])['total_count'].sum().reset_index()
    actions = data_actions.groupby(['type'])['total_count'].sum().reset_index().sort_values(by=['total_count'], ascending=False)

    # datas =  pd.concat([actions, delivered]).sort_values(by=['total_count'],ascending=False)
    datas = actions

    # Create a funnel chart using Plotly Express
    fig = px.funnel(datas, x='type', y='total_count', title='Funnel Chart Example')
    fig.update_layout(width=1000)

    # Display the funnel chart in Streamlit
    st.plotly_chart(fig)