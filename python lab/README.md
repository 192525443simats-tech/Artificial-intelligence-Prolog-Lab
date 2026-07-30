1. 8-Puzzle Problem
Start.
Input the initial state and goal state.
Create OPEN and CLOSED lists.
Add the initial state to the OPEN list.
Remove the first state from OPEN.
Check whether it is the goal state.
If the goal is reached, display the solution.
Otherwise, generate all possible valid moves.
Add new states to the OPEN list.
Repeat until the goal is found.
Stop.

2. 8-Queen Problem
Start.
Place the first queen in the first row.
Check all columns for a safe position.
Place the queen if the position is safe.
Move to the next row.
If no safe position exists, backtrack.
Repeat until all eight queens are placed.
Display the solution.
Stop.

3. Water Jug Problem
Start.
Initialize both jugs as empty.
Fill one jug.
Pour water into the other jug.
Empty a jug if required.
Repeat filling, pouring, and emptying operations.
Continue until the required quantity is obtained.
Display the solution.
Stop.

4. Crypt-Arithmetic Problem
Start.
Read the arithmetic expression.
Assign unique digits to each letter.
Check whether the assignment satisfies the equation.
If valid, display the solution.
Otherwise, try another assignment.
Repeat until the solution is found.
Stop.

5. Missionaries and Cannibals Problem
Start.
Initialize missionaries, cannibals, and boat.
Generate valid boat movements.
Check that missionaries are never outnumbered.
Move the boat across the river.
Repeat until everyone reaches the destination.
Display the solution.
Stop.

6. Vacuum Cleaner Problem
Start.
Check the current room.
If the room is dirty, clean it.
Otherwise, move to the next room.
Repeat until all rooms are clean.
Display the final state.
Stop.

7. Breadth First Search (BFS)
Start.
Create an empty queue.
Insert the starting node.
Remove the front node from the queue.
Visit the node.
Add all unvisited neighbouring nodes.
Repeat until the queue is empty.
Stop.

8. Depth First Search (DFS)
Start.
Create an empty stack.
Push the starting node.
Pop the top node.
Visit the node.
Push all unvisited neighbouring nodes.
Repeat until the stack becomes empty.
Stop.

9. Travelling Salesman Problem
Start.
Input the cities and distances.
Generate all possible routes.
Calculate the total distance for each route.
Compare all distances.
Select the shortest route.
Display the result.
Stop.


10. A* Algorithm
Start.
Insert the start node into the OPEN list.
Select the node with the lowest cost.
Check whether it is the goal node.
Generate neighbouring nodes.
Update the cost values.
Repeat until the goal is reached.
Display the shortest path.
Stop.

If your lab asks for a Feed Forward Neural Network in Python, here's a simple program using scikit-learn (no TensorFlow required).

First install the required package (if not already installed):

py -m pip install scikit-learn
Python Code (feed_forward_nn.py)
from sklearn.neural_network import MLPClassifier

# Training data (XOR)
X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

y = [0, 1, 1, 0]

# Create Feed Forward Neural Network
model = MLPClassifier(
    hidden_layer_sizes=(4,),
    activation='logistic',
    solver='adam',
    max_iter=5000,
    random_state=42
)

# Train the model
model.fit(X, y)

# Test data
test_data = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

# Predict
predictions = model.predict(test_data)

print("Feed Forward Neural Network Predictions:")
for i in range(len(test_data)):
    print(f"{test_data[i]} -> {predictions[i]}")
Expected Output
Feed Forward Neural Network Predictions:
[0, 0] -> 0
[0, 1] -> 1
[1, 0] -> 1
[1, 1] -> 0

If you get an error like:

ModuleNotFoundError: No module named 'sklearn'

run:

py -m pip install scikit-learn

If your lab manual specifically says "Implement Feed Forward Neural Network using TensorFlow/Keras", let me know. Since you're using Python 3.14, I'll show you how to use a compatible Python version for that experiment.

