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
  COUNTY.county_name,
  FIPS_STATE.state_name,
  COUNTY_2017.total_pop,
  COUNTY_2017.income_per_capita,
  "2017" as year
FROM
  `bigquery-public-data.census_bureau_acs.county_2017_5yr` AS COUNTY_2017
  INNER JOIN `bigquery-public-data.utility_us.us_county_area` AS COUNTY 
  ON COUNTY_2017.geo_id = COUNTY.geo_id
  INNER JOIN `bigquery-public-data.census_utility.fips_codes_states` AS FIPS_STATE
  ON COUNTY.state_fips_code = FIPS_STATE.state_fips_code
WHERE
  FIPS_STATE.state_postal_abbreviation in ('CA','NY','FL','TX','PA','IL')
UNION ALL
SELECT
  COUNTY.county_name,
  FIPS_STATE.state_name,
  COUNTY_2016.total_pop,
  COUNTY_2016.income_per_capita,
  "2016" as year
FROM
  `bigquery-public-data.census_bureau_acs.county_2016_5yr` AS COUNTY_2016
  INNER JOIN `bigquery-public-data.utility_us.us_county_area` AS COUNTY 
  ON COUNTY_2016.geo_id = COUNTY.geo_id
  INNER JOIN `bigquery-public-data.census_utility.fips_codes_states` AS FIPS_STATE
  ON COUNTY.state_fips_code = FIPS_STATE.state_fips_code
WHERE
  FIPS_STATE.state_postal_abbreviation in ('CA','NY','FL','TX','PA','IL')
UNION ALL
SELECT
  COUNTY.county_name,
  FIPS_STATE.state_name,
  COUNTY_2015.total_pop,
  COUNTY_2015.income_per_capita,
  "2015" as year
FROM
  `bigquery-public-data.census_bureau_acs.county_2015_5yr` AS COUNTY_2015
  INNER JOIN `bigquery-public-data.utility_us.us_county_area` AS COUNTY 
  ON COUNTY_2015.geo_id = COUNTY.geo_id
  INNER JOIN `bigquery-public-data.census_utility.fips_codes_states` AS FIPS_STATE
  ON COUNTY.state_fips_code = FIPS_STATE.state_fips_code
WHERE
  FIPS_STATE.state_postal_abbreviation in ('CA','NY','FL','TX','PA','IL')
    """
df = pandas_gbq.read_gbq(query, dialect='standard', progress_bar_type=None)

app = dash.Dash(
    __name__,
    server=server #,
)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]
    traces = []
    for i in filtered_df.state_name.unique():
        df_by_state = filtered_df[filtered_df['state_name'] == i]
        traces.append(dict(
            x=df_by_state['total_pop'],
            y=df_by_state['income_per_capita'],
            text=df_by_state['county_name'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
        ))

    return {
        'data': traces,
        'layout': dict(
            xaxis={'type': 'log', 'title': 'Population',
                   'range':[3.5, 7]},
            yaxis={'title': 'Income per Capita', 'range': [10000, 70000]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest',
            transition = {'duration': 500},
        )
    }

if __name__ == '__main__':
    app.run_server(debug=True)
