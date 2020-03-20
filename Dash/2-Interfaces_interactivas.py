#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 19:57:43 2020

@author: emmanuel
"""

# Importaciones iniciales
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

# Definiendo un campo de entrada y luego un campo de salida
app = dash.Dash()

app.layout = html.Div([
  dcc.Input(id='input', value='Escribe algo aqui!', type='text'),
  html.Div(id='output')
])

# Que corresponden las entradas y salidas
@app.callback(
  Output(component_id='output', component_property='children'),
  [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
  return 'Input: "{}"'.format(input_data)

# Carga en la web server
if __name__ == '__main__':
 app.run_server(debug=True)