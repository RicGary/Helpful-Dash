from dash import Dash, html, dcc
import dash


# Default setting: Dash(__name__) ---> Dash(___, use_pages=True) only if working with more pages.
app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True)


# app.layout because here goes the main "something" on your page.
app.layout = html.Div([

    html.Div(id='home-container', children=[
        html.H1('Multi-page app with Dash Pages'),

            html.Div(
                id='links-container',
                children=[
                    html.Div(
                        dcc.Link(
                            f"{page['name']} - {page['path']}", href=page["relative_path"]
                        )
                    )
                    for page in dash.page_registry.values()
                ]
            )
    ]),

	dash.page_container
])


# Great practice to run the server.
if __name__ == '__main__':
    # The default port 8050, if you want to change just do ---> app.run_server(___, port=xxxx).
    # You can disable debug once you'r finished.
	app.run_server(debug=True)