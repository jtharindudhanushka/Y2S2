# DSA Peer Notes Set 2 (transcribed)

Source: `DSA.pdf`, 63 handwritten pages (scanned, no text layer). Transcribed by Claude from page images for future agent reference. Only what is visible on the page is recorded; unclear items are flagged. Page numbers are PDF pages.

**Status:** all 63 pages read. Pages 1-29 (Parts 01-03 + C++ examples) are in the first section; pages 30-63 follow. Item flagged "(unclear)" could not be read confidently.

---

## Pages 1-29: Parts 01-03 with C++ worked examples

### Part 01 recap (pp. 1-2)
Same as slides: algorithm = finite well-defined set of steps; can be more than one algorithm per problem; good algorithm: correct, finite well-defined steps, produces output, terminates in finite time, efficient. Program = implementation of an algorithm in a programming language; good program: executes correctly, executes efficiently (within resource constraints), easy to read and understand, easy to maintain. Pseudocode bullets as on slides. Efficiency = memory and time needed to run a program written with a particular algorithm; used to pick the most appropriate one; determining efficiency = performance measurement, performance analysis.

### C++ refresher examples (pp. 3-18)
- **Smallest compilable C++ program (p.3):** `int main() { return 0; }`. Windows `echo %ERRORLEVEL%` shows the returned value (0). Flow: `test.cpp` → `test.exe`; OS calls `main`; main calls other functions; main returns an exit status to the OS.
- **Antivirus example of exit status:** `scan.exe test.exe` returns 0 = no virus, 1 = virus found → antivirus then runs `clean.exe test.exe` (0 = cleaned, 1 = clean failed) → then `quarantine.exe test.exe`.
- **Logical operators (p.3):** short circuit `&&`, `||`, `!` versus full evaluation (both sides evaluated) `&`, `|`, `~`. `if (expression1 && expression2)`.
- **Why full evaluation (p.4):** bitwise: change the last bit without affecting others, bit-to-bit manipulation. Example `10101010 | 00000001 → 10101011`.
- All global variables are automatically initialised. Uninitialised values are garbage values (page writes "Garbage collector"; the term for leftover random values is garbage value). "State in between local & global" (the static variable).
- **Return code 136 → division by zero error** (p.5).
- **Static example (p.5):** `void counter() { int count; count++; cout << count << "\n"; }` (uninitialised local, unpredictable) versus `static int count;` (initialised once). With `pollutateMemory()` first writing `int garbage = 999;` then calling `counter()` twice: static version prints 1, 2, 3 across calls (initialised once, keeps value); the plain-local version printed values like 1000, 1001, 1002 (it picked up leftover garbage). Use initialised variables, otherwise you get varying values because of garbage values.
- **continue (p.6):** array `{1, -4, 9, 16, -25}`, printing `num[i]` and `sqrt(num[i])`. Without a check, negatives print `-nan` (not a number). Small change: `if (num[i] < 0) continue;` skips them; output: 1 1, 9 3, 16 4.
- **break (pp. 6-7):** PIN checking array `{1234, 3456, 5678, 7890, 9012}`, target 5678; loop prints "Checking" until match, then "PIN is valid" and `break`. "break: exit from the loop, but not from all the loops, only from the inner loop." With `attempts = 3` outer loop and inner loop over pins: `break` exits the inner loop only; `return 0;` exits the entire program (exits inner and outer loop).
- **return in void function (p.8):** `void printSqrt(int n) { if (n < 0) return; cout << n << "\t" << sqrt(n) << "\n"; }` ("stop function and exit"). Output for the same array: 1 1, 9 3, 16 4.
- **checkPins example (p.9):** `void checkPins(int P[], int s, int a, int t)` with nested loops over attempts and size; prints "Checking" or "PIN valid" then `return;`. Numbered circles show the execution order (main first: 1 main, 2 array, 3 variables, 4 call, ... ). Not fully legible (unclear).
- **#define vs const (p.10):** `#define PI 3.14`: speciality = no memory allocation; useful because if a new value is needed, only one line changes instead of multiple lines. `const float pi = 3.14;` is the same idea but takes a memory allocation (memory use). During compilation PI is translated into 3.14 (circumference example `c = 2 * PI * r`).
- **Why constants (p.11):** variables can be assigned values at any time, so you may accidentally change values in the middle of the code; that is why constants are used for fixed values.
- **Conditional (ternary) operator (p.11):** `int inCity = 1; // in city 1, out of city 0` then `const int speed = inCity ? 30 : 70;` prints "Speed is 30 kmph".
- **Pointers (p.11):** a pointer can hold a memory address. `int *p = 0;` (zero = null pointer: points nowhere); `int n = 5; p = &n;` then `cout << n` → 5, `&n` → address (example 0xDEADBA11), `p` → same address, `*p` → 5. Diagram: box p holds the address, an arrow "points to" box n containing 5.
- **Wild pointers (p.12):** `int *p; cout << *p; *p = 999;` p holds a garbage address (e.g. 0x0BADDD11) and could point to any memory location. Always initialise pointers. Dynamic version: `int *p = 0; p = new int;` p now holds a real address (e.g. 0x0000CAFE) pointing to a 32-bit box; `*p = 999;` prints 999; `cout << p` prints the address.
- **Four segments of memory (p.13):**

