# AI Peer Notes: Geethma (handwritten, transcribed)

Source: `Notes - Geethma/AI 1.pdf` ... `AI 7.pdf` (37 scanned handwritten pages, no text layer). Transcribed by Claude from page images for future agent reference. Only what is visible is recorded; unclear items are flagged. Numbering AI 1-7 follows the PDFs (they match the first 7 lessons of the other peer notes: Intro, Prompting, Search, GA, ML, Supervised ML, Neural networks - confirmed per section below).

---

## AI 1: Introduction (5 pages; dated 22/06/2026)

Header on page 1: **Paper - 70% | Assignments - 30%**.

**Content list (course outline as the lecturer gave it):**
1. History of AI
2. Agents
3. Search - to solve problems. When AI is applied to a problem there is always a search. There is optimization in any AI application.
4. Genetic Algorithms (GA) - extended version of search
5. Machine Learning (ML)
6. Artificial Neural Networks - dominant AI approach today
7. Rule based AI systems - currently known as GOFAI (Good Old Fashioned AI)
   (Items 5-7 are bracketed with a note: "can be hybridized: LCS (Learning Classifier Systems)")
8. Fuzzy Logic Systems (binary linguistic rules)
9. Swarm Intelligence
10. Basics of Reinforcement Learning

- AI is the science of developing techniques to generate intelligence artificially.
- Inventors of AI: Marvin Minsky, John McCarthy.
- 1951: successful architecture of the neuron. (page text reads "1951 - Successful architecture of Neuron")
- **Turing test:** a computer and a human interrogator (the person who asks questions to evaluate or gather information from another person or system). The computer answers in written form. The human cannot see inside; he gives written questions. If the humans cannot identify it is a computer, the machine is intelligent.
- **Chinese Room argument - John Searle:** a room with a very powerful knowledge base (KB) and a mapping function f(x); it receives a question in Chinese, translates it and returns the answer (a mapping process). Even then the computer is not truly intelligent; it can act like intelligent.

**History (page 2):**
- AI discipline: **1956** - making a machine that can think like a human.
- Two scientists, Marvin & John, called a conference: a 9 months discussion of making a mechanical brain. It is called the **Dartmouth Conference**; its main purpose was to discuss how AI is to be built. The term "AI" was also introduced by them.
- In this conference they decided that **symbol processing** is the best way of creating the brain. e.g. if ... then ... (symbol processing).
- **Rule based approach:** facts and rules are made by symbols. e.g. if temperature > 38 C, then patient has a fever. (GOFAI - Good Old Fashioned AI.) Rule-based programming languages: **Prolog**; **LISP** (not rule based by default, but can be used for rule based AI; to implement this McCarthy created the language LISP).
- **Data driven approach (in the 1940s):** we have data and from that data we identify certain patterns in the environment (by continuous feed of data).
- Today the rule based approach is called **GOFAI** and the data driven approach is called **Machine Learning**.

**Disruptive technologies (page 3):**
- A disruptive technology is a technology that changes the normal way things are done and replaces older methods. Examples: AI, smartphones, cloud computing, blockchain, internet.
- Centralization is the base of modern technology. This concept was challenged and blockchain came into use, a disruptive technology with the concept of **decentralization**. However blockchain introduced decentralization as an alternative; both systems coexist based on use case.
- **Why study AI?** To face the disruptive technologies and create new products and tools. AI can give better solutions for problems we face (optimization).
- Humans - carbon brain; AI - silicon brain.
- **Strong AI:** machine is truly thinking as a human brain; functionality of a real human brain. e.g. chatbots (NLP), autonomous vehicles (as written).
- **Weak AI:** pretend to be intelligent; having a function. e.g. browsing the internet, disease detection, recommender systems in Amazon.

