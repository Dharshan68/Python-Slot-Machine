# Text-Based Slot Machine Game 🎰

This is a simple text-based slot machine game written in Python. The game allows players to deposit money, choose the number of lines to bet on, and set a bet amount per line. When the player spins the slot machine, they either win or lose based on the matching symbols in each line.

The goal of the game is to provide an engaging, simulated slot machine experience entirely through the console

***

## Features 🔥✨
- Allows players to deposit money and track their balance.
- Option to choose how many lines to bet on (up to 3).
- Customizable bet amount per line within a defined range.
- Randomly generates slot machine results and calculates winnings based on matched symbols.
- Tracks winnings and displays the updated balance after each round.

***

## Game Rules 📜🎲

- The player can bet on up to 3 lines.
- Symbols have different values (e.g., "A" has the highest payout, "D" the lowest).
- Winning occurs if all symbols in a line match.
- Payout is calculated based on the symbol's value and the bet amount.

***
## Game Play

### Symbols and Payouts

There are 4 symbol with the following payout rate:

- A: 6
- B: 4
- C: 3
- D: 2

If a user has made a bet of ₹50 per line, and after spinning, only one line out of bet lines matched with a "D". The prize would be **₹100** because `₹50 * 2 = ₹100`. However, if there is no match (loss), the total bet amount of ₹150 (₹50 \* 3 selected lines) will be deducted from the balance.

#### CASE-1
![image](https://github.com/Dharshan68/images/blob/main/Screenshot%202024-11-10%20220912.png?raw=true)


#### CASE-2
![image](https://github.com/Dharshan68/images/blob/main/Screenshot%202024-11-10%20221207.png?raw=true)