| Segment | Notes |
|---|---|
| Text | keeps the code |
| Data | keeps inputs, outputs and global variables; lifetime = full life of the program; a `static` variable goes here |
| Stack | small (a few megabytes), fast; created when a function is called and destroyed after the function; memory allocations are automatic |
| Heap | large; memory management by you; allocation and deallocation are slow; lifetime decided by the programmer |

  `int *p = new int(999); cout << *p;` (999) `*p = 1000;` (1000).
- **Memory leak and delete (p.14):** `void leakMemory() { int *p = new int(999); cout << *p; delete p; return; }`. Dynamic array: `int size; cin >> size; int *arr = new int[size];` release with `delete [] arr;`. Diagram: arr holds an address pointing to a block of boxes indexed 0-4. sizeof pointers: `char *a`, `int *b`, `float *c` → `sizeof` each prints 8 (on a 64-bit machine every pointer is 8 bytes).
- **Dynamic marks example (p.15):** read n; `int *marks = new int[n];` loop `cin >> marks[i]` with prompt "Marks of student i+1".
- **Pointer arithmetic (p.15):** `int n = 5; int *p = &n;` printing `p`, `p+1`, `p-1` gives 0x7ffd4294f5f4, ...f8, ...f0 (steps of 4 bytes for int). Array via pointer: `arr` holds address (0x0BADCAFE) of array `{2, 4, 8}` (indexes 0-2). `&arr[0]` = that address; `arr` = same address; `arr[0]` = 2; `*arr` = 2. `*(p+1)`, `*(p+2)` print later elements (note: p+3 goes beyond the array; garbage, p-1 also outside).
- **Pass by value swap (p.16):** `void swap(int a, int b) { int t = a; a = b; b = t; }` with `x = 3, y = 5`: output still `3 5` (a, b, t are copies of x and y; the swap affects only the copies).
- **Pass by pointer swap (p.17):** `void swap(int *a, int *b) { int t = *a; *a = *b; *b = t; }` called `swap(&x, &y)` with `x = 3, y = 5` prints `5 3`. (page drawing shows swap(x, y) in the main but the pointer version needs addresses.)
- **Default parameters (p.17):** `int power(int num, int expo = 2) { int result = 1; for (int i = 0; i < expo; i++) result = result * num; return result; }` `power(2, 3)` → 8, `power(2)` → 4.

### Part 02: Space Complexity (pp. 18-25)
- Space complexity: how much memory (RAM) a program needs while it is running. Why: to know whether enough memory is available; to compare two programs; to know the biggest problem a computer can solve.
- Components: instruction space, data space, environmental stack space.
  1. **Instruction space:** memory needed to store the program itself; usually fixed. Depends on the compiler used, compiler options used (code size optimisation, execution time optimisation), architecture of the target computer.
  2. **Data space:** memory for variables and constants: int 4 bytes, double 8 bytes, char 1 byte. Arrays: `int arr[100]` = 100 × 4 = 400 bytes. Example: `const double PI = 3.14;` (64 bits, named variable), `int r = 7;` (32 bits), `int c;` (32 bits; primitive variables); `c = 2 * PI * r; cout << c;`.
  3. **Environmental stack:** memory used when functions are called; when `hello()` is called the computer stores the return address, the parameters and the local variables. It is a data structure that keeps information needed to resume execution of partially completed functions. Rule of stack: First In Last Out (the page writes this; standard wording is Last In First Out).
