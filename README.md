# Vacuum Cleaner Robot Implementation

## **Members**
- **Jonathan Thom** : BIT/21/SS/030  
- **Bischof Nkhata** : BIT/21/SS/028  
- **Peter Zimba** : BIT/21/SS/031  

## **Introduction**
This project implements an AI-based Vacuum Cleaner Robot that autonomously moves between rooms to clean them. The robot follows a predefined logic to check the state of a room (dirty or clean), clean (suck) it if necessary, and then move to the next room.

The project is divided into two tasks:

1. **Task 1:** Implementation of a simple vacuum cleaner in a two-room environment.
2. **Task 2:** Extension of the implementation to multiple rooms, floors, and additional constraints.

---

## **Task 1: Simple Vacuum Cleaner Robot**
The objective of Task 1 was to simulate a Vacuum Cleaner AI Agent that operates in a simple environment consisting of two rooms. The agent detects whether a room is dirty or clean and acts accordingly.

### **1.1 Is the Robot Rational?**
Yes, it is rational because it manages to:  
- **Perceive its environment** (checks if a room is dirty).  
- **Take an appropriate action** (cleans the dirty room).  
- **Move out of the room** if it finishes cleaning.  

### **1.2 Implementation Approach**
Two levels have been implemented:

#### **Easy:**
The agent is initialized with a predefined environment state.   
  -Below is a codespace link for the easy task program;  
    https://bug-free-space-palm-tree-vx97769j6jx266q.github.dev/

#### **Hard:**
The agent is given random inputs from a text file with about 300 lines. Data is extracted line by line for the agent.  
  -Below is a codespace link for the Hard task program;  
    https://bug-free-space-palm-tree-vx97769j6jx266q.github.dev/

### **1.5 Results**
- The agent is able to check if the room is dirty or not.  
- The robot successfully cleans the dirty room and skips already clean rooms.  
- The robot moves between two rooms efficiently.  

---

## **Task 2: Multi-Room & Multi-Floor Vacuum Cleaner Robot**
This task extends the Vacuum Cleaner AI to handle multiple rooms, floors, and additional constraints:

1. A corridor-based movement system where the robot follows a structured path.  
2. Time-based simulation where the agent records the time it takes to clean a specific room.  
3. Multi-floor navigation, including stairs.  
4. Dynamic room availability, where some rooms are occupied or unavailable.  
5. A learning component, allowing the robot to predict which rooms are most likely to get dirty.  

### **2.2 Environment Representation**
The environment is represented using a **nested dictionary**, where:  
- Each **key** represents a room.  
- Each **value** represents its cleanliness state.  
- Empty values indicate clean rooms.  
- Asterisks (`*`) indicate dirty rooms (more `*` means more dirt).  

### **2.3 Implementation Approach**
1. **Building Representation:** A nested dictionary where each floor contains rooms with cleanliness states.  
2. **Two Implementation Methods:**  
   - **Hardcoded Dictionary:** Uses `empty` (clean) or `*` (dirty).      
        -Codespace link for Task 2 first implementation program;      
         https://bug-free-space-palm-tree-vx97769j6jx266q.github.dev/
      
   - **Randomly Generated Status:** Assigns a dirtiness score from `0` (clean) to `10` (very dirty).    
       -Codespace link for Task 2 second implementation program;   
         https://bug-free-space-palm-tree-vx97769j6jx266q.github.dev/

3. **Time-based simulation** tracks cleaning duration.  
4. **Room occupation status** (`free`, `occupied`, `makeup class`).  

### **2.4 Results**
- The robot successfully navigates multiple floors.  
- Cleaning time varies based on room dirtiness.  
- The agent avoids occupied rooms.  
- It skips rooms scheduled for makeup classes.  
- Each iteration assigns random room statuses.  

---

## **Conclusion**
This project demonstrates the implementation of an AI-based Vacuum Cleaner Robot with increasing complexity:

1. **Task 1** introduces a basic rational AI agent for two rooms.  
2. **Task 2** extends it to multiple rooms, floors, and real-world constraints.  

The robot efficiently cleans rooms, avoids obstacles, and minimizes time, making it a rational and effective AI agent.  

