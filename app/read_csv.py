# Lectura de archivos CSV
# Uno de los retos al leer un CSV es transformarlo a formato de diccionario
import csv

def read_csv(path):
  
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    headers = next(reader)
    data = []
    for row in reader:
      iterable = zip(headers, row)
      # Se utiliza un dict comprehension
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('data.csv')
  print(data[0])