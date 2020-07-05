import dash
import dash_html_components as html
import dash_core_components as dcc

external_stylesheets = [
    'assets\styles.css',
]

app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets)




markdown_text='''
*This text will be italic*

_This will also be italic_


**This text will be bold**

__This will also be bold__

_You **can** combine them_
'''  
app.layout = html.Div(
            className="content",
            children=[

            html.Div(
                className="left_menu",
                children=[
                    html.Div(
                        'This is the left menu'
                    ),
                ]
            ),

            html.Div(
                className="right_content",
                children=[
                    html.Div(
                        className="top_metrics",
                        children=[
                        'This is top metrics'
                        ]
                    ),
                    html.Div(
                        'This down top metrics'
                    ),
                ]
            ),

            html.Div([
                dcc.Markdown(children=markdown_text)
            ])
        ]
)

if __name__ == '__main__':
    app.run_server(debug=True)