import flask
import dash
import dash_html_components as html
import pandas as pd

from google.cloud import bigquery
bigquery_client = bigquery.Client()

server = flask.Flask(__name__)

query = \
    """
    SELECT
        COUNT(*) as Rec_Count 
    FROM 
        `bigquery-public-data.census_utility.fips_codes_all`
    """
df = pd.read_gbq(query)

app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/dash/'
)

app.layout = html.Div([
    dcc.Input(id='my-id', value=df['Rec_Count'].iloc[0], type='text'),
    html.Div(id='my-div')
])


if __name__ == '__main__':
    app.run_server(debug=True)