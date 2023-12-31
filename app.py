from dash import Dash, html
import dash_bootstrap_components as dbc
from layout import create_layout

def main():
  app = Dash(external_stylesheets=[dbc.themes.COSMO])
  server=app.server
  app.title='Solar Power by country'
  app.layout = create_layout(app)
  app.run_server(debug=True)

if __name__ == '__main__':
  main()
