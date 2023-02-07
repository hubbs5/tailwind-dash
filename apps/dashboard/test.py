from dash import Dash
from layout import layout
from callbacks import register_callbacks

if __name__ == "__main__":
    ext_scripts = [
        "https://tailwindcss.com/",
        {"src": "https://cdn.tailwindcss.com"}
    ]
    app = Dash(__name__, external_scripts=ext_scripts)
    app.layout = layout
    register_callbacks(app)
    app.run_server(debug=True)