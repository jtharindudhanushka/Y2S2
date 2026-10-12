# AI Peer Notes: Yasiru (converted from typed PDFs)

Source: `Notes- Yasiru/*.pdf` (typed Notion exports, converted with pdftotext; table layout may be flattened; diagrams not reproduced). Numbering follows the notes' own headings (1-7). `WhatsApp Image ...jpeg` is transcribed separately if relevant.


---

## 1 Introduction to AI  (`notion-page.pdf`)

```text
1. Introduction to AI

  1. What is AI?

   AI is the science of developing techniques to generate intelligence artificially —
   building machines that can think like humans (reason, learn, perceive, and decide).

   It is often described as a disruptive technology: a technology that doesn't just improve
   existing tools but fundamentally reshapes industries and the way work is done.

   Types of AI Based on Capabilities

   • ANI (Artificial Narrow Intelligence): Also known as "Weak AI." This AI is highly

         specialized and trained to excel at one specific task (e.g., face recognition, chess
         engines, language translation). It operates under strict constraints and cannot apply its
         intelligence to any problem outside its domain.

   • AGI (Artificial General Intelligence): Also known as "Strong AI" or human-level AI.

         This represents a hypothetical machine that possesses the ability to understand, learn,
         reason, and apply knowledge across any intellectual task that a human being can do.

   • ASI (Artificial Superintelligence): A futuristic, hypothetical form of AI that surpasses

         human intelligence across all domains, including scientific creativity, emotional
         intelligence, general wisdom, and social skills.

  2. A Bit of History — When Did AI Start?

   The field was formally named in 1956 at the Dartmouth Summer Research Project on
   Artificial Intelligence (the Dartmouth Conference). Key founding figures include:

   • John McCarthy — coined the term "Artificial Intelligence" and later created the LISP

         language.

   • Marvin Minsky — co-founder of the field and of the MIT AI Lab.

   (Other founders present in this era included Nathaniel Rochester and Claude Shannon.)

   How World War II acted as a catalyst for AI

   Although AI was named in 1956, the intellectual and technological groundwork was laid
   during World War II (1939–1945). The war turned abstract ideas about "thinking machines"
   into urgent, funded, practical problems:

   • Codebreaking and Alan Turing. At Britain's Bletchley Park, Turing helped design the

         electromechanical Bombe to break the German Enigma cipher. This showed that a
         machine could carry out tasks that previously seemed to require human reasoning — a
         direct conceptual seed for AI.

   • Birth of electronic computers. The war drove the creation of the first programmable

         electronic machines: Colossus (1943–44, built to break the Lorenz cipher) and, just
         after the war, ENIAC (1945, built to compute artillery firing tables). AI needs computers
         to run on — and the war is what produced them.

• Cybernetics and feedback control. Norbert Wiener worked on automatic anti-aircraft

     fire-control systems that had to predict a plane's future position. This work on feedback
     and control led to his 1948 book Cybernetics, a foundation for thinking about machines
     that sense, adjust, and act — the same loop that defines intelligent agents today.

• The artificial neuron. In 1943, McCulloch and Pitts published a model showing how

     networks of simple neuron-like units could compute logical functions — the ancestor
     of today's neural networks.

• Turing's 1950 paper. Building on his wartime experience, Turing published "Computing

     Machinery and Intelligence," proposing the Turing Test ("Can machines think?").

• The Turing Test - Proposed by Alan Turing in his landmark 1950 paper, this behavioral

     test evaluates whether a machine can exhibit intelligent behavior indistinguishable
     from a human.
     • The Setup: A human judge carries out a text-based, natural language conversation
     with two hidden entities: one human and one machine.
     • The Criterion: If the judge cannot reliably distinguish the machine from the human
     after a period of conversation, the machine passes the test.

• The term "Machine Learning" was officially coined by Arthur Samuel in 1959 during

     his tenure at IBM. He famously defined it as giving computers the ability to learn
     without being explicitly programmed, demonstrating this by building a checkers
     program that learned to play better than its creator.

In short, WWII supplied AI with three things it could not have started without: working
computers, funding and urgency, and a generation of scientists who had personally seen
machines do "intelligent" work. The 1956 Dartmouth Conference then gave the field its
name.

3. Two Major Approaches to Building AI

Approach                    Idea                              Examples / Tools
GOFAI ("Good Old-Fashioned
AI")                        Encode human knowledge as         LISP, Prolog, expert systems
                            explicit rules and logic; the
Data-Driven Approach        machine reasons by following
                            them. Also called the symbolic /
                            rule-based approach.

                            Don't hand-code rules — let the   Machine learning, deep
                            machine learn patterns from       learning, transformers
                            data.

The history of AI is largely a shift from the rule-based GOFAI approach toward the data-
driven approach that dominates today.

Why the Data-Driven Approach is Powerful Today

The historical paradigm shift away from rule-based GOFAI toward modern data-driven
approaches succeeded due to two primary modern catalysts:
1. Availability of Data (The Big Data Explosion): Early AI lacked the sheer amount of
training data required to find meaningful patterns. Today's hyper-connected world
continuously generates vast reservoirs of information.
2. Massive Computing Power: Modern deep learning relies heavily on intense matrix
mathematical operations. The rise of specialized hardware (GPUs and TPUs) along with
scalable cloud computing infrastructure made processing these massive computations
feasible.

What is Big Data? (Introduced in 2001)

The data explosion that fuels modern machine learning algorithms is known as Big Data.
Characterized by analyst Doug Laney in 2001, it is defined by the 3 Vs:
• Volume: The sheer, massive scale and quantity of data generated and stored every single
second.
• Velocity: The incredible speed at which new data is created, streamed, and needs to be
processed in real time.
• Variety: The structural diversity of data, encompassing structured data (databases), semi-
structured data (XML, logs), and unstructured data (text, video, audio formats).

4. The AI Landscape

AI is a broad umbrella containing many techniques. Some are classical / standalone
methods; others are nested inside one another.
Classical & complementary techniques (under the AI umbrella):

• GA — Genetic Algorithms (optimization inspired by evolution)
• SI — Swarm Intelligence (behaviour inspired by ants, birds, etc.)
• FL — Fuzzy Logic (reasoning with "degrees of truth" rather than strict true/false)
• RB — Rule-Based systems (the GOFAI style above)

• ML — algorithms that learn from data.
• NN — models loosely inspired by the brain.
• DL — many-layered neural networks.

• Transformers — the architecture behind modern large language models (e.g.,

     ChatGPT).

5. Discriminative vs. Generative AI

• Discriminative / Predictive AI — distinguishes between things: classification,

     prediction, detection (e.g., "is this email spam?", "will this customer churn?").

     ◦ Three Core Types of Discriminative Tasks
         ▪ Classification: Used when the model predicts a discrete class or category

                 label (e.g., predicting whether an email is "Spam" or "Not Spam", or
                 identifying an image as a "Cat" or "Dog").

         ▪ Regression: Used when the model predicts a continuous numerical value

                 (e.g., predicting the exact price of a house, a person's age, or future revenue
                 metrics).

         ▪ Time Series Forecasting: Used when the model predicts a sequential or

                 temporal value based on historical, time-ordered data points (e.g.,
                 predicting tomorrow's weather patterns, hourly server load, or stock market
                 fluctuations over the next week).

• Generative AI (Gen AI) — creates new content: text, images, audio, code (e.g.,

     ChatGPT, image generators).

6. Intelligent Agents — How an AI System Interacts with
the World

An intelligent system operates in a continuous sense → think → act loop with its
environment:

• Sensors — let the system sense / perceive the environment (cameras, microphones,

     inputs).

• Intelligent System — processes the input and decides what to do.
• Actuators — let the system act on the environment (motors, outputs, responses).

7. Embodied vs Disembodied AI

Type         Meaning                           Example

Embodied AI  AI that has a physical body and   Self-driving car
             acts in the real world through
             sensors and actuators.

Disembodied AI AI that exists purely as        ChatGPT

             software, with no physical form.
```


