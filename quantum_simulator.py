import numpy as np
import json
import random

class quantum_gate:
    def __init__(self, name = "identity", matrix = [[1, 0],[0, 1]]):
        match name:
            case "identity":
                self.matrix = np.identity(2, dtype = np.complex256)
            case "x":
                self.matrix = np.array([[0, 1],[1, 0]], dtype  = np.complex256)
            case "y":
                self.matrix = np.array([0, -1j],[1j, 0], dtype = np.complex256)
            case "z":
                self.matrix = np.array([[1, 0],[0, -1]], dtype = np.complex256)
            case "h":
                self.matrix = np.array([[1, 1],[1, -1]], dtype = np.complex256) / np.sqrt(2)
            case "custom":
                self.matrix = np.array(matrix, dtype = np.complex256)
                # normalize the matrix
                det = np.linalg.det(self.matrix)
                self.matrix = self.matrix / np.absolute(det)

class quantum_circuit:
    def __init__(self, filename):
        with open(filename, "r") as f:      
            data = json.load(f)
        self._load_registers(data["registers"])
        self.layers = []
        for layer in data["layers"]:
            self.layers.append(quantum_circuit_layer(layer))

    def _load_registers(self, registers):
        temp_register = []
        for register in registers:
            self.register.append(complex(register))
        self.registers = np.array(temp_register)

    def observe(self) -> list:
        quantum_state = self.registers
        for layer in self.layers:
            quantum_state = layer * quantum_state
        probability = [np.absolute(p)**2 for p in quantum_state]
        random_number = random.random()
        probability_sum = 0
        observed_state = -1
        for i in range(probability):
            probability_sum = probability_sum + probability[i]
            if probability_sum > random_number:
                observed_state = i
                break
        # case when sum of probabilities is smaller than 1 due to floating point inaccuracy.
        if observed_state == -1:
            observed_state = len(probability) - 1
        output = []
        for i in range(len(self.registers)):
            output.append(0 if int(observed_state / 2**(i)) % 2 == 0 else 1)
        return output

class quantum_circuit_layer:
    def __init__(self, layer_info: list):
        self.make_matrix(layer_info)
    
    def make_matrix(self) -> None:
        pass
    
    def add_gate(self, gate: str) -> None:
        pass

    def __mul__(self, val):
        if isinstance(val, np.array):
            return np.matmul(val, self.matrix)
        elif isinstance(val, quantum_circuit_layer):
            return np.matmul(val.matrix, self.matrix)
        else:
            raise ValueError(f"expected numpy.array or quantum_circuit_layer but got {type(val)}")
    
    def __str__(self):
        return self.matrix.__str__()