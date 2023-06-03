# Juego de piedra papel o tijera
# Reglas, que el juego termina cuando uno de los jugadores gana más de 1 vez. Si quedan empatados el juego continua.
import random


def chose_option():
  #Tupla
  options = ('piedra', 'papel', 'tijera')
  user_option = input('piedra, papel o tijera => ')
  user_option = user_option.lower()

  if not user_option in options:
    print('Opción no válida')
    return None, None

  computer_option = random.choice(options)
  print('Opción seleccionada => ', user_option)
  print('Opción seleccionada por computadora => ', computer_option)
  return user_option, computer_option
  
def check_rules(user_option, computer_option, puntos_u, puntos_c):
  if user_option == computer_option:
    print('Es un empate!')
  # Debe continuar el juego
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('Piedra gana a tijera')
      print('Usuario ganó!')
      puntos_u += 1

    elif computer_option == 'papel':
      print('Papel gana a piedra')
      print('Computadora ganó!')
      puntos_c += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('Tijera gana a papel')
      print('Usuario ganó!')
      puntos_u += 1

    elif computer_option == 'piedra':
      print('Piedra gana a tijera')
      print('Computadora ganó!')
      puntos_c += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('Papel gana a piedra')
      print('Usuario ganó!')
      puntos_u += 1

    elif computer_option == 'tijera':
      print('Tijera gana a papel')
      print('Computadora ganó!')
      puntos_c += 1
  return puntos_c, puntos_u
  
def check_winer(puntos_u, puntos_c):
  if puntos_u == 2:
    print('\nGanaste!')
    exit()
  if puntos_c == 2:
    print('\nLa compu ganó sss')
    exit()
    
def run_game():
  puntos_u = 0
  puntos_c = 0
  ronda = 1
  while True:
    print('*' * 10)
    print('RONDA', ronda)
    print('Usuario', puntos_u)
    print('PC', puntos_c)
    print('*' * 10)
    ronda += 1
    
    user_option, computer_option = chose_option()
    puntos_c, puntos_u = check_rules(user_option, computer_option,
                                            puntos_u, puntos_c)
    check_winer(puntos_u, puntos_c)
    
run_game() 

