import flask
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import pandas_gbq

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
df = pandas_gbq.read_gbq(query, dialect='standard', progress_bar_type=None)

app = dash.Dash(
    __name__,
    server=server #,
)

app.layout = html.Div([
    dcc.Input(id='my-id', value=df['Rec_Count'].iloc[0], type='text'),
    html.Div(id='my-div')
])

@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)

if __name__ == '__main__':
    app.run_server(debug=True)
