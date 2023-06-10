from .utill import Share_of_consumption
from dash import Dash, html, dcc
import plotly.express as px

def render(app):
    df = Share_of_consumption()
    fig = px.pie(df, names = 'Countries', values = 'Share_consumption', title = 'Vertical Bar Chart')
    return html.Div(dcc.Graph(figure=fig), id='pie_chart')

