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
- The state can be obtained by 



