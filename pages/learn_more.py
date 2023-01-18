import dash
from dash import html, dcc

dash.register_page(__name__)

layout = html.Div(children=[
    html.H1('Learn more on:'),

    html.A('Dash Doc', href='https://dash.plotly.com', className='links'),

    html.H1('Great site to search for colors:'),

    html.A('Color hunt', href='https://colorhunt.co', className='links'),

    html.H1('CSS Ideas:'),

    html.A('CSS Tricks', href='https://css-tricks.com', className='links'),
])