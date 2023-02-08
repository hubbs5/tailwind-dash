from django_plotly_dash import DjangoDash
from .layout import layout
from .callbacks import register_callbacks

app = DjangoDash("Dashboard")
app.css.append_css({"external_url": "/static/css/output.css"})

app.layout = layout
register_callbacks(app)