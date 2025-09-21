from __future__ import annotations
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.primitives import Sampler, Estimator

def hello_sampler(shots: int = 1000):
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    sampler = Sampler()
    result = sampler.run([qc], shots=shots).result()
    return result[0].data.meas.get_counts()

def bell_counts(shots: int = 1000):
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0,1],[0,1])
    sampler = Sampler()
    result = sampler.run([qc], shots=shots).result()
    return result[0].data.meas.get_counts()

def estimator_example():
    qc = QuantumCircuit(1)
    qc.h(0)  # |+>
    z_op = SparsePauliOp.from_list([('Z', 1.0)])
    x_op = SparsePauliOp.from_list([('X', 1.0)])
    est = Estimator()
    ez = est.run([(qc, z_op)]).result()[0].data.evs[0]
    ex = est.run([(qc, x_op)]).result()[0].data.evs[0]
    return float(ez), float(ex)

if __name__ == '__main__':
    print("Hello Sampler:", hello_sampler())
    print("Bell counts:", bell_counts())
    print("Estimator <Z>, <X> on |+>:", estimator_example())
