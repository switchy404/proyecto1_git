import dash
from dash import dcc  
from dash import html 
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv("SeoulBikeData_utf8.csv")
dft = df.groupby("Temperature(C)")["Rented Bike Count"].mean()
figt = px.scatter(dft, y = "Rented Bike Count", title = "Promedio de bicicletas por hora según temperatura", color_discrete_sequence=["Red"])
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([
    html.H4("Análisis de Bicicletas de Seúl"),
    
    html.Div([dcc.Graph(id ="scattergraph", figure = figt, style={'width': '100%'})]),
    html.P("Seleccione filtros para el Diagrama de Caja:"),
    dcc.Checklist(
        id='x-axis-box', 
        options=[
            {'label': 'Estaciones', 'value': 'Seasons'}, 
            {'label': 'Festivo', 'value': 'Holiday'}
        ],
        value=['Seasons'],  
        inline=True
    ),
    
    
    html.P("Seleccione filtros para el Gráfico de Barras por Hora:"),
    dcc.Dropdown(
        id='x-axis-bar', 
        options=["Estaciones","Festivo", "Ninguno" ],
        value=['Estaciones'] 
        
    ),
   
    html.Div([dcc.Graph(id="boxgraph", style={'width': '48%', 'display': 'inline-block'}),
    dcc.Graph(id="bargraph", style={'width': '48%', 'display': 'inline-block'})],
    style={'display': 'flex', 'justify-content': 'space-between'}  ),

    html.Div([
    html.H6("Introduzca los siguientes parámetros para estimar la demanda esperada:"),
    html.Div(["Temperatura (C) (use . como separación decimal): ",
              dcc.Input(id='temp-input', value=20, type='text')]),
    html.Div([" Elija una estación: ", 
                 dcc.Dropdown(
                     id = 'modelseason-input',
                     options = ["Invierno", "Primavera", "Verano", "Otoño"], 
                     value = ["Verano"])]),
    html.Div(["Elija si es festivo: ",
                dcc.Dropdown(
                    id = "holiday-input",
                    options = ["Festivo", "No Festivo"],
                    value = ["No Festivo"])]),
    html.Div([" Escriba la hora de interés (de 0 a 24, solo enteros): ",
                 dcc.Input(id='hour-input', value=15, type='text')]
            )       
            ]),                
    html.Br(),
    html.Div(id='model-output')
    ])

@app.callback(
    [Output("boxgraph", "figure"), 
     Output("bargraph", "figure")], 
    [Input("x-axis-box", "value"),
     Input("x-axis-bar", "value")
     
     ])
def update_graphs(box_x, bar_x):
    if box_x:
        if len(box_x) == 1:
            box_fig = px.box(df, x=box_x, y= "Rented Bike Count", title="Diagrama de caja de bicicletas alquiladas por hora")
        elif len(box_x) == 2:
            box_fig = px.box(df, x=box_x, y= "Rented Bike Count", color = box_x[1],  title="Diagrama de caja de bicicletas alquiladas por hora")
        else:
            box_fig = px.box(df, y="Rented Bike Count",  title="Diagrama de caja de bicicletas alquiladas por hora")
    if bar_x:
        if bar_x != "Ninguno":  
            bar_fig = px.bar(df.groupby(['Hour', bar_x])['Rented Bike Count'].mean().reset_index(),
                         x='Hour', y='Rented Bike Count', color=bar_x,
                         title=f"Promedio de bicicletas alquiladas por hora y {bar_x}", barmode = "group")

        else:
            bar_fig = px.bar(df.groupby('Hour')['Rented Bike Count'].mean().reset_index(),x = 'Hour' ,
                          y='Rented Bike Count', title="Promedio de bicicletas alquiladas por hora", barmode = "group")
    else:
            bar_fig = px.bar(df.groupby('Hour')['Rented Bike Count'].mean().reset_index(),x = 'Hour' ,
                          y='Rented Bike Count', title="Promedio de bicicletas alquiladas por hora", barmode = "group")
    return box_fig, bar_fig

@app.callback(
    [Output("model-output", 'children')], 
    [Input("temp-input", "value"),
     Input("modelseason-input", "value"),
     Input("holiday-input", "value"),
     Input("hour-input", "value")
     ])
def modelohecho(temp,seas,holi,hour):
    if seas == "Invierno":
        valorseason = 3
    elif seas == "Primavera":
        valorseason = 2
    elif seas == "Verano":
        valorseason = 1
    else:
        valorseason = 0
    
    if holi == "Festivo":
        valorholi = 1
    else:
        valorholi = 0
    
    estimado = 125.2485 + 22.9249*float(temp) + -62.4998*valorseason + -132.4332*valorholi + 33.3688*int(hour)
    estimado_rounded = round(estimado, 0)
    respuesta = ("Para esta ocasión, se espera la siguiente demanda de bicicletas: {} ".format(estimado_rounded))
    return [respuesta]

app.run_server(debug=True)