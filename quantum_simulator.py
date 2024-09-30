import numpy as np

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
    pass
    
class quantum_circuit_layer:
    pass