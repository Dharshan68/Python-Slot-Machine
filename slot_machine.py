import random

# Maximum number of lines a user can bet on
max_bet_lines = 3

# Minimum and maximum bet amount limits
min_bet_amount = 10
max_bet_amount = 100

# Slot machine layout (3 rows and 3 columns)
rows = 3
cols = 3

# Symbols and their frequency in the slot machine
symbols = {
           'A' : 2,  # 'A' appears twice in the list
           'B' : 4,
           'C' : 6,
           'D' : 8
          }

# Symbol values to determine winnings
symbols_value = {
                 'A' : 5,  # 'A' has the highest payout value
                 'B' : 4,
                 'C' : 3,
                 'D' : 2
                }


# Function to handle user deposit
def deposit_logic():
  while True:
    balance = input('enter the deposit amount: ')

    # Check if balance is a valid positive integer
    if balance.isdigit():
      balance = int(balance)
      if balance > 0:
        break
      else:
        print('please enter a valied amount')
    else:
      print('please enter a number')

  return balance


# Function to get the number of lines the user wants to bet on
def no_of_lines_bet_logic():
  while True:
    no_lines = input('please enter the number of lines u want to bet on: ')

     # Check if the input is a valid number within the allowed range
    if no_lines.isdigit():
      no_lines = int(no_lines)
      if 1 <= no_lines <= max_bet_lines:
        break
      else:
        print(f'please enter a number between 1 - {max_bet_lines}')
    else:
      print('please enter a number')

  return no_lines

# Function to get the amount the user wants to bet
def bet_amount_logic():
  while True:
    bet_amount =  input('enter the bet amount: ')

    # Check if the bet amount is within the allowed limits
    if bet_amount.isdigit():
      bet_amount = int(bet_amount)
      if min_bet_amount <= bet_amount <= max_bet_amount:
        break
      else:
        print(f'please enter a bet amount between ₹{min_bet_amount} - ₹{max_bet_amount}')
    else:
      print('please enter a number')

  return bet_amount

# Function to generate the slot machine spin result
def spin_logic(rows,cols,symbols):
  all_symbols = []

  # Fill the list with all the symbols based on their count
  for symbol,symbol_count in symbols.items():
    for _ in range(symbol_count):
      all_symbols.append(symbol)

  columns = []
  # For each column in the slot machine (outer loop),
  # we generate a list of symbols (inner loop) that represent the rows in that column.
  for _ in range(cols):
    column = []
    current_all_symbols = all_symbols[:]  # Copy to avoid modifying the original list

    # For each row in this column, select a random symbol and add it to the column list
    for _ in range(rows):
      chosen_ele = random.choice(current_all_symbols)
      column.append(chosen_ele)
      current_all_symbols.remove(chosen_ele)  # Remove chosen symbol to avoid repetition in the same column

    # Append the completed column to the columns list
    columns.append(column)

  # The columns list now contains 'cols' number of lists, each representing a column in the slot machine,
  # and each column has 'rows' number of symbols.
  return columns


# Function to display the slot machine spin result
def print_pattern_logic(columns):
  for i in range(len(columns[0])):
    for column in columns:
      print(column[i],end=' ')
    print()  # Newline after each row

# Function to calculate and display winnings
def check_winning(columns,symbols_value,no_lines_bet,bet_amount,total_bet_amount):
  winning_amount = 0

  # Check each line the user bet on for winning combinations
  for lines in range(no_lines_bet):
    check_value = columns[0][lines]
    for column in columns:
      if check_value != column[lines]:
        break
    else:
      # Add winning amount based on symbol value and bet amount
      winning_amount += symbols_value[check_value] * bet_amount

  print(f'\nYou have won \033[91m₹{winning_amount}\033[0m')

  # Return the net gain/loss after subtracting total bet
  return winning_amount - total_bet_amount

# Main game function that handles a single spin
def game(balance):
  no_lines_bet = no_of_lines_bet_logic()

  while True:
    bet_amount = bet_amount_logic()
    total_bet_amount = no_lines_bet * bet_amount  # Calculate total bet

    # Ensure the user has enough balance for the total bet
    if total_bet_amount <= balance:
      break
    else:
      print(f'your total bet amount ₹{total_bet_amount} is exceeding the balance amount ₹{balance}')

  print(f'\n\033[92mbalance: ₹{balance}, bet lines: {no_lines_bet}, total bet amount: ₹{total_bet_amount}\033[0m\n')

  # Generate and print slot machine spin result
  columns = spin_logic(rows,cols,symbols)
  print_pattern_logic(columns)

  # Calculate winnings and return the net change in balance           
  total_win_amount = check_winning(columns,symbols_value,no_lines_bet,bet_amount,total_bet_amount)
  return total_win_amount


# Main function to run the game
def main():
  balance = deposit_logic()  # Get initial deposit

  while True:
    print(f'Your balance is \033[94m₹{balance}\033[0m')
    status = input(f'\nPress ["y"] to spin again: ')

    print('\n=====================================================================================\n')

    # If balance is zero, prompt for a new deposit
    if balance == 0:
      print('your balance is nil')
      balance = deposit_logic()

    # Play a game round if the user wants to continue
    if status == 'y':
      balance += game(balance)
    else:
      # Play a game round if the user wants to continue
      print(f'please collect your balance amount ₹{balance}\nTHANK YOU')
      break

# Start the game
main()
