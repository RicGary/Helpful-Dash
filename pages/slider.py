import dash
from dash import html, dcc, Output, Input, callback


dash.register_page(__name__)


@callback(
    Output('output-vic', 'children'),
    Input('vic-slider', 'value')
)
def metal_love(value):
    if value == 10:
        return html.Img(src='assets\images\metaljpg.jpg', className='img-outside')

    else:
        return html.H2('Wrong')

layout = html.Div(className='content', children=[
    html.H1('How much does Vic loves Metal?'),

    dcc.Slider(
        className='sliders',
        id='vic-slider',
        min=0,
        max=10,
        step=0.1,
        value=5,
        updatemode='drag',

        # Here you can be creative
        tooltip={
            "placement": "bottom", 
            "always_visible": False
            },
        
        # Or just use None
        marks={
            0: {'label': '0', 'style': {'color': 'red'}},
            5: {'label': '5', 'style': {'color': 'blue'}},
            10: {'label': '10', 'style': {'color': 'green'}}
        },
    ),

    html.Div(id='output-vic')   
])