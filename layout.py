from dash import dcc, html
import dash_bootstrap_components as dbc
from components import  bar_chart,bar_v_chart, pie_chart, scatter_chart, dropdown_country

def create_layout(app):
    heading = html.H1("Share of consumption by Country",
        className="bg-primary text-white p-2 mb-3")
    return dbc.Container([
        dbc.Row([
            dbc.Col(heading)
        ]),
        dbc.Row([
            dbc.Col(bar_v_chart.render(app), lg=6),
            dbc.Col(pie_chart.render(app), lg=6),
        ]),
        dbc.Row([
            dbc.Col(scatter_chart.render(app), lg=6),
            dbc.Col(bar_chart.render(app), lg=6),
        ])
      
    ])









 #html.H1(
          #"Large Companies", className="header-title"
      #),
      #bar_v_chart.render(app),
      #pie_chart.render(app), 
      #scatter_chart.render(app),
      #bar_chart.render(app)