**Main areas of AI (page 4):**
1. **ANI** (Artificial Narrow Intelligence): AI designed to perform one specific task or a limited set of tasks. Siri/Alexa (voice assistants), Google Maps, face recognition systems.
2. **AGI** (Artificial General Intelligence): AI that can think, learn and perform any intellectual task like a human; can learn new tasks without retraining. Not yet achieved - hypothetical, e.g. a robot that can study, cook, drive and solve problems like a human.
3. **ASI** (Artificial Super Intelligence): AI that is far more intelligent than humans in every field. Future concept: AI that can outperform humans in science, creativity, decision making and emotions.
- Venn-style diagram "AI from the lens of science": big circle AI containing GA, SI, FL, and ML; inside ML nested circles: Neural Network, Deep neural network, Transformer technology (ChatGPT ...).

**Page 5:**
- AI splits into **Discriminative AI** (used to classify or predict something based on input data; "Predictive AI"; e.g. email spam detection, face recognition) and **Generative AI** (used to create new content like images, text, audio, video; "Gen AI"; e.g. ChatGPT, music generation AI).
- **Artificially built system:** Environment --Sense--> Intelligent system --Acts--> Environment. Sensors collect information from the environment; actuators perform actions in the environment.
- **Embodied AI:** AI residing in a physical body (self-driving cars, humanoid robots). **Disembodied AI:** AI residing only in a software component (ChatGPT, Google Translate).

---

## AI 2: Prompt Engineering (2 pages)

- **Prompt Engineering** is the process of creating clear and effective inputs for an AI system to guide it toward the desired output.
- **Why important:** improves accuracy by reducing vague or irrelevant responses; saves time by obtaining useful results in fewer attempts; enhances creativity when generating ideas, stories or designs; supports problem solving by guiding the AI through logical steps; increases reliability in tasks such as summarization, coding and analysis.
- **Elements of a good prompt** (margin: **T.R.A.D.E** = Task, Role, Audience, Details, Examples):
  - Clear instruction: state exactly what you want the AI to do.
  - Context: provide background information when necessary.
  - Specific details: mention the format, length, audience or style required.
  - Constraints: define limitations such as word count, tone or scope.
  - Examples: give sample input-output pairs if a particular pattern is needed.
- **Techniques:** (1) Zero-shot prompting: ask the AI to perform a task without examples. (2) Few-shot prompting: provide a few examples before asking the AI to complete a similar task. (3) Chain-of-thought prompting: encourage the AI to explain reasoning step by step. (4) Role prompting: assign a role such as "act as a teacher" or "act as a software engineer". (5) Constraint-based prompting: add rules such as "explain in 100 words".
- **Example:** weak prompt "Explain photosynthesis." Improved prompt: "Explain photosynthesis in simple terms for a grade 8 student in about 100 words."
- **Applications:** content generation; code generation and debugging; question answering and tutoring; data analysis and summarization; chatbots and virtual assistants.
- **Best practices:** simple and direct language; enough context; specify the expected output format; avoid ambiguous or overly broad instructions.
- **Limitations:** AI responses may still contain errors or outdated information; poorly designed prompts can lead to biased, incomplete or irrelevant outputs; prompt engineering does not guarantee perfect results.

---

## AI 3: Search / State Space Search (4 pages)

- **AI search** is the process of finding a sequence of actions or steps that lead from an initial state to a goal state in an AI system. Applications: problem solving, game playing, route planning and optimization. Examples of algorithms: Breadth-First Search (BFS), Depth-First Search (DFS).
- **Why search is important:** enabling machines to make intelligent decisions; solve complex problems; navigate through large, complex search spaces to find optimal or near-optimal solutions.
- AI is for problem solving and for that we build problem-solving AI. Examples of problem solving agents: Khan Academy, poised.com and sembly.ai (as written).
- **Three objectives of search:** (1) finding a solution; (2) finding all the solutions; (3) finding the best solution to the problem.
- **Examples of search in AI (p.2):**
  1. Finding the best W (weight) value in a neural network is also a search. Doing multiple training cycles reduces the error of the output; a neural network has many W values. (Sketch: error vs W curve with a minimum at the best W.)
  2. **Linear regression:** y = mx + c; there can be many (m, c) combinations; we get the best (m, c) by doing a search (the line with the least error).
  3. **Path finding agents:** find the shortest distance between A and E in a graph (nodes A-F); we do a search and get the shortest out of the multiple possible ways.
  4. **Travelling salesman problem:** cities A, B, ..., F; a salesman must travel to each city only once and come back to the same location; all cities are connected and paths are bidirectional. This is an NP-hard problem; when the problem is larger it cannot be solved (not solved yet). For n cities there are (n-1)! possible results.
  5. Games also need search to find paths avoiding obstacles and to decide the best moves of the characters. So searching is an essential part of AI.