- **Call-stack diagram (p.22):** main calls function1(int a) (stack frame: a, b, c, return address to main); function1 calls function2(int d) (frame: d, e, return address to function1); function2 calls function3() (frame: f, return address to function2). Steps numbered 1-6: frames are pushed on each call; when function3 returns, its frame is emptied and its local variables destroyed; then function2's; finally function1's frame is emptied and control returns to main.
- **Fixed vs variable space (p.19):**
  - Fixed: always the same; includes program instructions, constants, simple variables. `int a;` no matter what input you give, same memory.
  - Variable: depends on input size, e.g. `int arr[n];` n = 10 → 40 bytes, n = 1000 → 4000 bytes. Memory changes with input.
  - **Total space = constant space + variable space.** S(P) = C + S_P(input); C = fixed memory, S_P = variable.
  - Example: `int sum(int a, int b, int c)` only 3 integers, memory never changes: variable space = 0. Loop `for (i = 0; i < n; i++)`: n changes but the program doesn't create more variables (only 1 used): S_P(n) = 0, variable space = 0, overall space complexity = O(1).
- **Formal definition (pp. 22-23):** space complexity of algorithm A: S(n) = c + S_A(n), where c is the insensitive (constant) space contribution and S_A is the sensitive space contribution which is a function of instance characteristic n.
- **Search trace (pp. 20-21, dated 17/07/2026):** `arr = [35, 7, 19, 2, 0]`, size 5, target 2; `location INTEGER`, `outcome BOOLEAN`; `outcome ← search(arr, 5, 2, location)`; `IF (outcome) PRINT location`. Trace: index 0: 0<5, 2=35? no; index 1: 2=7? no; index 2: 2=19? no; index 3: 2=2 yes → true, location = 3. Second run with target 25: no match, indexes 0-4 checked, outcome false, index 5 (location ends at 5). Page 21 also draws memory boxes for by-value swap (x=3,y=5 copied into a,b,t; output 3 5) versus reference parameters ("no local copy": a and b are aliases of x and y).
- **Slide 7 notes (p.21):** post determination = performance measurement; pre determination = performance analysis.
- **Example 1, iterative sum (p.24, dated 27/07/2026):** `sum(array, 3)` with array {5, 1, 3} returns 9. Memory used by n, s, i is insensitive (primitive variables); the array is a structured variable but because 'a' is passed by reference its memory consumption is also insensitive to this algorithm. S(n) = c + 0, S(n) ≈ 0 variable. The algorithm is non-recursive, so environmental stack space is also insensitive.
- **Example 2, recursive sum:** `sum(a, n)` returns `sum(a, n-1) + a[n-1]`; trace for {5, 1, 3}: sum(a,3) = sum(a,2) + 3; sum(a,2) = sum(a,1) + 1; sum(a,1) = sum(a,0) + 5; sum(a,0) = 0; total 9. n is a primitive variable (insensitive); a[] is declared outside of scope (insensitive). Environment stack space consumption is **sensitive** to the problem being solved: for each function call the stack keeps n, a and the return address. Assuming a 32-bit machine: n = 4 bytes, a = 4 bytes, return address = 4 bytes, so each call keeps 4 + 4 + 4 = 12 bytes in the environment stack. Recursion depth n + 1, so S(n) = 12(n + 1) (written in the margin; partly cropped, unclear).

