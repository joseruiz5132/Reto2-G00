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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    data_structs = {
        'jobs': None,
        'skills': None,
        'employment-types': None,
        'multilocations': None,
        'year_experience': None,
        'map_jobs': None,
        'map_skills': None,
        'map_employment-types': None,
        'map_multilocations': None,
        'map_companies': None,
        'map_cities': None
    }

    data_structs['jobs'] = lt.newList('ARRAY_LIST', compare_map_name)
    data_structs['skills'] = lt.newList('ARRAY_LIST', compare_map_name)
    data_structs['employment-types'] = lt.newList('ARRAY_LIST', compare_map_name)
    data_structs['multilocations'] = lt.newList('ARRAY_LIST', compare_map_name)
    data_structs['map_jobs'] = mp.newMap(100, maptype='PROBING', cmpfunction=compare_map_name)
    data_structs['map_skills'] = mp.newMap(100, maptype='PROBING', cmpfunction=compare_map_name)
    data_structs['map_employment-types'] = mp.newMap(100, maptype='PROBING', cmpfunction=compare_map_name)
    data_structs['map_multilocations'] = mp.newMap(100, maptype='PROBING', cmpfunction=compare_map_name)
    data_structs['year_experience'] = mp.newMap(100, maptype='PROBING', cmpfunction=compare_map_name)
    data_structs['map_companies'] = mp.newMap(100, maptype='PROBING', cmpfunction=compare_map_name)
    data_structs['map_cities'] = mp.newMap(100, maptype='PROBING', cmpfunction=compare_map_name)

    return data_structs


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    pass

def add_job(data_structs, job):
    """
    Función para agregar nuevos trabajos a la lista
    """
    lt.addLast(data_structs['jobs'], job)
    entry = mp.get(data_structs['year_experience'], job['published_at'].year)
    if entry:
        year_info = me.getValue(entry)
    else:
        year_info = {
            'junior': lt.newList('ARRAY_LIST', compare_map_name),
            'mid': lt.newList('ARRAY_LIST', compare_map_name),
            'senior': lt.newList('ARRAY_LIST', compare_map_name)
        }
        mp.put(data_structs['year_experience'], job['published_at'].year, year_info)
    mp.put(data_structs['map_jobs'], job['id'], job)
    
    add_city(data_structs, job)
    add_company(data_structs, job)

    lt.addLast(year_info[job['experience_level']], job)

def add_skill(data_structs, skill):
    """
    Función para agregar nuevas habilidades a la lista
    """
    lt.addLast(data_structs['skills'], skill)
    mp.put(data_structs['map_skills'], skill['id'], skill)

def add_employment_type(data_structs, employment_type):
    """
    Función para agregar nuevos tipos de empleo a la lista
    """
    lt.addLast(data_structs['employment-types'], employment_type)
    mp.put(data_structs['map_employment-types'], employment_type['id'], employment_type)

def add_multilocation(data_structs, multilocation):
    """
    Función para agregar nuevas ubicaciones a la lista
    """
    lt.addLast(data_structs['multilocations'], multilocation)
    mp.put(data_structs['map_multilocations'], multilocation['id'], multilocation)

def add_city(data_structs, job):
    """
    Función para agregar nuevas ciudades a la lista
    """
    entry = mp.get(data_structs['map_cities'], job['city'])
    if not entry:
        city_info = lt.newList('ARRAY_LIST', compare_map_name)
        mp.put(data_structs['map_cities'], job['city'], city_info)
    else:
        city_info = me.getValue(entry)
    lt.addLast(city_info, job)

def add_company(data_structs, job):
    """
    Función para agregar nuevas empresas a la lista
    """
    entry = mp.get(data_structs['map_companies'], job['company_name'])
    if not entry:
        company_info = lt.newList('ARRAY_LIST', compare_map_name)
        mp.put(data_structs['map_companies'], job['company_name'], company_info)
    else:
        company_info = me.getValue(entry)
    lt.addLast(company_info, job)

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs, company_name, initial_date, final_date):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    jobs_company = me.getValue(mp.get(data_structs['map_companies'], company_name))
    total_offers = 0
    experience_offers = {
        'junior': 0,
        'mid': 0,
        'senior': 0
    }
    offers = lt.newList('ARRAY_LIST', compare_map_name)
    for job in lt.iterator(jobs_company):
        if initial_date <= job['published_at'] and job['published_at'] <= final_date:
            total_offers += 1
            experience_offers[job['experience_level']] += 1
            lt.addLast(offers, job)
    
    merg.sort(offers, sort_req3)
    return total_offers, experience_offers, offers


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs, city_name, inital_date, final_date):

    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    city_offers = me.getValue(mp.get(data_structs['map_cities'], city_name))
    companies = {}
    offers = lt.newList('ARRAY_LIST', compare_map_name)
    for job in lt.iterator(city_offers):
        if inital_date <= job['published_at'] and job['published_at'] <= final_date:
            lt.addLast(offers, job)
            if job['company_name'] not in companies:
                companies[job['company_name']] = 1
            else:
                companies[job['company_name']] += 1
    total_offers = lt.size(offers)
    total_companies = len(companies)
    max_enterprise = max(companies)
    max_enterprise_offers = companies[max_enterprise]
    min_enterprise = min(companies)
    min_enterprise_offers = companies[min_enterprise]
    merg.sort(offers, sort_req5)
    return total_offers, total_companies, [max_enterprise, max_enterprise_offers], [min_enterprise, min_enterprise_offers], offers
    pass