- **State space search - core behind AI:** looking for a state in a state space, and the state is the solution for the problem. **State space = all possible solutions.**
- **Water jug example (p.3):** two empty jugs A (3 L) and B (4 L), with enough water; collect 2 L of water in A or B. State written as (a, b) = (amount in 3L jug, amount in 4L jug). Start state (0,0); goal states written "(2,0), (0,2)" (as in the notes). Possible operations: 1 Fill 3L; 2 Fill 4L; 3 Transfer 3L to 4L; 4 Transfer 4L to 3L; 5 Empty 3L; 6 Empty 4L.
- **BFS (Breadth-First Search):** search the whole breadth of the problem, horizontally (level by level). The handwritten BFS tree expands (0,0) into (3,0) and (0,4), then level 2: from (3,0): (3,4), (0,3), (0,0); from (0,4): (3,4), (3,1), (0,0); deeper levels include (3,3), (0,4), (3,0), (0,0), (2,4), (1,0), (3,0), (0,3) ... Repeated/dead states are marked with a "perpendicular" (stop) sign. The goal **(2,0)** is circled at the bottom of the left branch. Path: (0,0) -> (3,0) -> (0,3) -> (3,3) -> (2,4) -> (2,0).
- **Page 4 (Google Maps - A* algorithm, heuristic method):** this uninformed method is also called **Blind Search / Exhaustive Search / Uninformed search / Brute Force search**.
  - Extra: **Uniform Cost Search** - a search algorithm that finds the lowest cost path by always expanding the node with the smallest total path cost.
  - Abdul Bari - an Indian computer science educator known for explaining algorithms, data structures and other CS topics (video reference).
  - **Knapsack problem** - an optimization problem where the goal is to select items with the maximum total value without exceeding a given weight limit (written "height limit").
  - **A\* (A-star) algorithm** - an informed search algorithm that finds the shortest path by using a formula.


---

## AI 4: Genetic Algorithms + Machine Learning and AI techniques (12 pages)

**Page 1: theory of evolution**
- The theory of evolution is the basic idea behind genetic algorithms. According to Darwin's theory, fit individuals get together and make fitter individuals. Two good solutions are combined to make better solutions.
- **Evolutionary optimization** branches: 1. Evolutionary computing; 2. Combinatorial optimization; 3. Genetic algorithms.
- **Evolutionary computing:** a problem-solving approach inspired by natural evolution. Uses selection, reproduction, crossover, mutation, fitness. The aim is to gradually produce better solutions.

**Page 2**
- **Combinatorial optimization:** the process of finding the best solution from a large number of possible combinations. Examples: shortest route problem, scheduling, travelling salesman problem, resource allocation, job assignment.
- **Genetic algorithm:** an optimization method that uses selection, crossover and mutation to find better solutions.
- **Key terms:** Population (a group of possible solutions); Chromosome (representation of one solution); Gene (a part of a chromosome); Fitness (how good a solution is); Selection (choosing good solutions); Crossover (combining two solutions); Mutation (randomly changing a solution); Generation (one complete cycle of the algorithm).