### Part 03: Time Complexity (pp. 26-29)
- Amount of time a program takes to run based on the size of inputs. It doesn't measure actual seconds.
- Why: real-time needs (some systems must respond instantly); choose the fastest when multiple algorithms solve the same problem; avoid timeout (ensure your program finishes within limits, especially for large data).
- Factors: 1. input size (n), the main one; 2. hardware and software; 3. operation types (arithmetic, comparison).
- **T(n) = c + T_A(n)**: c = constant time (does not depend on input size); T_A(n) = sensitive time (does depend on input size).
- Two approaches: 1. operation count; 2. step count.
- **Operation count:** key operation = the most time-consuming operator; other operations are not counted. Count how many times certain operations are performed; count only the most important operations like comparisons, additions, multiplications.
- **Example 1 (pp. 26-27):** `max(num, size)` returns the index of the largest integer. num = {16, 11, 2, 19, 6}, result index 3. Algorithm lines: 1 `i ← 0`, 2 `c ← 1`, 3 `LOOP (c < n)`, 4 `IF (a[i] < a[c])` ... 5 `i ← c` (when 19 > 16), 6 `END IF`, 7 `c ← c + 1`, 8 `END LOOP`. Comparisons traced: a[0]<a[1] (16<11 no), a[0]<a[2] (16<2 no), a[0]<a[3] (16<19 yes → i ← 3), a[3]<a[4] (19<6 no).
- **Finding the key operation (p.28):** the key operation is `IF (a[i] < a[c])` (it needs memory lookups for i, c, a[i], a[c] then a comparison). Number of times it executes: **T(n) = n − 1.**
- **Example 2 (p.28), search-style average case:** best n = 1: T1(n) = 1; n = 2: T2(n) = 2; n = 3: T3(n) = 3. Average: T(n) = (1 + 2 + 3 + ... + n)/n = (1/n) Σ i = (1/n)·n(n+1)/2 = **(n+1)/2**.
- **Step count approach (p.29), Algorithm 1 (iterative sum):**
  ```
  1 s ← 0                    1
  2 c ← 0                    1
  3 LOOP (c < n)             n+1
  4   s ← s + a[c]           n
  5   c ← c + 1              n
  6 END LOOP
  7 RETURN s                 1
  8 END sum
  T(n) = 3n + 4
  ```
  Loop test counted n + 1 times: for n = 3 the test 0<3, 1<3, 2<3 is true and 3<3 is false (4 evaluations). Example: num = {3, 6, 1}, size 3: s goes 0 → 3 → 9 → 10; c goes 1, 2, 3; T(3) = 3×3 + 4 = **13**.
- **Algorithm 2 (recursive, p.30):** `IF (n > 0)` n+1; `RETURN a[n-1] + sum(a, n-1)` n; `RETURN 0` 1; **T(n) = 2n + 2**.
Handwriting note: the writer's pseudocode uses `←` for assignment; "ALGORITHM ... END" style as in the slides.

---

## Part 04: Time Analysis (pp. 30-34)

**Running times (p.30)**
- Best case running time: time taken when the best possible thing happens. T(n) minimum.
- Worst case running time: takes a lot of time. T(n) maximum.
- Average case running time: T(n) would be the average (more complicated to analyze).

**Functions of time complexity:** time complexity of an algorithm is a function of n; n ≥ 0; T(n) ≥ 0 for all n.

**Worked count examples** (right column = number of times each line runs)

Linear function (ex 1, p.30):
```
1 i ← 1                 1
2 LOOP (i <= n)         n+1
3   i ← i + 1           n
4 END LOOP
T(n) = 2n + 2     (y = mx + c, a linear line)
```
Logarithm (ex 2, p.30), the loop variable doubles each pass:
```
1 i ← 1                 1
2 LOOP (i <= n)         log2(n) + 1
3   instruction 1       log2(n)
4   instruction 2       log2(n)
5   instruction 3       log2(n)
6   instruction 4       log2(n)
7   i ← i * 2           log2(n)
8 END LOOP
T(n) = 6 log2(n) + 2
```
Side working: i = 2^iterations; loop runs while i ≤ n; 2^maxIterations = n is the terminating point, so maxIterations = log2(n).

Linear logarithm (ex 3, p.31):
```
1 i ← 1                       1
2 LOOP (i <= n)               n+1
3   j ← 1                     n
4   LOOP (j <= n)             n (log2(n) + 1)
5     j ← j * 2               n (log2(n))
6   END LOOP
7   i ← i + 1                 n
8 END LOOP
T(n) = 2n log2(n) + 4n + 2
```
Quadratic (p.31):
```
1 i ← 1                       1
2 LOOP (i <= n)               n+1
3   j ← 1                     n
4   LOOP (j <= n)             n (n+1)
5     j ← j + 1               n (n)
6   END LOOP
7   i ← i + 1                 n
8 END LOOP
T(n) = 2n² + 4n + 2
```
(Each sheet also has a small sketch of the T(n) vs n curve: straight line, flattening log curve, steeper n log n, parabola.)

