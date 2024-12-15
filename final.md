# *Gatle: Gamifying Quantum Mechanics* 

* Project Name: *Gatle*

* Name (with Student ID): *Write Names of All Group Members*

## Objectives  
This project aims to implement a puzzle-style game similar to Wordle.  
The goal is to gamify the principles of quantum computing to make them easier to understand.  
1. **Quantum Entanglement**  
2. **Quantum Superposition**  

The game will utilize the Godot engine to visualize the quantum circuit UI and simulation results.  
Like Wordle, it will rely on an API server to provide game data.

---

## Game Design  

Wordle is a game where users guess a 5-letter word in a format similar to the game of baseball.  
We reinterpret Wordle by incorporating the core mechanisms of quantum computing into the gameplay.  

### Game Rules  
- The user designs quantum circuits using the UI.  
- After executing the circuit, the observation results are compared with the **answer bits** provided by the server.  
- Based on the results, the user adjusts the circuit and works towards identifying the correct answer.  

### Game Data  
The following information is generated daily by the server based on a unique Seed value:  
1. **Number of Bits ($n_{\text{bits}}$)**: Determines the game size (4 ~ 8).  
2. **Initial Qubit Values**: Randomly selected from $|0\rangle, |1\rangle, |+\rangle, |-\rangle$.  
3. **Answer Bits**: A list of $n_{\text{bits}}$ composed of $0$ and $1$, used for comparison with observation results.  

---

### Gameplay Flow  
1. **Placing Gates**  
   Users can add or modify gates on the circuit using the UI.  

2. **Executing the Circuit and Returning Results**  
   - Press the Submit button to send the circuit configuration to the server.  
   - The server simulates the quantum circuit and returns an array of $n_{\text{bits}}$ consisting of $0$s and $1$s as observation results.  
   - Due to quantum superposition, different results may be returned with each attempt.  

3. **Comparing Results and Providing Feedback**  
   The observation results are compared **element-wise** with the server’s answer bits:  
   - **Match** ($1$): Displayed in green.  
   - **Mismatch** ($0$): Displayed in red.  

4. **Iteration and Deduction**  
   The user modifies the circuit based on the feedback and executes it again to gradually approach the correct answer.  

---

## Result  

<Insert Game Screenshot>  

- **Left Side**: The circuit UI where gates can be placed.  
- **Right Side**: A list of available gates.  
- **Submit Button**: Used to check the results.  
- Available gates: $X, Y, Z, H$, and control gates (example $CNOT$).  

---

### Black Box  
The black box is a game feature simulating quantum entanglement, where the user cannot observe the internal circuit.  
- It is represented as a black box of size $n \times m$, internally consisting of a pre-designed quantum circuit.  
- Users must place gates before and after the black box to resolve the entangled state.  

**Note**:  
This feature is not implemented in the current demo.  
The black box will be implemented by hiding the pre-designed circuit and allowing gate placement in specific locations.  

---

## Scenario  

**Example Game Conditions**:  
- $n_{\text{bits}} = 3$, answer bits: $100$.  
- Assume the user designs a circuit and executes it, producing the following probabilities for observation results.  

**Observation Scenarios**:  
1. $000 \rightarrow 011$  
2. $010 \rightarrow 001$  
3. $100 \rightarrow 111$  
4. $111 \rightarrow 100$  


## Remarks
주목


## References
레퍼런스