from 1 to 16 give pseudo code

Sure! Below is the pseudocode for Experiments 1–16 in a simple format suitable for writing in your AI lab record.

1. 8-Puzzle Problem

Pseudo Code

Start
Input initial state and goal state
Create OPEN and CLOSED lists
Add initial state to OPEN
While OPEN is not empty
    Remove first state from OPEN
    If state is goal
        Display solution
        Stop
    Generate all possible moves
    Add valid states to OPEN
    Move current state to CLOSED
End While
Stop
2. 8-Queen Problem

Pseudo Code

Start
Place queens row by row
For each row
    Check each column
    If position is safe
        Place queen
        Move to next row
    Else
        Try next column
If all queens are placed
    Display solution
Else
    Backtrack
Stop
3. Water Jug Problem

Pseudo Code

Start
Initialize both jugs as empty
Repeat
    Fill a jug
    Empty a jug
    Pour water from one jug to another
Until required amount is obtained
Display solution
Stop
4. Crypt-Arithmetic Problem

Pseudo Code

Start
Input the arithmetic equation
Assign unique digits to letters
Check if assignments satisfy equation
If valid
    Display solution
Else
    Try another assignment
Repeat until solution found
Stop
5. Missionaries and Cannibals Problem

Pseudo Code

Start
Initialize missionaries, cannibals and boat
Move people across river
Check safety condition
If missionaries are safe
    Continue
Else
    Backtrack
Repeat until goal state
Display solution
Stop
6. Vacuum Cleaner Problem

Pseudo Code

Start
Check current room
If room is dirty
    Clean room
Else
    Move to next room
Repeat until all rooms are clean
Stop
7. Breadth First Search (BFS)

Pseudo Code

Start
Create queue
Insert starting node
While queue is not empty
    Remove front node
    Visit node
    Add unvisited neighbours to queue
End While
Stop
8. Depth First Search (DFS)

Pseudo Code

Start
Create stack
Push starting node
While stack is not empty
    Pop top node
    Visit node
    Push unvisited neighbours
End While
Stop
9. Travelling Salesman Problem

Pseudo Code

Start
Input cities and distances
Generate all possible routes
Calculate total distance
Find minimum distance
Display shortest route
Stop
10. A* Algorithm

Pseudo Code

Start
Add start node to OPEN list
While OPEN is not empty
    Select node with lowest cost
    If goal reached
        Display path
        Stop
    Generate neighbouring nodes
    Update costs
End While
Stop
11. Map Coloring using CSP

Pseudo Code

Start
Input map and colors
Assign color to first region
Check neighbouring regions
If conflict occurs
    Try another color
Repeat until all regions are colored
Display solution
Stop
12. Tic Tac Toe Game

Pseudo Code

Start
Create empty board
Repeat
    Player enters move
    Update board
    Check winner
    Switch player
Until game ends
Display result
Stop
13. Minimax Algorithm

Pseudo Code

Start
Generate all possible moves
Evaluate each move
Choose maximum score for AI
Choose minimum score for opponent
Repeat recursively
Display best move
Stop
14. Alpha-Beta Pruning

Pseudo Code

Start
Initialize Alpha and Beta
Generate possible moves
Update Alpha and Beta values
Prune unnecessary branches
Continue search
Display best move
Stop
15. Decision Tree

Pseudo Code

Start
Load dataset
Split data into training and testing sets
Train Decision Tree model
Predict test data
Evaluate accuracy
Display prediction and accuracy
Stop
16. Feed Forward Neural Network

Pseudo Code

Start
Load training dataset
Initialize network weights
Perform forward propagation
Calculate error
Update weights
Repeat until training completes
Test the network
Display prediction
Stop

These pseudocodes are written in a simple, lab-record style and are suitable for your AI laboratory manual.

give points wirh numbers

Here are the pseudocodes for Experiments 1–16 in numbered points, which are easy to write in your record.