---

## 2 Prompting  (`to.pdf`)

```text
2. Prompting

   What is Prompting?

   A prompt is simply the text instruction or question you give to an AI model to get a
   response.

   Prompt Engineering is the art of structuring your instructions clearly so the AI
   understands your context and delivers exactly what you need on the very first try.

  The TRADE Prompting Framework

   To move away from generic answers, we use a structured blueprint called the TRADE
   framework. It breaks a great prompt down into five essential building blocks:

   • T – Task (The What): Clearly state exactly what action you want the AI to perform. Use

         direct, specific action verbs like write, summarize, draft, analyze, reformat, or
         brainstorm.

   • R – Role (The Who): Assign a specific persona or expert identity to the AI. This instantly

         changes how the AI reasons, behaves, and what vocabulary it grabs (e.g., acting as a
         senior software engineer vs. a 5th-grade science teacher).

   • A – Audience (The Whom): Define exactly who will read or use the final output.

         Specifying the audience tells the AI how to calibrate its complexity (e.g., explaining a
         topic to a complete beginner vs. a corporate executive team).

   • D – Details (The Constraints): Provide rules, context, and formatting guidelines. This

         includes structural limits (use a markdown table, bullet points), length boundaries
         (under 200 words), or a specific tone (witty, professional, urgent).

   • E – Example (The Model): Provide a sample of what a successful output looks like. This

         technique is known in AI as "Few-Shot Prompting." Showing the AI a pattern ensures it
         mirrors the exact structure and style you want.

  Vague vs. TRADE Prompting

            The Vague Prompt:
        "Write an email about saving money."

        Why it struggles: The AI has no idea who is writing it, who is reading it, how long it
        should be, or what format to follow. It will likely give you a long, dry, and generic
        message.

  The TRADE Prompt:

• Role: "You are a friendly personal finance coach who specializes in helping young

    adults."

• Task: "Write a short newsletter email sharing 3 quick tips on how to save money

    on weekly groceries."

• Audience: "The audience is busy college students living on a tight budget."
• Details: "Keep it under 150 words. Use a casual, encouraging tone and format

    the tips using clear bullet points."

• Example: "Model the formatting like this:
    ◦ Tip 1: [Catchy Name] – [1-sentence action step]"
```


