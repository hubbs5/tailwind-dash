from django_plotly_dash import DjangoDash
from .layout import layout
from .callbacks import register_callbacks

app = DjangoDash("Dashboard")

app.layout = layout
register_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True)