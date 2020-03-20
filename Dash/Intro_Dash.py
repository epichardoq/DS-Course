#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 19:23:35 2020

@author: emmanuel
"""

# Importaciones iniciales
import dash
import dash_core_components as dcc
import dash_html_components as html

# Encabezado de la app
app = dash.Dash()

# Construcción en Flask parte 1 (texto sencillo)
#app.layout = html.Div('Tutoriales Dash en AprenderPython.com')

# Construcción en Flask parte 2 (inserta gráfico sin contenido)
#app.layout = html.Div(children=[
#  html.H1(children='Tutoriales Dash en AprenderPython.com'),
#  dcc.Graph()])

# Construcción en Flask parte 3 (inserta gráfico con contenido)
app.layout = html.Div(children=[
  html.H1(children='Tutoriales Dash en AprenderPython.com'),
  dcc.Graph(id='ejemplo',
    figure={
      'data': [
        {'x': [1, 2, 3, 4], 'y': [1, 8, 3, 7], 'type': 'line', 'name': 'Bicicletas'},
        {'x': [1, 2, 3, 4], 'y': [5, 2, 8, 8], 'type': 'bar', 'name': 'Bicicletas electricas'},
        ],
      'layout': {
      'title': 'Ejemplo básico en Dash'
        }
      })
  ])


# Carga en la web server
if __name__ == '__main__':
 app.run_server(debug=True)