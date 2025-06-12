import pandas as pd 
import matplotlib.pyplot as plt
import plotly.express as px


df = pd.read_csv("Countries.cvs")

fig = px.scatter_geo(
    df, 
    locations = "Country",
    locationmode = "country name",
    color="Average_IQ",
    size="GDP",
    hover_name="Country",
    hover_data=["Education_index","Internet"],
    projection="natural earth",
    title= "Distribution of intelligence and development"
)

fig.show()