**Asymptotic notation (p.32)**
- Expresses an algorithm's running time as its growth rate by dropping the less significant terms and constant coefficients.
- Example T(n) = 3n² + 50n + 200. Compare 3n² with 50n + 200:
  - n = 19: 1083 ≥ 1150 ✗ ; n = 20: 1200 ≥ 1200 ✓ ; n = 21: 1323 ≥ 1250 ✓ → for n ≥ 20, 3n² is the more significant term.
  - Compare n² with 50n + 200: n = 52: 2704 ≥ 2800 ✗ ; n = 53: 2809 ≥ 2850 ✗ ; n = 54: 2916 ≥ 2900 ✓ → for n > 53, n² is more significant, so the coefficient can be ignored.
  - lim (n→∞) (50n + 200) / (3n²) = 0.
- Purpose: to find the most appropriate algorithm for a problem we compare algorithms; to compare, we simplify like this.

**Big-O notation (pp. 33-34)**
- Asymptotic notation for the worst case running time of an algorithm.
- For all n ≥ n0: T(n) ≤ c·f(n), where T(n) ≥ 0, f(n) ≥ 0, c ≥ 0.
- Definition: for T(n) ≥ 0 and f(n) ≥ 0, T(n) is said to be O(f(n)) ("big oh of f of n") if there exist positive constants c and n0 such that T(n) ≤ c·f(n) for all n ≥ n0.
- Example 1: T(n) = 3n + 2 ≤ 3n + n for all n ≥ 2, so T(n) ≤ 4n for n ≥ 2 (c = 4, f(n) = n, n0 = 2). Checks: n=1: 5 ≤ 4 ✗; n=2: 8 ≤ 8 ✓; n=3: 11 ≤ 12 ✓. Therefore T(n) = O(n).
- Example 2: T(n) = 10n² + 4n + 2 ≤ 10n² + 4n + n for n ≥ 2; ≤ 10n² + 5n for n ≥ 2; ≤ 10n² + n² for n ≥ 5; ≤ 11n² for n ≥ 5 (c = 11, f(n) = n², n0 = 5). Therefore T(n) = O(n²).
- Ranking noted: O(log n) best, O(n) better, O(n²) worst.

## Part 05: Data Structures (pp. 35-36)

- **Atomic:** atomic data types = character data types (primitive data types); all data of the same type.
- **Composite:** decomposable; consists of a set of homogeneous or heterogeneous data.
  ```
  struct Day { int year; int month; int date; }
  Day birthDay;          // composed of atomic data types

  struct Person { char name[30]; int weight; Day dob; }
  Person He;             // name[0..29], weight, dob(year, month, date)
  ```
- **Data structure:** a structure that holds a set of atomic or composite data.
- Example 1: `int num[] = {3, 2, 1};` get and set operations: `print num[0];` `num[2] = 5;`
- Example 2: `Person employee[] = {"Perera", 60, 1990, 02, 10, "Silva", 45, 1998, 5, 31};` Heterogeneous; 2 compartments; operations: get `print employee[0].name;`, set `employee[1].height = 57;` (the page writes `height`, while the struct above uses `weight`); both atomic and composite; linear.

## Part 06: Stacks (pp. 37-42)

- Stack is a linear data structure. Additions = push; removals = pop; restricted to one end (top). Rule: Last In First Out (LIFO).
- 2 error conditions: **Overflow** (stack is full but you have to push: error); **Underflow** (empty stack but you have to pop: error).
- Before push make sure the stack isn't full: `isFull()`. Before pop make sure it isn't empty: `isEmpty()`.
- **Array-based stack (p.37):** example array a b c d e with size 10, top 4 (indexes 0-9). Need two variables, `size` and `top`; top is needed because we always push or remove items from the top; top keeps track of the top of the stack. Create operation takes: pointer to datatype, size, integer.
- **Linked list-based stack (p.38):** every element links to another.
  ```
  struct node { char data; node *next; }   // next can hold the address of a similar node
  node n;
  ```
