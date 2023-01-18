import dash
from dash import html, dcc, Output, Input, callback


dash.register_page(__name__)


layout = html.Div(className='content', children=[
    html.Img(id='cara-do-meme', src='assets\images\cara_do_meme.jpg', className='img-outside'),

    html.H1('Who is this guy?'),

    dcc.Dropdown(
    [
        {
            "label": html.Span(
                [
                    html.Img(src="assets\images\gandara.jpg", height=20),
                    html.Span("Gandara", style={'font-size': 15, 'padding-left': 10}),
                ], style={'align-items': 'center', 'justify-content': 'center'}
            ),
            "value": "Gandara",
        },


        {
            "label": html.Span(
                [
                    html.Img(src="assets\images\Hammer_and_sickle.svg.png", height=20),
                    html.Span("Communist", style={'font-size': 15, 'padding-left': 10}),
                ], style={'align-items': 'center', 'justify-content': 'center'}
            ),
            "value": "Communist",
        },


        {
            "label": html.Span(
                [
                    html.Img(src=r"assets\images\novo.png", height=20),
                    html.Span("Cara do partido novo", style={'font-size': 15, 'padding-left': 10}),
                ], style={'align-items': 'center', 'justify-content': 'center'}
            ),
            "value": "Novo",
        },
    ], id='droptest', className='dropdowns'),


    # Easier to-do
    dcc.Dropdown(
        id='droptest', className='dropdowns', 
        options=['Gandara', 'Communist', 'Cara do partido novo'],
        placeholder='Who who who?'
    )
])