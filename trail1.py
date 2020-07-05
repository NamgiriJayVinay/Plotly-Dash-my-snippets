import dash
import dash_html_components as html
import dash_core_components as dcc

app=dash.Dash()

app.layout = html.Div([
                        'outer',
                         html.Div(
                                    'inner-1',
                                     style={'borderRadius': 5, 'width': 220, 'height': 180, 'color': 'blue', 'padding':10, 'border': '2px blue solid'}
                                ),#gets inner 1 and 2 below
                                html.Div(
                                        'innne-2',
                                         style={'width':220,'height':150,'color':'green','border':'2px green solid'}
                                        ),
                       ],style={'width':1000,'height':500,'color':'red','border':'2px red solid'})


app.layout = html.Div([
                        'outer',
                         html.Div(
                                    'inner-1',
                                     style={'borderRadius': 5, 'width': 220, 'height': 180, 'color': 'blue', 'padding':10, 'border': '2px blue solid'}
                                ),#gets inner 1 and 2 below
                                html.Div(
                                        'innne-2',
                                         style={'width':220,'height':150,'color':'green','border':'2px green solid'}
                                        ),
                       ],style={'width':1000,'height':500,'color':'red','border':'2px red solid'})

if __name__=='__main__':
    app.run_server()