- **Test algorithm, array based (p.39):**
  ```
  ALGORITHM create (VAL s INTEGER)
  1 size ← s
  2 top ← -1
  3 P ← ALLOCATE MEMORY DATATYPE [size]
  END create

  ALGORITHM push (VAL d DATATYPE)
  1 IF (isFull())
  2   RETURN false
  3 ELSE
  4   top ← top + 1
  5   P[top] ← d
  6   RETURN true
  7 END IF
  END push

  ALGORITHM isFull()
  1 IF (top = size - 1)
  2   RETURN true
  3 ELSE
  4   RETURN false
  END isFull

  ALGORITHM pop (REF d DATATYPE)
  1 IF (isEmpty())
  2   RETURN false
  3 ELSE
  4   d ← P[top]
  5   top ← top - 1
  6   RETURN true
  7 END IF
  END pop

  ALGORITHM isEmpty()
  1 IF (top = -1)
  2   RETURN true
  3 ELSE
  4   RETURN false
  5 END IF
  END isEmpty

  ALGORITHM destroy()
  1 RELEASE MEMORY [] P
  END destroy
  ```
  Test driver: 1 create(stackSize) (example size 5, top -1); 2 READ(data); 3 LOOP (data ≠ endOfData AND push(data)); 4 READ(data); 5 END LOOP; 6 LOOP (pop(data)); 7 PRINT(data); 8 END LOOP; 9 destroy(); 10 END test. The page traces top and the stack contents (A, B, C pushed, then popped as C, B, A; an example with 4 elements A-E).

**Stack applications (pp. 40-42)**
1. *Reversing data* (p.40). A char array's last element is automatically the null character `'\0'`. Question: write an algorithm to accept a null-terminated string (text) and print it in reverse order.
   ```
   ALGORITHM reverseText (REF text[] CHAR)
   1 s ← stack()
   2 i ← 0
   3 ch ← text[i]
   4 LOOP (ch ≠ '\0' AND s.push(ch))
   5   i ← i + 1
   6   ch ← text[i]
   7 END LOOP
   8 LOOP (s.pop(ch))
   9   PRINT ch
   10 END LOOP
   END reverseText
   ```
   Margin note: using `s.push(ch)` inside the loop condition is much safer than a plain `LOOP (ch ≠ '\0')` with a separate push, because push reports failure (full stack). Why reverse is used: undo feature; back button in browser. These kinds of applications are implemented using a stack.
2. *Converting numbers* (p.41). Write an algorithm to accept a decimal number, convert it to binary, then print the binary number.
   ```
   ALGORITHM dtob (n INTEGER)
   s ← stack()
   LOOP (n > 0)
     bit ← n MOD 2
     s.push(bit)
     n ← n / 2
   END LOOP
   LOOP (s.pop(bit))
     PRINT bit
   END LOOP
   s.destroy()
   END dtob
   ```
   Worked example on the page: 25 ÷ 2 repeatedly gives remainders 1, 0, 0, 1, 1 (written as 25→12 r1, 12→6 r0, 6→3 r0, 3→1 r1, 1→0 r1); popping prints them in reverse: 11001.
3. *Parsing data* (p.42). Write an algorithm to accept a mathematical expression and check whether there is any bracket mismatch. Example expression `(a+b)×c` stored as a char array ending with `=`.
   ```
   ALGORITHM isBracketOk (REF exp[] CHAR)
   s ← stack()
   i ← 0
   ch ← exp[i]
   LOOP (ch ≠ '=')
     IF (ch == '(')
       s.push(ch)
     ELSE
       IF (ch == ')')
         IF (NOT s.pop(ch))
           RETURN false
         END IF
       END IF
     END IF
     i ← i + 1
     ch ← exp[i]
   END LOOP
   IF (s.pop(ch))
     RETURN false
   ELSE
     RETURN true
   END IF
   s.destroy()
   END isBracketOk
   ```
   Idea: push every opening bracket; on a closing bracket pop (fail = mismatch); at the end the stack must be empty. The page also has a rough first draft: read data; if opening bracket push; if closing bracket pop; at the end if stack is empty print "No mismatch" else print "Mismatch".