1. 8-Puzzle Problem
Start.
Input the initial state and goal state.
Create OPEN and CLOSED lists.
Add the initial state to the OPEN list.
Remove the first state from OPEN.
Check whether it is the goal state.
If the goal is reached, display the solution.
Otherwise, generate all possible valid moves.
Add new states to the OPEN list.
Repeat until the goal is found.
Stop.
2. 8-Queen Problem
Start.
Place the first queen in the first row.
Check all columns for a safe position.
Place the queen if the position is safe.
Move to the next row.
If no safe position exists, backtrack.
Repeat until all eight queens are placed.
Display the solution.
Stop.
3. Water Jug Problem
Start.
Initialize both jugs as empty.
Fill one jug.
Pour water into the other jug.
Empty a jug if required.
Repeat filling, pouring, and emptying operations.
Continue until the required quantity is obtained.
Display the solution.
Stop.
4. Crypt-Arithmetic Problem
Start.
Read the arithmetic expression.
Assign unique digits to each letter.
Check whether the assignment satisfies the equation.
If valid, display the solution.
Otherwise, try another assignment.
Repeat until the solution is found.
Stop.
5. Missionaries and Cannibals Problem
Start.
Initialize missionaries, cannibals, and boat.
Generate valid boat movements.
Check that missionaries are never outnumbered.
Move the boat across the river.
Repeat until everyone reaches the destination.
Display the solution.
Stop.
6. Vacuum Cleaner Problem
Start.
Check the current room.
If the room is dirty, clean it.
Otherwise, move to the next room.
Repeat until all rooms are clean.
Display the final state.
Stop.
7. Breadth First Search (BFS)
Start.
Create an empty queue.
Insert the starting node.
Remove the front node from the queue.
Visit the node.
Add all unvisited neighbouring nodes.
Repeat until the queue is empty.
Stop.
8. Depth First Search (DFS)
Start.
Create an empty stack.
Push the starting node.
Pop the top node.
Visit the node.
Push all unvisited neighbouring nodes.
Repeat until the stack becomes empty.
Stop.
9. Travelling Salesman Problem
Start.
Input the cities and distances.
Generate all possible routes.
Calculate the total distance for each route.
Compare all distances.
Select the shortest route.
Display the result.
Stop.
10. A* Algorithm
Start.
Insert the start node into the OPEN list.
Select the node with the lowest cost.
Check whether it is the goal node.
Generate neighbouring nodes.
Update the cost values.
Repeat until the goal is reached.
Display the shortest path.
Stop.
11. Map Coloring using CSP
Start.
Read the map and available colors.
Select a region.
Assign a color.
Check neighbouring regions for conflicts.
If a conflict occurs, choose another color.
Repeat until all regions are colored.
Display the colored map.
Stop.

12. Tic Tac Toe Game
Start.
Create an empty game board.
Allow Player X to make a move.
Update the board.
Check for a winner or draw.
Switch to Player O.
Repeat until the game ends.
Display the result.
Stop.

13. Minimax Algorithm
Start.
Generate all possible moves.
Evaluate each move.
Find the maximum score for the AI.
Find the minimum score for the opponent.
Continue recursively.
Select the best move.
Display the result.
Stop.

14. Alpha-Beta Pruning
Start.
Initialize Alpha and Beta values.
Generate all possible moves.
Update Alpha and Beta values.
Prune unnecessary branches.
Continue until the search is complete.
Select the best move.
Display the result.
Stop.

15. Decision Tree
Start.
Load the dataset.
Split the data into training and testing sets.
Train the Decision Tree model.
Test the model with sample data.
Predict the output.
Display the prediction and accuracy.
Stop.

16. Feed Forward Neural Network
Start.
Load the training dataset.
Initialize the network weights.
Perform forward propagation.
Calculate the error.
Update the weights.
Repeat until the model is trained.
Test the trained network.
Display the predicted output.
Stop.
