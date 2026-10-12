# DSA Peer Notes (transcribed)

Source: `CamScanner 06-10-2026 19.42.pdf` (25 handwritten pages, scanned images, no text layer).
Transcribed by Claude from page images for future agent reference. Handwriting was read visually; a few words may be slightly off. Pages 4-25 are rotated 90 degrees in the PDF.

**How to use:** these notes mix (a) C++ refresher material the lecturer covered in class that is NOT in the slides, and (b) condensed versions of slide Parts 01-08. Items tagged **[EXTRA]** are not in the lecture PDFs. Page-to-lesson mapping is at the bottom.

---

## Part 01: Introduction to Algorithms (pp. 1, 8-9)

- Algorithm: a finite, well-defined set of steps for solving a problem.
- A good algorithm should: be correct; be composed of a finite number of well-defined steps; produce output; terminate in finite time; be efficient.
- Program: an implementation of an algorithm using a programming language.
- Good program should: execute correctly; execute efficiently; be easy to read and understand; be easy to maintain.
- Pseudocode: a kind of structured English for specifying algorithms; cannot be compiled nor executed; no strict syntax rules; easy to read and understand; programming language independent.
- Pseudocode example (search): header `ALGORITHM search(REF list[] INTEGER, size INTEGER, target INTEGER, REF index INTEGER)`
  - REF = "passed by reference".
  - One line about the purpose: "finds target in unordered list".
  - PRE = conditions on input (list is an array with at least one element; size is number of elements; target contains integer to find).
  - POST = conditions on output (if found, index gives matching index).
  - RETURN = conditions on return values (true if found, otherwise false).
  - Statements are numbered and indented for clarity.
- Efficiency of an algorithm: amount of memory and time needed to run a program written with a particular algorithm. Determining efficiency: performance measurement -> experimental; performance analysis -> a-priori determination, **preferred**.

## [EXTRA] C++ refresher from class (pp. 1-8)

**Streams (p.1):** `<<` is the stream insertion operator; `cout` = "character out".

**Q&A (pp. 2-3):**
- Why does the OS need an exit status? It tells the OS whether the program succeeded or failed (e.g. Program A -> B -> C chain; status 0 = success, non-zero = failure stops the chain).
- Why a namespace? To prevent name collisions; lets different libraries use the same names safely. Two `void print();` in one scope is an error; `namespace A { void print(); }` and `namespace B { void print(); }` are fine, called as `A::print();` and `B::print();`.
- Which variables need explicit initialisation? Local: must be initialised. Global: automatically initialised. Static: automatically initialised, and retains its value between function calls.
- What if a variable is not initialised? Its value will be unpredictable.
- Garbage value: random leftover data in memory before you assign a value to a variable.
- Garbage collector: automatically frees memory that is no longer being used.
  - Pros: prevents memory leaks, safer, easier programming, better productivity.
  - Cons: slower execution, uses more memory, less control, unpredictable pauses.

**Extras (dated 2026/07/03) (p.3-4):**
- `sqrt` is a function in the `<cmath>` library.
- Array declaration: `int arr[] = {};`
- `continue`: loop control statement; skips the rest of the current iteration and immediately starts the next iteration. Makes code cleaner, improves readability, reduces nesting.
- `break`: immediately terminates loops; stops unnecessary work; useful for input validation; improves efficiency. To break out of all (nested) loops we can use either `return` or functions, according to the context.
- `exit(0)` is valid syntax but not recommended, as it may lead to data leaks.
- `#define`: preprocessor directive in C++; tells the preprocessor to perform text substitution before the actual compilation begins. Form: `#define NAME replacement`. Common uses: constants, macros. Advantages: simple text replacement, no run-time overhead. Disadvantages: no type checking, no scope, harder to debug, can produce unexpected output, makes code less readable.
- Ternary operator `condition ? true : false;` (called so because there are three operands). Pros: shorter code, better for simple assignments, can be used when a `const` needs to be initialised according to a condition.