## Part 07: Queues (pp. 43-44) [pages 43-44 only; no further queue pages in this set]

- Operations: `enqueue()` adds an item; `dequeue()` takes an item out.
- **Array-based queue:** the place from which you dequeue is called `front` (index of front, position 0 at the start). The place to which you enqueue is called `rear` (index of the element to which the next item is enqueued).
  - When you add more items, rear moves to the right. When you remove items, front moves to the right.
  - Example 1: a b c d e in an array of 7 (indexes 0-6): count = 5, rear = 5, front = 0.
  - Example 2 (after removing a, adding f): b c d e f: count = 5, rear = 6, front = 1.
  - After inserting more items the array wraps around: in a 10-slot array k l m n o sit at the start and b c d e at the end (array becoming full). "When you imagine this as a bent array with the ends connected, you will understand this" (ring picture).
- Imagine bending the array and connecting the two ends as a ring. Queue empty and queue full: rear and front are at the same place (so a count is needed to tell them apart). Circular array: `rear ← rear MOD size` (circular behaviour comes from this line, "line no 7" in the algorithm).
- **Linked list-based queue:** a node holds `data` and `next`. `p→data = d;` is the same as `(*p).data = d;`. `rear→next ← d` means: using rear, go to next and assign.

## Recursion (pp. 45-46) (page 45 carries the heading "Trees", but the content is iteration vs recursion)

Iteration vs recursion, countdown:
```
ALGORITHM countdown()           // iteration
int x
IF x > 0
  LOOP (x > 0)
    Print x
    x = x - 1
  END LOOP
ELSE
  Print "Error"
END IF

ALGORITHM countdown (VAL n INTEGER)   // recursion
IF n > 0                              // page writes "x > 0" here; n is meant
  PRINT n
  countdown (n - 1)
ELSE
  RETURN
END IF
END ALGORITHM
```
"Function should accept any positive integer and return the summation":
```
ALGORITHM sum (VAL n INTEGER)
IF n > 0
  return n + sum (n - 1)
ELSE
  return 0
END IF
END sum
```
(An earlier draft on the page uses a `tot` variable: `tot = tot + sum(x-1)` and prints `tot`, then is replaced by the version above.)

## Part 08: Trees (pp. 47-62)

- **Order** = the maximum number of children a node can have (diagram: a tree of order 3).
- **Binary tree:** max child nodes are 2. Has a root, a left subtree and a right subtree; each subtree is again a binary tree.
- **Binary tree traversal:** visiting every node once and only once, without missing any node.
- Example tree used throughout: root **a**; a's children b (left) and e (right); b's children c (left) and d (right); e has a single child f on its right.
- **Preorder:** (1) visit the root, (2) traverse the left subtree in preorder, (3) traverse the right subtree in preorder. "In preorder" means: again visit the root of that subtree first, then its left subtree, then its right subtree. Result: **a b c d e f**. Walk-through (p.48): at c there is no left subtree, so go back up to its root b (already visited), then right d is written down; d has no left, go back to roots and continue until done.
- **Inorder:** visiting happens in the middle: (1) traverse the left subtree in inorder, (2) visit the root, (3) traverse the right subtree in inorder. Result: **c b d a e f**. The first item output is the leftmost node (c). The note stresses the first step is always the left traversal.
- **Postorder:** visiting happens last: (1) traverse the left subtree in postorder, (2) traverse the right subtree in postorder, (3) visit the root. Result: **c d b f e a**.
- **Binary search tree (p.51):** all left subtree nodes contain values less than the root; all right subtree nodes contain values equal or greater than the root; all subtrees must follow the same rule (every subtree must be a BST). Example: 70 root; left 50 (children 30 and 60; 30 has children 20 and 40); right 80. **Inorder traversal gives 20, 30, 40, 50, 60, 70, 80** (sorted).

