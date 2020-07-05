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




#<------------------Interactive Graph callbacks------------->

df = pd.read_csv('data\gapminderDataFiveYear.csv')


year_options = []
for year in df['year'].unique():
    year_options.append({'label':str(year),'value':year})



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

                        id='year-picker',
                        options=year_options,
                        value=df['year'].min(),
                        #multi=True
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
                                #Graph preview
                                html.Div([
                                    dcc.Graph(id='graph')
                                ])
                                ],
                                
                                    
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


#decorators for text box in bottom right panel ui and input box in left panel  interactions
@app.callback(Output(component_id='text_div', component_property='children'),
                                [Input(component_id='input_text',component_property='value')])


#single call back
def upadate_plane(input_value):
    return "You Entered :{}".format(input_value)

#decorator for graph call back from left panel dropdown to  right -top panel 
@app.callback(Output('graph','figure'),
                    [Input('year-picker','value')])
#update graph function
def update_figure(selected_year):

    #data only for selected year from dropdown
    filtered_df = df[df['year'] == selected_year]
    
    traces = []
    
    for continent_name in filtered_df['continent'].unique():
        df_by_continent = filtered_df[filtered_df['continent'] == continent_name]
        traces.append(go.Scatter(
            x=df_by_continent['gdpPercap'],
            y=df_by_continent['lifeExp'],
            mode='markers',
            opacity=0.7,
            marker={'size': 15},
            name=continent_name
        ))

    return {'data': traces,
            'layout': go.Layout(title='My Plot',
                                xaxis={'title': 'GDP per Cap', 'type': 'log'},
                                yaxis={'title': 'Life Expectancy'})}





if __name__ == '__main__':
    app.run_server(debug=True)