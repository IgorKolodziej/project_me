import dash_leaflet as dl
import dash_mantine_components as dmc
import gpxpy
from app import app
from dash import dcc, html
from dash.dependencies import Input, Output


def parse_gpx(file_path):
    with open(file_path, "r") as gpx_file:
        gpx = gpxpy.parse(gpx_file)
        track = gpx.tracks[0]
        segment = track.segments[0]
        # Extracting coordinates and times
        coords = [(point.latitude, point.longitude) for point in segment.points]
        times = [point.time for point in segment.points]
    return coords, times


route1_coords, route1_times = parse_gpx("data/routes/test1.gpx")
route2_coords, route2_times = parse_gpx("data/routes/test2.gpx")
route3_coords, route3_times = parse_gpx("data/routes/test3.gpx")

routes = {
    "route1": {"coords": route1_coords, "times": route1_times},
    "route2": {"coords": route2_coords, "times": route2_times},
    "route3": {"coords": route3_coords, "times": route3_times},
}


# layout = dmc.Container(
#     [
#         dmc.Title("Map", color="blue", size="h1"),
#       #  dmc.Text("This is a subpage. Navigate back to the main page or interact with the elements below.", size="md"),
#         dcc.Link(
#             dmc.Button("Home Page", variant="outline"),
#             href='/',
#         ),
#         dcc.Link(
#             dmc.Button("Map", variant="outline"),
#             href='/subpage',
#         ),
#         # ... include specific components for the subpage here
#     ],
#     fluid=True,
# )


# Define a function to format times for the slider marks
def format_times(times):
    marks = {}
    for i, time in enumerate(times):
        if i % (len(times) // 5) == 0:  # Check if divisible by 60
            marks[i] = {"label": time.strftime("%H:%M:%S")}

    return marks


layout = html.Div(
    [
        dmc.Container(
            [
                # dmc.Title("Main Page", color="blue", size="h1"),
                # dmc.Text("This is the main page of the multi-page dashboard.", size="md"),
                dcc.Link(
                    dmc.Button("Home Page", variant="outline"),
                    href="/",
                ),
                dcc.Link(
                    dmc.Button("Map", variant="filled"),
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
        ),
        html.Div(
            [
                # Left Column for Map and Slider
                html.Div(
                    [
                        dl.Map(
                            [
                                dl.TileLayer(),
                                dl.Polyline(id="route", positions=route1_coords),
                            ],
                            id="map",
                            style={
                                "width": "100%",
                                "height": "500px",
                            },
                            center=(route1_coords[0][0], route1_coords[0][1]),
                            zoom=14,
                        ),
                    ],
                    className="left-column",
                    style={"padding-right": "20px"},
                ),
                # Right Column for RadioItems and Labels
                html.Div(
                    [
                        html.Div(
                            [
                                dmc.Text(
                                    "Każdy z nas wybrał się na indywidualny bieg w okolicach Woli, by w sportowym duchu porównać czasy i trasy naszych przebieżek.",  # noqa: E501
                                    color="black",
                                    size="h3",
                                    align="left",
                                ),
                                dmc.Text(
                                    "Mateusz, Igor oraz Nazari, wyposażeni w smartfony, wyruszyli w różne strony, eksplorując malownicze ścieżki i ulice dzielnicy.",  # noqa: E501
                                    color="black",
                                    size="h3",
                                    align="left",
                                    style={"marginTop": "20px"},
                                ),
                            ]
                        ),
                        dmc.RadioGroup(
                            id="route-selector",
                            value="route1",
                            orientation="vertical",
                            withAsterisk=True,
                            # label="Select a Route",
                            # description="Choose a route to display on the map.",
                            size="md",
                            style={"marginBottom": "40px"},
                            children=[
                                dmc.Radio(label="Mateusz", value="route1"),
                                dmc.Radio(label="Igor", value="route2"),
                                dmc.Radio(label="Nazari", value="route3"),
                            ],
                        ),
                        # Label for displaying current time and speed
                        html.Div(id="time-speed-label", style={"fontSize": 20}),
                        dcc.Slider(
                            id="time-slider",
                            min=0,
                            max=len(route1_times) - 1,
                            value=0,
                            step=1,
                            updatemode="drag",
                            # marks=None
                            marks=format_times(
                                route1_times
                            ),  # Use the updated function
                        ),
                    ],
                    className="right-column",
                    style={
                        "display": "grid",
                        "gridTemplateRows": "1fr 1fr",
                        "gap": "10px",
                    },
                ),
            ],
            style={
                "display": "grid",
                "gridTemplateColumns": "1fr 1fr",
                "gap": "20px",
                "alignItems": "center",
                "justifyContent": "center",
                "alignContent": "center",
                "height": "100%",
                "width": "80%",
                "margin": "0 auto",
            },
        ),
    ],
    style={"textAlign": "center", "width": "100%", "margin": "0 auto"},
)


@app.callback(Output("route", "positions"), [Input("route-selector", "value")])
def update_route(selected_route):
    return routes[selected_route]["coords"]


@app.callback(
    [Output("time-slider", "max"), Output("time-slider", "marks")],
    [Input("route-selector", "value")],
)
def update_slider(selected_route):
    max_val = len(routes[selected_route]["times"]) - 1
    marks = format_times(routes[selected_route]["times"])
    return max_val, marks


@app.callback(
    Output("map", "children"),
    [Input("time-slider", "value"), Input("route-selector", "value")],
)
def update_marker(slider_value, selected_route):
    route_coords = routes[selected_route]["coords"]
    return [
        dl.TileLayer(),
        dl.Polyline(positions=route_coords),
        dl.Marker(position=route_coords[slider_value], id="marker"),
    ]
