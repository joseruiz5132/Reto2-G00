"""
  * Copyright 2020, Departamento de sistemas y Computación, Universidad
  * de Los Andes
  *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def new_controller():
    """
         Se crea una instancia del controlador
     """
     #TODO: Llamar la función del controlador donde se crean las estructuras de datos
     control = controller.new_controller()
     return control


 def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")
def load_data(control):
    """
     Carga los datos
     """
     #TODO: Realizar la carga de datos

     jobs, skills, employment_types, multilocations = controller.load_data(control)

     jobs_table = print_tabulate(control['model']['jobs'], ['published_at', 'title', 'company_name', 'experience_level', 'country_code', 'city'])
     print(jobs_table)



     pass


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
     #TODO: Realizar la función para imprimir un elemento
     pass

 def print_tabulate(data_struct, columns):
     data = data_struct

     if lt.isEmpty(data):
         return 'No hay datos'

     #Filtrar solo ultimos y primeros 3 datos si es muy grande la lista
     if lt.size(data_struct) > 10:
         data = controller.get_first_last(data_struct)
         print(f'Se encontraron {lt.size(data_struct)}  resultados. Imprimiendo primeros y ultimos 5...')

     #Lista vacía para crear la tabla
     reduced = []

     #Iterar cada línea de la lista
     for result in lt.iterator(data):
         line = []
         #Iterar las columnas para solo imprimir las deseadas
         for column in columns:
             line.append(result[column])
         reduced.append(line)
     table = tabulate(reduced, headers=columns, tablefmt="grid", maxcolwidths=30)
     return table


 def print_req_1(control):
     """
         Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass
def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass
def print_req_3(control):
    """
         Función que imprime la solución del Requerimiento 3 en consola
     """
     # TODO: Imprimir el resultado del requerimiento 3
     company_name = input('Ingrese el nombre de la empresa: ')
     initial_date = input('Ingrese la fecha inicial (YYYY-MM-DD): ')
     final_date = input('Ingrese la fecha final (YYYY-MM-DD): ')
     total_offers, experience_offers, offers = controller.req_3(control, company_name, initial_date, final_date)
     answer_table = print_tabulate(offers, ['published_at', 'title', 'experience_level', 'city', 'country_code', 'company_size', 'workplace_type', 'open_to_hire_ukrainians'])
     print(answer_table)
     pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass
def print_req_5(control):
    """
         Función que imprime la solución del Requerimiento 5 en consola
     """
     # TODO: Imprimir el resultado del requerimiento 5
     city_name = input('Ingrese el nombre de la ciudad: ')
     initial_date = input('Ingrese la fecha inicial (YYYY-MM-DD): ')
     final_date = input('Ingrese la fecha final (YYYY-MM-DD): ')
     total_offers, total_companies, max_info, min_info, offers = controller.req_5(control, city_name, initial_date, final_date)
     answer_table = print_tabulate(offers, ['published_at', 'title', 'company_name', 'workplace_type', 'company_size'])
     print(answer_table)
     pass


def print_req_6(control):
    """
         Función que imprime la solución del Requerimiento 6 en consola
     """
     # TODO: Imprimir el resultado del requerimiento 6
     n_cities = int(input('Ingrese el número de ciudades a buscar: '))
     experience_level = input('Ingrese el nivel de experiencia: ')
     year = int(input('Ingrese el año: '))
     answer_list = controller.req_6(control, n_cities, experience_level, year)
     table_answer = print_tabulate(answer_list, ['name', 'country', 'total_offers', 'average_salary', 'total_enterprises', 'best_enterprise', 'best_offer', 'best_offer', 'worst_offer'])
     print(table_answer)
     pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass
def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass
# Se crea el controlador asociado a la vista
control = new_controller()