**Pointers (pp. 5-9):**
- Pointers must be initialised, at least as a null pointer, otherwise unexpected results can occur.
  ```
  int *p = 0;   // null pointer
  int n = 5;    // pointer and the pointed type must be same
  p = &n;       // & = address-of operator
  cout << *p;   // 5   (* = value-at operator)
  ```
- If not initialised it becomes a **wild pointer**: points at garbage addresses.
- Need: modify variables from another function; dynamic memory allocation (`int *marks = new int[];`); efficiently working with arrays.
- Why does a pointer need a type? Because the compiler needs to know what type of data is stored at the address it points to.
- Pointer arithmetic: instead of changing the value stored in memory, it changes the memory address a pointer refers to. Used to move between memory locations. `int *p; p++;` moves to the next integer (+4 bytes), not one byte; `p--` likewise. char = 1 byte, int = 4 bytes, double = 8 bytes.
- Pointers and arrays: the array name represents the address of the first element. `arr` = `&arr[0]`; `int *p = arr;` accessing elements: `arr[0] == *(p)`.
- Passing arrays to functions: `int function(int arr[])` / `int function(int *arr)`; call `function(arr)`.
- Value parameters: a copy of the argument is passed. Reference parameters: create an alias for the original variable, e.g. `void change(int &x)` called as `change(x)`.
- Pointer parameters: instead of the variable, its address is passed: `(int *p)` called as `(&p)`. We need pointers even if we have reference because reference can't access null type; for nullable variables, nothing will happen with a pointer but an error will occur with a reference.
- We need reference even if we have value because: when an array is passed by value a separate copy is created, which is slow and uses extra memory; references are also useful when the function needs to modify the caller's variable.
- Default parameters: `void greet(string name, string role = "guest")`; `greet("pipuni", "admin")` -> "Hello pipuni: admin"; `greet("pipuni")` -> "Hello pipuni: guest".

**Program memory (p.6, dated 2026/07/10):**
- Code (compiled instructions) and global/static memory (global variables, static variables): exist for the program's lifetime.
- Stack: memory that the compiler manages automatically. Function calls, local variables. Fast, automatic, limited size. Lifetime: function lifetime.
- Heap: dynamic memory (`new`/`delete`), grows. Dynamic allocation.
- Initialise a dynamic variable at declaration: `int *p = new int(10);` then `delete p;`
- Memory leak: occurs when a program allocates memory but never releases it after it is no longer needed.
- Dynamic arrays: array whose size is determined at runtime. `int *arr = new int[n];` ... `delete[] arr;`
- `sizeof(p)` -> size of a pointer variable depends on the architecture, not on the type.

## Part 02: Space Complexity (pp. 10-12)

- Amount of memory that a program with a particular algorithm needs to run to its completion.
- Why important: to know whether available memory is enough to run the program written with our algorithm; prefer programs that consume less memory when there are several algorithms for a given problem; could estimate the largest problem that our algorithm can solve against the memory available.
- Components: 1. Instruction space; 2. Data space; 3. Environmental stack space.
- **Instruction space:** memory needed to load the compiled version of a program. Depends on: (1) compiler used (machine code created from same source can vary by compiler); (2) compiler options used, e.g. execution-time optimisation; (3) architecture of the target machine.
- **Data space:** memory needed to hold all the constants and variables of a program.
- **Environment stack space:** memory needed for the environment stack (runtime stack, call stack): a data structure that keeps information needed to resume execution of partially completed functions.
- Factors of space complexity: some factors are not known at the time of algorithm development.
  - **Insensitive factors** (insensitive to the problem being solved): (1) instruction space contribution; (2) data space contribution from literal constants, named constants and primitive variables; (3) environment stack space contribution from non-recursive functions.
  - **Sensitive factors** (sensitive to the problem being solved): (1) data space contribution from structured variables and dynamic memory allocation; (2) environment stack space contribution from recursive functions.
- Space complexity is a function of n (instance characteristic): **S(n) = c + S_A(n)**, where c is the insensitive (constant) space contribution and S_A(n) is the sensitive contribution, which is a function of instance characteristic n.
- **[EXTRA]** Data type sizes in bytes:

