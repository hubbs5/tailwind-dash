from dash import dcc, html

layout = html.Div(
    className="bg-green-100 container mx-auto my-auto px-15 py-5",
    children=[
        html.Div(
            className="bg-red-100 py-5",
            children=[
                dcc.Dropdown(
                    id="symbol-input",
                    options=[
                        {"label": "Apple", "value": "AAPL"},
                        {"label": "Tesla", "value": "TSLA"},
                        {"label": "Meta", "value": "META"},
                        {"label": "Amazon", "value": "AMZN"}
                    ],
                    searchable=True,
                    value="AAPL",
                )
            ]),
        html.Div(
            className="max-w-full shadow-2xl rounded-lg border-3",
            id="price-chart"
        )
    ]
)