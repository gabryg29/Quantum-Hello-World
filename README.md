# Quantum Hello World 

**Ever dreamed of running a *Hello World* on a quantum computer?**  
This repository is your guided entry point into the fascinating world of **quantum computing with Qiskit**.  

Here you’ll build and run your first quantum circuits, explore the basics of **qubits, superposition, entanglement, and measurement**, and understand how to use Qiskit’s new **primitives** (`Sampler` and `Estimator`). You will be able to execute everything locally with a simulator and (optionally) on real quantum hardware via **IBM Quantum**.

---

##  What you’ll learn

- What a **qubit** is and how it differs from a classical bit.  
- How to create **superposition** using the Hadamard gate.  
- How to generate **entanglement** (Bell state) with `H` and `CX`.  
- How to use the **Sampler** to get output distributions.  
- How to use the **Estimator** to calculate expectation values of observables.  
- How to run the same experiments on **IBM Quantum’s cloud backends**.  

---

##  Requirements

- Python 3.10+ (recommended)  
- `pip` and optionally `virtualenv`  
- An [IBM Quantum account](https://quantum.ibm.com/) (optional, for running on the cloud)  


##  Getting started

1. **Run locally (simulator):**  
   Open the notebook `notebooks/hello_world.ipynb` and execute the cells in the *Local execution* section using Qiskit’s reference primitives.

2. **Run on IBM Quantum (optional):**  
   - Create an API key in your IBM Quantum account.  
   - Configure `QiskitRuntimeService` in the notebook.  
   - Start a `Session` with a backend and run the same circuits on the cloud.  

---

##  Quick fundamentals

- **Qubit** → quantum state |0⟩, |1⟩, or a superposition.  
- **Superposition** → combine |0⟩ and |1⟩ (Hadamard gate).  
- **Entanglement** → correlations beyond classical physics (Bell states).  
- **Measurement** → collapses state to classical bitstrings with probabilities.  
- **Primitives**:  
  - `Sampler`: returns **output distributions** from circuits.  
  - `Estimator`: computes **expectation values** of observables.  

---

##  References

- [IBM Quantum Documentation — Hello World tutorial](https://quantum.cloud.ibm.com/docs/en/tutorials/hello-world)  
- [Qiskit Installation Guide](https://qiskit.org/documentation/getting_started.html)  
- [Qiskit API Docs](https://qiskit.org/documentation/apidoc/)  

---

##  Contributing

Contributions are welcome!  
Feel free to open issues or PRs with suggestions, corrections, or new didactic examples (e.g., CHSH game, variational algorithms, quantum kernels).

---

##  License

MIT © 2025
