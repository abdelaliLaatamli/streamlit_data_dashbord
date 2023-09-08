import plotly.express as px
import pandas as pd
from pandasql import sqldf
import plotly.graph_objs as go


def set_area_plot(st,data):
    # df_pivot = data.groupby(['date','type'])['total_count'].sum().reset_index()
    # df_pivot['date'] = df_pivot['date'].astype(str)
    # df_pivot = df_pivot.pivot(index='date', columns='type', values='total_count')
    # df_pivot = df_pivot.fillna(0)
    # st.line_chart( df_pivot , height=500)

    dat = prepare_date( data)
    st.bar_chart( dat , height=500)




def prepare_date(data):


    query = """
    SELECT 
        job_id ,
        (select COALESCE( sum(dts.total_count) , 0) from data as dts where dt.job_id = dts.job_id and dts.type='open') as opens ,
        (select COALESCE( sum(dts.total_count) , 0) from data as dts where dt.job_id = dts.job_id and dts.type='click') as clicks
    FROM data as dt
    group by job_id
    order by opens desc , clicks desc
    limit 10
    """

    new_dt = sqldf(query)
    new_dt['job_id'] = new_dt['job_id'].astype(str)
    new_dt = new_dt.set_index( 'job_id' )
    return new_dt