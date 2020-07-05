import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd





external_stylesheets = [
    'assets\styles.css',
]

app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets)

markdown_text='''
In linear regression, the relationships are modeled using linear predictor functions whose unknown model parameters are estimated from the data. Such models are called linear models.[3] Most commonly, the conditional mean of the response given the values of the explanatory variables (or predictors) is assumed to be an affine function of those values; less commonly, the conditional median or some other quantile is used. Like all forms of regression analysis,
'''  
app.layout = html.Div([

    
    
    #left panel
    html.Div(
                className="left_menu",
                children=[
                    html.Div(
                        'This is the left menu'
                    ),

                    #Dropdown Multi
                    dcc.Dropdown(
                        
                        options=[
                            {'label': 'New York City', 'value': 'NYC'},
                            {'label': 'Montréal', 'value': 'MTL'},
                            {'label': 'San Francisco', 'value': 'SF'}
                                ],
                        value='MTL',
                        multi=True
                            ),
    
                    html.Div(className="Text",children=[
                                dcc.Markdown(children=markdown_text)
                            ]),

                    #Input box
                    dcc.Input(
                            id="input_text",
                            type='text',
                            style={'padding':10}
                        ),
                ]
            ),
    #Right Panel
        html.Div(
                className="right_content",
                children=[
                     #Top-right panel
                            html.Div(
                                className="top_metrics",
                                children=[
                                'This is top metrics',

                                #Slider
                                html.Label("Slider"),
                                        dcc.Slider(
                                        min=0,
                                        max=9,
                                        marks={i: 'Label {}'.format(i) for i in range(10)},
                                        value=5,
                                        ),
                                ],
                                #Graph preview
                                    
                            ),
                    #Bottom-right panel
                            html.Div(
                                id='text_div',
                                className="down_bottom",
                                children=[
                                        'This down top metrics'
                                ]
                                
                            ),
                        ]
            ),
])


#decorators for ui and input interactions
@app.callback(Output(component_id='text_div', component_property='children'),
                                [Input(component_id='input_text',component_property='value')])


#single call back
def upadate_plane(input_value):
    return "You Entered :{}".format(input_value)

#<------------------Interactive Graph callbacks------------->

df = pd.read_csv('data\gapminderDataFiveYear.csv')








if __name__ == '__main__':
    app.run_server(debug=True)