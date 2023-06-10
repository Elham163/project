from .utill import Share_of_consumption
from dash import html, dcc
import plotly.express as px
from dash.dependencies import Input, Output

def render(app):
    df = Share_of_consumption()

    dropdown = dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in df['Countries']],
        value=df['Countries'].iloc[0]
    )

    @app.callback(
        Output('hbar_chart', 'children'),
        [Input('country-dropdown', 'value')]
    )
    def update_graph(country):
        filtered_df = df[df['Countries'] == country]
        fig = px.bar(filtered_df, x='Countries', y='Share_consumption', title=f'Share of Consumption for {country}')
        graph = dcc.Graph(figure=fig)
        return graph

    return html.Div([
        dropdown,
        html.Div(id='hbar_chart')
    ])
