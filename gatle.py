import numpy as np

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
    init_qubits = permute_qubits(n_bit)
    
    return {
        'n_bits': n_bit, 
        'answer' : answer,
        'init_qubits': init_qubits
        }

KET_0 = np.array([[1], [0]], dtype=np.clongdouble)
KET_1 = np.array([[0], [1]], dtype=np.clongdouble)

KET_PLUS = (KET_0 + KET_1) / np.sqrt(2)
KET_MINUS = (KET_0 - KET_1) / np.sqrt(2)

STATES = [KET_0, KET_1, KET_PLUS, KET_MINUS]

def permute_qubits(n_bit):
    return np.array([random.choice(STATES) for _ in range(n_bit)])
    
def play_game(data):
    game = set_game()
    random.seed()
    
    circuit = quantum_circuit(data=data)
    r = circuit.set_registers(game['init_qubits'])

    # set register
    observed = circuit.run()
    
    bin_answer = bin(game['answer'])[2:].zfill(game['n_bits'])
    bin_answer = [int(digit) for digit in bin_answer]
    correct = [a == b for a, b in zip(bin_answer, observed)]
    
    return {
        'correct': correct
    }
    
    
    
if __name__ == '__main__':
    set_game()