**Page 3: GA flowchart**
1. Decide the population size
2. Decide the chromosome structure
3. Decide the fitness
4. Loop: 4.1 Selection (choose good solutions from the current population: roulette wheel selection, binary tournament) -> 4.2 Crossover (combine two selected parent solutions to create children) -> 4.3 Mutation (randomly change some genes in the children) -> decision "More children to make?" Yes: back to selection; No: continue
5. Make the new population -> decision "Stopping criteria met?" No: back to the loop; Yes: stop.
- **Chromosome representation:** a binary string e.g. 1 1 0 1 1 0 with genes x1 ... x6; x = (x1, ..., x6) is the chromosome/solution; z = f(x) is the fitness function. Each chromosome represents one possible solution; the genes (0 or 1) are the decision variables; fitness (F) shows how good the solution is.

**Page 4**
- Population N = initial population, Generation 0 (F0) -> Generation 1 (F1/G1) -> Generation 2. The population contains many chromosomes (solutions); in each generation the population evolves; good solutions survive and produce better solutions.
- **Fitness over generations:** an S-shaped rising curve that flattens. At the beginning fitness is low; as generations increase, better solutions are found and fitness increases. After some time improvement becomes very small and fitness almost constant: the algorithm has **converged** to a good solution.
- **GA example:** Max z = x^2, 0 <= x < 32, x integer. Population size N = 4:

| Chromosome | Binary | x | f(x) = x^2 | Fitness share (as written) |
|---|---|---|---|---|
| A | 00010 | 2 | 4 | 4/633 ~ "1 %" |
| B | 00111 | 7 | 49 | 49/633 ~ "17 %" (as written) |
| C | 10000 | 16 | 256 | 256/633 ~ "33 %" (as written) |
| D | 10010 | 18 | 324 | 324/633 ~ "49 %" (as written) |
| Total | | | 633 | |

  **Check:** 4 + 49 + 256 + 324 = 633 is right, but the exact shares are 4/633 = 0.6 %, 49/633 = 7.7 %, 256/633 = 40.4 %, 324/633 = 51.2 %. The percentages written in the notes (1, 17, 33, 49) do not match; use the exact values.

**Page 5: selection, crossover, mutation**
- **Roulette wheel selection:** the probability of selecting an individual depends on its fitness; p_i = fitness_i / total fitness. (Pie chart labelled 49 %, 33 %, 17 %, 1 % for D, C, B, A as written.)
- **Binary tournament selection:** randomly choose two chromosomes and select the one with better fitness. Example: choose A (fitness 4) and C (fitness 256): winner = C (256 > 4).
- **Crossover:** combines parts of two parent chromosomes to produce children. Parts after the crossover point are exchanged (binary crossover). Example drawn: P1 = 0 0 1 | 1 1 0 0 ... P2 = 0 1 0 | 0 0 0 0 ... children C1 = 0 0 1 0 0 0 ..., C2 = 0 1 0 1 1 0 0 (the digit-by-digit bits are partly unclear in the scan; the idea is "swap the tails after the crossover point").
- **Mutation:** randomly changes one or more genes (0 <-> 1). Before mutation (C1): 0 0 1 0 0 0 0; after: 0 0 1 1 1 0 0 style change with one gene shown in red (partly unclear). Purpose of mutation: introduce new variation; maintain diversity; avoid local optimum.

**Page 6: TSP and random keys**
- **Travelling salesman problem:** arrange cities in an order to get the minimum total distance. Chromosome = a permutation. Crossover on permutations produces invalid children: P1 = 1 4 3 | 6 5 2 and P2 = 3 2 1 | 6 4 5 give C1 = 1 4 3 6 4 5 (city 4 twice, 2 missing) and C2 = 3 2 1 6 5 2 (city 2 twice). "Crossover method is not working well here, so we need another algorithm."
- **Random Keys algorithm:** represents a solution using random real numbers, usually between 0 and 1. Sort the random keys in ascending order to get the city order.
  - P1 keys: 0.97 0.68 0.72 0.15 0.48 0.32 (cities 1..6). Sorted ascending: 0.15 (city 4), 0.32 (city 6), 0.48 (city 5), 0.68 (city 2), 0.72 (city 3), 0.97 (city 1). **City order = 4 6 5 2 3 1.**
  - P2 keys: 0.62 0.38 0.87 0.92 0.16 0.32 (shown, not worked on the page).