---

## 3 State Space Search  (`3.pdf`)

```text
3. State Space Search

1. What Is State Space Search

A problem solving method in AI. The problem is described as a set of situations (states),
and the computer moves from one state to another using legal steps until it reaches a
state that satisfies the goal.

Four components:

Component      Meaning
Initial state
Operators      Where the problem starts

State space    The legal steps that change one state
               into another
Goal test
               All states reachable from the initial
               state

               A check for whether a state is an
               acceptable answer

The answer is the path — the sequence of operators used — not just the final state.
    The "instructions" that change one state into another are correctly called operators.

2. Traditional Process vs Continuous in ML

State space search is a traditional (classical) AI technique, and in that form it is discrete:
states are separate and countable, and we jump from one to the next by applying an
operator. A chess board is in one arrangement or another, never in between.

In machine learning the same idea of searching a space applies, but the space is
continuous. The state is a set of parameter values (for example neural network weights),
which are real numbers, so infinitely many states lie between any two. They cannot be
listed or expanded one by one. Instead the search takes small steps guided by
optimisation methods such as gradient descent, and the goal becomes a region of low
error rather than one exact state.

Same concept in both cases: find a good configuration inside a space of possible
configurations. Only the shape of the space and the way we move through it differ.

3. What Is a State

A state is a possible solution configuration — a complete snapshot of the problem at one
moment, containing everything needed to decide what can happen next.

• Every state is a candidate answer; the goal state is the one that passes the goal test.
• States are written compactly, for example a tuple (2, 4) .
• Two states are the same if their contents are identical, even if reached by different

     paths. This is what allows repeated work to be pruned.

4. Why Graphical and Simplex Methods Cannot Be Used

These come from Linear Programming and assume a linear objective, linear constraints,
continuous variables, and a convex feasible region.

The world is not linear. Real relationships are curved, conditional and interacting, so no
straight line can express them. In addition:

• Many states are discrete, not continuous — a jug holds 2 litres or 3, never 2.4 as a

     meaningful answer.

• The answer is a sequence of actions, not a single point. LP returns values, not a plan.
• Constraints are logical rules ("you cannot pour into a full jug"), not linear inequalities.
• The graphical method only works for two or three variables.
• In a non-convex space, a corner point is not guaranteed to be the optimum, so simplex

     logic fails.

Therefore we must explore the space step by step instead of solving it algebraically.

5. Search Strategies

Uninformed (blind / exhaustive / brute force) search knows only the operators and the
goal test. It cannot tell which state is closer to the goal. BFS and DFS belong here.

    Breadth First Search (BFS)hu

Explores the tree level by level — every state at depth 1, then every state at depth 2, and
so on.

• Data structure: queue (First In, First Out)
• Visited list: record of generated states, used to prune repeats

Steps:

 1. Put the initial state in the queue and mark it visited.
 2. Remove the front state. If it passes the goal test, stop and return the path.
 3. Apply every operator to it.
 4. Discard successors that cause no change or are already visited.
 5. Add the rest to the back of the queue, mark them visited, and repeat.

• Complete: yes.
• Optimal: yes, with equal step costs.
• Time and space: O(bd), where b is the branching factor and d the depth of the goal.
• Its main weakness is memory, since a whole level must be held at once.

Depth First Search (DFS)

Follows one branch as deep as possible, then backtracks to the most recent state with an
unexplored option.

• Data structure: stack (Last In, First Out), or recursion
• Complete: no, it can loop forever in a deep or cyclic space.

• Optimal: no.
• Time: O(bm).
• Space: O(b⋅ m). Its strength is low memory use.

Aspect         BFS         DFS
Order
Structure      Level by level (wide) Branch by branch (deep)
Shortest path
Memory         Queue       Stack

               Guaranteed  Not guaranteed

               High        Low

Heuristics

A heuristic h(n) estimates how close a state is to the goal; a lower value means a more
promising state. It lets the search expand promising states first instead of treating all
states equally, which greatly reduces the number of expansions. Examples: straight line
distance to a destination, or the number of misplaced tiles in the 8-puzzle. A heuristic is an
estimate, not a guarantee. Greedy Best First Search and A* are built on this idea.

6. BFS Example: The Two Jug Problem

Problem

Two jugs with no markings: 3 litres and 4 litres, with unlimited water. Measure exactly 2
litres.

• State: (x, y) where x is the amount in the 3L jug and y the amount in the 4L jug
• Initial state: (0,0)
• Goal: (2,0) or (0,2)

Operators (always try in this order)

No.            Operator    Result

1              Fill 3L     (3, y)

2              Fill 4L     (x, 4)

3              Empty 3L    (0, y)

4              Empty 4L    (x, 0)

5              Pour 3 → 4  pour until the 4L jug is full or

                           the 3L jug is empty

6              Pour 4 → 3  pour until the 3L jug is full or

                           the 4L jug is empty

A successor is discarded if it produces no change, or if it is already visited (pruned,
otherwise the search would repeat work and loop).

Queue Trace

Level  Queue          Expanded          New states added
0                                        (3,0) , (0,4)
1      (0,0)          (0,0)              (3,4) , (0,3) , (3,1)
2                                        (3,3) , (0,1)
3      (3,0) , (0,4)  both               (2,4) , (1,0)
4                                        (2,0) — goal
       (3,4) , (0,3) , (3,1) all three

       (3,3) , (0,1)  both

       (2,4) , (1,0)  (2,4)

Eleven states out of twenty were generated. The rest were never needed.

What the Example Shows

• BFS is blind: it never knew (3,3) was better than (3,4) ; it expanded both because

     both were on the same level.

• Pruning is essential: without the visited list, (3,0) would regenerate (0,0) , which

     would regenerate (3,0) , looping forever. It also removed the duplicate (3,4) that
     two parents both produced.

• The first goal found is the shortest, because no level is skipped.
• The cost is memory: a whole level must be stored at once, which is why heuristic

     search was developed.

7. Summary

• State space search = states joined by operators, explored from an initial state to a goal

     state.

• A state is a possible solution configuration.
• Classical search is discrete; ML searches a continuous parameter space using

     optimisation.

• Graphical and simplex methods fail because they assume linear, continuous, convex

     problems, while real problems are non-linear, discrete and rule based.

• BFS: queue, level by level, shortest path guaranteed, heavy memory use.
• DFS: stack, deep first, light memory, no shortest path guarantee.
• Both are blind. Heuristics add problem knowledge to guide the search.
```


