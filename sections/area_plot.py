import plotly.express as px
import pandas as pd
from pandasql import sqldf

def set_area_plot(st,data):
    dt = prepare_date(data)
    # st.dataframe(dt)
    dt['Drop'] = 'ID - ' + dt['Drop'].astype('string') 

    melted_df = dt.melt(id_vars='Drop', var_name='Value_Type', value_name='Value')
    
    # Create a spline area chart using Plotly Express
    fig = px.area(melted_df, x='Drop', y='Value', color='Value_Type', title='Spline Area Chart with Multiple Values',line_shape='spline')
    fig.update_layout(width=1100)
    # Render the chart using Streamlit
    st.plotly_chart(fig)


def prepare_date(data):
    dd = data
    dd['bounce_type']=data['bounce_type'].fillna("--")

    query = """
    SELECT 
        job_id as 'Drop',
        (select sum(d.total_count) from dd as d where ddd.job_id = d.job_id and d.type='bounce') as bounce ,
        (select sum(d.total_count) from dd as d where ddd.job_id = d.job_id and d.type='delivered') as delivered,
        sum(total_count) as total  
    FROM dd as ddd
    group by job_id
    order by total asc

    limit 10;
    """


    # Run the query
    new_dt = sqldf(query)
    
    new_dt['delivered']=new_dt['delivered'].fillna(0)
    new_dt['bounce']=new_dt['bounce'].fillna(0)
    # df['ID'] = df['ID'].astype('int64')
    # print( new_dt )
    return new_dt
