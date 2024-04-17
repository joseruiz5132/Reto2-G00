"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import time
import csv
import tracemalloc
from datetime import datetime
from DISClib.ADT import list as lt

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {
        'model': None
    }
    control['model'] = model.new_data_structs()
    return control


# Funciones para la carga de datos

def load_data(control, filesize='10-por'):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    
    jobs = load_jobs(control, filesize)
    skills = load_skills(control, filesize)
    employment_types = load_employment_types(control, filesize)
    multilocations = load_multilocations(control, filesize)

    return jobs, skills, employment_types, multilocations



def load_jobs(control, filesize):
    """
    Carga los datos de los trabajos
    """
    jobs_dir = cf.data_dir+ filesize + "-jobs.csv"
    input_file = csv.DictReader(open(jobs_dir, encoding="utf-8"), delimiter=';')
    for job in input_file:
        job['published_at'] = datetime.strptime(job['published_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
        job['open_to_hire_ukrainians'] = str(job['open_to_hire_ukrainians']).lower()
        model.add_job(control['model'], job)  
    return lt.size(control['model']['jobs'])

def load_skills(control, filesize):
    """
    Carga los datos de las habilidades
    """
    skills_dir = cf.data_dir+ filesize + "-skills.csv"
    input_file = csv.DictReader(open(skills_dir, encoding="utf-8"), delimiter=';')
    for skill in input_file:
        skill['level'] = int(skill['level'])
        model.add_skill(control['model'], skill)

    return lt.size(control['model']['skills'])

def load_employment_types(control, filesize):
    """
    Carga los datos de los tipos de empleo
    """
    employment_types_dir = cf.data_dir+ filesize + "-employments_types.csv"
    input_file = csv.DictReader(open(employment_types_dir, encoding="utf-8"), delimiter=';')
    for employment_type in input_file:
        try:
            employment_type['salary_from'] = int(employment_type['salary_from'])
        except:
            employment_type['salary_from'] = 0
        
        try:
            employment_type['salary_to'] = int(employment_type['salary_to'])
        except:
            employment_type['salary_to'] = 0

        model.add_employment_type(control['model'], employment_type)

    return lt.size(control['model']['employment-types'])

def load_multilocations(control, filesize):
    """
    Carga los datos de las locaciones
    """
    multilocations_dir = cf.data_dir + filesize + "-multilocations.csv"
    input_file = csv.DictReader(open(multilocations_dir, encoding="utf-8"), delimiter=';')
    for multilocation in input_file:
        model.add_multilocation(control['model'], multilocation)
    
    return lt.size(control['model']['multilocations'])

# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo
def get_first_last(list):
    filtered = lt.newList("ARRAY_LIST")
    for i in range(1, 6):
        lt.addLast(filtered, lt.getElement(list, i))
    for i in range(-4, 1):
        lt.addLast(filtered, lt.getElement(list, i))
    return filtered


def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(control, company_name, initial_date, final_date):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    i_date = datetime.strptime(initial_date, '%Y-%m-%d')
    f_date = datetime.strptime(final_date, '%Y-%m-%d')
    total_offers, experience_offers, offers = model.req_3(control['model'], company_name, i_date, f_date)
    return total_offers, experience_offers, offers


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control, city_name, initial_date, final_date):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass
    i_date = datetime.strptime(initial_date, '%Y-%m-%d')
    f_date = datetime.strptime(final_date, '%Y-%m-%d')
    total_offers, total_companies, max_info, min_info, offers = model.req_5(control['model'], city_name, i_date, f_date)
    return total_offers, total_companies, max_info, min_info, offers

def req_6(control, n_cities, experience_level, year):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    answer_list = model.req_6(control['model'], n_cities, experience_level, year)
    return answer_list


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
