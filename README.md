# A-Star-Search-Algorithm

Run the program by navigating to the directory with the astar.py file and execute the
following command:
```
python3 astar.py
```
Once running, the program will prompt the user to select a heuristic function or analysis
option:
```
Enter a number to select a heuristic
1: Straight Line Distance 2: Manhattan Distance
3: Sum of first two heuristics 4: Average of first two heuristics
5: Run and analyze all heuristics')
Heuristic selected:
```

Enter a number and hit Enter to submit the input to the program. The program only runs one
function at a time after input, requiring the user to restart these steps to select another
function to perform.

<h2>Analyzing Output</h2>
<p>A) If a user selects an individual heuristic, the program will iterate over each of the 10
predetermined routes and display the expanded nodes (path travelled), the optimal path for
each route, as well as whether or not the path searched using that heuristic is optimal.</p>
<p>B) If a user selects the heuristic analysis option, the previous output A is displayed for each
heuristic, and a graph is generated with the results (example shown in Results section). The
graph is saved in the same directory as the main program astar.py file with the title
results.png.</p>