| Type | 16-bit | 32-bit | 64-bit |
|---|---|---|---|
| char | 1 | 1 | 1 |
| bool | 1 | 1 | 1 |
| short | 2 | 2 | 2 |
| int | 2 | 4 | 4 |
| long | 4 | 4 | 8 |
| float | 4 | 4 | 4 |
| double | 8 | 8 | 8 |
| pointer | 2 | 4 | 8 |

## Part 03: Time Complexity (pp. 13-14)

- Amount of time that a program written with a particular algorithm needs to run to its completion.
- Why interested: some problems require a real-time response to their solution; will prefer the program that runs fast when there are several algorithms for a given problem; to guarantee the users that the program written with our algorithm can run to its completion without any time-out.
- Factors of time complexity: depends on factors that the space complexity depends. **T(n) = c + T_A(n)**.
- Determining time complexity, two approaches: 1. Operation count; 2. Step count.
- **Operation count approach:** identify one or more key operations of the algorithm. Time complexity is estimated by determining the number of times these key operations are performed.
- **Step count approach:** estimated by accounting the time spent for all program steps; estimated by determining the number of steps that the program takes to complete.
- Weaknesses of the operation count approach: doesn't measure actual execution time; choosing the key operation may be difficult.
- Programming instrumentation: the process of modifying a program by adding extra code to collect information about its execution.

## Part 04: Time Analysis (pp. 14-16)

- Running times:
  - Best case: time taken when the best possible thing happens.
  - Worst case: time taken when the worst possible thing happens.
  - Average case: time taken for some probability distribution of instance characteristic n.
- Functions of time complexity: n is always positive; T(n) >= 0 for all n.
- Why interested: would like to know whether the algorithm becomes reasonably or incredibly slow when the problem grows.
- Linear function: y = mx + c, e.g. sequential search.
- Logarithmic function: x^y = m, i.e. log_x(m) = y, e.g. binary search. **Binary search is more efficient than sequential search.** (Sketches of linear, logarithmic, linear-logarithmic and quadratic growth curves are drawn on p.15.)
- Asymptotic notation: expresses an algorithm's running time as its growth rate by dropping the less significant terms and constant coefficients. Done to make equations simple. Growth rate: how fast the function grows with the input size.
- **Big-O notation:** asymptotic notation for the worst-case running time of an algorithm. Definition: for T(n) >= 0 and f(n) >= 0, T(n) is said to be O(f(n)) if there exist positive constants c and n0 such that T(n) <= c f(n) for all n >= n0.

## Part 05: Data Structures (pp. 16-17)

- Atomic data type: a set of non-decomposable data. Consists of a set of homogeneous data and a set of operations that can be performed on data (primitive, elemental).
- Composite data type: a set of decomposable data, composed using atomic and composite data types; could consist of a set of homogeneous or heterogeneous data.
- Data structure: a structure that holds a set of atomic or composite data. Consists of a set of homogeneous or heterogeneous data and a set of operations that can be performed on data.

## Part 06: Stacks (pp. 17-19)

- A linear data structure. All data additions (push) and removals (pop) are restricted to one end (top). Last in, first out (LIFO).
- Error conditions: Overflow (trying to push onto a full stack); Underflow (attempting to pop from an empty stack).
- Array-based stack: conceptual (vertical stack with top) vs physical (array with a `size` and a `top`). Operations: create(), destroy(), isEmpty(), isFull(), push(), pop().
- Note: an array-based stack requires a predefined maximum capacity, even if the entire capacity is not used. This wasted memory can be avoided in most cases with linked lists that can grow and shrink dynamically during runtime.
- Linked list-based stack: `top` points to the head node; each node points to the one below; the bottom node points to null. Operations: create(), destroy(), isEmpty(), push(), pop().
- Stack applications: reversing data; converting numbers; parsing data; converting mathematical expressions; evaluating mathematical expressions; backtracking.

## Part 07: Queues (pp. 19-21)

