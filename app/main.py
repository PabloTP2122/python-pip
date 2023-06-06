# Para importar todo
import utils
# Para importar funciones específicas
from utils import get_population, get_all_population
from read_csv import read_csv
import charts
# Usando pandas para evitar usar mucho código
import pandas as pd

path = 'data.csv'


def run():
  # Estos datos ya son un diccionario de la forma clave valor
  datos = read_csv(path)
  country = input('Type Country => ')
  countryExist = utils.population_by_country(datos, country)


  if len(countryExist) > 0:
    # Se coloca la pasicíón cero, debido a que retorna una lista con el diccionario. Si no se pasa la posición 0, se retorna una lista y no un diccionario.
    country = countryExist[0]
    labels, values = get_population(country)
    #print(countryExist[0])
    charts.generate_bar_chart(country['Country/Territory'],labels, values)
    #Pie charts
    ## usando pandas
    df = pd.read_csv(path)
    df = df[df['Continent'] == 'North America']
    #country, percentage = get_all_population(datos)
    country = df['Country/Territory']
    percentage = df['World Population Percentage']
    charts.generate_pie_chart('Population',country, percentage)
    
    
  
  
  print(countryExist)
# Para garantizar que cuando se ejecuta desde la terminal el main y no desde un import ejeute run, se utiliza el entry point.

if __name__ == '__main__':
  run()