---

## 4 Genetic Algorithms  (`notion-page (1).pdf`)

```text
4. Genetic Algorithms

   In optimization, there are 3 must needed requirements for all problems.
    1. Decision Variables - What we need to optimize
    2. Objective function - What we expect at last
    3. Constraints - Limitations on what we can do or use

   Usually, when we know the first derivative(f ′(x)) of a function, we can find optimum value
   by finding the values of x which makes f ′(x) = 0.
   But in most of the cases , we can’t find the f ′(x). So we have to use other ways to solve

   those questions.

   For that, scientists found that we can solve these questions using how nature solves
   problems and how evolution made species survived throughout tough times. One of them
   is Genetic Algorithms.

  What is a genetic algorithm?

   First, what is a gene?

   A gene is a collection of nucleotides. They are organized in a pattern and that pattern
   decides whether this person is suitable to survive or now.
   In the same way, when people create genetic algorithms, they select a feasible solution for
   the problem and encode them in a finite characters.
   In GAs, objective function is called “fitness Function”.
   Each string inside a feasible solution is called as a phenotype. So each phenotype has a
   fitness value.

   Genetic Operators

   When we use genetic Algorithms, we use 3 operators to solve the problems. This can be
   easily explained using how humans receive genetic information from their parents.
   Selection

First, we have to select 2 people to breed. In the same way, we choose 2 answers from a
huge number of answers. It’s done through a probability proportionate to fitness of those.
For that, we usually use roulette wheel selection and fitness value of each gene.

Crossover
After we chose 2 samples, we need to make the result a product of both parents (Like we
have features from both mother and father). Usually what we do is find a separation
randomly and make 2 new child answers from them.

Mutation
For a difference from both parents, we change the value of each child (offspring) answer,
maybe a higher value or a smaller value.

After all these, we destroy answers with least fitness and do this same operations again
and again until some conditions are met (Termination condition).
```


---

## 5 Machine Learning  (`notion-page (2).pdf`)

