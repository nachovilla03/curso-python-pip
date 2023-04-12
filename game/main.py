import random

def choose_options():
  options = ("piedra", "papel", "tijera")
  user_option = input("Piedra, Papel o Tijera? --->")
  user_option = user_option.lower()
  
  if not user_option in options:
    print("opcion no valida, intenta nuevamente".upper())
    # continue
    return None, None
  
  computer_option = random.choice(options)
  
  print("USUARIO ELIGIO: ", user_option)
  print("CPU  ELIGIO: ", computer_option)
 
  return user_option, computer_option 


def check_rules(user_option, computer_option,user_wins ,computer_wins):
  if user_option == computer_option:
    print("EMPATE")
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("piedra gana a tijera")
      print("GANO USUARIO")
      user_wins +=1
    else: 
      print("papel gana a tijera")
      print("GANO CPU")
      computer_wins +=1
  elif user_option == "papel":
    if computer_option == "piedra":
      print("papel gana a piedra")
      print("GANO USUARIO")
      user_wins +=1
    else: 
      print("tijera gana a papel")
      print("GANO CPU")
      computer_wins +=1
  elif user_option == "tijera":
    if computer_option == "papel":
      print("tijera gana a papel")
      print("GANO USUARIO")
      user_wins +=1
    else: 
      print("piedra gana a tijera")
      print("GANO CPU")
      computer_wins +=1
  return user_wins, computer_wins

  def check_winner(user_wins, computer_wins):
      if computer_wins ==2:
        print("CPU GANADOR DE LA PARTIDA")
        exit()
  
      if user_wins ==2:
        print("USUARIO GANADOR DE LA PARTIDA")
        exit()

def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1
  while True:

    print("*" *10)
    print("ROUND", rounds)
    print("*" *10)
  
    print("CPU: ", computer_wins)
    print("USUARIO: ", user_wins)
    rounds +=1
  
    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
    
    if computer_wins == 2:
      print('El ganador es la computadora')
      break

    if user_wins == 2:
      print('El ganador es el usuario')
      break
    
run_game()