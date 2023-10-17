import plotly.io as pio
import plotly.express as px
import rasterio
from rasterio.plot import show
import pandas as pd
import requests

#this function visualized any given COG inside of a mapbox view
def visualize_COG(layer_url, zoom=None):
    pio.renderers.default = 'notebook'
    # pio.renderers.default = 'jupyterlab'
    # pio.renderers.default = 'colab'

    # seed value, for mapbox to load in colab
    df = pd.DataFrame([[1001, 5.3],[1001, 5.3]])
    df.columns = ["flips", "unemp"]
    fig = px.choropleth_mapbox(
                                df, 
                                color='unemp',
                                color_continuous_scale="Viridis",
                                range_color=(0, 12),
                                mapbox_style="carto-positron",
                                zoom=4, center = {"lat": 33.543682, "lon": -86.779633},
                                opacity=0.5,
                              )
    fig.update_layout(
        mapbox_layers=[
            {
                "sourcetype": "raster",
                "source": [layer_url]
            }
          ])
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.update_layout(mapbox_style="stamen-terrain")
    fig.layout.mapbox.zoom = 1
    fig.show()
