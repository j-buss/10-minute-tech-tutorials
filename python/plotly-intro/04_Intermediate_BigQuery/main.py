import flask
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import pandas_gbq
import numpy as np

#from google.cloud import bigquery
#bigquery_client = bigquery.Client()

server = flask.Flask(__name__)

query = \
    """
    SELECT
      FIPS_STATE.state_name,
      COUNTY.county_name,
      '2017' as year,
      FORMAT("%10.f", COUNTY_2017.total_pop) as total_pop,
      FORMAT("%10.f",COUNTY_2017.income_per_capita) as income_per_capita,
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
      FIPS_STATE.state_name,
      COUNTY.county_name,
      '2016' as year,
      FORMAT("%10.f", COUNTY_2016.total_pop) as total_pop,
      FORMAT("%10.f",COUNTY_2016.income_per_capita) as income_per_capita,
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
      FIPS_STATE.state_name,
      COUNTY.county_name,
      '2015' as year,
      FORMAT("%10.f", COUNTY_2015.total_pop) as total_pop,
      FORMAT("%10.f",COUNTY_2015.income_per_capita) as income_per_capita,
    FROM
      `bigquery-public-data.census_bureau_acs.county_2015_5yr` AS COUNTY_2015
      INNER JOIN `bigquery-public-data.utility_us.us_county_area` AS COUNTY 
      ON COUNTY_2015.geo_id = COUNTY.geo_id
      INNER JOIN `bigquery-public-data.census_utility.fips_codes_states` AS FIPS_STATE
      ON COUNTY.state_fips_code = FIPS_STATE.state_fips_code
    WHERE
      FIPS_STATE.state_postal_abbreviation in ('CA','NY','FL','TX','PA','IL')
    UNION ALL
    SELECT
      FIPS_STATE.state_name,
      COUNTY.county_name,
      '2014' as year,
      FORMAT("%10.f", COUNTY_2014.total_pop) as total_pop,
      FORMAT("%10.f",COUNTY_2014.income_per_capita) as income_per_capita,
    FROM
      `bigquery-public-data.census_bureau_acs.county_2014_5yr` AS COUNTY_2014
      INNER JOIN `bigquery-public-data.utility_us.us_county_area` AS COUNTY 
      ON COUNTY_2014.geo_id = COUNTY.geo_id
      INNER JOIN `bigquery-public-data.census_utility.fips_codes_states` AS FIPS_STATE
      ON COUNTY.state_fips_code = FIPS_STATE.state_fips_code
    WHERE
      FIPS_STATE.state_postal_abbreviation in ('CA','NY','FL','TX','PA','IL')
    UNION ALL
    SELECT
      FIPS_STATE.state_name,
      COUNTY.county_name,
      '2013' as year,
      FORMAT("%10.f", COUNTY_2013.total_pop) as total_pop,
      FORMAT("%10.f",COUNTY_2013.income_per_capita) as income_per_capita,
    FROM
      `bigquery-public-data.census_bureau_acs.county_2013_5yr` AS COUNTY_2013
      INNER JOIN `bigquery-public-data.utility_us.us_county_area` AS COUNTY 
      ON COUNTY_2013.geo_id = COUNTY.geo_id
      INNER JOIN `bigquery-public-data.census_utility.fips_codes_states` AS FIPS_STATE
      ON COUNTY.state_fips_code = FIPS_STATE.state_fips_code
    WHERE
      FIPS_STATE.state_postal_abbreviation in ('CA','NY','FL','TX','PA','IL')
    UNION ALL
    SELECT
      FIPS_STATE.state_name,
      COUNTY.county_name,
      '2012' as year,
      FORMAT("%10.f", COUNTY_2012.total_pop) as total_pop,
      FORMAT("%10.f",COUNTY_2012.income_per_capita) as income_per_capita,
    FROM
      `bigquery-public-data.census_bureau_acs.county_2012_5yr` AS COUNTY_2012
      INNER JOIN `bigquery-public-data.utility_us.us_county_area` AS COUNTY 
      ON COUNTY_2012.geo_id = COUNTY.geo_id
      INNER JOIN `bigquery-public-data.census_utility.fips_codes_states` AS FIPS_STATE
      ON COUNTY.state_fips_code = FIPS_STATE.state_fips_code
    WHERE
      FIPS_STATE.state_postal_abbreviation in ('CA','NY','FL','TX','PA','IL')
    UNION ALL
    SELECT
      FIPS_STATE.state_name,
      COUNTY.county_name,
      '2011' as year,
      FORMAT("%10.f", COUNTY_2011.total_pop) as total_pop,
      FORMAT("%10.f",COUNTY_2011.income_per_capita) as income_per_capita,
    FROM
      `bigquery-public-data.census_bureau_acs.county_2011_5yr` AS COUNTY_2011
      INNER JOIN `bigquery-public-data.utility_us.us_county_area` AS COUNTY 
      ON COUNTY_2011.geo_id = COUNTY.geo_id
      INNER JOIN `bigquery-public-data.census_utility.fips_codes_states` AS FIPS_STATE
      ON COUNTY.state_fips_code = FIPS_STATE.state_fips_code
    WHERE
      FIPS_STATE.state_postal_abbreviation in ('CA','NY','FL','TX','PA','IL')
    UNION ALL
    SELECT
      FIPS_STATE.state_name,
      COUNTY.county_name,
      '2010' as year,
      FORMAT("%10.f", COUNTY_2010.total_pop) as total_pop,
      FORMAT("%10.f",COUNTY_2010.income_per_capita) as income_per_capita,
    FROM
      `bigquery-public-data.census_bureau_acs.county_2010_5yr` AS COUNTY_2010
      INNER JOIN `bigquery-public-data.utility_us.us_county_area` AS COUNTY 
      ON COUNTY_2010.geo_id = COUNTY.geo_id
      INNER JOIN `bigquery-public-data.census_utility.fips_codes_states` AS FIPS_STATE
      ON COUNTY.state_fips_code = FIPS_STATE.state_fips_code
    WHERE
      FIPS_STATE.state_postal_abbreviation in ('CA','NY','FL','TX','PA','IL')
    ORDER BY state_name
    """

df = pandas_gbq.read_gbq(query, dialect='standard', progress_bar_type=None)

df = df.replace(to_replace='None', value=np.nan).dropna()
df['year'] = df['year'].astype('int64')
df['total_pop'] = df['total_pop'].astype('int64')
df['income_per_capita'] = df['income_per_capita'].astype('int64')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(
    __name__,
    server=server,
    external_stylesheets=external_stylesheets
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
def update_figure(value):
    filtered_df = df[df.year == value]
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
                   'range': [2.5, 8]},
            yaxis={'title': 'Income per Capita', 'range': [10000, 72000]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest',
            transition={'duration': 500},
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)
