# Import packages
import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, callback, dash_table, dcc

# Incorporate data
df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"  # noqa:E501
)  # Initialize the app - incorporate a Dash Mantine theme
external_stylesheets = [dmc.theme.DEFAULT_COLORS]
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
app.layout = dmc.Container(
    [
        dmc.Title(
            "My First App with Data, Graph, and Controls",
            color="blue",
            size="h3",  # noqa:E501
        ),
        dmc.RadioGroup(
            [dmc.Radio(i, value=i) for i in ["pop", "lifeExp", "gdpPercap"]],
            id="my-dmc-radio-item",
            value="lifeExp",
            size="sm",
        ),
        dmc.Grid(
            [
                dmc.Col(
                    [
                        dash_table.DataTable(
                            data=df.to_dict("records"),
                            page_size=12,
                            style_table={"overflowX": "auto"},
                        )
                    ],
                    span=6,
                ),
                dmc.Col(
                    [dcc.Graph(figure={}, id="graph-placeholder")], span=6
                ),  # noqa:E501
            ]
        ),
    ],
    fluid=True,
)


# Add controls to build the interaction
@callback(
    Output(component_id="graph-placeholder", component_property="figure"),
    Input(component_id="my-dmc-radio-item", component_property="value"),
)
def update_graph(col_chosen):
    fig = px.histogram(df, x="continent", y=col_chosen, histfunc="avg")
    return fig


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
