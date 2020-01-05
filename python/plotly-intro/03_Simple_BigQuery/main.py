import flask
import dash
import dash_html_components as html

from google.cloud import bigquery
bigquery_client = bigquery.Client()

server = flask.Flask(__name__)

@server.route('/')
def index():
    # Define query_job and query object
    query_job = bigquery_client.query(
        """
        SELECT 
          COUNT(*) as Rec_Count 
        FROM 
          `bigquery-public-data.census_utility.fips_codes_all`
        """
    )
    return 'Hello Flask app'

app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/dash/'
)

app.layout = html.Div("My Dash app")

if __name__ == '__main__':
    app.run_server(debug=True)  