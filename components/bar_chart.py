from .utill import Share_of_consumption
from dash import Dash, html, dcc
import plotly.express as px

def render(app):
    df = Share_of_consumption()
    fig = px.bar(df, x= 'Countries', y = 'Share_consumption', title = 'Horizontal Bar Chart')
    return html.Div(dcc.Graph(figure=fig), id='hbar_chart')