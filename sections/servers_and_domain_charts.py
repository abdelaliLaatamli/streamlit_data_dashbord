import plotly.express as px
from pandasql import sqldf

def set_servers_and_domain_charts(st , data ):
    col1, col2 = st.columns(2)
    with col1 :
        dt = prepare_date(data)
        melted_df = dt.melt(id_vars='Server', var_name='Value_Type', value_name='Value')
        fig = px.bar(melted_df, x='Value', y='Server', orientation='h', color='Value_Type' , barmode='group')
        st.plotly_chart(fig)
    with col2:
        dt = data[data['type'] == 'delivered'].groupby(['email_domain'])['total_count'].sum().reset_index().head(10).sort_values(by=["total_count"],ascending=True)
        fig = px.pie(dt, names='email_domain', values='total_count', hole=0.5)
        fig.update_layout(title='Deliverable by Domain')
        st.plotly_chart(fig)


def prepare_date(data):
    dd = data
    dd['bounce_type']=data['bounce_type'].fillna("--")

    query = """
    SELECT 
        server_name as Server,
        sum(total_count) as total ,
        (select sum(d.total_count) from dd as d where ddd.server_name = d.server_name and d.type='delivered') as delivered ,
        (select sum(d.total_count) from dd as d where ddd.server_name = d.server_name and d.type='bounce') as bounce
    FROM dd as ddd
    group by server_name
    order by total asc

    limit 10;
    """

    # Run the query
    return sqldf(query)