```text
5. Machine Learning

   Machine learning (ML) is a branch of artificial intelligence where computers learn to spot
   patterns and make decisions from data, rather than following rigid, hand-written rules.

1. The Three Main Types of Machine Learning

Type                         How It Learns                                 Input Data                       Everyday
                                                                           Labeled data (inputs + target
Supervised Learning (SL)     Learns with a "teacher" by                    answers)                         Studying
                             studying questions paired with                                                 questions
                             correct answers.                              Unlabeled data (inputs only, no  answers o
                                                                           answers)
Unsupervised Learning (USL) Discovers hidden structures or                                                  Sorting a
                                            natural groupings on its own.  Feedback signals (rewards and    shape an
                                                                           penalties)                       their valu
Reinforcement Learning (RL)  Learns through trial and error
                             by taking actions in an                                                        Training a
                             environment.                                                                   good beh
                                                                                                            them for

• Supervised Learning (SL): You give the computer thousands of examples that include

     both the input and the right answer. Over time, the model learns the relationship
     between them so it can predict the answer for brand-new data it has never seen before.

• Unsupervised Learning (USL): The computer receives data with zero guide or answer

     keys. Its job is to explore the data, find underlying similarities, and group matching
     pieces together.

• Reinforcement Learning (RL): An autonomous system (called an agent) makes

     decisions inside an environment. When it takes a good action, it gets a reward; when it
     makes a mistake, it receives a penalty. It constantly updates its strategy to collect the
     highest possible reward over time.

2. Three Types of Supervised Learning

Supervised learning splits into tasks based on the kind of answer you want to predict:

• Classification (Predicting Categories): The target answer is a label, bucket, or

     category.

     ◦ How it works: The model draws decision boundaries between distinct classes. If

           there are only two choices (like Yes/No), it is binary classification; if there are three
           or more, it is multiclass classification.

     ◦ Examples: Filtering email into "Spam" vs. "Inbox", or scanning an X-ray to detect

           whether a bone fracture is present.

• Regression (Predicting Numbers): The target answer is a continuous numerical value.
     ◦ How it works: The algorithm fits a line or mathematical curve through past data

           points to estimate quantities on an unbroken scale.

     ◦ Examples: Estimating a house's selling price based on square footage and

           location, or predicting tomorrow's temperature in degrees.

• Time Series Predictions (Forecasting Sequences Over Time): The target is an

     ordered sequence where chronological order is the primary predictor.

     ◦ How it works: Unlike standard regression where data points are treated as

           independent events, time series models explicitly track time-based traits like
           seasonality (weekly or monthly cycles), long-term trends, and lag (how yesterday’s
           number directly impacts today’s).

     ◦ Examples: Forecasting electricity grid demand for the upcoming weekend, or

           projecting monthly inventory supply needs for retail stores.

3. Core Types of Unsupervised Learning (Not necessary)

Because unsupervised algorithms work without a teacher, they focus on finding patterns
and relationships:

• Clustering: Partitioning a dataset into natural groups where items in the same group

     are more similar to each other than to items in other groups.

     ◦ How it works: The algorithm calculates the mathematical similarity (or distance)

           between every data point and groups nearby neighbors together.

     ◦ Example: Customer segmentation — an online store grouping shoppers into

           "bargain hunters", "weekend casuals", and "luxury buyers" based on their
           browsing behavior, without anyone manually defining those groups beforehand.

• Association Rule Mining: Uncovering interesting relationships and "if-then"

     connections between items that frequently occur together.

     ◦ How it works: It scans transactions to measure how often items co-occur and

           checks if the presence of item $A$ reliably points to the purchase or presence of
           item $B$.

     ◦ Example: Market Basket Analysis — discovering that supermarket shoppers who

           purchase hamburger patties and buns also buy ketchup 80% of the time, helping
           stores optimize shelf layouts and promotional bundles.

4. Dimensions of Data and High-Dimensional Spaces

In machine learning, dimension simply means the number of attributes, variables, or
features recorded for each individual item.

                   Attribute = Feature = Dimension = Column

• 1 Dimension (1D): Only 1 feature measured (e.g., just height). The data sits on a single

     line.

• 2 Dimensions (2D): 2 features measured (e.g., height and weight). The data plots on a

     flat surface or chart.

• 3 Dimensions (3D): 3 features measured (e.g., height, weight, and shoe size). The data

     occupies a 3D physical space (a cube).

• High-Dimensional Space: When you track tens, hundreds, or thousands of features per

     item. For instance, a medical record with 200 lab metrics is a point in 200-dimensional
     space, and an image made of 1,000 pixels is a point in 1,000-dimensional space.

The Challenge: The "Curse of Dimensionality"

When data moves into high dimensions, intuitive geometry breaks down, creating three
practical problems:

 1. Extreme Sparsity (Empty Space): The volume of the space grows exponentially with
     each added dimension. Because the volume becomes enormous, data points end up
     isolated far away from one another. A dataset that comfortably fills a 2D square
     becomes virtually empty in a 50-dimensional space.

 2. Distance Measurements Lose Meaning: Most ML algorithms measure how close or far
     two points are (using distance formulas). In very high dimensions, almost every point
     ends up roughly the exact same distance from every other point. When all distances
     look identical, clustering and classification algorithms struggle to identify which items
     are truly related.

 3. Overfitting and High Compute Costs: With hundreds of variables, models require
     massive computational power and can easily pick up random noise as if it were a
     genuine pattern.

To solve this, machine learning uses dimensionality reduction techniques (such as
Principal Component Analysis or Autoencoders). These tools compress the data into fewer
dimensions while preserving the essential patterns that actually drive predictions.
```


---

## 6 Supervised Machine Learning  (`notion-page (3).pdf`)