**Array-based tree (pp. 52-58)**
- Root at n = 1. Parent = n; left child = 2n; right child = 2n + 1 (e.g. 70 at 1, 50 at 2, 80 at 3, 30 at 4, 60 at 5, 20 at 8, 40 at 9). The tree is stored in a 1-D array; some elements remain empty unless the tree is very balanced. Array of size 12 initialised with 0 (0 = empty). Resulting array: index 1=70, 2=50, 3=80, 4=30, 5=60, 8=20, 9=40; others 0.
- Recursive insert(d, n) traced for 70, 50, 80, 30, 20, 40, 60:
  ```
  insert (d, n)
    IF n < size                      // within the array
      IF P[n] = 0                    // empty slot
        P[n] ← d ; return true
      ELSE IF d < P[n]
        insert (d, 2n)               // go left
      ELSE
        insert (d, 2n + 1)           // go right
  ```
  Traces: insert(70,1) stores at 1. insert(50,1): P[1]≠0, 50<70 → insert(50,2) stores at 2. insert(80,1) → 80<70 false → insert(80,3) stores at 3. insert(30,1) → insert(30,2) → 30<50 → insert(30,4) stores at 4. insert(20,1) → (20,2) → (20,4) → (20,8) stores at 8. insert(40,1) → (40,2) → (40,4): 40<30 false → (40,9) stores at 9. insert(60,1) → (60,2): 60<50 false → (60,5) stores at 5 (the page's last line says `P[6] ← 60`, which looks like a slip for P[5]). Parameters from returned calls are deleted after the call returns.
- traverseInorder(n) traced for n = 1 (pp. 56-57): `IF n < size AND P[n] ≠ 0: traverseInorder(2n); Print P[n]; traverseInorder(2n+1)`. Output: 20, 30, 40, 50, 60, 70, 80. (Calls with index ≥ size, e.g. 16 < size false, or P[n] = 0, simply return.)
- **Why array trees waste memory (p.58):** tree heights: h=0: 1 node, total 1 = 2^1 − 1; h=1: 2 nodes, total 3 = 2^2 − 1; h=2: 4 nodes, total 7 = 2^3 − 1; h=3: 8 nodes, total 15 = 2^4 − 1. In general a tree of height h needs **2^(h+1) − 1** nodes (full), so you need 2^(h+1) array elements to accommodate it. Example: 4 levels need 16 array elements and 15 nodes. If the tree is unbalanced and height increases, the memory wastage increases dramatically (sketch: a chain of 5 nodes, levels 0-4).
- Disadvantages of array-based tree: cannot grow; cannot shrink; waste would be dramatic. Solution: linked-list-based tree (can grow, can shrink). If you don't know the height or it is not balanced, go with linked-list-based.

**Linked list-based tree (pp. 58-62)** (flexible, more memory efficient)
- Each node holds `data`, `left`, `right` (left and right are addresses; 0 = none). A `root` pointer holds the address of the first node; `P` is used as the current pointer.
- `addNode(root, d)`: if P = 0 (empty) create a node and store d; else if d < P.data go `addNode(P.left, d)`; else `addNode(P.right, d)`. Traced for 70, 50, 80, 30, 20, 40, 60, producing the same tree as the BST above (70; 50 and 80; 30 and 60 under 50; 20 and 40 under 30).
- `traverseInorder(P)`: `IF P ≠ 0: traverseInorder(P.left); PRINT P.data; traverseInorder(P.right)`. Trace output 20, 30, 40, 50, 60, 70, 80.

**Tree applications (p.63)**
- Represent hierarchically related data (maintain folders / files).
- Represent mathematical expressions: expression trees; parent node = operator, child nodes = operands (examples drawn: 3 + 5; and 3 + 5 × 2 with `×` below `+`).
- Data compression and encoding.
- Efficiently search dynamic sets of data: to insert/remove data the only thing to do is change addresses (very efficient); in arrays all elements have to shift for very small changes.

p.63 ends with a "Recommended References" heading (empty). p.62 is the linked-tree inorder trace.

---

## Still to do for this set
Verification: pp. 1-29 and 30-45 were checked against the page images; pp. 47, 52, 57, 58, 62, 63 were spot-checked and match. Remaining tree pages (46, 48-51, 53-56, 59-61) were transcribed in an earlier pass and not re-verified.