- A linear data structure. Data additions are restricted to one end and removals can only be done from the other end. FIFO. Error conditions: overflow, underflow. Operations: enqueue(), dequeue().
- Array-based queue. Global variables: `count` = number of elements; `front` = index of the first element; `rear` = index of the element after the last one; `size`. When `front = rear` the queue is full or empty (hence `count`).
  - Operations: create(queueSize), destroy(), isFull(), isEmpty(), enqueue(data), dequeue(&data).
  - After enqueue: `rear <- rear MOD size`; after dequeue: `front <- front MOD size` (the MOD is to maintain the circular nature of an array; note: rear/front are incremented before the MOD).
- Linked list-based queue: `front` points to first node, `rear` to last node (e.g. front -> [a] -> [b] <- rear, last node's next is null).
  - Global variables: `Type node: data DATATYPE, next POINTER to node. END node.` `front POINTER to node, rear POINTER to node.`
  - Operations: create(), destroy(), isEmpty(), enqueue(data), dequeue(&data). Notation: `p->data = d` is the same as `(*p).data = d`.
- Queue applications: process scheduling in OS; printer spooling; network traffic handling; many other data processing and service providing applications.

## Part 08: Trees (pp. 22-25)

- Tree: a set of nodes that holds atomic or composite data. Nodes are connected to other nodes with edges. Terms: Root, Leaf. Order: maximum child nodes a node can have.
- Binary tree: a tree with an order of two. A finite set of elements partitioned into three subsets: root, left subtree, right subtree.
- Binary tree traversal: visiting each node of a binary tree once and only once.
  1. **Preorder** (each node is visited when it is traversed): visit the root; traverse the left subtree in preorder; traverse the right subtree in preorder.
  2. **Inorder** (each node is not visited till its left subtree is traversed): traverse the left subtree in inorder; visit the root; traverse the right subtree in inorder.
  3. **Postorder** (each node is not visited until both of its subtrees are traversed): traverse the left subtree in postorder; traverse the right subtree in postorder; visit the root.
- Binary search tree: a binary tree in which data in any node of the left subtree is less than that of the root; data in any node of the right subtree is greater than or equal to that of the root; each subtree itself is a binary search tree. When a BST is traversed in inorder it becomes a sorting algorithm.
- Array-based trees: root of the tree is at index 1; left child of node n is 2n; right child of node n is 2n+1.
  - Problem with array-based trees: for a balanced tree of height h, 2^(h+1) - 1 nodes must be there. Example: 1033 slots... (page reads "1033"; likely 1023 = 2^10 - 1 for h = 9). Assume the tree is highly unbalanced, only 10 nodes will be used; the memory allocated to the rest will never be used.
  - Even so this is a valid option if the tree is balanced, and also if it doesn't change the maximum height and you know the maximum height.
  - If there are duplicated values it is taken as the right child.
- Tree applications: represent hierarchically related data (maintaining folders and files; maintaining a land registry); represent mathematical expressions (expression trees: every mathematical expression can be divided into operands and operator; root is operator, children are operands, leaf nodes are operands); support data compression and encoding; efficiently search large dynamic sets of data.
- Binary search can only be done when the array is sorted, so it is not efficient if we have to insert and delete data, because we have to shift data to maintain the sorted state. Here trees are efficient (linked list: insertions and deletions are efficient, just change one pointer set). But searching in a linked list is not efficient. So a linked-list-based binary search tree is very efficient for this specific scenario.

---

## Page map

| PDF pages | Content | Lesson |
|---|---|---|
| 1 | Part 01 basics + `<<`/cout | 01 |
| 2-3 | C++ Q&A (exit status, namespace, init, garbage) | 01 [EXTRA] |
| 3-8 | continue/break, #define, ternary, pointers, memory, params, pseudocode intro | 01 [EXTRA] |
| 8-9 | Pseudocode example, efficiency | 01 |
| 10-12 | Space complexity (+ data type size table) | 02 |
| 13-14 | Time complexity, operation/step count | 03 |
| 14-16 | Time analysis, growth functions, Big-O | 04 |
| 16-17 | Atomic/composite data types, data structure | 05 |
| 17-19 | Stacks | 06 |
| 19-21 | Queues | 07 |
| 22-25 | Trees | 08 |
