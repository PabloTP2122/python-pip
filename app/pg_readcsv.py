import csv
import functools

def read_csv(path):
  # Tu código aquí 👇
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    # Save reader in a list for use in for loop
    data = list(reader)
    # Dict comprehensions
    departments = {key: int(value) for key, value in data}
  # List comprehensions
  expenses = [expense for expense in departments.values()]
  # Using reduce
  total = functools.reduce(lambda count, item: count + item, expenses,0)
 
  return total

# Mejorando eficiencia y complejidad algoritmica
def read_csv2(path):
  with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        departments = {}
        total = 0
        
        for row in reader:
            department = row[0]
            expense = int(row[1])
            
            departments[department] = expense
            total += expense
    
  return total
  
response = read_csv('./app/data2.csv')
response2 = read_csv2('./app/data2.csv')
print(response)
print(response2)