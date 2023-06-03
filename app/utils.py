import re
# Normalmente los archivos que tienen utilidades, tienen solo funciones

# Función que devuelve las keys y los values para poder crear las gráficas de barras key = label, values = values
def get_population(country_dict):
  # Esta es una solución válida, otra solución puede ser con re (regular expressions)
  population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values

#A = 'Hola
def get_all_population(dict):
  '''
  percentages = {
  'Country': percentage,
  
  }
  '''
  percentages = { country['Country/Territory']: float(country['World Population Percentage']) for country in dict}
  labels = percentages.keys()
  values = percentages.values()
  return labels, values

def quitar_tildes(texto):
    # Definir el diccionario de reemplazo
    reemplazos = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'Á': 'A',
        'É': 'E',
        'Í': 'I',
        'Ó': 'O',
        'Ú': 'U'
    }

    # Crear una expresión regular que coincide con los caracteres a reemplazar
    patron = re.compile('|'.join(reemplazos.keys()))

    # Realizar el reemplazo utilizando la función re.sub()
    texto_sin_tildes = patron.sub(lambda x: reemplazos[x.group()], texto)

    return texto_sin_tildes

# Quitar acentos del valor del diccionario, sin modificar el diccionario original
def countries(item):
  item_c = item.copy()
  item_c['Country/Territory'] = quitar_tildes(item_c['Country/Territory']).lower()
  return item_c['Country/Territory']

# Retorna la población por ciudad buscada
def population_by_country(data, country):
  country = quitar_tildes(country).lower()
  result = list(filter(lambda item: countries(item) == country, data))
  
  return result