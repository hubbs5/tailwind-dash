from dash import dcc, html
from dash.dependencies import Input, Output
import yfinance as yf
import plotly.express as px

def register_callbacks(app):
    
    @app.callback(
        Output("price-chart", "children"),
        Input("symbol-input", "value"),
    )
    def get_data(symbol):
        df = yf.Ticker(symbol).history()
        fig = px.line(
            x=df.index,
            y=df.Close,
            title=f"Price for {symbol}",
            labels={
                "x": "Date",
                "y": "Price ($)",
            }
            )
        return dcc.Graph(
            id="price-chart-1",
            figure=fig
            )