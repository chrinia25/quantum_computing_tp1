import random
from datetime import date

from quantum_simulator import quantum_circuit

def set_day_seed():
    today = date.today().strftime("%Y%m%d")
    random.seed(int(today))

def set_game() -> tuple[int]:
    set_day_seed()
    n_bit = random.randint(4,8)
    answer = random.randint(1, 2 ** n_bit) - 1

    return {
        'n_bits': n_bit, 
        'answer' : answer
        }
    
def play_game(data):
    n_bit, answer = set_game()
    
    random.seed()
    observed = quantum_circuit(data)
    
    bin_answer = bin(answer)[2:]
    bin_answer = [int(digit) for digit in bin_answer]
    
    correct = [a == b for a, b in zip(bin_answer, observed)]
    
    return {
        'correct': correct
    }
    
    
    
if __name__ == '__main__':
    set_game()