import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import pages.components
from dash import html

layout = dbc.Container(
    [
        pages.components.top_layout,
        # Nowy div z gridem
        dbc.Row(
            [
                # Lewa kolumna z tekstem
                dbc.Col(
                    [
                        dmc.Title(
                            "Dane i bieganie to przyszłość ",
                            color="blue",
                            size="h1",
                            style={"margin": "0 0 10px"},
                        ),
                        dmc.Text(
                            "Ten projekt, będący krzyżówką technik wizualizacji danych i pasji do biegania, celebruje połączenie świata liczb z energią ruchu. W nim każdy przebyty metr zamienia się w wizualną opowieść, a oddech biegacza rytmicznie splata się z pulsującymi danymi.",  # noqa: E501
                            align="left",
                            style={"margin": "0 0 10px"},
                        ),
                        dmc.Text(
                            "W tej innowacyjnej przestrzeni, dane i bieganie stanowią dwa filary ludzkiego dążenia - do poznania i aktywności. Tu, w harmonii cyfr i kroków, tworzymy nie tylko projekt, lecz narrację o życiu, odkryciach i nieustającym marszu naprzód.",  # noqa: E501
                            align="left",
                        ),
                    ],
                    width=3,
                ),
                # Prawa kolumna z placeholderem na zdjęcie
                dbc.Col(
                    [
                        html.Div(
                            "Tu będzie zdjęcie",
                            style={
                                "width": "80%",
                                "height": "500px",
                                "backgroundColor": "#f0f0f0",
                                "textAlign": "center",
                                "lineHeight": "200px",
                                "padding": "10px",
                                "margin": "0 auto",
                            },
                        )
                    ],
                    width=6,
                ),
            ],
            style={
                "width": "100%",
                "height": "100%",
                "display": "flex",
                "justifyContent": "center",
                "alignItems": "center",
            },
        ),
        # ... można dodać inne komponenty
    ],
    fluid=True,
    style={
        "textAlign": "left",
        "width": "100%",
        "maxWidth": "1200px",
        "margin": "10px auto 50px",
        "height": "100vh",
    },
)
