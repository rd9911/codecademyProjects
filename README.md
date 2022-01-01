# codecademyProjects
Projects finished during learning thru Codecademy during 2020.

## Algorithms


### Blossom - easy access to information of your favorite flowers.
- Hash map is used in order to connect names of flowers to their meanings.
- Linked list data sctructure used thru separate chaining to avoid collisions.
- 2 main features: assign (assiggn hash value when linked list is added) & retrieve(get meaning nased on user input)

### SkyRoute - find your underground route.
- Finding a route from point A to point B by using breadth-first, and depth-first algorithms.
- Assuming that it takes the same amount of time to get from each station to each of its connected neighboring stations.
- Has 3 features:
    1. Get route from a user input: starting and ending stations.
    2. Checking whether the given route is possible in a condition when some stations are under construction with the help of depth-first-search algorithm.
    3. If there is no stations under the construction, then find the shortest route among the all possible routes with a help of breadth-first seach.

### Sorted Tale - sorting beyond the limitations of tima and space.
- Sorting books by author name, title, number of charachters in the title, or reverse of the authors' name using bubble sort, or quick sort (whichever requires shorter time).
- Main features:
    1. Load books.
    2. Get the sorting type.
    3. Sort it by using the chosen sorting algorithm.


## Data Structures

### Tower of Hanoi - can you move the tower?
- Stack disks should be moved from left to rigt based on 3 rules:
    1. Move only one disk at a time.
    2. Move only upper disk and place it on top of another disk or empty rod.
    3. Only smaller disks can be placed on top of another disk.
- The game is implemented with stack data structure and has simple I/O functions such as:
    1. Choosing which stack to move
    2. Choosing to which rode to move 
    3. The program will check validity of the move and either moves the disk or warns about the invalid move.
    3. Giving the result and  optimal number of moves for comparison.

### Wilderness Escape - choose your own destiny.
- Adventure game based on user input that are limitedto 1 and 2.
- Monitor user input and paths by implementing tree data structure.


## Object-orient programming

### Pokemon - CLI based pokemon game.
- Pokemon fighting game based on CLI user inputs.
- Main features:
    1. Stats of pokemon such as experience, and health.
    2. Unique abilities of each pokemon in attacking.
    3. Attack command.
    4. Updating stats of the pokemon based on result of the fight.