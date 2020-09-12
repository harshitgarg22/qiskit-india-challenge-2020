
### WRITE YOUR CODE BETWEEN THESE LINES - START
    
# import libraries that are used in the function below.
from qiskit import QuantumCircuit
import numpy as np
from math import sqrt, pi
### WRITE YOUR CODE BETWEEN THESE LINES - END

def build_state():
    
    # create a quantum circuit on one qubit
    circuit = QuantumCircuit(1)
    
    ### WRITE YOUR CODE BETWEEN THESE LINES - START
    circuit.initialize([1/sqrt(2), -1j/sqrt(2)],0)
    circuit.rz(-pi/2,0)
    circuit.h(0)
#     circuit.z(0)
#     circuit.h(0)
#     circuit.h(0)
#     circuit.z(0)
#     circuit.h(0)
    # apply necessary gates
    
    ### WRITE YOUR CODE BETWEEN THESE LINES - END
    return circuit
