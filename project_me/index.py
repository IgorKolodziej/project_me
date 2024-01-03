from dash import dcc, html
from dash.dependencies import Input, Output
from app import app
from pages import main
from pages import subpage
from pages import about

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return main.layout
    elif pathname == '/subpage':
        return subpage.layout
    elif pathname == '/about':
        return about.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
