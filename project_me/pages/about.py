from dash import html, dcc
import dash_mantine_components as dmc

layout = dmc.Container(
    [
        dcc.Link(
            dmc.Button("Home Page", variant="outline"),
            href='/',
        ),
        dcc.Link(
            dmc.Button("Map", variant="outline"),
            href='/subpage',
        ),
        dcc.Link(
            dmc.Button("About", variant="filled"),
            href='/about',
        ),
        # Nowy div z gridem
        html.Div([
            # Lewa kolumna z tekstem
            html.Div([
                dmc.Title("Dane i bieganie to przyszłość ", color="blue", size="h1",style={'margin':'0 0 10px'}),
                dmc.Text("Ten projekt, będący krzyżówką technik wizualizacji danych i pasji do biegania, celebruje połączenie świata liczb z energią ruchu. W nim każdy przebyty metr zamienia się w wizualną opowieść, a oddech biegacza rytmicznie splata się z pulsującymi danymi.",
                         align="left",style={'margin':'0 0 10px'}),
                dmc.Text("W tej innowacyjnej przestrzeni, dane i bieganie stanowią dwa filary ludzkiego dążenia - do poznania i aktywności. Tu, w harmonii cyfr i kroków, tworzymy nie tylko projekt, lecz narrację o życiu, odkryciach i nieustającym marszu naprzód.",
                         align="left")
            ], style={'width': '30%', 'display': 'inline-block','paddingRight':'30px'}),

            # Prawa kolumna z placeholderem na zdjęcie
            html.Div([
                # Tutaj można umieścić rzeczywisty obrazek, używając html.Img()
                # Poniżej znajduje się przykładowy placeholder.
                html.Div("Tu będzie zdjęcie", style={'width': '80%', 'height': '500px', 'backgroundColor': '#f0f0f0', 'textAlign': 'center', 'lineHeight': '200px','padding':'10px','margin':'0 auto'})
            ], style={'width': '50%', 'display': 'inline-block'})
        ], style={'width': '100%','height':'100%', 'display': 'flex','justifyContent': 'center','alignItems': 'center'})
        # ... można dodać inne komponenty
    ],
    fluid=True,
    style={'textAlign': 'left', 'width': '100%', 'maxWidth': '1200px', 
           'margin':'10px auto 50px','height':'100vh'}
)