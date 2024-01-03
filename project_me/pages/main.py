import dash_mantine_components as dmc
from dash import dcc, html
from layouts import create_dropdown

layout = dmc.Container(
    [
        # dmc.Title("Main Page", color="blue", size="h1"),
        # dmc.Text("This is the main page of the multi-page dashboard.", size="md"),
        dcc.Link(
            dmc.Button("Home Page", variant="filled", color="black"),
            href="/",
        ),
        dcc.Link(
            dmc.Button("Map", variant="outline"),
            href="/subpage",
        ),
        dcc.Link(
            dmc.Button("About", variant="outline"),
            href="/about",
        ),
        # create_dropdown()
        # ... include other components from the original app here
    ],
    fluid=True,
    style={
        "textAlign": "left",
        "width": "100%",
        "maxWidth": "1200px",
        "margin": "10px auto 50px",
    },
)
