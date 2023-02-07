import dash
import pandas as pd
import plotly.express as px
from dash import dcc, html

external_scripts = [
    "https://tailwindcss.com/",
    {"src": "https://cdn.tailwindcss.com"}
]

app = dash.Dash(__name__, external_scripts=external_scripts)
app.scripts.config.serve_locally = True

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas"] * 2,
    "Amount": [4, 1, 2, 3, 2, 5],
    "Airport": ["ZRH", "IAH", "ORD", "SFO", "BNA", "SEA"]
    })

count = df.Fruit.count()
amt = df.Amount.sum()
airports = df.Airport.count()
variables = df.shape[1]

fig = px.bar(
    df,
    x="Fruit", 
    y="Amount",
    color="Airport"
)

fig1 = px.box(
    df,
    x="Airport",
    y="Amount",
    color="Airport"
)

app.layout = html.Div(
    className="bg-[#ebeaee] container mx-auto px-14 py-4",
    children=[
        html.Div(
            className="flex max-w-full justify-between items-center",
            children=[
                html.Div(
                    className="w-full mx-14 px-16 shadow-lg bg-white -mt-14 px-6 container my-3",
                    children=[
                        html.H1(
                            children="Dash + Tailwind",
                            className="py-3 text-5xl font-bold text-gray-800"
                            ),
                        html.Div(
                            children="",
                            className="text-left prose prose-lg text-2xl py-3 text-gray-600",
                        ),
                    ],
                ),
                html.Div(
                    html.Div(
                        className="my-4 w-full grid grid-flow-rows grid-cols-1 lg:grid-cols-4 gap-y-r lg:gap-[60px]",
                        children=[
                            html.Div(
                                className="shadow-xl py-4 px-14 text-5xl bg-[$76c893] text-white font-bold text-gray-800",
                                children=[
                                    f"${amt}",
                                    html.Br(),
                                    html.Span(
                                        "Total Sales",
                                        className="text-lg font-bold ml-4"
                                            )
                                ]
                            ),
                            html.Div(
                                className="shadow-xl py-4 px-14 text-5xl bg-[$76c893] text-white font-bold text-gray-800",
                                children=[
                                    count,
                                    html.Br(),
                                    html.Span(
                                        "Fruit Count",
                                        className="text-lg font-bold ml-4"
                                    )
                                ]
                            ),
                            html.Div(
                                className="shadow-xl py-4 px-14 text-5xl bg-[$76c893] text-white font-bold text-gray-800",
                                children=[
                                    airports,
                                    html.Br(),
                                    html.Span(
                                        "Airport Count",
                                        className="text-lg font-bold ml-4"
                                    )
                                ]
                            )
                        ]
                    )
                )
            ]
        ),
        html.Div(
            className="shadow-xl w-full border-3 rounded-sm",
            children=[
                dcc.Graph(
                    id="example-graph",
                    figure=fig
                    )
            ]
        ),
        html.Div(
            className="w-full shadow-2xl rounded-sm",
            children=[
                dcc.Graph(
                    id="example-graph1",
                    figure=fig1
                )
            ]
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)