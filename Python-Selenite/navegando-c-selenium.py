#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 17:48:35 2020

@author: emmanuel
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(executable_path=r'/usr/local/bin/geckodriver')

#Interacción con la página
#driver.get("http://www.google.com")
#element = driver.find_element_by_id("passwd-id")
#element = driver.find_element_by_name("passwd")
#element = driver.find_element_by_xpath("//input[@id=' passwd-id']")

    #Campo de texto
#element.send_keys("algún texto")
    #Clase Keys
#element.send_keys("y algunos", Keys.ARROW_DOWN)

    #Borrar fácilmente el contenido de un campo o área de texto con el método claro
#elemento.clear()




#Llenado de formularios

#element = driver.find_element_by_xpath("//select[@name=' name']")
#all_options = elemento.find_elements_by_tag_name("option")
#for option in all_options:
#  print("Valor es: %s" opción %. get_attribute ("value")
#  opción.click()
  
    #elementos SELECT
#select = Select(driver.find_element_by_name('name'))
#select.select_by_index(index)
#select.select_by_visible_text("text")
#select.select_by_value(value)

    #Deseleccionar todas las opciones seleccionadas
#select = Select(driver.find_element_by_id('id'))
#select.deselect_all()

    #Método de propiedad que devuelve una lista
#select = Select(driver.find_element_by_xpath("xpath"))
#all_selected_options = select.all_selected_options
    #Obtener todas las opciones disponibles
#options = select.options
   
    #Envío del formulario
# Assume the button has the ID "submit" :)
#driver.find_element_by_id("submit").click()

    #Envío elemento x elemento
#elemento.submit()




#Arrastrar y soltar (drop & drag)

    #Drag & Drop elementos
#element = driver.find_element_by_name("source")
#target = driver.find_element_by_name("target")

#from selenium.webdriver import ActionChains
#action_chains = ActionChains(driver)
#action_chains.drag_and_drop(element, target).perform()




# Desplazamiento entre ventanas y Frames

    #“switch_to_window”
#driver.switch_to_window ("windowName")

    #Iterar en cada ventana abierta
#for handle in driver.window_handles:
#  driver.switch_to_window(handle)

    #Oscilar de cuadro a cuadro (o hacia iframes)
#driver.switch_to_frame ("frameName")

    #Acceder a los subtramas separando la ruta
#driver.switch_to_frame ("frameName. 0. child")

    #Regresar al frame inicial
#driver.switch_to_default_content()




#Diálogos emergentes

#alert = driver.switch_to_alert ()



#Navegación: historial y localización

#driver.get("http://www.example.com")

    #Avanzar en historial
#driver.forward ()
    #Regresar en historial
#driver.back ()




#Galletas / Cookies

# Go to the correct domain
#driver.get("http://www.example.com")

# Now set the cookie. This one's valid for the entire domain
#cookie = {‘name’ : ‘foo’, ‘value’ : ‘bar’}
#driver.add_cookie(cookie)

# And now output all the available cookies for the current URL
#driver.get_cookies()