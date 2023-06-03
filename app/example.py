# Los archivos pueden ser módulos, y pueden ser scripts
# Solo existe un inconveniente al queren tratar como módulo un
# archivo script, el cual es que se ejecuta el script completo y no
# solo la parte que nos interesa.

# El problema se soluciona colocando la la lógica de todo el script 
# main en una función llamada run(), que solo se ejecuta si se cumple una condición

import main

print(main.datos)