def req_6(data_structs, n_cities, experience_level, year):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    year_map = data_structs['year_experience']
    cities_jobs = mp.newMap(100, maptype='PROBING', cmpfunction=compare_map_name)
    if experience_level != 'indiferente':
        levels = [experience_level]
    else:
        levels = ['junior', 'mid', 'senior']

    for level in levels:
        jobs = me.getValue(mp.get(year_map, year))[level]
        for job in lt.iterator(jobs):
            entry = mp.get(cities_jobs, job['city'])
            if not entry:
                city = {
                    'name': job['city'],
                    'jobs': lt.newList('ARRAY_LIST', compare_map_name),
                    'country': job['country_code'],
                    'total_offers': 0,
                    'average_salary': 0,
                    'sumatory_salary': 0,
                    'best_offer': [job, me.getValue(mp.get(data_structs['map_employment-types'], job['id']))],
                    'worst_offer': [job, me.getValue(mp.get(data_structs['map_employment-types'], job['id']))],
                    'enterprises': {},
                    'best_enterprise': ["", 0],
                    'total_enterprises': 0
                }
                mp.put(cities_jobs, job['city'], city)
            else:
                city = me.getValue(entry)
            
            lt.addLast(city['jobs'], job)
            city['total_offers'] = lt.size(city['jobs'])
            salary_from = me.getValue(mp.get(data_structs['map_employment-types'], job['id']))['salary_from']
            salary_to = me.getValue(mp.get(data_structs['map_employment-types'], job['id']))['salary_to']
            salary = (salary_from + salary_to) / 2
            city['sumatory_salary'] += salary
            city['average_salary'] = city['sumatory_salary'] / city['total_offers']
            job_employment_type = me.getValue(mp.get(data_structs['map_employment-types'], job['id']))
            try:
                if job_employment_type['salary_to'] > city['best_offer'][1]['salary_to']:
                    city['best_offer'] = [job, job_employment_type]
            except:
                pass
            try:
                if job_employment_type['salary_from'] < city['worst_offer'][1]['salary_from']:
                    city['worst_offer'] = [job, job_employment_type]
            except: 
                pass
            
            if job['company_name'] not in city['enterprises']:
                city['enterprises'][job['company_name']] = 1
            else:
                city['enterprises'][job['company_name']] += 1
            
            city['total_enterprises'] = len(city['enterprises'])
            city['best_enterprise'][0] = max(city['enterprises'])
            city['best_enterprise'][1] = city['enterprises'][city['best_enterprise'][0]]

    setCities = mp.valueSet(cities_jobs)
    cities_array = lt.newList('ARRAY_LIST')
    for city in lt.iterator(setCities):
        lt.addLast(cities_array, city)
    
    merg.sort(cities_array, sort_by_n_offers)

    answer_list = lt.newList('ARRAY_LIST')
    for i in range(1, n_cities + 1):
        if i <= lt.size(cities_array):
            city = lt.getElement(cities_array, i)
            lt.addLast(answer_list, city)
    
    return answer_list
            





    

    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare_map_name(data1, data2):

    dataentry = me.getKey(data2)
    if data1 > dataentry:
        return 1
    elif data1 < dataentry:
        return -1
    else:
        return 0

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass

def sort_by_n_offers(data1, data2):
    if data1['total_offers'] > data2['total_offers']:
        return True
    elif data1['total_offers'] < data2['total_offers']:
        return False
    else:
        if data1['average_salary'] > data2['average_salary']:
            return True
        else:
            return False

def sort_req3(data1, data2):
    if data1['published_at'] > data2['published_at']:
        return True
    elif data1['published_at'] < data2['published_at']:
        return False
    else:
        if data1['country_code'] < data2['country_code']:
            return True
        else:
            return False

def sort_req5(data1, data2):
    if data1['published_at'] > data2['published_at']:
        return True
    elif data1['published_at'] < data2['published_at']:
        return False
    else:
        if data1['company_name'] < data2['company_name']:
            return True
        else:
            return False


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
