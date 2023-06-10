import plotly.express as px
from dash import Dash, html, dcc
from .utill import Share_of_consumption

def render(app):
    df=Share_of_consumption()
    fig=px.bar(df, x="Countries", y="Share_consumption",orientation= 'v', title='')
    return html.Div(dcc.Graph(figure=fig), id="barv_chart")