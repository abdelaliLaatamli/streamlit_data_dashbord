import os 
from pathlib import Path
import pandas as pd
import plotly.express as px

# https://plotly.com/python/builtin-colorscales/
def set_map_plot(st,data):
    grouped_by = data[['country' , 'total_count']] \
        .groupby('country')['total_count'] \
        .agg('sum') \
        .reset_index() \
        .sort_values(by=['total_count'], ascending=False)

    countries = pd.read_csv( Path( os.path.join( os.getcwd() , "./data/all.csv") ).resolve() )[['alpha-2', 'alpha-3']]

    joined = grouped_by.join(countries.set_index('alpha-2'), on='country')[['alpha-3', 'total_count']]
    joined.rename(columns={'alpha-3': 'country'}, inplace=True)
   
    custom_colors = ["#FF5733", "#FFC300", "#4CAF50", "#008CBA", "#5634A1"]


    fig = px.choropleth(
        joined,
        locations='country',  # Column with ISO-3 country codes
        color='total_count',             # Column with data values
        hover_name='country',  # Tooltip labels
        color_continuous_scale="Viridis",  # Color scale
        # color_continuous_scale=custom_colors,
        title="Choropleth Map with DataFrame"
    )

    # Adjust the layout to make the map width 100%
    fig.update_layout(
        autosize=False,
        width=1200,  # Set the width to the screen width
        height=800  # Set the height as needed
    )


    # Display the Plotly figure using Streamlit
    st.plotly_chart(fig)