**Page 7: types of optima**
- Optimization is the process of finding the best solution. Kinds of optima:
  1. **Global optimum:** the best solution among all possible solutions; highest (or lowest) fitness value.
  2. **Local optimum:** better than its neighbouring solutions but not the best overall solution.
  3. **Near optimum:** a solution very close to the global optimum but not exactly the best.
  (Each with a fitness-vs-solution-space curve with several peaks.)
- **Stopping criteria examples:** maximum number of generations reached; desired fitness achieved; no improvement for several generations.

**Page 8: Machine Learning and AI techniques (KDD '98)**
- **KDD'98** is a classic direct-marketing dataset used to illustrate how AI/ML techniques are chosen to solve a real business problem.
- **The business problem:** a charity is deciding how to contact potential donors. Cost of contacting a person by phone call: 10 /- ; by letter: 25 /- (units as written). The dataset contains records of 1 million potential donors. Table columns: Donor ID, characteristics, donated last year (1/0), amount, prediction M1 (will donate? 1/0), amount M2 (predicted amount), profitability p x q (e.g. 70 % x 1200; 60 % x 500; 0).
- AI techniques can be used to solve problems by using ML models: 1. Regression; 2. Classification; 3. Forecasting (time series prediction); 4. Optimization.
- **Regression:** an ML technique used to predict a numerical value. Inputs (x1, x2, x3, ...) -> Model -> e.g. ?/100. Examples: predicting exam marks, donation amount, temperature.

**Page 9**
- **Classification:** an ML technique used to assign an input to a class/category: (x1, x2, ...) -> ML model -> class. **Binary classification:** two possible classes (1/0), e.g. predict whether someone is going to donate or not. **Multiclass classification:** more than two classes (class 1 .. class 4; model predicts one of the four).
- **Donor prediction example:** about 1 million records, around 250000 identified as donors. **Model 1 -> classification:** whether someone will donate; classification alone does not tell how much the person will donate. **Model 2 -> amount of donation:** a regression problem because the output is a numerical value.

**Page 10**
- Combining models: prediction 1, amount 1200, probability 70 % x 1200; prediction 1, amount 500, 60 % x 500; prediction 0, amount 0 -> 0.
- **Expected value = sum over i=1..n of P_i * D_i**, P_i = probability, D_i = predicted donation amount. Example: 70 % -> 0.70 x 1200 = 840.
- **Genetic algorithm** (here used for optimisation): an AI optimization technique inspired by natural selection and evolution. A binary chromosome (p1 p2 p3 p4 p5) = (1 1 0 1 1) selects which donors to contact; objective written R / (P - C) (profit related; as written).
- **Forecasting:** predicting future values using previous observations (time series; example values d1..d10: 300, 310, 312, 320, 325, ..., 340; value-vs-day rising curve).
- **Optimization:** finding the best possible solution according to one or more objectives (minimize objective functions); e.g. minimize cost, minimize emissions. **Multi-objective optimization** (extra): optimizing two or more objective functions at the same time, e.g. CO2 emission and fuel cost; minimize cost and emission.

**Page 11: Machine Learning**
- ML is a branch of AI in which a computer system learns patterns from data and uses those patterns to make predictions, decisions or generate outputs. (Venn: AI containing FL, GA, SI and ML.)
- **Predictive ML:** focuses on predicting an outcome from given information (predict future values, predict exam marks). **Generative ML:** focuses on generating new content or sequences based on learned patterns (next word prediction in a sequence).
- Three types: **Supervised ML** (learns from labelled data; classification, regression); **Unsupervised ML** (works with data without predefined output labels; **clustering** groups similar data items together; **association rule mining** discovers relationships between items); **Reinforcement learning** (an agent learns by interacting with an environment and receiving feedback/rewards; states s1, s2, s3...; actions a1, a2, a3...; the agent learns which action is best for a particular state).

**Page 12**
- Reinforcement learning uses a feedback/reward system. Feedback can be positive or negative: positive reward = desirable action; negative reward/penalty = undesirable action. Boston Dynamics robots (robotics company): robots can use RL concepts to learn suitable actions through interaction and feedback.
- **Real coded genetic algorithm:** represents solutions using real valued numbers rather than only binary values, e.g. (0.25, 1.73, 4.62, 2.15). Useful when the decision variables are naturally continuous.


---

## AI 5: Machine Learning (5 pages)

(Overlaps with the last pages of AI 4; page 1 repeats RL and real-coded GA.)

**Page 1 extras:** Boston Dynamics: first they made robots for military; 4-leg robots like dogs, etc. **Supervised ML is mostly predictive. Unsupervised: generative. Generative ML = unsupervised ML + supervised fine tuning + reinforcement learning.** Supervised ML: predicting a class (classification); predicting a number (regression); predicting a value from a time series.

**Page 2: Reinforcement learning**
- RL is a type of ML where an agent learns by interacting with an environment and receiving feedback in the form of rewards (+) or penalties (-). Example: robots developed by Boston Dynamics learn movements and actions through interaction and feedback.
- **RL representation:** State (s) = current situation; Action (a) = action taken by the agent; Policy (pi) = rule used to select actions; Probability (P) = probability of selecting the action. **pi(s, a_i) = P_i**.
- **Unsupervised ML:** works without target labels. 1. Clustering; 2. Association rule mining.
- **Clustering:** grouping similar data items together without using predefined labels. Example "Student data" table: Height, Weight, Z score, GPA1, GPA2, GPA3. Plotting only Height (H) vs Weight (W) gives **2 clusters** (we can predict those two are male and female).

**Page 3**
- Adding a new dimension (Z score) makes existing clusters disappear and new clusters form. Many more dimensions = **high dimensional space**.
- **Curse of dimensionality:** when the number of dimensions increases, data becomes sparse; distance calculations become difficult; learning becomes more complex.
- **Association rule mining:** discovers relationships among data items.
- Table "students who completed degree" with Final GPA (0-4) and Grade (1C/2L/2U/S/F...): predicting a numeric value (Final GPA) = **regression**; predicting a category (Grade) = **classification**.
- **Train/test split:** data with columns x1, x2, x3, GPA, Grade split into **training data 80 %** and **test data 20 %**. The population (all students) vs samples (S); an ML model (M) is trained using sample data. If one sample is trained too much it may perform poorly on other samples: this is the **bias-variance problem** (model overfitted to one sample).

**Page 4**
- For prediction we need techniques: **Linear Regression** (Model 1: GPA, numeric) and **Logistic Regression** (Model 2: GRADE, category). Artificial neural networks are good for both numerical and categorical data.
- **Linear regression:** Simple (one input feature) or Multiple (multiple input features). Inputs X = {x1, x2, x3}; y depends on X; find the relationship **y = f(x)**.
- **Feature engineering** and **feature selecting** are data preprocessing methods.
- For one feature X = {x1}: sketch with training points and a test point; "model overfitted to train data" (wiggly line through all training points misses the test point).
- **y-hat = W1 x1 + W0** (W1 = weight, written "height" in the notes; W0 = bias). By changing W1 and W0 we can draw an infinite number of possible lines; we need to find the best one. **Error at each point** = difference between the actual value and the predicted value.

**Page 5: error function**
- **Sum of Squared Error (SSE):** E = e1^2 + e2^2 + e3^2 + ... = sum over i=1..n of (y_i - y-hat_i)^2. Since y-hat = W1 x1 + W0: E = sum (y_i - (W1 x_i + W0))^2, so **E = f(W1, W0)**.
- Different values of (W0, W1) give different amounts of error. **ML = finding the parameter values (W0, W1, ...) that minimize E.** The line with the least total squared error is the optimal line.
- **Two features:** y-hat = W1 x1 + W2 x2 + W0; E = sum (y - (W1 x1 + W2 x2 + W0))^2; E = f(W0, W1, W2).
- Plotting error (E) vs weight (W) typically produces a **convex curve**. The algorithm takes small steps (jumps) down the curve toward the minimum error. **Large jumps:** faster but risk overshooting the minimum. **Small jumps:** more precise but take much longer to converge. **eta = learning rate**, controls the step size taken at each iteration while minimizing E.

---

## AI 6: Supervised ML: linear and logistic regression (4 pages)

**Page 1**
- "All models are wrong. Some are useful."
- **Curve fitting:** finding a mathematical function or model that represents the relationship between input data and output data. (Sketch: population curve, a circled part = sample.)
- Training data table (x = hours of study per week, y = GPA): (5, 2.7), (2, 3.2), (1, 4), (3, 2.9), (6, 3.5) (as written; the rows are slightly unclear).
- **Linear regression uses a linear function to fit the data:** y-hat = m x + c. E = sum over i=1..5 of (y-hat_i - y_i)^2 = sum [(m x_i + c) - y_i]^2; **E = f(m, c)**. The error depends on the values of m and c.
- **Bias-variance problem** is an issue in curve fitting: **high bias** = model is too simple -> **underfitting**; **high variance** = model is too complex -> **overfitting**; good model balances both. Bias-variance problem = finding the right model complexity.
- **Hyperplane:** a decision boundary that separates data into different classes.

**Page 2: logistic regression**
- Classification problem table: (x, y) = (2, 0), (1, 0), (5, 1), (3, 0), (6, 1), (4, ?). Plot: S-shaped curve going from 0 to 1 over x; errors e1, e2, e3 shown.
- Instead of directly using a straight line as the output, **logistic regression uses a sigmoid function:** y-hat = 1 / (1 + e^-(m x + c)); 0 <= y-hat <= 1. Error again E = sum (y_i - y-hat_i)^2 with y-hat substituted; E = f(m, c).
- **With multiple inputs:** Model A - linear regression: y-hat = W1 x1 + W2 x2 + W0 = sum_{i=0..2} W_i x_i with x0 = 1. Model B - logistic regression: y-hat = 1 / (1 + e^-(W1 x1 + W2 x2 + W0)) = 1 / (1 + e^-(sum_{i=0..2} W_i x_i)), x0 = 1.

**Page 3: single neuron architecture**
- Inputs x1 (weight W1) and x0 = 1 (bias, weight W0) -> neuron (aggregation z, then activation) -> output y-hat. **z = W0 x0 + W1 x1 = sum_{i=0..1} W_i x_i**; y-hat = W0 x0 + W1 x1 (linear regression neuron: c = W0, m = W1).
- **Single-neuron worked example:** if W1 = 0.8, W0 = 1.2 for the table (x1, y): (2, 2.8), (1, 3.2), (3, 3.8), (5, 3.6), (6, 2.9) (some y values partly unclear). Sample 1: 2 x 0.8 + 1 x 1.2 = 2.8 = z = y-hat; error = (2.8 - 2.8)^2 = 0. Sample 2: 1 x 0.8 + 1 x 1.2 = 2.0 = y-hat; error = (2.0 - 3.2)^2 = (1.2)^2; ... E = sum.
- **Weight learning:** final output minimizing the error. Update rules: W1_new = W1_old + delta W1; W0_new = W0_old + delta W0. (E vs W curve with learning-rate step.)
- **Epoch:** one complete exposure/pass through the entire training dataset. Example: if the dataset contains 1000 samples, the model processes all 1000 once: 1 epoch. **Why multiple epochs:** a model may not learn enough from seeing the dataset only once.

**Page 4**
- **Classification with a single neuron architecture is equal to logistic regression** (neuron with sigmoid activation).
- **Simple models cannot fit every dataset:** a bell-shaped "logistics" dataset and a rising-then-flat "linear" dataset cannot easily be represented using only a straight line or basic sigmoid curve. A model that is too simple to capture the pattern = **underfitting**; a model that becomes unnecessarily complex and memorizes training data = **overfitting**.

---

## AI 7: Neural networks (5 pages)

**Page 1: training an AND gate**
- A logic gate produces an output from binary inputs (0 or 1). An artificial neuron can be trained using input-output examples of a logic gate. For two inputs x1, x2: the neuron calculates **z = W0 + W1 x1 + W2 x2** and produces **y-hat = f(z)**, f = activation function.
- **AND gate** (features x1, x2; target y): (0,0)=0, (0,1)=0, (1,0)=0, (1,1)=1. The neuron adjusts its weights until its outputs are close to these target values.
- **Activation function:** determines how the weighted input z is converted into neuron output: y-hat = f(z). Four important activation functions: **Sigmoid, Tanh, Linear activation, ReLU.**

**Page 2: activation functions**
- **Sigmoid:** suitable when the required output is between 0 and 1; sigma(z) = 1 / (1 + e^-z); 0 < sigma(z) < 1; S-shaped.
- **Tanh:** hyperbolic tangent; produces values between -1 and 1; f(z) = tanh(z); S-shaped, centred at 0.
- **Linear activation:** creates a linear relationship between input and output; f(z) = z; range -inf to +inf; straight line.
- **ReLU** (Rectified Linear Unit): f(z) = max(0, z) = 0 if z < 0, z if z >= 0. Range 0 to +inf; negative values become 0 while positive values remain positive.

**Page 3: error during AND learning**
- For training sample i: e_i = y_i - y-hat_i. Using squared error: E = sum_{i=1..4} (y_i - y-hat_i)^2 with y-hat_i = 1 / (1 + e^-(W0 + W1 x1 + W2 x2)); **E = f(W1, W2, W0)**. The aim of training is to find weights that produce a small error.
- **Weight adjustment:** the derivative of the error shows how strongly the error changes when a weight changes: dE/dW0. The size of the weight adjustment is controlled by the learning rate eta: **delta W0 = eta . dE/dW0** (as written; in standard gradient descent the update subtracts this term: W_new = W_old - eta dE/dW).
- **AND can be learned by one neuron:** class 0: (0,0), (0,1), (1,0); class 1: (1,1). These points can be separated by one straight line. Therefore **AND is linearly separable** and a single neuron can learn the AND gate.

**Page 4: XOR gate**
- XOR table: (0,0)=0, (0,1)=1, (1,0)=1, (1,1)=0. Target outputs from a trained network are shown as 0.03 -> 0, 0.97 -> 1, 0.96 -> 1, 0.04 -> 0.
- Class 1: (0,1), (1,0); class 0: (0,0), (1,1). **XOR is not linearly separable.** No single straight line can place both class 1 points on one side and both class 0 points on the other. So a single neuron cannot correctly solve XOR. Basic logistic regression also cannot directly solve XOR. This is why adding more neurons becomes necessary.

**Page 5: hidden layer and MLP**
- **Hidden layer:** an intermediate layer located between the input layer and output layer. Diagram: inputs x1, x2 -> three hidden neurons (activations a1, a2, a3, weights W1-W6) -> output neuron (weights W7, W8, W9) -> y-hat = 1 / (1 + e^-z), **z = a1 W7 + a2 W8 + a3 W9 + bias**.
- **Multi-Layer Perceptron (MLP):** a neural network that contains an input layer, at least one hidden layer and an output layer.
- Each hidden neuron can represent a different boundary or intermediate pattern. One neuron = one linear boundary; hidden neuron 1 = boundary 1, hidden neuron 2 = boundary 2. **Hidden layers allow a neural network to solve XOR.** Activation functions introduce nonlinear behaviour into the network.
