{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [],
   "source": [
    "# creating the necessary imports\n",
    "\n",
    "import numpy as np\n",
    "from qiskit import *\n",
    "from qiskit.circuit import Parameter\n",
    "from math import radians"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<qiskit.circuit.instructionset.InstructionSet at 0x12ea89ec8e0>"
      ]
     },
     "execution_count": 135,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Defining the ideal circuit to generate Bell State: |01> + |10>\n",
    "\n",
    "theta = Parameter('param1')\n",
    "\n",
    "qc = QuantumCircuit(2, 2)\n",
    "state1 = [1,0]\n",
    "state2 = [0,1]\n",
    "qc.initialize(state1, 0)\n",
    "qc.initialize(state2, 1)\n",
    "qc.barrier()\n",
    "qc.ry(theta, 0)\n",
    "qc.barrier()\n",
    "qc.cx(0, 1)\n",
    "qc.barrier()\n",
    "qc.measure(0, 0)\n",
    "qc.measure(1, 1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre style=\"word-wrap: normal;white-space: pre;background: #fff0;line-height: 1.1;font-family: &quot;Courier New&quot;,Courier,monospace\">     ┌─────────────────┐ ░ ┌────────────┐ ░       ░ ┌─┐   \n",
       "q_0: ┤ initialize(1,0) ├─░─┤ RY(param1) ├─░───■───░─┤M├───\n",
       "     ├─────────────────┤ ░ └────────────┘ ░ ┌─┴─┐ ░ └╥┘┌─┐\n",
       "q_1: ┤ initialize(0,1) ├─░────────────────░─┤ X ├─░──╫─┤M├\n",
       "     └─────────────────┘ ░                ░ └───┘ ░  ║ └╥┘\n",
       "c_0: ════════════════════════════════════════════════╩══╬═\n",
       "                                                        ║ \n",
       "c_1: ═══════════════════════════════════════════════════╩═\n",
       "                                                          </pre>"
      ],
      "text/plain": [
       "     ┌─────────────────┐ ░ ┌────────────┐ ░       ░ ┌─┐   \n",
       "q_0: ┤ initialize(1,0) ├─░─┤ RY(param1) ├─░───■───░─┤M├───\n",
       "     ├─────────────────┤ ░ └────────────┘ ░ ┌─┴─┐ ░ └╥┘┌─┐\n",
       "q_1: ┤ initialize(0,1) ├─░────────────────░─┤ X ├─░──╫─┤M├\n",
       "     └─────────────────┘ ░                ░ └───┘ ░  ║ └╥┘\n",
       "c_0: ════════════════════════════════════════════════╩══╬═\n",
       "                                                        ║ \n",
       "c_1: ═══════════════════════════════════════════════════╩═\n",
       "                                                          "
      ]
     },
     "execution_count": 136,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# drawing the circuit\n",
    "qc.draw()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# defining the function to execute the given number of shots on quantum simulator \n",
    "\n",
    "def execute_circuit(angle,shots):\n",
    "    '''\n",
    "        Parameters: angle - the initial random angle given as input\n",
    "                    shots - number of shots to be executed on simulator\n",
    "        Returns   : dictionary of possible states after execution with their respective counts\n",
    "    '''\n",
    "    rad = radians(angle) # conversion to degrees\n",
    "    job = execute(qc, backend = Aer.get_backend('qasm_simulator'),shots = shots , parameter_binds=[{theta: rad}])\n",
    "    counts = job.result().get_counts()\n",
    "    return counts\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "def costfunction(prob_avg_01,prob_avg_10):\n",
    "    '''\n",
    "         Parameters: prob_avg_01 - average probability of getting the state 01 on measurement\n",
    "                     prob_avg_10 - average probability of getting the state 10 on measurement\n",
    "         Returns   : Mean Squared Error of the probabilities as a value to be improved with optimization techniques\n",
    "    '''\n",
    "    return pow((prob_avg_01 - prob_avg_10),2)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [],
   "source": [
    "def costfunction_NAG(prob_avg_01,prob_avg_10,gama,V_t):\n",
    "    '''\n",
    "         Parameters: prob_avg_01 - average probability of getting the state 01 on measurement\n",
    "                     prob_avg_10 - average probability of getting the state 10 on measurement\n",
    "                     gama        - constant value parameter for Nesterov Accelerated Gradient\n",
    "                     V_t         - using γV(t−1) in cost function for modifying the weights so that θ−γV(t−1) tells us the future location\n",
    "         Returns   : Mean Squared Error of the probabilities as a value to be improved with optimization techniques\n",
    "    '''\n",
    "    return pow((prob_avg_01 - prob_avg_10 - gama*V_t),2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [],
   "source": [
    "# from tqdm import tqdm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Measurement counts for initial angle:  120  and shots:  1 \t {'10': 1}\n",
      "Measurement counts for initial angle:  120  and shots:  10 \t {'10': 2, '01': 8}\n",
      "Measurement counts for initial angle:  120  and shots:  100 \t {'10': 22, '01': 78}\n",
      "Measurement counts for initial angle:  120  and shots:  1000 \t {'10': 222, '01': 778}\n"
     ]
    }
   ],
   "source": [
    "init_angle = 120        # in degrees\n",
    "no_of_shots = [1,10,100,1000]\n",
    "learn_rates = [0.03,0.19,0.9,2]   # increasing learn rates for lesser time for convergence to optimum\n",
    "\n",
    "for i in no_of_shots:\n",
    "    print(\"Measurement counts for initial angle: \",str(init_angle),\" and shots: \",str(i),\"\\t\",str(execute_circuit(init_angle,i)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Optimized parameter 'angle' in degrees:  89.99999999999886  ; initial parameters, angle: 120  and shots:  1 \t Resultant state counts:  {'10': 1}\n",
      "Optimized parameter 'angle' in degrees:  90.71720000000147  ; initial parameters, angle: 120  and shots:  10 \t Resultant state counts:  {'10': 6, '01': 4}\n",
      "Optimized parameter 'angle' in degrees:  89.05043999999889  ; initial parameters, angle: 120  and shots:  100 \t Resultant state counts:  {'10': 49, '01': 51}\n",
      "Optimized parameter 'angle' in degrees:  90.8033839999995  ; initial parameters, angle: 120  and shots:  1000 \t Resultant state counts:  {'10': 472, '01': 528}\n"
     ]
    }
   ],
   "source": [
    "# classical gradient descent optimization step: θ=θ−α⋅∇J(θ)\n",
    "#-----------------------------------------------\n",
    "# learning_rate = 0.00001\n",
    "max_i = 1000\n",
    "init_angle = 120\n",
    "\n",
    "for k,shots in enumerate(no_of_shots):\n",
    "    learning_rate = learn_rates[k]\n",
    "    angle = init_angle\n",
    "    for i in range(max_i):\n",
    "        counts = execute_circuit(angle,shots)\n",
    "    \n",
    "        try:\n",
    "            prob_avg_01 = counts['01']/shots\n",
    "        \n",
    "        except:\n",
    "            prob_avg_01 = 0\n",
    "    \n",
    "        try:\n",
    "            prob_avg_10 = counts['10']/shots\n",
    "        except:\n",
    "            prob_avg_10 = 0\n",
    "         \n",
    "        angle = angle - learning_rate*(costfunction(prob_avg_01,prob_avg_10))\n",
    "    print(\"Optimized parameter 'angle' in degrees: \",str(angle),\" ; initial parameters, angle:\",str(init_angle),\" and shots: \",str(shots),\"\\t\",\"Resultant state counts: \",str(counts))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Optimized parameter 'angle' in degrees:  89.99999999999886  ; initial parameters, angle: 120  and shots:  1 \t Resultant state counts:  {'01': 1}\n",
      "Optimized parameter 'angle' in degrees:  90.55760000000163  ; initial parameters, angle: 120  and shots:  10 \t Resultant state counts:  {'10': 4, '01': 6}\n",
      "Optimized parameter 'angle' in degrees:  88.83299999999915  ; initial parameters, angle: 120  and shots:  100 \t Resultant state counts:  {'10': 54, '01': 46}\n",
      "Optimized parameter 'angle' in degrees:  90.75191999999939  ; initial parameters, angle: 120  and shots:  1000 \t Resultant state counts:  {'10': 498, '01': 502}\n"
     ]
    }
   ],
   "source": [
    "#  NAG optimization step: V(t)=γV(t−1)+α.∇J( θ−γV(t−1) )\n",
    "#-----------------------------------------------\n",
    "max_i = 1000\n",
    "gama = 0.9\n",
    "V_t = 0\n",
    "\n",
    "for k,shots in enumerate(no_of_shots):\n",
    "    learning_rate = learn_rates[k]\n",
    "    angle = init_angle\n",
    "    for i in range(max_i):\n",
    "        counts = execute_circuit(angle,shots)\n",
    "    \n",
    "        try:\n",
    "            prob_avg_01 = counts['01']/shots\n",
    "        \n",
    "        except:\n",
    "            prob_avg_01 = 0\n",
    "    \n",
    "        try:\n",
    "            prob_avg_10 = counts['10']/shots\n",
    "        except:\n",
    "            prob_avg_10 = 0\n",
    "         \n",
    "        V_T = gama*V_t + learning_rate*(costfunction_NAG(prob_avg_01,prob_avg_10,gama,V_t))\n",
    "        angle = angle - V_T\n",
    "        V_T = V_t\n",
    "    print(\"Optimized parameter 'angle' in degrees: \",str(angle),\" ; initial parameters, angle:\",str(init_angle),\" and shots: \",str(shots),\"\\t\",\"Resultant state counts: \",str(counts))\n",
    "    \n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