```text
6. Supervised Machine Learning

   Linear regression and classification models build on a single idea: using mathematical
   functions to trace the path through real-world data points with as little error as possible.

  1. Linear Regression

Linear regression finds the best possible straight line (or flat plane) through a set of data
points to predict an unknown continuous number.
At its core, this is simply curve fitting using a known mathematical template:

                                        y^​ = w ⋅ x + b

• x (Input Feature): The information you feed the model (e.g., house size in square

     feet).

• y^​ (Prediction): The number the model outputs (e.g., estimated house price).
• w (Weight): The slope of the line. It controls how steep the line is and reflects how

     strongly the feature x affects the prediction.

• b (Bias): The offset or vertical intercept. It shifts the line up or down so it doesn't have

     to pass through (0, 0) . It acts as a baseline value when x = 0 .

Fitting the curve simply means sliding and tilting the line by testing different values of w
and b until it sits as close to every actual data point as possible.

2. The Error Function: Sum of Squared Errors (SSE)

To know whether a line fits well, the computer needs a score sheet. That score sheet is
called an error function (or loss function).

For every data point i :

1. The real value is y .i​

2. The model's prediction is y^i​ ​ .

3.  The gap between them is the error:          ei ​  =  y − y^ i​i .​​

The Sum of Squared Errors (SSE) squares each individual mistake and adds them all
together:

                            n                         n                                     2

    SSE  =                  ∑(y​  i​  −  y^ )2i​​=    ∑ (y ​  i​  −    (w  ⋅  xi ​  +  b))

                            i=1                       i=1

Why square the errors?

• Cancels signs: If one point is 5 units above the line and another is 5 units below,

     simply adding them would give zero error ( +5 - 5 = 0 ). Squaring turns all errors positive
     ( 25 + 25 = 50 ).

• Penalizes big mistakes: Squaring turns an error of 2 into 4 , but an error of 10 into

     100 . This forces the algorithm to avoid extreme misses.

Why SSE is a function of weights and biases
In any training dataset, the actual data points (xi,​ yi)​ are permanent facts; they never

change. The only variables you can adjust are the slope w and the intercept b .

Because of this, SSE(w, b) forms a bowl-shaped surface. Finding the "best fit" line means

finding the specific pair of (w, b) values that sits at the very bottom of that bowl, where
error is lowest.

3. Underfitting (High Bias) vs. Overfitting (High Variance)

When fitting a curve through data, models struggle with two common failure modes:

Underfitting (High Bias)

• What happens: The model is far too simple to capture the underlying pattern (e.g.,

     forcing a rigid straight line onto data that naturally curves like an S).

• The meaning of "Bias": The algorithm brings rigid, false assumptions to the table and

     ignores what the data is actually trying to show.

• Result: High error on training data, and high error on new, unseen test data.

Overfitting (High Variance)

• What happens: The model is overly complex and flexible (e.g., using a high-degree

     polynomial that zigzags to touch every single dot). It memorizes background noise and
     random flukes instead of the true pattern.

• The meaning of "Variance": If you trained this model on a slightly different sample of

     data, the fitted curve would swing wildly and look completely different.

• Result: Near-zero error on training data, but huge error on new test data because it

     cannot generalize.

The Sweet Spot (Balanced Fit)

A good model captures the broad underlying shape of the data while smoothly ignoring
random noise and outliers.

4. How Training Works: Learning Rate and
Backpropagation

Training is the automated process of rolling down the SSE error bowl to reach the lowest
point (the minimum error).

Gradient Descent & Learning Rate

 1. The model starts with random guesses for w and b .
 2. It checks the slope of the error bowl at its current position (the gradient), which points

     downhill toward lower error.
 3. It takes a small step in the downhill direction to update w and b .

The size of that step is controlled by the Learning Rate (α):

• Too large: The model takes giant leaps, jumps back and forth across the valley, misses

     the bottom entirely, and may spiral out of control.

• Too small: The model takes microscopic steps. Training takes hours or days, and it risks

     stalling before reaching the bottom.

5. Logistic Regression: Classification via Probabilities

Despite having the word "regression" in its name, logistic regression is a classification
algorithm. It is used to predict the likelihood that an input belongs to a specific category—
most commonly a binary choice such as Yes/No, Spam/Not Spam, or Pass/Fail.

    1. Why Not Just Use a Straight Line?

If you try to classify data using linear regression ( y = w ⋅ x + b ), you run into two major

issues:

• Unbounded Outputs: A straight line continues forever in both directions. It can output

     values like -1.5 or +3.2 . But a probability must always stay strictly between 0 (0%)
     and 1 (100%).

• Sensitivity to Outliers: Adding a single extreme data point far to the right or left tilts

    the entire straight line, shifting the cutoff point and causing correct classifications to
    become wrong.

   2. The Sigmoid (Logistic) Function

To solve this, logistic regression calculates the standard linear combination first:

                                       z = w⋅x+b

Then, instead of outputting z directly, it feeds z into a special mathematical curve
called the Sigmoid function (denoted as \sigma ):

                                                 1
                              y^​ = σ(z) = 1 + e−z ​

This function acts like a numerical clamp:

• Large positive z : e−z approaches 0 , so σ(z) approaches 1 (100%).

• Large negative z : e−z grows massive, so the denominator explodes and \sigma(z)

   approaches 0 (0%).

•  When  z  =  0  :  σ(0)  =   1     =  0.5  (50%).
                              1+1 ​

No matter how large or small the input number is, the Sigmoid function squashes it into a
smooth, S-shaped curve strictly contained between 0 and 1 .

    3. Turning Probabilities into Decisions (The Decision Boundary)

Once the model calculates a probability, it uses a decision threshold (by default, 0.5 ) to
make a final categorical call:

                                       1 if y^​ ≥ 0.5
               Prediction = { ​
                                                                   ​

                                       0 if y^​ < 0.5

• If the model estimates an email has a 0.82 (82%) chance of being spam, it classifies it

     as Spam ( 1 ).

• If the estimate is 0.15 (15%), it classifies it as Inbox ( 0 ).

The exact line or surface where z = 0 (and probability equals 0.5 ) is called the decision
boundary. Data on one side of this boundary gets labeled Class 1, and data on the other
side gets labeled Class 0.

6. Linear Regression vs. Logistic Regression

Despite sharing the word "regression" in their names, these two algorithms serve
fundamentally different goals.

Feature        Linear Regression                           Logistic Regression
Primary Task
Target Output  Regression (predicting                      Classification (predicting
Core Equation  continuous amounts)                         categories / labels)

               Any continuous number                       A probability score strictly
                                                           bounded between 0 and 1
               (−∞ to + ∞ )
                                                           y^ = ​           1        (Sigmoid
               y^​ = w ⋅ x + b                                        1+e−(w⋅x+b) ​

                                                           function)

Typical Use Case Predicting house prices, stock            Predicting whether an email is
                           values, or outdoor temperature  spam (0 or 1), or a tumor is
                                                           malignant
```


