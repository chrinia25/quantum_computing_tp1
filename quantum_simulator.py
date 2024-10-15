import numpy as np
import json
import random

class quantum_gate:
    def __init__(self, name = "identity", matrix = [[1, 0],[0, 1]]):
        match name:
            case ["identity", "NONE"]:
                self.matrix = np.identity(2, dtype = np.clongdouble)
            case "X":
                self.matrix = np.array([[0, 1],[1, 0]], dtype  = np.clongdouble)
            case "Y":
                self.matrix = np.array([0, -1j],[1j, 0], dtype = np.clongdouble)
            case "Z":
                self.matrix = np.array([[1, 0],[0, -1]], dtype = np.clongdouble)
            case "H":
                self.matrix = np.array([[1, 1],[1, -1]], dtype = np.clongdouble) / np.sqrt(2)
            case _:
                self.matrix = np.array(matrix, dtype = np.clongdouble)
                # normalize the matrix
    def __mul__(self, val):
        if isinstance(val, np.ndarray):
            return np.matmul(val, self.matrix)
        elif isinstance(val, quantum_gate):
            return np.matmul(val.matrix, self.matrix)
        else:
            raise ValueError(f"expected numpy.array or quantum_circuit_layer but got {type(val)}")
    
    def __str__(self):
        return self.matrix.__str__()

class quantum_circuit:
    def __init__(self, filename):
        with open(filename, "r") as f:      
            data = json.load(f)
        self._load_registers(data["registers"])
        self.layers = []
        self.custom_gates = {}
        for gate_name in data["custom_gates"]:
            self.custom_gates[gate_name] = quantum_gate(gate_name, data["custom_gates"][gate_name])
        for layer in data["layers"]:
            self.layers.append(quantum_circuit_layer(layer, self.custom_gates))
        self.calculation_result = None
        self.register_count = data["register_count"]

    def _load_registers(self, registers):
        first = True
        for register in registers:
            if first:
                temp_register = np.array([complex(register[0]), complex(register[1])], dtype=np.clongdouble)
                first = False
            else:
                temp_register = np.kron(np.array([complex(register[0]), complex(register[1])], dtype=np.clongdouble), temp_register)
        self.registers = temp_register

    def run(self) -> list:
        if self.calculation_result == None:
            self.calculate_result()
        return self.observe()

    def calculate_result(self) -> None:
        quantum_state = self.registers
        for layer in self.layers:
            quantum_state = layer * quantum_state
        probability = [np.absolute(p)**2 for p in quantum_state]
        self.calculation_result = probability
        

    def observe(self) -> list:
        random_number = random.random()
        probability_sum = 0
        observed_state = -1
        for i in range(len(self.calculation_result)):
            probability_sum = probability_sum + self.calculation_result[i]
            if probability_sum > random_number:
                observed_state = i
                break
        # case when sum of probabilities is smaller than 1 due to floating point inaccuracy.
        if observed_state == -1:
            observed_state = len(self.calculation_result) - 1
        output = []
        for i in range(self.register_count):
            output.append(0 if int(observed_state / 2**(i)) % 2 == 0 else 1)
        return output


def apply_gate_local(matrix : np.array, gate : quantum_gate, row1 : int, row2: int) -> None:
    template = np.array([[matrix[row1,row1], matrix[row1,row2]], [matrix[row2,row1], matrix[row2,row2]]])
    template = gate * template
    matrix[row1, row1] = template[0,0]
    matrix[row1, row2] = template[0,1]
    matrix[row2, row1] = template[1,0]
    matrix[row2, row2] = template[1,1]

class quantum_circuit_layer:
    def __init__(self, layer_info: list, custom_gate_dict : list):
        self.make_matrix(layer_info, custom_gate_dict)
    
    def make_matrix(self, layer_info, custom_gate_dict) -> None:
        self.matrix = np.identity(2**len(layer_info), dtype = np.clongdouble)
        controls = {}
        for i in range(len(layer_info)):
            if layer_info[i][0] == 'c':
                control_target = layer_info[i][1]
                if control_target not in controls.keys():
                    controls[control_target] = []
                controls[control_target].append(i)

        for i in range(len(layer_info)):
            if not (layer_info[i].lower() == "none" or layer_info[i][0] == 'c'):
                if layer_info[i] in custom_gate_dict:
                    gate = custom_gate_dict[layer_info[i]]
                else:
                    gate = quantum_gate(layer_info[i])
                target_qubit = i
                print(gate)
                print(self.matrix)
                if target_qubit not in controls.keys():
                    for j in range(2**len(layer_info)):
                        if j % (2 ** (target_qubit + 1)) == 0:
                            apply_gate_local(self.matrix, gate, j, j + 2**target_qubit)
                else:
                    control_qubits = controls[target_qubit]
                    for j in range(2**len(layer_info)):
                        if j % (2 ** (target_qubit + 1)) == 0:
                            flag = True
                            for control_qubit in control_qubits:
                                if j % (2 ** (control_qubit + 1)) == 1:
                                    flag = False
                                    break
                            if flag == True:
                                apply_gate_local(self.matrix, gate, j, j + 2**target_qubit)

    def __mul__(self, val):
        if isinstance(val, np.ndarray):
            return np.matmul(val, self.matrix)
        elif isinstance(val, quantum_circuit_layer):
            return np.matmul(val.matrix, self.matrix)
        else:
            raise ValueError(f"expected numpy.array or quantum_circuit_layer but got {type(val)}")
    
    def __str__(self):
        return self.matrix.__str__()