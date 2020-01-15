import flask
import dash
import dash_html_components as html

server = flask.Flask(__name__)

app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/'
)

app.layout = html.Div("My Dash app")

if __name__ == '__main__':
    app.run_server(port=8080)