---

## 7 Neural Networks  (`o.pdf`)

```text
7. Neural Networks

   An artificial neural network is a network of simple processing units called neurons (or
   nodes) wired together in layers, loosely inspired by the human brain.

  1. How Logistic Regression Connects to Neural Networks

   Logistic regression is simply an artificial neural network with a single neuron.

           Input Features (x1,​ x2,​ … ) ⟶ [Weighted Sum + Bias] ⟶
                    [Sigmoid Function] ⟶ Output Probability (y^)​

   • A Single Neuron: Takes multiple inputs, assigns a weight to each, adds a bias, and runs

         the result through a Sigmoid curve to output a probability between 0 and 1. That is the
         exact mathematical definition of logistic regression.

   • A Neural Network: Takes that single building block and duplicates it hundreds or

         millions of times. By arranging neurons into an input layer, one or more hidden layers,
         and an output layer, the network can solve problems with complex curves and non-
         linear patterns that a single logistic regression unit cannot handle.

  2. Inside a Neuron: Aggregation and Activation

   Every individual neuron in a network processes information in two distinct, sequential
   steps:

Step 1: Aggregation (The Weighted Sum)

The neuron gathers all incoming signals, scales each one by its importance, and adds a
baseline offset:

      n

z  =  ∑(w ​  i​  ⋅  xi )​  +  b  =  (w x1 1 ​  ​  +  w x2 2 ​  ​  +  ⋯  +  ​w x ) n n ​ +  b

      i=1

• Each input xi​ has a dedicated weight (wi)​ that amplifies or suppresses that signal.

• The bias (b) acts as an internal baseline, shifting the combined signal up or down.

Step 2: Activation (The Output Filter)
The raw sum z is passed into an activation function f (z) to produce the neuron's final

output:

                                           a = f (z)

The activation function decides how strongly this neuron should "fire" its signal forward to
the next layer. Without this step, stacking multiple layers would just be adding straight
lines together, which collapses mathematically into another straight line.

3. The Biological Parallel: How Real Brain Cells Work

Artificial neural networks borrow their structure directly from biological neurons in the
human nervous system:

Biological Element What It Does in the Body            Artificial Counterpart

Dendrites         Branch-like fibers that receive      Inputs (x)
                  incoming chemical signals from
                  neighboring cells.

Synapse Strength  The physical connection gap          Weights ( w )
                  between neurons; can grow
                  stronger or weaker with
                  experience.

Cell Body (Soma)  Pools and aggregates electrical      Summation / Aggregation ( Σ )
                  charges arriving through all
                  dendrites.

Axon Hillock      Checks if total incoming charge      Activation Function ( f ) & Bias ( b
                  crosses a physical threshold (about  )

                  −55 mV).

Axon              The output cable that fires an       Neuron Output ( a or y )
                  electrical spike (action potential)
                  to the next cells.

A Real-Life Incident: Touching a Warm Mug vs. a Hot Stove

• Warm Mug: Your finger's heat receptors send weak signals. Your sensory neurons

     aggregate these charges, but they barely hover near the threshold. The neurons fire
     slowly and intermittently, letting you know it is safe to hold.

• Hot Stove: Intense thermal energy triggers an huge amount of incoming signals across

     thousands of dendrites. The total charge at the soma easily blows past the threshold.
     The neuron fires a rapid, maximum-strength action potential down its axon,
     commanding your hand muscles to pull back instantly.

Biological neurons follow an "all-or-none" law: a neuron either fires completely or does
not fire at all. Activation functions in artificial networks are a smoothed mathematical
version of this firing mechanism.

4. How the Network Learns: Weight Training and Epochs

A neural network does not start out smart; it learns by trial, error, and repetition.

• Weight Training:

       1. The network starts with small, randomized weights and biases.
       2. It runs data through the network to make a guess (Forward Pass).
       3. It calculates how far the guess is from the correct answer using a loss function.
       4. It works backward to calculate the error share of every weight (Backpropagation).
       5. It uses an optimization algorithm (like Gradient Descent) to nudge the weights in

           the direction that lowers the error.

• Epoch: One complete cycle where the entire training dataset has passed through the

     network forward and backward once.

     ◦ Why we need multiple epochs: A network cannot absorb every pattern in a single

           pass. Just as a human needs to read a textbook chapter several times to
           remember the details, a model needs dozens or hundreds of epochs to gradually
           steer its weights into their optimal values.

5. Output Activation Functions: Regression vs.
Classification

While hidden layers typically use non-linear functions (like ReLU) to capture complex
shapes, the output layer's activation function is chosen based on the final task:

Linear Activation Function (For Regression)

The linear activation function does not transform or squash the signal at all:

 f(z) = z

• Output Range: Any real number (−∞ to + ∞).
• When to use it: At the output layer of Regression tasks where the target is a

     continuous, unbounded quantity (e.g., predicting house prices, temperature, revenue,
     or car speed).

Sigmoid Activation Function (For Binary Classification)

The Sigmoid function compresses the aggregated sum into an S-shaped curve:

                                                    1
                                      σ(z) = 1 + e−z ​

• Output Range: Strictly between 0 and 1.
• When to use it: At the output layer of Binary Classification tasks. The number

     represents a probability (e.g., a 0.88 value means an 88\% chance an image contains a
     tumor), allowing a simple cutoff threshold like 0.5 to make the final decision.

Detailed Breakdown of Each Function

1. Linear Activation: f (z) = z​

The linear activation does not alter the neuron's input; what enters is exactly what leaves.

• How it behaves: If the input is 5 , the output is 5 . If the input is -12.4 , the output is

     -12.4 .

• Best used for: The output layer of regression models, where the goal is to predict an

     unbounded, continuous value (like house prices or temperatures).

• Major limitation: If used in hidden layers, stacking multiple linear layers collapses

     mathematically into a single linear equation. A network with only linear activations
     cannot learn curves, boundaries, or complex real-world relationships.

2. Sigmoid Activation:  f (z) =     1   ​  ​
                                 1+e−z

Sigmoid squashes any real number into an S-shaped curve between 0 and 1 .

• How it behaves: Large positive numbers approach 1 , large negative numbers

    approach 0 , and 0 becomes exactly 0.5 .

• Best used for: The output layer of binary classification models, because its output

    directly maps to a probability (from 0% to 100%).

• Major limitations:
    ◦ Vanishing Gradients: When inputs are very large or very small, the curve

          becomes nearly flat. The derivative (slope) in these flat regions drops close to
          zero, causing backpropagation to stop updating weights in early layers.

    ◦ Not Zero-Centered: Because all outputs are positive numbers between 0 and 1 ,

          the gradients during backpropagation all take the same sign (all positive or all
          negative), forcing weights to update in an inefficient zig-zag path.

3. Tanh (Hyperbolic Tangent):    f (z) =      ez  −e−z  ​  ​
                                              ez  +e−z

Tanh is a scaled and shifted version of the Sigmoid function that squashes numbers
between -1 and +1 .

• How it behaves: It maintains an S-shaped curve like Sigmoid, but crosses (0, 0) .

    Negative inputs yield negative outputs, and positive inputs yield positive outputs.

• Advantage over Sigmoid: Because its outputs are centered around zero, the average

    output is close to 0 . This balances weight updates and speeds up training convergence.

• Major limitation: It still flattens out completely when inputs are very high or very low,

    meaning it still suffers heavily from the vanishing gradient problem in deep networks.

4. ReLU (Rectified Linear Unit): f (z) = max(0, z)​

ReLU acts like a one-way electrical valve: it blocks all negative numbers and allows all
positive numbers to pass straight through unchanged.

• How it behaves: If z ≤ 0 , the output is 0 . If z > 0 , the output is simply z .
• Why it dominates modern deep learning:

     ◦ Computationally Cheap: Calculating max(0, z) requires just a simple if

         check, avoiding expensive exponential calculations (ez).

     ◦ No Saturation for Positive Numbers: For positive values, the slope is a constant

           1 . Gradients never shrink or vanish, allowing networks with dozens or hundreds
           of layers to train quickly and reliably.

     ◦ Sparse Activation: Turning negative values to zero keeps many neurons dormant

           at any given time, making the network lightweight and efficient.

• Major limitation (The "Dying ReLU" Problem): If a neuron's weights update in a way

     that its input is always negative, it will consistently output 0 with a slope of 0 . That
     neuron effectively "dies" and permanently stops learning.

Side-by-Side Comparison

Activation Function Mathematical Formula Output Range  Zero-Centered? Vanishing Gradient?
                                                       Yes (if input is) No
Linear   f (z) = z            (−∞, +∞)                 No (all positive) Severe at extremes
Sigmoid
         f (z)  =     1       (0, 1)
                   1+e−z ​

Tanh     f (z)  =  ez −e−z    (-1, 1)                  Yes  Severe at extremes
                   ez +e−z ​

ReLU     f (z) = max(0, z)    [0, +∞)                  No   None for z > 0 ; freezes if z ≤
```
