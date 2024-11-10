import random

max_bet_lines = 3

min_bet_amount = 10
max_bet_amount = 100

rows = 3
cols = 3

symbols = {
           'A' : 2,
           'B' : 4,
           'C' : 6,
           'D' : 8
          }

symbols_value = {
                 'A' : 5,
                 'B' : 4,
                 'C' : 3,
                 'D' : 2
                }


def deposit_logic():

  while True:
    balance = input('enter the deposit amount: ')

    if balance.isdigit():
      balance = int(balance)
      if balance > 0:
        break
      else:
        print('please enter a valied amount')
    else:
      print('please enter a number')

  return balance


def no_of_lines_bet_logic():

  while True:
    no_lines = input('please enter the number of lines u want to bet on: ')

    if no_lines.isdigit():
      no_lines = int(no_lines)
      if 1 <= no_lines <= max_bet_lines:
        break
      else:
        print(f'please enter a number between 1 - {max_bet_lines}')
    else:
      print('please enter a number')

  return no_lines


def bet_amount_logic():

  while True:
    bet_amount =  input('enter the bet amount: ')

    if bet_amount.isdigit():
      bet_amount = int(bet_amount)
      if min_bet_amount <= bet_amount <= max_bet_amount:
        break
      else:
        print(f'please enter a bet amount between ₹{min_bet_amount} - ₹{max_bet_amount}')
    else:
      print('please enter a number')

  return bet_amount


def spin_logic(rows,cols,symbols):

  all_symbols = []

  for symbol,symbol_count in symbols.items():
    for _ in range(symbol_count):
      all_symbols.append(symbol)

  columns = []
  for _ in range(cols):
    column = []
    current_all_symbols = all_symbols[:]
    for _ in range(rows):
      chosen_ele = random.choice(current_all_symbols)
      column.append(chosen_ele)
      current_all_symbols.remove(chosen_ele)

    columns.append(column)

  return columns


def print_pattern_logic(columns):

  for i in range(len(columns[0])):
    for column in columns:
      print(column[i],end=' ')
    print()


def check_winning(columns,symbols_value,no_lines_bet,bet_amount,total_bet_amount):
  winning_amount = 0
  for lines in range(no_lines_bet):
    check_value = columns[0][lines]
    for column in columns:
      if check_value != column[lines]:
        break
    else:
      winning_amount += symbols_value[check_value] * bet_amount

  print(f'\nYou have won \033[91m₹{winning_amount}\033[0m')

  return winning_amount - total_bet_amount


def game(balance):
  no_lines_bet = no_of_lines_bet_logic()

  while True:

    bet_amount = bet_amount_logic()
    total_bet_amount = no_lines_bet * bet_amount

    if total_bet_amount <= balance:
      break
    else:
      print(f'your total bet amount ₹{total_bet_amount} is exceding the balance amount ₹{balance}')

  print(f'\n\033[92mbalance: ₹{balance}, bet lines: {no_lines_bet}, total bet amount: ₹{total_bet_amount}\033[0m\n')

  columns = spin_logic(rows,cols,symbols)

  print_pattern_logic(columns)

  total_win_amount = check_winning(columns,symbols_value,no_lines_bet,bet_amount,total_bet_amount)

  return total_win_amount


def main():
  balance = deposit_logic()

  while True:
    print(f'Your balance is \033[94m₹{balance}\033[0m')
    status = input(f'\nPress ["y"] to spin again: ')

    print('\n=====================================================================================\n')

    if balance == 0:
      print('your balance is nil')
      balance = deposit_logic()

    if status == 'y':
      balance += game(balance)
    else:
      print(f'please collect your balance amount ₹{balance}\nTHANK YOU')
      break


main()
