import dash
import dash_mantine_components as dmc

external_stylesheets = [dmc.theme.DEFAULT_COLORS]
app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets,
)
server = app.server
