# Auto Bell-State Generator


>## TASK-2 from the screening tasks for QOSF mentorship program
>**Submitted by:** Raghav Rawat<br><br>
>**From:** Jaipur, India<br><br>
>**Date of Submission:** <br><br>
>**Time of Submission:** <br><br>

## Contents

---

## Problem Statement ##
Implement a circuit that returns |01> and |10> with equal probability.  
**Requirements for the task**  
- The circuit should consist only of CNOTs, RXs and RYs. 
- Start from all parameters in parametric gates being equal to 0 or randomly chosen. 
- You should find the right set of parameters using gradient descent (you can use more advanced optimization methods if you like). 
- Simulations must be done with sampling - i.e. a limited number of measurements per iteration and noise. 
- Compare the results for different numbers of measurements: 1, 10, 100, 1000.

**Requirements met**  
- Ideal circuit involves just one RY and CNOT gate each. :D 
- Code has parameters, 'shots' and 'theta', initially being equal to 0 or randomly chosen. 
- Ideal values of parameter 'theta' obtained using both Gradient descent and Nesterov Accelerated Gradient, followed by a performance comparison.  
- Results of the optimizer have been compared for four different amounts of measurements: 1, 10, 100, 1000.

---
## Instructions to Run Program ##
1. Install `qiskit`
2. Clone repository and execute python file `main.py`

## Circuit Design ##
- Ideal state
 ![Ideal state](media/ideal_state.png)
- The state can be obtained by first applying `Hadamard` and `X` gates to q0 and q1
 ![Hadamard](media/Hadamard.png)
- And then applying `CNOT` (0 -> 1) gate
 ![CNOT](media/cnot.png)

## Ideal quantum circuit
- The ideal circuit can then be consolidated as follows
![Circuit](media/circuit.png)

## Design Partitions
- The problem statement can be approached with a Hybrid Classical-Quantum optimization model, having three major partitions. 
  1. The `Bell State Generator` instantiates a quantum circuit required for the state generation, but with one optimizable parameter `theta`. It is a Quantum circuit.
  2. `Cost Function` calculates the cost or error for the parameter value of current iteration.It is a classical calculation.
  3. `Optimizer`, is a classical machine learning optimizer, updates the values of parameter `theta` for better performance of the circuit. Two classical optimizers namely - 'gradient descent' and 'Nesterov Accelerated Gradient' have been used and compared.

  ![Design](media/design.png)
  







