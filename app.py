import dash
import dash_core_components as dcc
import dash_html_components as html

app=dash.Dash()
server=app.server

app.layout = html.Div(children =[
    html.H1('Hellow Dash')
    ])
if __name__=='main':
    app.run_server()