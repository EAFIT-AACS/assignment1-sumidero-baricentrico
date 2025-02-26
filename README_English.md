## team: 
- David Alejandro Gutiérrez Leal  
- Ginna Alejandra Valencia Macuace  
- Kadiha Muhamad Orta  

**Class Code:** 7308  
**Operating System:** Windows 10  

**Programming Language Used:** Python 3.12  

**Tools:** PyCharm 2024.2.4 / onlineGDB  

## **Execution Instructions:**  
To run the code, you must create or download a text file containing DFA examples in the specified format described in the document for this activity. The file should be saved in the same folder as the Python script, or alternatively, the full path should be provided in the `nombre_archivo` variable inside the `main()` function. Once this adjustment is made, execute the script in a Python 3-compatible environment. If the file is not found or has an incorrect format, the program will display an error message and terminate execution.  

## **Algorithm Explanation:**  
This implementation finds equivalent states in a Deterministic Finite Automaton (DFA) using partition refinement:  

1. **Partition Initialization:** States are divided into two groups: final states and non-final states.  

2. **Iterative Partition Refinement:**  
   - Each state is assigned a signature based on its transitions and which partition those transitions lead to.  
   - States with the same transition signatures remain in the same partition.  
   - If a state has transitions to different partitions compared to another state in the same partition, a new partition is created.  
   - This process repeats until the partitions no longer change.  

3. **Extraction of Equivalent States:**  
   - At the end of the partitioning process, states that remain in the same partition are considered equivalent.  
   - The algorithm outputs these pairs of equivalent states.  
