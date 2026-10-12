# AI Peer Made Notes 1 (converted from HTML)

Source: `Peer Made Notes 1/lesson01..12_*.html` (JS-driven tabbed notes; text of every tab extracted; diagrams marked [diagram]; quizzes included where present). Numbering is the notes' own (12 lessons).


---

# lesson01_introduction_to_ai.html  (Lesson 1: Introduction to AI | AI Notes)


## Tab 1: What is AI?

What is AI?
⚡ At a glance
🧠 Idea: AI means making machines do things that normally need human thinking.
🧪 Example: Face unlock on a phone recognises your face. A chess program picks the best move.
✅ Remember: Only narrow AI (ANI) exists today. General AI (AGI) and super AI (ASI) are still ideas.

Artificial Intelligence (AI) is the science of making machines do tasks that normally need a human brain: thinking, learning, seeing, understanding speech and making decisions.

Start with a picture
Think of a calculator. It is brilliant at one thing: adding and multiplying. But it cannot recognise your face, play chess or hold a conversation. Now think of a person. A person can learn to do almost anything. AI sits somewhere between these two pictures. That is why we describe AI in three levels.

ANI
Artificial Narrow Intelligence (also called "weak AI")
Does one job very well.
Face unlock, spam filter, translator, chess engine.
This is all the AI that exists today.

AGI
Artificial General Intelligence (also called "strong AI")
Could learn and do any thinking job a human can.
Does not exist yet.

ASI
Artificial Super Intelligence
Would be smarter than all humans at everything, even creativity and feelings.
Does not exist yet.

🌍 Memory trick: Narrow = one job. General = any job, like a human. Super = better than every human.

Why is it called a "disruptive technology"?
"Disruptive" means it does not just make old tools a little better. It changes how whole industries work, like smartphones changed cameras, maps and shopping.

Examples of disruptive technologies: AI, smartphones, cloud computing, blockchain and the internet. Another example is blockchain. For a long time, centralization (one authority holds and controls the data) was the base of modern technology. Blockchain introduced decentralization (no single owner) as an alternative. Both systems exist side by side, and the choice depends on the use case.

Why do we need to study AI?
To face disruptive technologies and to create new products and tools. AI can give better solutions to the problems we face (often by optimization: finding the best answer). AI is the science of developing techniques to generate intelligence artificially. A simple picture: humans have a "carbon brain" and AI is a "silicon brain".

Strong AI and weak AI (older names)

- Strong AI: a machine that is truly thinking like a human brain, with the functionality of a real human brain. (This is close to what we now call AGI.)
- Weak AI: a machine that pretends to be intelligent and performs a function, such as browsing the internet, disease detection or the recommendations on a shopping site. (This is close to ANI.)

More examples of narrow AI (ANI): voice assistants like Siri and Alexa, Google Maps and face recognition systems. AGI would be able to learn new tasks without being retrained. A hypothetical example is a robot that can study, cook, drive and solve problems like a human.

Check yourself 1
A chess program is which type of AI? Answer: ANI, because it does only one job.

Check yourself 2
Which type of AI could do any thinking task a human can? Answer: AGI. It does not exist yet.

## Tab 2: A short history

A short history of AI
⚡ At a glance
🧠 Idea: AI got its name in 1956. World War II pushed computers forward.
🧪 Example: Alan Turing helped break the Enigma code. In 1959 Arthur Samuel's checkers program learned to beat its own creator.
✅ Remember: 1950 Turing Test. 1956 the name "AI" (McCarthy). 1959 the name "Machine Learning" (Samuel).

AI did not appear overnight. A few key moments explain where it came from.

1939 to 1945: World War II. Wars need fast thinking. Enigma was a German machine that scrambled messages into secret code. Alan Turing helped build a machine called the Bombe to find the settings and break the code. Colossus and ENIAC became some of the first electronic computers.

1943. McCulloch and Pitts made the first maths model of an artificial neuron. (You will see neurons again in Lesson 7.)

1948. Norbert Wiener wrote about Cybernetics: systems that sense, adjust and act in a loop. A thermostat is a simple example: it senses the temperature and switches the heater on or off.

1950. Alan Turing asked, "Can machines think?" and proposed the Turing Test.

1956. The Dartmouth Conference. John McCarthy named the field "Artificial Intelligence". (He also made LISP, an early AI programming language.) Marvin Minsky helped found the field and the MIT AI Lab.

1959. Arthur Samuel at IBM named "Machine Learning": computers learning without being given every step. His checkers program learned to beat its creator.

The Turing Test, in simple words
A judge chats by text with two hidden players: a human and a machine. If the judge cannot tell which is the machine, the machine passes. It tests whether a machine behaves like a human, not whether it truly understands.

🌍 Analogy: a phone call where you must guess whether the voice is a real person or a robot.

A challenge to the Turing Test: the Chinese Room (John Searle)
Imagine a person who does not understand Chinese, sitting in a room with a huge, very powerful rule book (a knowledge base). Questions written in Chinese are passed in. The person looks up the rules, follows them (a mapping function from question to answer) and passes out perfect answers in Chinese. To someone outside, it looks as if the person understands Chinese. But inside, nobody understands anything: they are just following rules.

Searle's point: a computer can act intelligent without really being intelligent. It may pass a test like the Turing Test just by following rules, without any understanding.

🌍 Analogy: a parrot that repeats perfect sentences. It sounds clever, but it does not know what the words mean.

Check yourself 1
Who named "Artificial Intelligence", and in which year? Answer: John McCarthy, 1956.

Check yourself 2
When does a machine pass the Turing Test? Answer: When the judge cannot tell it apart from the human.

## Tab 3: Rules vs data

Two ways to build AI: rules or data
⚡ At a glance
🧠 Idea: Old AI follows rules that people write. New AI learns the rules from examples.
🧪 Example: Rule-based: "If the email says WIN MONEY, it is spam." Data-driven: learn from 10,000 emails already marked spam or not spam.
✅ Remember: Data-driven AI wins today because of big data and fast computers.

There are two big ways to build an AI system. Understanding the difference is the key to this whole module.

Way 1: write the rules (GOFAI)
GOFAI means "Good Old-Fashioned AI". Experts write the rules by hand and the computer follows them. It is also called rule-based or symbolic AI. An expert system is a program that stores an expert's rules, such as "if fever and rash, then possible measles".

Rule-based approach: facts and rules are written with symbols. Example: IF temperature > 38&deg;C THEN the patient has a fever. Rule-based programming languages include Prolog and LISP (LISP is not rule-based by default but can be used for rule-based AI; McCarthy created it to implement these ideas).

Data-driven approach: we have lots of data, and from the data we find patterns in the environment, with a continuous feed of new data. Today the rule-based approach is called GOFAI and the data-driven approach is called Machine Learning.

Way 2: learn from data
Nobody writes the rules. We show the computer thousands of examples and it finds the pattern itself.

🌍 Analogy: Rule-based AI is cooking from a recipe book: you follow exact steps someone wrote. Data-driven AI is a child learning what a dog is by seeing many dogs. Nobody gave the child a rule book.

Why does data-driven AI work so well today?

- Lots of data from phones, websites and sensors.
- Huge computing power. A GPU is a chip that does thousands of small calculations at the same time. A TPU is a chip made by Google for AI maths. Cloud computing means renting powerful computers over the internet.

Big data and the 3 Vs
"Big data" is described with three words (Doug Laney, 2001):

📦 Volume
How much data
⚡ Velocity
How fast new data arrives
🎨 Variety
How many types: tables, text, video, audio

🌍 Analogy: a river. Volume = how much water. Velocity = how fast it flows. Variety = what floats in it: fish, leaves, plastic.

Check yourself 1
What does GOFAI use? Answer: Rules written by people.

Check yourself 2
Name the 3 Vs. Answer: Volume, Velocity, Variety.

## Tab 4: How machines learn

How a machine learns: the StatQuest story
⚡ At a glance
🧠 Idea: Build a model from training data. Judge it on testing data it has never seen.
🧪 Example: A wiggly line can fit the training dots perfectly and still predict new dots badly.
✅ Remember: Choose a method by how well it does on testing data, not by how fancy it is.

🎬 StatQuest: "A Gentle Introduction to Machine Learning"
The video says machine learning is all about making predictions and classifications. It shows this with two examples, a decision tree and a line fitted to dots, and then makes one big point: to decide which method is best, test it on data it has not seen. The three parts below follow the video.

Part 1: a decision tree (classification)
A decision tree is a set of yes/no questions that ends in a prediction. In the video, a silly tree predicts whether a person will love StatQuest:

Do they like machine learning?
 ├─ Yes → they will love StatQuest
 └─ No  → Do they like statistics?
          ├─ Yes → they will love StatQuest
          └─ No  → they might not love StatQuest

(In the video the tree also asks about silly songs first, but the answers lead to the same result. The idea is what matters: questions lead to a prediction.) Classification means predicting a category, like "will love" or "will not love".

Part 2: a line fitted to dots (prediction of a number)
The video imagines measuring how much yam people eat and how fast they run the 100 metres. Each person is a dot. A straight line through the dots shows the trend: more yam, faster running. To predict, you read a new person's yam amount, go to the line, and read off the predicted speed. This is called regression (predicting a number).

Part 3: training data and testing data
The dots we use to build the model are the training data. We draw two lines on them:

- A straight black line that goes through the middle of the dots, missing some of them a little.
- A wiggly green squiggle that touches almost every training dot, so it fits the training data better.

Which is better? You cannot tell from the training dots alone. So we measure new people that the model has never seen. These are the testing data. For each new person, measure the distance between the prediction and the real speed, then add up all the distances. This is the total error.

Model | Total error on training data | Total error on testing data
Straight black line | 8 | 12
Wiggly green squiggle | 0 | 30

(These numbers are an example to show the pattern.) The squiggle looks perfect on the training data (error 0) but is much worse on the testing data (error 30). The black line is the better model, because it predicts new people better. When a model fits the training data very well but predicts new data badly, we call it overfitting. It has memorised the training dots, including their random wiggles.

🌍 Analogy: practice papers and the real exam. Training data = practice papers. Testing data = the real exam with new questions. A student who memorises the answers of the practice papers may score 100% at home and still fail the real exam.

The big message

- There are many fancy machine learning methods (deep learning, neural networks, and new ones every year).
- The most important thing is not how fancy the method is. It is how well it predicts the testing data.
- So we try several methods, test each one on the testing data, and pick the best.
- Which dots become training and which become testing is a choice. There are proper ways to decide the split (you will see 80% training and 20% testing in Lesson 5).

Check yourself 1
A model has training error 0 and testing error 30. Another has training error 8 and testing error 12. Which is better? Answer: The second one, because it predicts unseen data better. The first is overfitting.

Check yourself 2
What do we use testing data for? Answer: To measure how well a model predicts data it has never seen, so we can choose the best method.

## Tab 5: The AI map

The AI map: how the big words fit together
⚡ At a glance
🧠 Idea: AI is the big umbrella. Machine learning sits inside it, then neural networks, then deep learning.
🧪 Example: ChatGPT is a transformer, which is a kind of deep learning model.
✅ Remember: AI contains ML, which contains NN, which contains DL.

You will hear many big words: AI, ML, neural networks, deep learning. They are not separate things. They fit inside each other like Russian dolls.

AI (the whole umbrella)ML: learns from dataNN: neural networks, brain-inspiredDL: deep learning, networks with many layersTransformers (used in ChatGPT)

- Neural network (NN): layers of simple connected units that pass numbers along, loosely inspired by the brain.
- Deep learning (DL): a neural network with many layers.
- Transformer: a deep learning model that reads all the words of a text together and decides which words matter to each other.

Other AI methods that sit beside machine learning
GA
Genetic Algorithms: copy evolution to find good answers (Lesson 4)
SI
Swarm Intelligence: copy ants and birds
FL
Fuzzy Logic: "degrees of true" instead of only true or false
RB
Rule-Based systems (the GOFAI style)

These methods can be mixed (hybridized). For example, Learning Classifier Systems (LCS) combine ideas from genetic algorithms and machine learning.

Check yourself 1
Put in order, biggest to smallest: DL, AI, NN, ML. Answer: AI, ML, NN, DL.

Check yourself 2
What does "deep" mean in deep learning? Answer: The neural network has many layers.

## Tab 6: Predict or create

Predictive AI and Generative AI
⚡ At a glance
🧠 Idea: Predictive AI answers questions about data. Generative AI makes new things.
🧪 Example: Predict a house price (regression). Write a poem (generative).
✅ Remember: A label means classification. A number means regression. A future value means time series.

Most AI does one of two jobs: it predicts something from data, or it creates something new.

🌍 Analogy: Predictive AI is an examiner who checks and labels things. Generative AI is an artist who makes something new.

Predictive AI: three kinds
Kind | The answer is... | Example
Classification | A category | Is this email spam or not?
Regression | A number | What will this house sell for?
Time series forecasting | A future value, using past values in time order | What will tomorrow's temperature be?

Generative AI
It creates new text, images, audio, video or code. For example, ChatGPT writes text one word at a time, and music-generation AI makes new songs. This is also called Gen AI.

Predictive AI is also called discriminative AI: it is used to classify or predict something from input data, such as email spam detection or face recognition.

Check yourself 1
Predicting a student's final mark out of 100 is which kind? Answer: Regression, because the answer is a number.

Check yourself 2
Deciding if a photo shows a cat or a dog is which kind? Answer: Classification, because the answer is a category.

## Tab 7: AI agents

How AI interacts with the world
⚡ At a glance
🧠 Idea: An AI system senses, thinks and acts in a loop.
🧪 Example: Robot vacuum: a bump sensor feels a wall, the system picks a new path, the wheels turn.
✅ Remember: Sensors in, system decides, actuators out.

An AI system often works as a loop: it senses the world, decides what to do, and acts. Then it senses again.

👀 Sensors
camera, microphone
➜🧠 Intelligent system
decides
➜🦾 Actuators
motors, outputs

🌍 Analogy: you. Your eyes and ears sense. Your brain decides. Your hands and legs act. Then you look again.

Embodied and disembodied AI
🚗 Embodied AI
Has a physical body and acts in the real world.
A self-driving car, a robot vacuum.
💬 Disembodied AI
Software only, with no body.
ChatGPT, a spam filter.

More examples: embodied AI includes self-driving cars and humanoid robots. Disembodied AI includes ChatGPT and Google Translate.

Check yourself 1
What do actuators do? Answer: They act on the world, like motors and wheels.

Check yourself 2
Is a spam filter embodied or disembodied? Answer: Disembodied, because it is software only.

## Tab 8: Words list

Hard words in one place
⚡ At a glance
🧠 Idea: A quick reference for the difficult words in this lesson.
🧪 Example: GPU = a chip that does thousands of small calculations at the same time.
✅ Remember: Come back here whenever a word is unclear.

Word | Plain meaning

Algorithm | Step-by-step instructions to solve a problem, like a recipe

Enigma | A German machine that scrambled messages into secret code in WWII

Bombe | Turing's machine that helped break the Enigma code

Colossus, ENIAC | Among the first electronic computers (1940s)

Cybernetics | Systems that sense, adjust and act in a loop, like a thermostat

LISP, Prolog | Old programming languages made for AI

Expert system | A program that stores an expert's if-then rules

GPU, TPU | Chips that do thousands of small calculations at once. Great for AI maths.

Cloud computing | Renting powerful computers over the internet

Model | The pattern a machine learns from data

Training data | The examples used to build a model

Testing data | New examples used only to check the model

Overfitting | Fitting the training data too closely, so new data is predicted badly

Decision tree | A set of yes/no questions that leads to a prediction

---

# lesson02_prompting.html  (Lesson 2: Prompting | AI Notes)


## Tab 1: What is a prompt?

Lesson 2: Talking to an AI
⚡ At a glance
🧠 Idea: A prompt is the instruction you type to an AI. A clear prompt gets a better answer.
🧪 Example: "Write an email" gives a boring answer. "Write a 100-word friendly email to a customer about a late delivery" gives a useful one.
✅ Remember: The AI cannot read your mind. It only knows what you tell it.

A prompt is the text you type to tell an AI what to do. Prompt engineering means writing it clearly so you get a good answer the first time.

Start with a picture
🌍 Analogy: taxi directions. If you tell a taxi driver "take me somewhere", you get nowhere useful. If you say "take me to the airport by the fastest road, I have 2 bags", you get exactly what you need. The AI is the driver. Your prompt is the directions.

Vague prompt vs clear prompt
❌ Vague
"Write an email about saving money."
The AI does not know who is writing, who will read it, how long it should be or what style to use. So it guesses, and you get a long, dull, generic email.

✅ Clear
"You are a friendly finance coach. Write a short email with 3 tips to save money on groceries, for busy college students. Under 150 words, casual tone, bullet points."

The clear prompt answers questions the AI would otherwise have to guess: Who am I? What must I do? Who is reading? How long? What style? The next tab turns these questions into a simple memory framework.

Check yourself 1
Why does a vague prompt give a generic answer? Answer: The AI has to guess the missing details, so it gives a general answer.

Check yourself 2
What is prompt engineering? Answer: Writing the prompt clearly so the AI gives a good answer the first time.

## Tab 2: The TRADE framework

TRADE: five parts of a great prompt
⚡ At a glance
🧠 Idea: TRADE lists the five things a good prompt tells the AI.
🧪 Example: Task: write 3 tips. Role: finance coach. Audience: students. Details: under 150 words. Example: a sample tip.
✅ Remember: Task, Role, Audience, Details, Example.

🌍 Analogy: briefing a new employee. Tell them the task, who they are acting as (role), who the customer is (audience), the rules (details), and show an example of good work. Then they get it right the first time.

T Task (the WHAT)
Use an action verb: write, summarize, draft, analyze, explain.

R Role (the WHO)
Give the AI an identity: "You are a senior engineer" or "a 5th grade teacher". It changes the words and depth of the answer.

A Audience (the WHOM)
Who will read it: a beginner or a CEO? This sets how simple or advanced the answer is.

D Details (the RULES)
Length, format (bullets, table) and tone (casual, formal).

E Example (the MODEL)
Show a sample of the answer you want. This is called few-shot prompting.

Build a prompt in 5 steps
Start with the vague prompt "Explain photosynthesis" and add one TRADE part at a time.

- Task: Explain photosynthesis.
- Role: You are a friendly science teacher. Explain photosynthesis.
- Audience: ...for Grade 6 students.
- Details: ...in under 120 words, using simple words and 4 bullet points.
- Example: ...Use this style: "Step 1: Sunlight. Leaves catch it."

Each step makes the answer more exact. The final prompt tells the AI who it is, what to do, who is listening, how to format the answer and what it should look like.

Zero-shot and few-shot

- Zero-shot prompting: you ask with no examples. "Say if this review is Positive or Negative: 'Love the camera'."
- Few-shot prompting: you give one or more solved examples first so the AI copies the pattern.

Review: "Great phone"          -> Positive
Review: "Battery dies fast"     -> Negative
Review: "Love the camera"       -> ?

With the two examples above, the AI sees the pattern and answers "Positive".

Check yourself 1
In "You are a vet. Write 5 bullet tips on feeding puppies for first-time owners, under 100 words", find Role, Task, Audience and Details. Answer: Role: a vet. Task: write 5 tips on feeding puppies. Audience: first-time owners. Details: 5 bullets, under 100 words.

Check yourself 2
What is few-shot prompting? Answer: Giving the AI examples of the answer you want so it copies the pattern.

## Tab 3: Techniques and practice

Prompt engineering techniques, uses and limits
⚡ At a glance
🧠 Idea: Five techniques change how you ask: zero-shot, few-shot, chain-of-thought, role and constraint prompting.
🧪 Example: 'Think step by step' helps the AI show its reasoning.
✅ Remember: Prompts guide the AI but never guarantee a perfect answer.

Prompt engineering is the process of creating clear and effective inputs for an AI system to guide it toward the desired output.

Why it is important

- It improves accuracy by reducing vague or irrelevant responses.
- It saves time: you get useful results in fewer attempts.
- It enhances creativity when generating ideas, stories or designs.
- It supports problem solving by guiding the AI through logical steps.
- It increases reliability in tasks such as summarizing, coding and analysis.

Elements of a good prompt
Element | Meaning | TRADE part
Clear instruction | State exactly what you want the AI to do | Task
Context | Give background information when necessary | Role and Audience
Specific details | Mention the format, length, audience or style | Details
Constraints | Limits such as word count, tone or scope | Details
Examples | Sample input and output pairs when a pattern is needed | Example

Five prompting techniques

- Zero-shot prompting: ask the AI to do a task without examples.
- Few-shot prompting: give a few examples before asking the AI to complete a similar task.
- Chain-of-thought prompting: encourage the AI to explain its reasoning step by step.
- Role prompting: assign a role, such as "act as a teacher" or "act as a software engineer".
- Constraint-based prompting: add rules, such as "explain in 100 words".

Chain-of-thought example
Plain prompt: "A pen costs 20 rupees. I buy 3 pens and pay with a 100 rupee note. What is my change?"

Chain-of-thought prompt: "...Think step by step." The AI then reasons: 3 pens cost 3 × 20 = 60 rupees. Change = 100 &minus; 60 = 40 rupees. Showing the steps makes mistakes easier to spot.

🌍 Analogy: a maths teacher who says "show your working". When the steps are visible you can see where a mistake happened.

Weak prompt and improved prompt
Weak: "Explain photosynthesis."

Improved: "Explain photosynthesis in simple terms for a grade 8 student in about 100 words." (It has an audience and a length constraint.)

Applications

- Content generation.
- Code generation and debugging.
- Question answering and tutoring.
- Data analysis and summarization.
- Chatbots and virtual assistants.

Best practices

- Use simple and direct language.
- Provide enough context for the AI to understand the task.
- Specify the expected output format.
- Avoid ambiguous or overly broad instructions.

Limitations

- AI responses may still contain errors or outdated information.
- Poorly designed prompts can lead to biased, incomplete or irrelevant outputs.
- Prompt engineering does not guarantee perfect results. Always check important facts.

Check yourself 1
Which technique asks the AI to explain its reasoning step by step? Answer: Chain-of-thought prompting.

Check yourself 2
"Act as a teacher" is which technique? Answer: Role prompting.

## Tab 4: Words list

Hard words in one place
⚡ At a glance
🧠 Idea: A quick reference for the words in this lesson.
🧪 Example: Zero-shot = no examples in the prompt.
✅ Remember: Come back here whenever a word is unclear.

Word | Plain meaning

Prompt | The instruction or question you give to an AI

Prompt engineering | Writing the prompt clearly so the AI gives a good answer first time

Task | What you want the AI to do (the verb)

Role | Who the AI should act as

Audience | Who will read the answer

Details | The rules: length, format and tone

Example | A sample of the answer you want

Zero-shot prompting | A prompt with no examples

Few-shot prompting | A prompt with one or more solved examples for the AI to copy

---

# lesson03_state_space_search.html  (Lesson 3: State Space Search | AI Notes)


## Tab 1: What is AI search?

What is AI search, and why does it matter?
⚡ At a glance
🧠 Idea: AI search is finding a sequence of steps that leads from a starting situation to a goal.
🧪 Example: Finding the shortest route from A to E on a map.
✅ Remember: Three aims of search: find a solution, find all solutions, find the best solution.

AI search is the process of finding a sequence of actions (steps) that leads from an initial state to a goal state.

🌍 Analogy: finding your way in a new city. You are at the bus stand (start). You want to reach the hotel (goal). You try roads, turn back from dead ends, and compare routes. That trial and comparison is search.

Where search is used

- Problem solving (puzzles, scheduling).
- Game playing (finding moves, avoiding obstacles).
- Route planning (maps and navigation).
- Optimization (finding the best settings).

Why search is important in AI

- It lets machines make intelligent decisions.
- It solves complex problems.
- It lets us navigate huge search spaces to find optimal (best) or near-optimal (almost best) solutions.

Problem-solving AI agents, such as AI assistants that plan tasks or answer questions, need to do some search to get their job done.

Three aims of a search
1. Find a solution
Any answer that works.
2. Find all the solutions
Every answer that works.
3. Find the best solution
The answer with the lowest cost or highest value.

Search appears in many places

- Weights of a neural network. Finding the best weight values is a search. Each training cycle changes the weights and reduces the output error. We look for the weight value where the error is lowest (Lesson 7).
- Linear regression. We can try many (m, c) pairs for the line y = m x + c. The best pair is the one with the least error, found by search (Lesson 6).
- Path-finding agents. To find the shortest distance from A to E on a map with many routes, we search among the possible routes.
- The travelling salesman problem. Visit every city once and come back, as cheaply as possible (see the "Famous problems" tab).
- Games. A game character needs search to find a path that avoids obstacles and to pick the best moves.

State space search is the core idea behind much of AI. The next tab shows how we describe a search problem.

Check yourself 1
Name the three aims of search. Answer: Find a solution, find all solutions, find the best solution.

Check yourself 2
Why is choosing the best weights in a neural network called a search? Answer: We try different weight values and look for the ones that give the lowest error.

## Tab 2: State space search

State space search: describing the problem
⚡ At a glance
🧠 Idea: Describe a problem as states joined by legal steps, then explore from the start to a goal.
🧪 Example: In a maze, each spot is a state and each move is an operator.
✅ Remember: Initial state, operators, state space, goal test. The answer is the path.

In state space search the problem is a set of situations (states). The computer moves from one state to another using legal steps until it reaches a state that passes the goal test.

🌍 Analogy: a maze or GPS. Every spot in the maze is a state. Every move is an operator. Where you start is the initial state. The exit is the goal.

The 4 parts
Initial state
Where the problem starts.
Operators
The legal steps that change one state into another.
State space
All the states reachable from the initial state.
Goal test
A check for whether a state is an acceptable answer.

The "instructions" that change one state into another are called operators.

What is a state?
A state is a possible solution configuration: a complete snapshot of the problem at one moment, holding everything needed to decide what can happen next.

- Every state is a candidate answer. The goal state is the one that passes the goal test.
- States are written compactly, for example the pair (2, 4).
- Two states are the same if their contents are identical, even if they were reached by different paths. This is what lets us avoid repeating work.

The answer is the path
The answer is the path, the sequence of operators used, not just the final state. A GPS gives you the route, not only the address.

The same idea in classical AI and in ML
 | Classical search | Machine learning
The states are | Separate and countable (a chess board is in one arrangement or another) | Sets of parameter values, such as neural network weights, which are real numbers
Type of space | Discrete | Continuous: infinitely many states between any two
How we move | Apply an operator to jump to the next state | Take small steps guided by gradient descent
The goal | One exact state | A region of low error

🌍 Analogy: stairs and a ramp. Discrete = stairs: you stand on step 2 or step 3, never 2.4. Continuous = a ramp: endless positions in between. The idea is the same (find a good configuration in a space of possibilities). Only the shape of the space and the way we move differ.

Check yourself 1
What are the 4 parts of a search problem? Answer: Initial state, operators, state space, goal test.

Check yourself 2
Are the states (3, 1) reached two different ways the same state? Answer: Yes. States with identical contents are the same state, whatever path reached them.

## Tab 3: BFS

Breadth-First Search (BFS)
⚡ At a glance
🧠 Idea: Search the whole breadth first: every state at depth 1, then depth 2, and so on.
🧪 Example: On the tree A, B, C, D, E, F the order is A, B, C, D, E, F.
✅ Remember: Queue, visited list, complete, shortest path, high memory.

Blind search has many names
Breadth-first and depth-first search are called uninformed, blind, exhaustive or brute force search. They know only the operators and the goal test. They cannot tell which state is closer to the goal.

BFS explores the search tree level by level, horizontally. It uses a queue (first in, first out) and a visited list of generated states, used to prune repeats.

🌍 Analogy: ripples on a pond. Drop a stone and the ripple widens one ring at a time. Or: check every room on floor 1, then every room on floor 2.

The steps

- Put the initial state in the queue and mark it visited.
- Remove the front state. If it passes the goal test, stop and return the path.
- Apply every operator to it.
- Discard successors that cause no change or are already visited.
- Add the rest to the back of the queue, mark them visited, and repeat.

Worked example on a small tree
        A
       / \
      B   C
     / \   \
    D   E   F  (goal)

Step | Take from the front | Queue after adding children
1 | A | B, C
2 | B | C, D, E
3 | C | D, E, F
4 | D | E, F
5 | E | F
6 | F: goal found |

Properties

- Complete: yes. If a solution exists, BFS finds it.
- Optimal: yes, when every step costs the same. The first goal found is the shallowest.
- Time and space: about bd, where b is the branching factor (choices per state) and d is the depth of the goal. With b = 2 and d = 3: 2 × 2 × 2 = 8 states. With b = 10 and d = 5: 100,000.
- Weakness: memory, since a whole level must be held at once.

Check yourself 1
Which structure does BFS use? Answer: A queue.

Check yourself 2
Why is BFS memory-hungry? Answer: It stores a whole level of the tree at once, and the number of states grows like bd.

## Tab 4: DFS

Depth-First Search (DFS)
⚡ At a glance
🧠 Idea: Follow one branch as deep as possible, then back up (backtrack) to try another.
🧪 Example: On the same tree the order is A, B, D, E, C, F.
✅ Remember: Stack, low memory, not complete, not guaranteed shortest.

DFS follows one branch as deep as possible, then backtracks to the most recent state that still has an unexplored option. It uses a stack (last in, first out), or recursion.

🌍 Analogy: exploring one tunnel to its end. You walk to the end, then walk back to the last junction and try a different tunnel.

Worked example (same tree)
We take the top item of the stack and push its children, with the first child on top.

Step | Take from the top | Stack after pushing children (top first)
1 | A | B, C
2 | B | D, E, C
3 | D | E, C
4 | E | C
5 | C | F
6 | F: goal found |

DFS visited A, B, D, E, C, F. It went all the way down the left side before trying C.

Properties

- Complete: no. It can loop forever in a deep or cyclic space.
- Optimal: no.
- Time: about bm, where m is the maximum depth.
- Space: about b × m. Its strength is low memory use, since it keeps only one branch.

BFS compared with DFS
 | BFS | DFS
Order | Level by level (wide) | Branch by branch (deep)
Structure | Queue | Stack
Shortest path | Guaranteed (equal step costs) | Not guaranteed
Complete? | Yes | No
Memory | High | Low

Check yourself 1
Which structure does DFS use? Answer: A stack (or recursion).

Check yourself 2
Why does DFS need little memory? Answer: It stores only the current branch (about b × m states).

## Tab 5: The two-jug puzzle

A full BFS example: the two-jug puzzle
⚡ At a glance
🧠 Idea: Use BFS to measure exactly 2 litres with a 3L jug and a 4L jug.
🧪 Example: Start (0,0). Fill the 4L jug to get (0,4). Pour into the 3L jug to get (3,1).
✅ Remember: Prune repeats with a visited list. BFS finds the goal (2,0) after 5 steps.

Two jugs with no markings: 3 litres and 4 litres, with unlimited water. Measure exactly 2 litres.

Set it up

- State: (x, y), where x = litres in the 3L jug and y = litres in the 4L jug.
- Initial state: (0, 0). Goal: (2, 0) or (0, 2).

The 6 operators (tried in this order)
No. | Operator | Result
1 | Fill 3L | (3, y)
2 | Fill 4L | (x, 4)
3 | Empty 3L | (0, y)
4 | Empty 4L | (x, 0)
5 | Pour 3L into 4L | pour until the 4L jug is full or the 3L jug is empty
6 | Pour 4L into 3L | pour until the 3L jug is full or the 4L jug is empty

How much does a pour move? The smaller of (what the source holds) and (the free space in the other jug). From (0, 4), pour 4L into 3L: the source holds 4 and the 3L jug has 3 free, so 3 litres move and we get (3, 1).

A successor is discarded if it causes no change, or if it is already visited. Otherwise the search would repeat work and loop.

Run BFS
Level | Queue | Expanded | New states added

0 | (0,0) | (0,0) | (3,0), (0,4)

1 | (3,0), (0,4) | both | (3,4), (0,3), (3,1)

2 | (3,4), (0,3), (3,1) | all three | (3,3), (0,1)

3 | (3,3), (0,1) | both | (2,4), (1,0)

4 | (2,4), (1,0) | (2,4) | (2,0): goal

The goal is found 5 steps from the start. Eleven states out of twenty were generated. The rest were never needed.

The answer is the path
(0,0) → (3,0) → (0,3) → (3,3) → (2,4) → (2,0). In words: fill the 3L jug, pour it into the 4L jug, fill the 3L jug again, pour into the 4L jug until it is full (leaving 2 litres in the 3L jug), then empty the 4L jug.

What the example shows

- BFS is blind. It never knew (3,3) was better than (3,4). It expanded both because both were on the same level.
- Pruning is essential. Without the visited list, (3,0) would regenerate (0,0), which would regenerate (3,0), forever. It also removed the duplicate (3,4) that two parents both produced.
- The first goal found is the shortest, because no level is skipped.
- The cost is memory. A whole level is stored at once, which is why heuristic search was developed.

The order in which you try the operators is a choice. A different order can change the order in which states are found, but BFS still finds a shortest path.

Check yourself 1
From (3, 0), what does "pour 3L into 4L" give? Answer: (0, 3). The 3L jug holds 3 and the 4L jug has 4 free, so 3 litres move.

Check yourself 2
Why is the first goal that BFS finds a shortest path? Answer: BFS checks level by level and never skips a level.

## Tab 6: Heuristics and A*

Informed search: heuristics, Greedy, Uniform cost and A*
⚡ At a glance
🧠 Idea: Use a smart guess h(n) of the distance to the goal to search the most promising states first.
🧪 Example: A* scores a state by f = g + h: cost so far plus the guess of the cost to go.
✅ Remember: Greedy uses only h. Uniform cost uses only g. A* uses g + h.

A heuristic h(n) estimates how close a state is to the goal. A lower value means a more promising state. It lets the search expand promising states first, which greatly reduces the number of expansions. It is an estimate, not a guarantee.

🌍 Analogy: the hot-and-cold game, or Google Maps. A map app knows the straight-line distance to your destination. It uses this to try roads that head the right way first. Google Maps style route finding uses this idea (the A* method).

Examples of heuristics

- The straight-line distance to a destination.
- The number of misplaced tiles in the 8-puzzle.

Three methods, one small map
Start S, goal G. Roads (with distance): S–A 1, S–B 4, A–B 2, A–G 6, B–G 3. The heuristic h(n) is the guessed distance to G: h(S) = 5, h(A) = 4, h(B) = 2, h(G) = 0. The costs of the full routes: S→A→B→G = 1 + 2 + 3 = 6. S→B→G = 4 + 3 = 7. S→A→G = 1 + 6 = 7. The best route is S, A, B, G with cost 6.

1. Uniform Cost Search (uninformed)
Always expand the state with the smallest total path cost so far, g(n). It finds the lowest-cost path, but it does not use any guess about the goal, so it can explore many states.

2. Greedy Best-First Search (informed)
Always expand the state with the smallest h(n), ignoring the cost so far. From S the neighbours are A (h = 4) and B (h = 2), so it goes to B, then to G (h = 0). The route S, B, G costs 7. It is fast, but it is not guaranteed to be the best route.

3. A* (A-star)
f(n) = g(n) + h(n)

g(n) = the real cost from the start to n. h(n) = the guessed cost from n to the goal. A* always expands the state with the smallest f. If h never overestimates the true remaining cost (an admissible heuristic), A* finds the shortest path.

Step | Expand | What A* finds (g, h, f)

1 | S (f = 0 + 5 = 5) | A: g = 1, h = 4, f = 5. B: g = 4, h = 2, f = 6.

2 | A (smallest f = 5) | B through A: g = 1 + 2 = 3, f = 3 + 2 = 5 (better than 6, so update). G through A: g = 1 + 6 = 7, f = 7.

3 | B (f = 5) | G through B: g = 3 + 3 = 6, f = 6 + 0 = 6 (better than 7, so update).

4 | G (f = 6) | Goal reached. Total cost 6.

A* returns S → A → B → G with cost 6, the best route, and it used the guess to avoid wandering.

Method | Uses | Best route guaranteed?
Uniform cost | g(n) only | Yes
Greedy best-first | h(n) only | No (found cost 7 here)
A* | g(n) + h(n) | Yes, with an admissible h

Check yourself 1
g = 3 and h = 4 for a state. What is f in A*? Answer: f = 3 + 4 = 7.

Check yourself 2
Why can Greedy best-first miss the best route? Answer: It looks only at the guess h(n) and ignores the cost already spent.

## Tab 7: Why not equations?

Why not solve it with equations?
⚡ At a glance
🧠 Idea: Straight-line maths methods (like linear programming) assume linear, continuous, convex problems. Search problems are not.
🧪 Example: A jug holds 2 or 3 litres, never 2.4.
✅ Remember: The answer is a sequence of actions, so we explore step by step.

The graphical and simplex methods come from Linear Programming (LP). They assume a linear objective, linear constraints, continuous variables and a convex region of allowed answers.

What is linear programming?
Example: a bakery makes cakes (profit 5 each) and cookies (profit 2 each). A cake takes 2 hours, a cookie takes 1 hour, and there are 10 hours. Maximize 5 × cakes + 2 × cookies, with 2 × cakes + cookies ≤ 10.

The best answer is at a corner of the allowed area. Corners: (0 cakes, 0 cookies) gives profit 0. (5, 0) gives 25. (0, 10) gives 20. The best is 5 cakes, profit 25. The graphical method draws the limits on a graph and picks the best corner. The simplex method hops from corner to corner.

Why they cannot be used for search problems

- The world is not linear. Real relationships are curved, conditional and interacting.
- Many states are discrete. A jug holds 2 litres or 3, never 2.4 as a meaningful answer.
- The answer is a sequence of actions, not a single point. LP returns values, not a plan.
- Constraints are logical rules ("you cannot pour into a full jug"), not linear inequalities.
- The graphical method works only for two or three variables.
- In a non-convex space (a shape with dents and several peaks), a corner point is not guaranteed to be the best, so simplex logic fails.

So we must explore the space step by step instead of solving it algebraically.

Check yourself 1
Why can't LP give the steps of the jug puzzle? Answer: LP returns values, not a sequence of actions, and the jug rules are logical, not linear.

Check yourself 2
What does "convex" mean? Answer: A shape with no dents, so a best corner is guaranteed.

## Tab 8: Famous problems

Famous search problems: travelling salesman and knapsack
⚡ At a glance
🧠 Idea: Some search problems have so many possible answers that trying them all is impossible for big cases.
🧪 Example: 10 cities have 9! = 362,880 routes with a fixed start. 20 cities have about 1.2 × 1017.
✅ Remember: For n cities with a fixed start there are (n &minus; 1)! orders.

The travelling salesman problem (TSP)
A salesman must visit each city exactly once and come back to the starting city. All cities are connected and the paths work both ways. Find the cheapest (shortest) tour.

With a fixed starting city, there are (n &minus; 1)! possible orders for n cities. (The sign ! means factorial: 4! = 4 × 3 × 2 × 1 = 24.)

Cities n | Routes (n &minus; 1)!
5 | 4! = 24
10 | 9! = 362,880
20 | 19! = 121,645,100,408,832,000 (about 1.2 × 1017)

(If a route and its reverse count as the same tour, the number is half of this.)

TSP is called NP-hard: there is no known fast method that always finds the best tour for every size. When the problem is large, trying every route cannot be done. So we use smart methods such as heuristics and genetic algorithms (Lesson 4) to find very good routes.

🌍 Analogy: planning a delivery round through 20 shops. Even if you could check a million routes every second, 1.2 × 1017 routes would take about 3,800 years. You need a clever shortcut.

The knapsack problem
You have a bag that can carry a limited weight, and items with a weight and a value. Choose the items with the greatest total value without going over the weight limit.

Example: weight limit 5. Items: A (weight 2, value 3), B (weight 3, value 4), C (weight 4, value 5).

Choice | Total weight | Total value | Allowed?
A + B | 5 | 7 | Yes
A + C | 6 | 8 | No, too heavy
B + C | 7 | 9 | No, too heavy
C alone | 4 | 5 | Yes
B alone | 3 | 4 | Yes

The best allowed choice is A + B with value 7. With many items, the number of combinations explodes, so it is also a hard search problem.

Check yourself 1
How many routes for 6 cities with a fixed start? Answer: 5! = 120.

Check yourself 2
In the knapsack example, why is A + C not allowed? Answer: Its weight is 2 + 4 = 6, which is over the limit of 5.

## Tab 9: Words list

Hard words in one place
⚡ At a glance
🧠 Idea: A quick reference for the words in this lesson.
🧪 Example: Backtrack = go back to the last choice and try another.
✅ Remember: Come back here whenever a word is unclear.

Word | Plain meaning

Search | Finding a sequence of steps from a start to a goal

State | A snapshot of the problem at one moment, like (3, 1)

Operator | A legal step that changes one state into another

State space | All the states reachable from the start

Goal test | A check that says whether a state is an answer

Path | The list of steps from the start to the goal

Visited list | States already seen, to avoid repeating them

Pruning | Dropping states that are repeats or add nothing

Blind (uninformed) search | Search that knows only operators and the goal test (BFS, DFS)

Queue / stack | First in, first out / last in, first out

Backtrack | Go back to the last choice and try another

Branching factor (b), depth (d) | Choices per state / steps to the goal

Complete | Always finds a solution if one exists

Optimal | Always finds the best solution

Heuristic h(n) | A guess of how close a state is to the goal

g(n) | The real cost from the start to state n

Admissible | A heuristic that never overestimates the true remaining cost

NP-hard | No known fast method that always finds the best answer for every size

Discrete / continuous | Separate steps like stairs / endless values like a ramp

---

# lesson04_genetic_algorithms.html  (Lesson 4: Genetic Algorithms | AI Notes)


## Tab 1: The problem

Step 1: What problem are we solving?
⚡ At a glance
🧠 Idea: Optimization means finding the best answer among many possible answers.
🧪 Example: Which study timetable gives the highest total marks?
✅ Remember: Every optimization problem has decision variables, an objective function and constraints.

Optimization = finding the best answer. A genetic algorithm (GA) is a way to find very good answers when we cannot just calculate them.

The three parts of any optimization problem
1. Decision variables
The things we can change. Example: how many hours to study each subject.
2. Objective function
The score we want to make as big (or small) as possible. Example: total marks.
3. Constraints
The limits we must obey. Example: only 10 hours in a day.

The old way: use the slope
If we have a formula f(x), we can look for the top of the hill. At the very top you stop going up and start going down, so for a moment the ground is flat. The slope there is 0.

Example: f(x) = 9 &minus; (x &minus; 3)&sup2;. Then f(2) = 8, f(3) = 9, f(4) = 8. The values rise to 9 at x = 3 and then fall, so the top is at x = 3.

What is a slope? It is how steep the ground is at one spot. Uphill is positive, downhill is negative, and a flat top is 0.

The problem with the old way
In real life we often do not have a neat formula. Then we cannot find the slope. We need a method that works without one.

🌍 Analogy: finding the highest hill in thick fog. You cannot see the whole landscape and you have no map. A GA sends out many hikers. Each hiker checks how high they are. The ones who are higher get to "have children": new hikers who start near the good spots. After many rounds the group gathers near the top.

The big idea: copy how nature solves problems. Nature found animals that survive in tough places by evolution. A GA copies that.

Check yourself 1
Name the 3 parts of an optimization problem. Answer: Decision variables, objective function, constraints.

Check yourself 2
Why can't we always use the slope method? Answer: Often there is no formula f(x), so we cannot find its slope.

## Tab 2: What is f(x)?

Step 2: The example problem and what f(x) means
⚡ At a glance
🧠 Idea: f(x) is a machine: you put x in and a score comes out.
🧪 Example: f(x) = x&sup2;. Put in 7 and get 49.
✅ Remember: In a GA, f(x) is the fitness function. z = f(x) is the same thing.

We will use one simple problem all through this lesson: find the whole number x from 0 to 31 that makes x&sup2; as big as possible. (We can see the answer is 31, but we will let the GA discover it, so we can check that the GA works.)

What is a function?
A function is a machine. You put a number in and one number comes out. f(x) is read "f of x". It means "the output when the input is x". It is not f multiplied by x. The letter f is just the name of the machine.

🌍 Analogy: a juice machine. Put in 1 orange and get 1 glass. The rule inside the machine is the function. f(x) is "how much juice you get when you put in x oranges".

What does x&sup2; mean?
The small 2 means "squared": multiply the number by itself. (You may also see x2 or x^2.)

Input x | Rule: x × x | Output f(x)
2 | 2 × 2 | 4
7 | 7 × 7 | 49
18 | 18 × 18 | 324
31 | 31 × 31 | 961

Reading the problem line by line
Max z = x&sup2;, 0 ≤ x < 32, x is a whole number

- Max z = x&sup2;: make the score z as big as possible. This is the objective function. z is just another name for f(x).
- x: the number we are free to choose. This is the decision variable.
- 0 ≤ x < 32: x can be 0, 1, 2 ... up to 31. This is a constraint.
- x is a whole number: another constraint.

In a real problem nobody gives you x&sup2;. You write your own f(x) to measure what you care about, such as profit, distance or cost. The GA steps stay exactly the same. Only f(x) changes.

Check yourself 1
What is f(5) if f(x) = x&sup2;? Answer: 5 × 5 = 25.

Check yourself 2
In "Max z = x&sup2;", which part is the decision variable? Answer: x, the number we choose.

## Tab 3: Nature's idea

Step 3: The idea from nature
⚡ At a glance
🧠 Idea: Keep the fittest answers, mix them to make new ones, and repeat.
🧪 Example: A farmer saves seeds from the best plants every year, so the crop gets stronger.
✅ Remember: Population, chromosome, gene, fitness, selection, crossover, mutation, generation.

Darwin's idea: the fittest survive and have children. Children inherit good traits. Over many generations the group gets better. A GA does this with answers instead of animals.

🌍 Analogy: a farmer saving seeds. Every year the farmer keeps seeds from the best plants and plants them again. After many years the crop is much stronger.

The words of a GA, with a picture for each
Word | Meaning in a GA | Think of it as

Population | A group of possible answers | A crowd of hikers

Chromosome | One answer, written as a string | One person's DNA code

Gene | One part of a chromosome | One letter of the code

Fitness | A score of how good an answer is | A survival score

Selection | Choosing good answers as parents | Picking who has children

Crossover | Mixing two parents to make children | A child gets features from mum and dad

Mutation | Randomly changing a gene | A rare random change in DNA

Generation | One full cycle of the algorithm | One generation of a family

How an answer becomes a chromosome
Computers write numbers with 0s and 1s (binary). Each position has a place value. From the right they are 1, 2, 4, 8, 16, each double the one before. A bit of 1 means "count this place" and a bit of 0 means "ignore it".

Place value | 16 | 8 | 4 | 2 | 1
Chromosome 10010 | 1 | 0 | 0 | 1 | 0
Bit × place value | 16 | 0 | 0 | 2 | 0

So 10010 stands for 16 + 0 + 0 + 2 + 0 = 18. Other examples: 00111 = 4 + 2 + 1 = 7. 10000 = 16. 00010 = 2. Each 0 or 1 is a gene.

Why 5 genes? With n bits we can make 2n different numbers. 25 = 32 numbers, which covers 0 to 31.

Some books call the string the chromosome (genotype) and call the real solution you get after decoding it the phenotype. Here, 10010 is the chromosome and 18 is the solution it stands for.

Check yourself 1
Decode 01101. Answer: 8 + 4 + 1 = 13.

Check yourself 2
How many genes do we need to write the numbers 0 to 31? Answer: 5, because 25 = 32.

## Tab 4: The GA loop

Step 4: The GA loop
⚡ At a glance
🧠 Idea: Make random answers. Then repeat: select, crossover, mutate, replace.
🧪 Example: Population 2, 7, 16, 18. The fitter ones are more likely to be picked as parents.
✅ Remember: Selection = who. Crossover = mix. Mutation = surprise.

A GA is a loop. Each trip around the loop is one generation.

1. Decide the population size
▼2. Decide how to write a chromosome
▼3. Decide the fitness formula
▼
4.1 Selection: pick two good parents
▼4.2 Crossover: make children
▼4.3 Mutation: randomly change genes
▼More children to make? Yes: go back to 4.1
▼5. The children become the new population
▼Stopping rule met? No: repeat. Yes: STOP

Why each step exists

- Selection pushes the group toward good answers. Without it, the search is just random.
- Crossover combines good parts of two good answers. Two good answers together may make an even better one.
- Mutation adds fresh variety so the group does not get stuck with the same ideas.

Setting up (steps 1 to 3)
Step 1: population size N is how many chromosomes are in the group. Too small means too little variety and the GA gets stuck. Too large means each generation takes longer. Real GAs often use tens or hundreds. In this lesson we use N = 4 so you can do the sums on paper.

The labels you may see: N is the initial population. G0 is generation 0 (the first random group), G1 is the group after one cycle, G2 after two cycles, and so on. A chromosome is written x = (x1, x2, ..., x6): each x with a small number is one gene, which is one decision variable. And z = f(x) is that chromosome's fitness.

Step 2: how to write a chromosome depends on the problem:

Problem | Chromosome | Why this form

Maximize x&sup2; for x from 0 to 31 | 10010 (5 bits) | 5 bits cover 0 to 31

Contact or skip 5 donors | 1 1 0 1 1 | One yes/no gene per donor

Order of 6 cities (travelling salesman) | Random keys (see Special cases) | Always gives a valid route

Continuous settings like speed or temperature | Real numbers: (0.25, 1.73, 4.62, 2.15) | The variables are naturally continuous

Step 3: the fitness formula must give a higher score to a better answer. For x&sup2;, fitness = x&sup2;. For a shortest-route problem we want a small distance, so a common trick is fitness = 1 &divide; total distance. A 100 km route gives 1 &divide; 100 = 0.01 and an 80 km route gives 1 &divide; 80 = 0.0125, so the shorter route scores higher.

Check yourself 1
Which GA step makes sure the group improves instead of searching randomly? Answer: Selection.

Check yourself 2
For a shortest-route problem, why use fitness = 1 &divide; distance? Answer: A shorter route gives a bigger number, so a better route gets a higher fitness.

## Tab 5: Selection

Step 5: Selection, choosing the parents
⚡ At a glance
🧠 Idea: Better answers get a bigger chance of becoming parents.
🧪 Example: Fitness 4, 49, 256, 324 (total 633). The best has 324 &divide; 633 = 51.2% of the wheel.
✅ Remember: Probability = fitness &divide; total fitness.

Our group (N = 4) is 00010, 00111, 10000 and 10010. We call them A, B, C and D.

First, score every chromosome
Chromosome | Decode to x | Fitness = x × x
A 00010 | 2 | 4
B 00111 | 4 + 2 + 1 = 7 | 49
C 10000 | 16 | 256
D 10010 | 16 + 2 = 18 | 324

Method 1: the roulette wheel
Imagine a wheel where each answer has a slice. A better fitness means a bigger slice, so a better chance of being picked. Even weak answers keep a small chance, which keeps the group varied.

P(i) = f(i) &divide; F

P(i) is the chance of picking answer i, f(i) is its fitness, and F is the total fitness. Here F = 4 + 49 + 256 + 324 = 633.

- P(A) = 4 &divide; 633 = 0.0063, which is 0.6%
- P(B) = 49 &divide; 633 = 0.0774, which is 7.7%
- P(C) = 256 &divide; 633 = 0.4044, which is 40.4%
- P(D) = 324 &divide; 633 = 0.5118, which is 51.2%

Check: the shares add up to about 100%. D and C have the biggest slices because their x is large.

How a computer spins the wheel
A computer cannot spin a wheel. It lines the slices up on a ruler from 0 to 1 using a running total, then picks a random number r between 0 and 1. Whoever owns that spot on the ruler is picked.

Chromosome | P | Running total | Owns this part of the ruler
A | 0.0063 | 0.0063 | 0 to 0.0063
B | 0.0774 | 0.0063 + 0.0774 = 0.0837 | 0.0063 to 0.0837
C | 0.4044 | 0.0837 + 0.4044 = 0.4881 | 0.0837 to 0.4881
D | 0.5118 | 0.4881 + 0.5118 = 1.0 | 0.4881 to 1.0

- r = 0.30 is between 0.0837 and 0.4881, so C is picked.
- r = 0.75 is between 0.4881 and 1.0, so D is picked.
- r = 0.05 is between 0.0063 and 0.0837, so B is picked.

🌍 Analogy: a lucky draw. Fitter answers hold more tickets, so they win more often. But even a few tickets can win.

Method 2: binary tournament
Pick two answers at random. The one with the better fitness wins. Example: A (fitness 4) against C (fitness 256). C wins. No division is needed.

Check yourself 1
Fitness values are 10, 30 and 60. What is the roulette chance of 30? Answer: Total = 100, so 30 &divide; 100 = 0.30 = 30%.

Check yourself 2
Running totals are A 0.1, B 0.4, C 1.0. Which is picked for r = 0.25? Answer: B, because 0.25 is between 0.1 and 0.4.

## Tab 6: Crossover

Step 6: Crossover, how two parents make children
⚡ At a glance
🧠 Idea: Cut two parents at the same place and swap the tails.
🧪 Example: 10|010 and 00|111 give 10111 and 00010.
✅ Remember: Children get pieces of both parents. Crossover only reshuffles genes that already exist.

Crossover takes two parents, cuts both at the same place, and swaps the pieces after the cut. This makes two children.

🌍 Analogy: two answer sheets. Student 1 got the first half of the exam right. Student 2 got the second half right. You make a new sheet with the first half from student 1 and the second half from student 2. It could score higher than both.

Why does it help?
Take D = 10010 (x = 18) and B = 00111 (x = 7). D is strong because its first gene is 1, worth 16. B is weak overall, but its last three genes (111) are worth 7. Put D's strong front with B's strong back and you get 10111 = 23, better than both parents. Crossover combines the good parts of two answers.

The 4 steps

- Take two parents (from selection).
- Choose a cut point, a random place between two genes. A chromosome with 5 genes has 4 possible cut points.
- Split both parents at the cut into a front and a back.
- Swap the backs. Child 1 = front of Parent 1 + back of Parent 2. Child 2 = front of Parent 2 + back of Parent 1.

Worked example
Parent 1 = 001 | 100 and Parent 2 = 010 | 000, cut after gene 3. Purple = from Parent 1, pink = from Parent 2.

- Child 1 = 001000
- Child 2 = 010100

Another: D = 10|010 and B = 00|111, cut after gene 2. Child 1 = 10 + 111 = 10111 = 16 + 4 + 2 + 1 = 23 (fitness 529). Child 2 = 00 + 010 = 00010 = 2 (fitness 4). Child 1 beats both parents (324 and 49).

Does the cut point matter? Yes
Take P1 = 11001 (x = 25, fitness 625) and P2 = 00110 (x = 6, fitness 36). Try every cut:

Cut after gene | Child 1 | Child 2 | Fitness of the children

1 | 1|0110 = 22 | 0|1001 = 9 | 484 and 81

2 | 11|110 = 30 | 00|001 = 1 | 900 and 1

3 | 110|10 = 26 | 001|01 = 5 | 676 and 25

4 | 1100|0 = 24 | 0011|1 = 7 | 576 and 49

The same parents give different children for different cuts. With the cut after gene 2, a child scored 900, better than both parents (625 and 36). The cut is chosen at random, and no cut is always best.

Limits of crossover

- It only reshuffles genes that already exist. If every parent has 0 in gene 5, every child will too. (This is why we need mutation.)
- Identical fronts give copies. If both parents share the same genes before the cut, the children look like the parents and nothing new appears.
- It can break some problems. In the travelling salesman problem it makes invalid routes (see Special cases).

Check yourself 1
P1 = 101|10 and P2 = 010|01, cut after gene 3. Find the children and their x. Answer: Child 1 = 101 + 01 = 10101 = 21. Child 2 = 010 + 10 = 01010 = 10.

Check yourself 2
Why can crossover alone never create a 1 in gene 5 if every parent has 0 there? Answer: It only swaps genes that already exist.

## Tab 7: Mutation

Step 7: Mutation, a small random change
⚡ At a glance
🧠 Idea: Randomly flip a gene (0 to 1, or 1 to 0).
🧪 Example: 10111 (23) becomes 11111 (31).
✅ Remember: Mutation is rare and small. It adds new variety and helps escape local optima.

Mutation randomly changes one or a few genes of a child. In a binary chromosome it flips 0 to 1 or 1 to 0.

🌍 Analogy: a typing mistake while copying. You copy a recipe by hand and write 2 spoons of sugar instead of 1. Usually the dish gets worse. Once in a while it becomes a new favourite. In nature mutation is a small random change in DNA, and sometimes it helps survival.

How it works

- Take a child made by crossover.
- Pick a gene at random. (Usually each gene has only a small chance of being picked.)
- Flip it. 0 becomes 1, and 1 becomes 0.

Example: Child = 001000. Flip gene 4: 001100. Before: 001000 = 8, fitness 64. After: 001100 = 12, fitness 144. It improved.

Which gene you flip matters
Take 10111 (x = 23, fitness 529) and flip each gene, one at a time:

Gene flipped | New chromosome | x | Fitness | Result

1 (worth 16) | 00111 | 7 | 49 | Much worse

2 (worth 8) | 11111 | 31 | 961 | Much better

3 (worth 4) | 10011 | 19 | 361 | Worse

4 (worth 2) | 10101 | 21 | 441 | Worse

5 (worth 1) | 10110 | 22 | 484 | Slightly worse

Three lessons: (1) mutation can help or hurt. (2) Flipping a high-value gene changes the answer a lot. (3) A bad mutation is not a disaster: the weak child scores low, so selection rarely picks it as a parent, and it fades away.

Why we really need mutation
Imagine the group 10010 (18), 10100 (20), 11000 (24) and 10000 (16). The last gene of all four is 0. Crossover only swaps genes between parents, so every child also has 0 in the last gene, forever. The best the group can reach is 11110 = 30. The true best answer 11111 = 31 needs a 1 in the last gene, and no parent has one to give. Only mutation can create a brand-new gene value: flip the last gene once and the group can reach 31.

🌍 Analogy: a library where everyone has read every book. Mixing chapters from those books (crossover) never gives a completely new idea. A new author writing a brand-new page (mutation) can.

Not too much, not too little

- Too little: the group loses variety and gets stuck.
- Too much: good answers are destroyed again and again, and the GA becomes a random guess.

If genes are real numbers, such as (0.25, 1.73, 4.62, 2.15), we cannot flip a bit. We nudge a gene to a slightly higher or lower value, such as 4.62 to 4.80.

Check yourself 1
Flip gene 3 of 11001. Answer: Gene 3 is 0, so it becomes 1: 11101 = 29 (fitness 841, up from 25 and 625).

Check yourself 2
Why can crossover alone not find 11111 from the group above? Answer: No parent has a 1 in the last gene, and crossover cannot create new gene values. Only mutation can.

## Tab 8: One full round

Step 8: One full round, put together
⚡ At a glance
🧠 Idea: Score, select, cross, mutate, replace. Then compare the new group with the old.
🧪 Example: Average fitness goes from 158.25 to 517.5 in one round.
✅ Remember: If the average fitness rises, the whole group is improving.

We now follow the group A, B, C, D (2, 7, 16, 18) through one generation.

- Score them. Fitness: 4, 49, 256, 324. Total 633. Average = 633 &divide; 4 = 158.25. Best = 324.
- Select parents. D and B are picked by the roulette wheel (D is very likely, B less so).
- Crossover D = 10|010 and B = 00|111 to get 10111 (23) and 00010 (2).
- Mutate. Flip gene 2 of 10111 to get 11111 (31).
- Repeat selection, crossover and mutation until the new group is full. One possible new group is {31, 23, 18, 16}.

 | Generation 1 | New generation
Chromosomes (x) | 2, 7, 16, 18 | 31, 23, 18, 16
Fitness | 4, 49, 256, 324 | 961, 529, 324, 256
Total fitness | 633 | 961 + 529 + 324 + 256 = 2070
Average fitness | 633 &divide; 4 = 158.25 | 2070 &divide; 4 = 517.5
Best fitness | 324 | 961

(Real runs use random numbers, so the exact new group changes each time. This is one possible result.) Both the best and the average went up, so the group improved.

The fitness graph

- At the start, fitness is low.
- As generations pass, better answers appear and fitness rises.
- Later the improvement becomes tiny and the curve goes flat. This is called convergence: the GA has settled on a good answer.

🌍 Analogy: learning a new sport. You improve quickly in the first weeks. Later each extra week makes only a small difference.

Check yourself 1
A group has fitness 10, 20, 30, 40. What is the average fitness? Answer: (10 + 20 + 30 + 40) &divide; 4 = 25.

Check yourself 2
What does a flat fitness graph show? Answer: The GA has converged: it has settled on a good answer and further improvement is tiny.

## Tab 9: Best vs good enough

Step 9: Best, nearly best, and when to stop
⚡ At a glance
🧠 Idea: A global optimum is the best of all. A local optimum is the best nearby, but not overall.
🧪 Example: Mount Everest versus a small hill in the fog.
✅ Remember: Stop at a maximum number of generations, a target fitness, or no improvement for several generations.

🏔️ Global optimum
The best answer among ALL answers.
⛰️ Local optimum
Better than its neighbours, but NOT the best overall.
🥈 Near optimum
Very close to the global optimum but not exactly the best.

🌍 Analogy: hiking in fog. You climb until every step goes down. You think you are at the top, but you are on a small hill (local optimum). Mount Everest (global optimum) is somewhere else. A near optimum is a peak a few metres below the very top.

How GA escapes a small hill
Use 3-bit chromosomes for x = 0 to 7 with these fitness values: x = 0: 1, 1: 3, 2: 6, 3: 3, 4: 2, 5: 5, 6: 9, 7: 4. The small hill is x = 2 (fitness 6). The highest peak is x = 6 (fitness 9). Suppose the whole group sits near the small hill: 001 (1), 010 (2), 011 (3). All three start with 0. Crossover can never make a first gene of 1, so it can never reach 6 = 110. Mutation flips the first gene of 010 to get 110 = 6, fitness 9, and the group climbs a higher peak.

A GA also keeps a whole population spread over the landscape, and roulette selection gives weaker answers a small chance. These keep variety and help find the global optimum.

When does the GA stop?

- A maximum number of generations is reached (like a time limit).
- A desired fitness is reached (like hitting a target score).
- There is no improvement for several generations (progress has stalled).

Check yourself 1
What is a local optimum? Answer: An answer better than its neighbours but not the best overall.

Check yourself 2
Name two ways to decide when a GA stops. Answer: Maximum generations reached, desired fitness reached, or no improvement for several generations.

## Tab 10: Special cases

Step 10: Special cases
⚡ At a glance
🧠 Idea: Some problems need special tools: travelling salesman (Random Keys), real numbers, and several goals at once.
🧪 Example: Keys 0.15, 0.32, 0.48 ... sorted give the route 4, 6, 5 ...
✅ Remember: Random Keys always give a valid route.

1. The travelling salesman problem (TSP)
TSP: visit every city once, in an order that makes the total distance as small as possible. A chromosome is an order of cities, such as 1 4 3 6 5 2.

Why normal crossover fails. P1 = 1 4 3 | 6 5 2 and P2 = 3 2 1 | 6 4 5. Swapping tails gives the child 1 4 3 | 6 4 5. City 4 appears twice and city 2 is missing. A route must visit each city exactly once, so this child is invalid.

2. Random Keys: the fix
Give every city a random number between 0 and 1, its key. Then sort the keys from smallest to largest and read off the cities in that order. That order is the route, and it can never repeat or miss a city.

City | 1 | 2 | 3 | 4 | 5 | 6
Random key (P1) | 0.97 | 0.68 | 0.72 | 0.15 | 0.48 | 0.32

Sorted: 0.15 (city 4), 0.32 (city 6), 0.48 (city 5), 0.68 (city 2), 0.72 (city 3), 0.97 (city 1). Route: 4, 6, 5, 2, 3, 1.

Another parent P2 has keys 0.62, 0.38, 0.87, 0.92, 0.16, 0.32. Sorted: 0.16 (city 5), 0.32 (city 6), 0.38 (city 2), 0.62 (city 1), 0.87 (city 3), 0.92 (city 4). Route: 5, 6, 2, 1, 3, 4.

Crossover now works. Cross over the keys, cutting after position 3:

- C1 keys = first 3 of P1 + last 3 of P2 = 0.97, 0.68, 0.72, 0.92, 0.16, 0.32. Sorted: 0.16 (city 5), 0.32 (6), 0.68 (2), 0.72 (3), 0.92 (4), 0.97 (1). Route: 5, 6, 2, 3, 4, 1.
- C2 keys = first 3 of P2 + last 3 of P1 = 0.62, 0.38, 0.87, 0.15, 0.48, 0.32. Sorted: 0.15 (city 4), 0.32 (6), 0.38 (2), 0.48 (5), 0.62 (1), 0.87 (3). Route: 4, 6, 2, 5, 1, 3.

Both children are valid routes.

🌍 Analogy: students pick random lottery numbers and then line up from smallest to largest. Everyone appears exactly once, however the numbers fall.

3. Real-coded GA
Instead of 0s and 1s, genes are real numbers, such as (0.25, 1.73, 4.62, 2.15). Use it when the variables are naturally continuous, like speed, length or temperature.

4. Combinatorial and multi-objective optimization

- Combinatorial optimization: finding the best from a huge number of combinations, such as the shortest route, scheduling, travelling salesman, resource allocation and job assignment.
- Multi-objective optimization: chasing two or more goals at the same time, such as minimizing both cost and CO&#8322; emissions. These often fight each other: the cheapest option may pollute more. So there is no single best answer, only good trade-offs.

🌍 Analogy: choosing a phone. You want it cheap and you want a great camera. The cheapest has a poor camera, and the best camera costs more. You choose a balance.

Check yourself 1
Keys for cities 1 to 4 are 0.9, 0.2, 0.5, 0.1. What is the route? Answer: Sort: 0.1 (city 4), 0.2 (city 2), 0.5 (city 3), 0.9 (city 1). Route: 4, 2, 3, 1.

Check yourself 2
Why does Random Keys always give a valid route? Answer: Each city has exactly one key, so sorting lists every city exactly once.

## Tab 11: Formulas

All the formulas in one place
⚡ At a glance
🧠 Idea: Every formula in this lesson is a short sentence in symbols.
🧪 Example: P(i) = f(i) &divide; F. For D: 324 &divide; 633 = 51.2%.
✅ Remember: Learn what each letter means, not just the shape.

What | Formula | Meaning of the symbols

Decode binary | x = sum of (bit × place value) | Place values from the right: 1, 2, 4, 8, 16, ...

Genes needed | 2n ≥ number of values | n = number of genes. 32 values need n = 5.

Fitness (this lesson) | f(x) = x&sup2; | The score of an answer. The formula changes with the problem.

Fitness for shortest route | 1 &divide; total distance | A shorter route scores higher

Total fitness | F = f(1) + f(2) + ... + f(N) | N = population size

Selection probability | P(i) = f(i) &divide; F | Share of the wheel for answer i

Running total | C(i) = P(1) + ... + P(i) | Used with a random number r

Average fitness | F &divide; N | Shows if the whole group improves

Crossover (cut after k genes) | Child 1 = P1[first k] + P2[rest]
Child 2 = P2[first k] + P1[rest] | P1, P2 = parents

Mutation | flip 0 and 1 at a chosen gene | A small random change

Random keys | sort keys ascending, read the city numbers | The smallest key goes first

Method for a GA calculation question

- Decode each chromosome to x.
- Calculate fitness f(x).
- Add them to get the total F.
- Calculate P(i) = f(i) &divide; F. Check they add to 1.
- Use selection to pick parents.
- Do crossover at the given cut. Then mutation at the given gene.
- Decode the children and calculate their fitness. Say whether it improved.

## Tab 12: Words list

Hard words in one place
⚡ At a glance
🧠 Idea: A quick reference for the words in this lesson.
🧪 Example: Chromosome = one answer written as a string like 10010.
✅ Remember: Come back here whenever a word is unclear.

Word | Plain meaning

Optimization | Finding the best answer

Objective function | The score we want to make big or small

Constraint | A limit we must obey

Slope | How steep the ground is at one spot

Binary | Numbers written with only 0 and 1

Population (N) | The group of answers

Chromosome, gene | One answer as a string / one position in it

Fitness | The score of an answer

Generation (G0, G1...) | One cycle of the algorithm

Crossover, mutation | Mix two parents / randomly change a gene

Convergence | The improvement becomes tiny because the GA has settled

Global / local optimum | The best of all / the best nearby only

Combinatorial | Choosing the best from a huge number of combinations

Multi-objective | Two or more goals at once

---

# lesson05_machine_learning.html  (Lesson 5: Machine Learning | AI Notes)


## Tab 1: What is ML?

What is machine learning?
⚡ At a glance
🧠 Idea: A computer learns patterns from examples and uses them to predict or decide. Nobody writes the rules.
🧪 Example: Show it 1,000 photos labelled cat or dog. It learns the difference, then names a new photo.
✅ Remember: Data in, pattern (the model) learned, predictions out.

Machine learning (ML) is a branch of AI where a computer system learns patterns from data and uses those patterns to make predictions, decisions or new content.

🌍 Analogy: learning to spot a ripe mango. Nobody gives you a rule book. You see many mangoes and slowly learn: yellow and slightly soft means ripe. After enough mangoes you can judge a new one you have never seen. A computer does this with numbers instead of mangoes.

Where ML sits
ML is one branch of AI. Genetic algorithms, swarm intelligence and fuzzy logic are other AI methods that sit beside it (Lesson 1). The pattern that ML learns is called a model.

Two big kinds of ML work
🎯 Predictive
Predict an outcome from given information.
Example: predict next month's sales or a student's exam marks.
🎨 Generative
Create new content based on learned patterns.
Example: predict the next word, again and again, to write text.

Careful: people often say "supervised ML is mostly predictive, unsupervised is generative". But understand the difference: unsupervised is about how a machine learns (no answers given). Generative is about what it makes (new content). They overlap, but they are not the same thing.

The four jobs ML can do

- Regression: predict a number.
- Classification: predict a category.
- Forecasting: predict future values from past values in time order.
- Optimization: find the best possible answer for one or more goals (like the genetic algorithm in Lesson 4).

Check yourself 1
Is "predict the temperature tomorrow" classification or regression? Answer: Regression, because the answer is a number.

Check yourself 2
What is a "model"? Answer: The pattern a machine learns from data.

## Tab 2: 3 ways to learn

The three ways a machine can learn
⚡ At a glance
🧠 Idea: Learn with answers, learn without answers, or learn from rewards.
🧪 Example: Emails marked spam or not (supervised). Sorting shoppers into groups (unsupervised). A game character earning points (reinforcement).
✅ Remember: Answers given? Supervised. No answers? Unsupervised. Rewards and penalties? Reinforcement.

The three types are three different ways of learning: with a teacher, without a teacher, or by trial and error.

👩‍🏫 Supervised (SL)
Learns with a teacher. The data has questions AND correct answers.
🔍 Unsupervised (USL)
No teacher. The data has no answers. The machine finds groups and patterns itself.
🎮 Reinforcement (RL)
Learns by trying actions and getting rewards or penalties.

One picture for each

- Supervised: studying past exam questions together with their model answers. Later you answer a new question.
- Unsupervised: sorting a pile of mixed buttons into groups by shape and colour, with nobody telling you the groups.
- Reinforcement: training a puppy. A treat for sitting, no treat for jumping on the sofa.

Supervised learning splits again

- Predicting a class (classification).
- Predicting a number (regression).
- Predicting a value from a time series (forecasting).

The quickest way to tell them apart

- Does the data have correct answers? Supervised.
- No answers, just finding groups? Unsupervised.
- An agent acting and getting rewards? Reinforcement.

Check yourself 1
A robot learns to walk by getting a reward for each step forward. Which type? Answer: Reinforcement learning.

Check yourself 2
Grouping customers by behaviour with no labels is which type? Answer: Unsupervised learning (clustering).

## Tab 3: Data words

The words used to describe data
⚡ At a glance
🧠 Idea: A data table has rows (records), columns (features) and one answer column (the label).
🧪 Example: Row = one student. Features = hours studied and attendance. Label = final grade.
✅ Remember: Features go in. The label is what the model tries to predict.

Before we go further, learn the small set of words used for data. Every ML topic uses them.

Student | Hours studied (x1) | Attendance % (x2) | Final GPA | Grade
1 | 10 | 90 | 3.4 | B
2 | 2 | 50 | 1.8 | D

- Record (example): one row, one student.
- Feature (input, x): one column that describes the record: hours studied, attendance. Also called attribute or dimension.
- Label (answer, y): the thing we want to predict. Here GPA (a number, so regression) or Grade (a category, so classification).
- Labelled data: every record has its answer. Unlabelled data: no answer column.
- Model: the pattern the machine learned. Think of it as a rule it worked out by itself.
- Training: showing the machine many examples. Prediction: the model's answer for a new input.
- Sample: the small part of the data we actually have. Population: everyone we care about.
- Noise: random flukes that are not a real pattern, like a hard-working student who scored low because they were sick that day.

🌍 Putting it together: you give the machine a table of past students. Each row is a record. Hours and attendance are features. The grade column is the label. The machine trains on it and builds a model. Then you give it a new student's features and it makes a prediction.

Check yourself 1
In the table, which columns are features and which is the label (for predicting Grade)? Answer: Features: hours studied and attendance. Label: Grade.

Check yourself 2
What is noise? Answer: Random flukes in the data that are not a real pattern.

## Tab 4: Supervised ML

Supervised learning: predicting answers
⚡ At a glance
🧠 Idea: Learn from solved examples, then predict the answer for a new input.
🧪 Example: Pass or fail = classification. Marks out of 100 = regression. Next week's sales = time series.
✅ Remember: A category means classification. A number means regression. A future value in time order means time series.

Supervised learning is split by the kind of answer we want: a category, a number, or a future value.

1. Classification: predict a category
The model puts an input into a class. Two choices (yes/no, spam/not spam) is binary classification. Three or more choices (class 1, 2, 3, 4) is multiclass classification. Examples: is this email spam? Does this X-ray show a broken bone?

A decision tree is one classification method: a set of yes/no questions that ends in a prediction (Lesson 1).

2. Regression: predict a number
The model gives a number on a smooth scale: exam marks, house price, tomorrow's temperature.

3. Time series (forecasting): predict the future from the past
The data is in time order, so the order matters. The model looks for a trend (going up over time), seasonality (repeating cycles like weekends) and lag (yesterday affects today).

Example: sales on days 1 to 5 were 300, 310, 312, 320, 325. What will day 6 be?

- Follow the trend: the daily changes are 10, 2, 8, 5. Their average is (10 + 2 + 8 + 5) &divide; 4 = 6.25. Day 6 is about 325 + 6.25 = 331.25.
- Average the last 3 days: (312 + 320 + 325) &divide; 3 = 319. This is lower, because an average of old values lags behind a rising trend.
- Let ML learn it with lag features: a table with yesterday's sales as input and today's as the answer (the full method is in Lesson 8).

Check yourself 1
Predict whether a customer will buy (yes or no). Which kind? Answer: Binary classification.

Check yourself 2
Daily changes of 4, 6 and 5 give an average change of? Answer: (4 + 6 + 5) &divide; 3 = 5.

## Tab 5: Donor example

A real example: choosing whom to contact
⚡ At a glance
🧠 Idea: Use two models to decide who to contact: will they give, and how much?
🧪 Example: 70% sure × 1200 = 840 expected. Minus a phone cost of 10 gives 830 profit.
✅ Remember: Expected value = probability × amount. Contact a person only if it beats the cost.

A charity has records of 1 million possible donors. Contacting a person costs money, so the charity wants to contact only the people who are likely to give enough to be worth it. This is the classic "KDD'98" marketing problem.

The problem

- Contacting a person by phone call costs 10/-. A letter costs 25/-.
- Contacting all 1 million people wastes money on those who will give nothing.
- So we use ML to guess who will give, and how much.

The data
Donor ID | Donated last year | Amount last year | Model 1 prediction | Model 2 amount | Probability × amount

1 | 1 | 1000 | 1 | 1200 | 70% × 1200

2 | 0 | 0 | 1 | 500 | 60% × 500

3 | 1 | 5000 | 0 | 0 | 0

- Donated last year and Amount last year are facts from the past (1 = yes, 0 = no). Together with other details like age and income, they are the features.
- Model 1 is a classification model: will this person donate this time? 1 = yes, 0 = no.
- Model 2 is a regression model: how much would they give?

Step by step: should we contact this person?

- Model 1 says whether they will give. Donor 3 gets 0, so we stop there.
- Model 2 says how much (donor 1: 1200).
- Expected value = probability × amount. Donor 1: 0.70 × 1200 = 840. Donor 2: 0.60 × 500 = 300.
- Subtract the contact cost to see the real profit. Donor 1 by phone: 840 &minus; 10 = 830. Donor 2 by letter: 300 &minus; 25 = 275. Donor 3 by phone: 0 &minus; 10 = &minus;10, a loss, so skip.

The general formula is Expected value = sum of (P × D), where P is the probability and D is the predicted amount. The "sum" sign means add up the same thing for every case.

🌍 Analogy: a shopkeeper has 1 million flyers and each costs money to deliver. He gives flyers only to houses likely to buy something worth more than the flyer cost.

Where the genetic algorithm fits
A GA (Lesson 4) can choose which donors to contact. A chromosome (1 1 0 1 1) for donors P1 to P5 means: contact donors 1, 2, 4 and 5, skip donor 3. The fitness is the profit = expected income minus cost.

Worked example. Expected incomes: 840, 300, 0, 200, 120. Each contact costs 10.

- Chromosome 11011: income 840 + 300 + 200 + 120 = 1460. Cost 4 × 10 = 40. Profit = 1420.
- Chromosome 11111: income 1460. Cost 5 × 10 = 50. Profit = 1410.

11011 wins because contacting donor 3 costs 10 and brings nothing.

Optimization in simple words
Optimization means finding the best possible solution for one or more goals. Example: minimize cost. Multi-objective optimization chases two or more goals at once, such as minimizing both cost and CO&#8322; emissions.

Check yourself 1
Probability 0.80, amount 500, letter cost 25. Profit? Answer: 0.80 × 500 = 400. 400 &minus; 25 = 375.

Check yourself 2
Why is donor 3 skipped? Answer: Expected income is 0, so contacting costs 10 and brings nothing.

## Tab 6: Preparing data

Getting the data ready
⚡ At a glance
🧠 Idea: Clean and improve the data before the machine learns from it.
🧪 Example: Date of birth becomes age (engineering). Student ID is dropped (selection).
✅ Remember: Engineering = make a new useful feature. Selection = remove useless ones. Z-score = how far from average.

Before a machine learns, we prepare the data. This is called data preprocessing. Two main methods are feature engineering and feature selection.

🌍 Analogy: cooking. Before cooking you wash, peel and chop the ingredients, and you leave out ingredients that do not belong in the dish. A good meal needs good preparation, and so does a good model.

1. Feature engineering: make better features

- From date of birth, make age. A model can use age easily, but a date is hard to use.
- From weight and height, make BMI = weight &divide; height&sup2;. For 60 kg and 1.5 m: 1.5 × 1.5 = 2.25, and 60 &divide; 2.25 = 26.7.

2. Feature selection: keep only the useful features
Drop columns that do not help. To predict marks, hours studied helps, but student ID number does not. Fewer features means a faster model, less noise and less trouble from too many dimensions (see "Too many features").

3. The Z-score
A Z-score tells you how far a value is from the average, counted in steps called standard deviations.

z = (x &minus; mean) &divide; standard deviation

Example: marks 40, 50, 60, 70, 80.

- Mean = (40 + 50 + 60 + 70 + 80) &divide; 5 = 60.
- Differences from the mean: &minus;20, &minus;10, 0, 10, 20.
- Square them: 400, 100, 0, 100, 400. Add: 1000. Divide by 5: 200.
- Square root: standard deviation = about 14.14.
- For the mark 80: z = (80 &minus; 60) &divide; 14.14 = 1.41. For 60: z = 0. For 40: z = &minus;1.41.

Meaning: 80 is 1.41 steps above average. 60 is exactly average. 40 is 1.41 steps below.

Why useful: it puts features of very different sizes on the same scale. Without it, a big-number feature like salary would drown a small-number feature like age when the machine measures distances.

Check yourself 1
Making "age" from "date of birth" is engineering or selection? Answer: Feature engineering.

Check yourself 2
Mean 60, standard deviation 10, value 80. Z-score? Answer: (80 &minus; 60) &divide; 10 = 2.

## Tab 7: Unsupervised ML

Unsupervised learning: finding patterns without answers
⚡ At a glance
🧠 Idea: No answers are given. The machine finds groups (clustering) or items bought together (association).
🧪 Example: Shoppers fall into groups like bargain hunters and luxury buyers. Burger patties and buns often come with ketchup.
✅ Remember: The machine finds the groups. Humans give them names.

There is no teacher and no answer column. The machine looks at the data and groups similar things.

1. Clustering: make groups of similar items
The machine measures how close items are (their distance) and puts nearby items into the same group, called a cluster.

🌍 Analogy: students at a school assembly. Without any instruction they naturally stand in groups of friends. A clustering method does the same with data points.

Example: student data with height, weight, Z-score, GPA 1 and GPA 2. If we look at only height and weight we may see 2 clusters, which we can guess are two groups of students. The machine does not know the names of the groups. It only sees 2 clusters. A human gives the names.

Adding a feature can change the clusters. If we add a third feature, such as the Z-score, the old clusters can disappear and new ones can form, because the points are now measured in a new way. This leads to the idea of "too many features" later.

2. Association rules: find "if this, then that"
It looks at many shopping baskets and finds items that often appear together.

Example: 10 shopping baskets. 5 baskets contain patties and buns. Of those 5, 4 also contain ketchup.

- Support = how common the whole combination is = 4 &divide; 10 = 40%.
- Confidence = how reliable the rule is = 4 &divide; 5 = 80%.

The rule: patties + buns, then ketchup (confidence 80%). A shop can put ketchup near the buns or sell a bundle.

🌍 Analogy: in a class of 10, 5 students carry a red pen and a ruler, and 4 of them also carry a calculator. So if a student has a red pen and a ruler, there is an 80% chance of a calculator too.

Check yourself 1
Does the machine name the clusters? Answer: No. It only finds the groups. Humans name them.

Check yourself 2
8 baskets have bread and butter, and 6 of them also have jam. Confidence of "bread and butter, then jam"? Answer: 6 &divide; 8 = 75%.

## Tab 8: Reinforcement

Reinforcement learning (RL)
⚡ At a glance
🧠 Idea: An agent tries actions in an environment and learns from rewards (+) and penalties (-).
🧪 Example: A dog sits and gets a treat. It jumps on the sofa and hears "no". It learns what to do.
✅ Remember: State, then action, then reward. The policy is the rule for choosing the action.

Reinforcement learning is a type of ML where an agent learns by interacting with an environment and getting feedback as rewards (positive) or penalties (negative).

🌍 Analogy: training a dog, or playing a video game. The dog sits and gets a treat (reward). It jumps on the sofa and hears "no" (penalty). After many tries it learns what to do. A game character learns the same way: collect coins (+), fall in the lava (-).

Real example: robots from Boston Dynamics (some walk on four legs like dogs) can use RL ideas to learn useful movements by trying and getting feedback.

The four words of RL
Word | Symbol | Meaning | Robot example
State | s | The current situation | The robot is standing in front of a step
Action | a | What the agent does | Lift the leg, turn, or wait
Policy | &pi; | The rule for choosing actions | "In front of a step, usually lift the leg"
Probability | p | The chance of choosing that action | 0.7 for lifting the leg

Read the table like a story: the robot is in a state (in front of a step). It must pick an action (lift leg, turn or wait). Its policy is the rule that decides, and the rule gives each action a probability.

The policy formula: &pi;(s, a) = p
Read it as: "In state s, the policy &pi; picks action a with probability p." Example: in state s1 (in front of a step), &pi;(s1, lift leg) = 0.7, &pi;(s1, turn) = 0.2, &pi;(s1, wait) = 0.1. The probabilities add up to 1 (0.7 + 0.2 + 0.1 = 1.0), because the robot must choose something.

Learning means changing these probabilities. Actions that earn rewards get a higher p over time.

Check yourself 1
In RL, what is the "agent"? Answer: The learner that takes actions, such as the robot or the game character.

Check yourself 2
Can the probabilities in a policy for one state be 0.5, 0.4 and 0.3? Answer: No. They must add up to 1, and these add up to 1.2.

## Tab 9: Too many features

Too many features: dimensions and PCA
⚡ At a glance
🧠 Idea: A dimension is one feature (one column). Too many features make the data spread out and look empty.
🧪 Example: 1 feature = a line. 2 = a page. 3 = a box. 200 features = a space you cannot picture.
✅ Remember: More features means emptier space, which makes learning harder. PCA squeezes many features into few.

Attribute = feature = dimension = column. These four words mean the same thing. A record with 200 features is a point in 200 dimensions.

Features | What we measure | Where the data lives
1 | height only | on a line
2 | height and weight | on a flat page (a graph)
3 | height, weight, shoe size | inside a box
hundreds | many measurements | in a space we cannot picture

Problem 1: the data becomes sparse (empty)
Suppose each feature has 10 possible levels and we have 100 data points. Count the "boxes" the data must fill:

Features | Boxes (10 to the power of features) | Points per box (100 &divide; boxes)
1 | 10 | 10
2 | 100 | 1
3 | 1,000 | 0.1
50 | 1050 | almost 0

With 1 feature there are 10 boxes. With 2 features there are 10 × 10 = 100 boxes. The count multiplies by 10 each time we add a feature. With 3 features most boxes are empty (0.1 points each). The data looks like a few dots lost in a huge empty space, and the model has too little data around each spot to learn from.

Problem 2: distances lose meaning
Many methods measure how close two items are. In very high dimensions almost every pair of points ends up about the same distance apart. If everything looks equally far, the machine cannot tell which items are truly similar.

🌍 Analogy: compare two students on 1 subject and you can easily say who is closer. Compare them on 200 subjects and almost every pair differs somewhere, so all pairs look about equally different.

Problem 3: overfitting and heavy computing
With hundreds of features the model needs a lot of computing power, and it can mistake random noise for a real pattern (overfitting, next tab).

The fix: dimensionality reduction with PCA
PCA (Principal Component Analysis) makes a few new features that keep most of the important variation in the data. Variation means how spread out the data points are. If every student had the same height, height would tell us nothing. PCA keeps the directions with the most spread.

🌍 Analogy: a photo. A real scene is 3D but a photo is 2D. A good photo keeps most of what you care about. PCA looks for the best "angle".

Example: four students with (height, weight): (150, 45), (160, 52), (170, 60), (180, 68). Taller students are heavier, so the points lie almost on one line. One number, "overall body size", describes each student almost as well as two numbers. That number is the first principal component (PC1). If PC1 holds 95% of the variation, keeping only PC1 halves the columns and loses only 5% of the information.

An autoencoder is a small neural network that squeezes the data into a short code and rebuilds the original from it. If the rebuilt data is close, the code is a good summary.

Check yourself 1
With 10 levels per feature, how many boxes do 4 features make? Answer: 10 × 10 × 10 × 10 = 10,000.

Check yourself 2
What does PCA do? Answer: It makes a few new features that keep most of the information, so we can use fewer columns.

## Tab 10: Train, test, bias, variance

Training, testing, bias and variance
⚡ At a glance
🧠 Idea: Train on one part of the data. Test on a part the model has never seen.
🧪 Example: With 1,000 records: 800 to train and 200 to test.
✅ Remember: Good on training but bad on testing = overfit. Bad on both = underfit. Good on both = just right.

🎬 StatQuest: "Machine Learning Fundamentals: Bias and Variance"
The video predicts a mouse's height from its weight. The true relationship is a curve. It shows that a straight line (linear regression) cannot follow the curve, which is bias, and that a very flexible squiggly line fits the training data almost perfectly but does badly on new data, which is variance. The aim is to find a balance between the two. Ways to find the balance include regularization, boosting and bagging.

Step 1: sample and population
We cannot measure every mouse in the world (the population). We measure a few (a sample) and build the model from it. A model trained on one sample can perform badly on other samples. This is the bias-variance problem.

Step 2: split into training and testing sets
Keep about 80% for training (the model learns from it) and 20% for testing (the model never sees it while learning). With 1,000 records that is 800 and 200.

🌍 Analogy: training data = practice papers. Testing data = the real exam. A student who memorised the practice answers may look brilliant at home and still fail the real exam.

Step 3: the straight line has high bias (underfitting)
The true link between weight and height is a curve. A straight line cannot bend, so it misses the shape. This failure to capture the real relationship is bias. A model that is too simple is underfitting: it makes big errors on the training data and on the testing data.

Step 4: the squiggly line has high variance (overfitting)
A very flexible squiggly line can pass through every training dot, so its training error is almost zero. But it also copies the random noise. On the testing data it does badly, and its predictions would change a lot if we trained on a different sample. That is variance, and the result is overfitting.

Step 5: the sweet spot
A good model is flexible enough to follow the real pattern but not so flexible that it copies the noise. It does well on both training and testing data.

Model | Training error | Testing error | Problem
Straight line | 10 | 12 | High bias (underfit)
Balanced curve | 4 | 5 | Good
Squiggly line | 0 | 20 | High variance (overfit)

(Example numbers. "Error" is a score of how wrong the model is, so lower is better.) The straight line has high error on both. The squiggly line has zero training error but a big testing error, and the big gap warns you of overfitting. The balanced curve has low error on both. Always compare training error with testing error.

Check yourself 1
Training error 1 and testing error 15. Diagnosis? Answer: Overfitting (high variance): it memorised the training data.

Check yourself 2
Training error 12 and testing error 13. Diagnosis? Answer: Underfitting (high bias): the model is too simple, so both errors are high.

## Tab 11: Judging a model

How good is a model? Scores and cross-validation
⚡ At a glance
🧠 Idea: Count the model's hits and misses, then turn them into scores.
🧪 Example: A spam filter with 85 correct answers out of 100 has accuracy 85%.
✅ Remember: Accuracy, precision, recall. Cross-validation tests on every part of the data in turn.

1. The confusion matrix
A spam filter checks 100 emails. 40 are really spam and 60 are normal. Results:

 | Filter says SPAM | Filter says NORMAL
Really spam (40) | 30 (TP) | 10 (FN)
Really normal (60) | 5 (FP) | 55 (TN)

- TP (true positive): spam correctly caught. 30.
- FN (false negative): spam that slipped through. 10.
- FP (false positive): a normal email wrongly called spam. 5.
- TN (true negative): a normal email correctly left alone. 55.

Check: 30 + 10 + 5 + 55 = 100.

2. Four scores from the same numbers

- Accuracy = (TP + TN) &divide; all = (30 + 55) &divide; 100 = 85%. How often is it right overall?
- Precision = TP &divide; (TP + FP) = 30 &divide; 35 = 85.7%. When it says spam, how often is it right?
- Recall (sensitivity) = TP &divide; (TP + FN) = 30 &divide; 40 = 75%. Of all real spam, how much did it catch?
- Specificity = TN &divide; (TN + FP) = 55 &divide; 60 = 91.7%. Of all normal emails, how many did it leave alone?

🌍 Analogy: a fishing net. Recall asks "how many of the fish did my net catch?". Precision asks "of what I caught, how much is fish and not rubbish?".

3. Cross-validation
One 80/20 split can be lucky or unlucky. In cross-validation we cut the data into several parts (folds), for example 5. Each round, 4 parts train the model and the 1 left-out part tests it. We do this 5 times so every part is the test part once. Then we average the scores.

Example scores: 80, 84, 78, 86, 82. Average = (80 + 84 + 78 + 86 + 82) &divide; 5 = 410 &divide; 5 = 82.

🌍 Analogy: instead of judging a student on one exam, you use 5 different exams and take the average.

Check yourself 1
TP = 20, FN = 10, FP = 10, TN = 60. Accuracy? Answer: (20 + 60) &divide; 100 = 80%.

Check yourself 2
Scores 70, 80, 90 from 3 folds. Average? Answer: (70 + 80 + 90) &divide; 3 = 80.

## Tab 12: The ML workflow

The steps of an ML project
⚡ At a glance
🧠 Idea: An ML project follows 8 steps, from the question to using the model.
🧪 Example: Predict whether a student will pass the module.
✅ Remember: Define, collect, prepare, split, train, test, improve, use.

Everything in this lesson fits into one workflow. Here it is, using "predict whether a student will pass the module" as the example.

- Define the problem. We predict pass or fail, so this is classification.
- Collect data. Records of past students: hours studied, attendance and the result.
- Prepare the data. Fix missing values, make good features, drop useless columns.
- Split the data. For example 80% to train and 20% to test.
- Train a model on the training data.
- Test it on the testing data. Check accuracy, precision and recall.
- Improve it. If both errors are high the model is too simple. If training is good but testing is bad, it is overfitting. Try more data or another method.
- Use it. Predict for the new students.

Check yourself 1
What is the first step of an ML project? Answer: Define the problem: what to predict and what type of task it is.

Check yourself 2
Training is great and testing is bad. What next? Answer: The model is overfitting. Try more data, a simpler model or a different method.

## Tab 13: Words list

Hard words in one place
⚡ At a glance
🧠 Idea: A quick reference for the words in this lesson.
🧪 Example: Feature = one column that describes a record.
✅ Remember: Come back here whenever a word is unclear.

Word | Plain meaning

Model | The pattern a machine learns from data

Feature, label | An input column / the answer we want to predict

Supervised, unsupervised, reinforcement | Learning with answers / without answers / from rewards

Classification, regression | Predict a category / predict a number

Cluster | A group of similar items

Support, confidence | How common a combination is / how reliable an if-then rule is

Agent, policy | The learner in RL / its rule for choosing actions

Z-score | How many standard deviations a value is from the average

Dimension | One feature (one column)

PCA | A way to squeeze many features into a few

Bias | A model too simple to capture the real pattern

Variance | A model that changes a lot with different training data

Overfitting, underfitting | Too closely fitted to the training data / too simple

Confusion matrix | A table of hits and misses (TP, FN, FP, TN)

Cross-validation | Testing on each part of the data in turn and averaging the scores

---

# lesson06_supervised_machine_learning.html  (Lesson 6: Supervised Machine Learning | AI Notes)


## Tab 1: The big picture

The big picture: learning from solved examples
⚡ At a glance
🧠 Idea: We show the machine examples with answers, and it finds a rule that predicts the answer for new inputs.
🧪 Example: Hours studied → predicted GPA (a number). Hours studied → Pass or Fail (a category).
✅ Remember: Number = regression (linear regression). Category = classification (logistic regression).

In supervised learning, every training example comes with the right answer. The machine uses these to find a rule. This lesson covers the two most important methods: linear regression (predict a number) and logistic regression (predict a category).

🌍 Analogy: a ruler on a scatter plot. You scatter dots on paper, one for each student: hours studied across, GPA up. Then you lay a ruler so it passes as close to all the dots as possible. To predict a new student's GPA, you read the height of the ruler at their hours. The ruler is the model.

The path of this lesson

- Symbols and maths: a quick refresher so no step feels hard.
- Linear regression: the straight-line rule ŷ = w × x + b.
- Error: how to score how good a line is.
- Gradient descent: how the machine finds the best line by itself.
- Underfitting and overfitting: when a model is too simple or too wiggly.
- Logistic regression: how to predict categories using probabilities.

Check yourself 1
Predicting a student's GPA is regression or classification? Answer: Regression, because GPA is a number.

Check yourself 2
Predicting Pass or Fail uses which method in this lesson? Answer: Logistic regression (classification).

## Tab 2: Symbols and maths

The symbols and the maths you need
⚡ At a glance
🧠 Idea: A formula is a short sentence. Each letter stands for one thing.
🧪 Example: ŷ = w × x + b reads: prediction = weight × input + bias.
✅ Remember: A hat on a letter (ŷ) means predicted. No hat (y) means the real answer.

Symbol | Name | Plain meaning | Example

x | input (feature) | What we give the model | Hours studied = 3

y | actual value | The real answer from the data | Real GPA = 3.2

ŷ | y-hat, prediction | The answer the model guesses | Model says 2.8

w (also written m) | weight, slope | How strongly x affects the prediction. A steep line has a big w. | w = 0.8

b (also written c or w0) | bias, intercept | The starting value of the line when x = 0. It slides the line up or down. | b = 1.2

&epsilon; | error | Actual minus predicted: &epsilon; = y &minus; ŷ | 3.2 &minus; 2.0 = 1.2

E or SSE | total error | The sum of all the squared errors | 13.65

&Sigma; | sigma, sum | "Add up this thing for every data point" | &Sigma; &epsilon;&sup2;

&eta; (or &alpha;) | learning rate | How big each learning step is | 0.1

z | weighted sum | w × x + b before any squashing | z = 1.5

&sigma;(z) | sigmoid | Squashes any number into 0 to 1 | &sigma;(0) = 0.5

e (the number) | Euler's number | A fixed number, about 2.718, used inside the sigmoid. It is NOT the error. The error uses &epsilon;. | e &asymp; 2.718

Different letters, same idea: some books write the weight as w, m or H, and the bias as b, c or w0. For example ŷ = m x + c and ŷ = w1 x1 + w0 both mean: prediction = (weight × input) + bias.

Maths refresher
1. Slope of a straight line = how much it goes up for each step right: rise &divide; run. A line from (0, 1) to (3, 7): rise = 6, run = 3, slope = 2. Positive slope goes up to the right. Negative goes down. Zero is flat.

2. Slope of a curve at one point. A bowl is a curve, so its steepness changes from place to place. The slope at one point is the steepness of a tiny straight piece touching the curve. Trick: move a tiny bit to the right and see how much the height changes.

Example: E(w) = (w &minus; 3)&sup2;. At w = 0: E = 9. At w = 0.001: E = (&minus;2.999)&sup2; = 8.994001. The height changed by &minus;0.005999 over a step of 0.001, so the slope is about &minus;6. Negative slope means moving right makes the error smaller, so downhill is to the right. (Calculus gives the short formula 2 × (w &minus; 3); you do not need to derive it.)

3. Squares. Squaring means a number times itself: 4&sup2; = 16. A negative number squared becomes positive: (&minus;4)&sup2; = 16.

4. &Sigma;. For errors 1, &minus;2 and 3: &Sigma; &epsilon;&sup2; = 1 + 4 + 9 = 14.

5. Powers. A negative power means "one over": 2&minus;1 = 0.5. On a calculator use the ex button: e2 = 7.389, so e&minus;2 = 1 &divide; 7.389 = 0.135.

6. Probability is a number from 0 (impossible) to 1 (certain). Multiply by 100 for a percent: 0.82 is 82%.

7. Words that sound hard. Linear = straight line. Regression = predicting a number. Parameters = the numbers the machine adjusts while learning (w and b). Iteration = one round of updating.

Check yourself 1
A line rises 8 over a run of 4. Slope? Answer: 8 &divide; 4 = 2.

Check yourself 2
Errors are 2, &minus;3 and 1. What is &Sigma; &epsilon;&sup2;? Answer: 4 + 9 + 1 = 14.

## Tab 3: Linear regression

Linear regression: fitting a straight line
⚡ At a glance
🧠 Idea: Draw the best straight line through the dots, then use the line to predict a number.
🧪 Example: Line: ŷ = 2 × x + 1. For x = 3 hours, ŷ = 2 × 3 + 1 = 7.
✅ Remember: The line is ŷ = w x + b. Training means finding good w and b.

Linear regression finds the best straight line through the data so we can predict a number. This is also called curve fitting: finding a function that matches the data.

The formula
ŷ = w × x + b

- x is the input (hours studied).
- w (weight) is the slope: how much the prediction rises for each extra hour.
- b (bias) is where the line starts when x = 0.
- ŷ is the prediction.

Example: if w = 0.8 and b = 1.2, then for x = 2 hours: ŷ = 0.8 × 2 + 1.2 = 1.6 + 1.2 = 2.8. For x = 5: ŷ = 0.8 × 5 + 1.2 = 5.2.

Fitting means choosing w and b
Different w and b make different lines. There are infinitely many possible lines. "Training" means finding the w and b that give the best line. The next tab shows how to decide what "best" means.

Simple vs multiple linear regression
Type | Inputs | Formula | Example
Simple | 1 feature | ŷ = w1 x1 + w0 | marks from hours studied
Multiple | 2 or more features | ŷ = w0 + w1 x1 + w2 x2 + ... | marks from hours and attendance

Multiple example: ŷ = 20 + 5 × hours + 0.3 × attendance. For 4 hours and 90% attendance: 5 × 4 = 20, and 0.3 × 90 = 27. So ŷ = 20 + 20 + 27 = 67 marks. With two features the model fits a flat plane instead of a line.

The x0 = 1 trick
We can write ŷ = &Sigma; w_i x_i with x0 = 1. This just means: pretend there is an extra input that is always 1. Then w0 × 1 = w0, so the bias is treated like any other weight. It makes the formula shorter and is used in neural networks.

Check yourself 1
ŷ = 0.5 x + 2. Predict for x = 6. Answer: 0.5 × 6 + 2 = 5.

Check yourself 2
What does the bias b do? Answer: It sets the value of the line when x = 0, sliding the line up or down.

## Tab 4: How good is a line?

How good is a line? Error, SSE and R&sup2;
⚡ At a glance
🧠 Idea: Measure each miss, square it, add them all. A smaller total means a better line.
🧪 Example: Misses of 3 and &minus;4 give 9 + 16 = 25 total error.
✅ Remember: SSE = &Sigma; (y &minus; ŷ)&sup2;. The best line has the smallest SSE.

🎬 StatQuest: fitting a line with least squares
StatQuest fits a line to dots (mouse weight against mouse size) like this: draw a line, measure how far each dot is from the line (the residuals), square them and add them up. Then rotate the line and measure again. The line with the smallest sum of squares is the best-fitting line. That method is called least squares. Then R&sup2; tells you how much of the variation the line explains.

Step 1: the error of one point
&epsilon; = y &minus; ŷ. This is the gap between the real value and the prediction, like measuring how far an arrow landed from the bullseye. In statistics this gap is also called a residual.

Step 2: square it

- It stops errors cancelling. One point is 5 above the line (+5) and another is 5 below (&minus;5). Adding gives 0, which wrongly says "perfect". Squaring gives 25 + 25 = 50.
- It punishes big mistakes. An error of 2 becomes 4. An error of 10 becomes 100.

Step 3: add them up
SSE = &Sigma; (y &minus; ŷ)&sup2;

Worked example: two lines on the same data
Data (x = hours, y = GPA): (2, 2.8), (1, 3.2), (3, 3.8), (5, 3.6), (6, 2.9).

Line A: ŷ = 0.8 x + 1.2

x | y (actual) | ŷ (predicted) | &epsilon; = y &minus; ŷ | &epsilon;&sup2;
2 | 2.8 | 0.8 × 2 + 1.2 = 2.8 | 0 | 0
1 | 3.2 | 0.8 × 1 + 1.2 = 2.0 | 1.2 | 1.44
3 | 3.8 | 0.8 × 3 + 1.2 = 3.6 | 0.2 | 0.04
5 | 3.6 | 0.8 × 5 + 1.2 = 5.2 | &minus;1.6 | 2.56
6 | 2.9 | 0.8 × 6 + 1.2 = 6.0 | &minus;3.1 | 9.61

SSE of Line A = 0 + 1.44 + 0.04 + 2.56 + 9.61 = 13.65.

Line B: ŷ = 0.1 x + 3

x | y | ŷ | &epsilon; | &epsilon;&sup2;
2 | 2.8 | 3.2 | &minus;0.4 | 0.16
1 | 3.2 | 3.1 | 0.1 | 0.01
3 | 3.8 | 3.3 | 0.5 | 0.25
5 | 3.6 | 3.5 | 0.1 | 0.01
6 | 2.9 | 3.6 | &minus;0.7 | 0.49

SSE of Line B = 0.16 + 0.01 + 0.25 + 0.01 + 0.49 = 0.92. That is much smaller than 13.65, so Line B fits far better.

Rotating the line (the StatQuest idea) with numbers
Take the data (1, 2), (2, 3), (3, 5), (4, 4), (5, 6). The average x is 3 and the average y is 4. Keep each line passing through the point (3, 4) and just rotate it (change the slope):

Slope of the line | Line | SSE
0 (flat) | ŷ = 4 | 10
0.5 | ŷ = 2.5 + 0.5 x | 3.5
0.9 | ŷ = 1.3 + 0.9 x | 1.9
1.2 | ŷ = 0.4 + 1.2 x | 2.8

As we rotate from flat, the SSE falls (10, 3.5, 1.9) and then rises again (2.8). The lowest is near slope 0.9. That is the least squares line: ŷ = 1.3 + 0.9 x.

R&sup2;: how much does the line explain?
Compare two errors: the SSE around the average (the dumb guess: always predict 4) and the SSE around the fitted line.

- Around the average: (2&minus;4)&sup2; + (3&minus;4)&sup2; + (5&minus;4)&sup2; + (4&minus;4)&sup2; + (6&minus;4)&sup2; = 4 + 1 + 1 + 0 + 4 = 10.
- Around the line ŷ = 1.3 + 0.9 x (predictions 2.2, 3.1, 4.0, 4.9, 5.8): 0.04 + 0.01 + 1.0 + 0.81 + 0.04 = 1.9.

R&sup2; = (SSE around the average &minus; SSE around the line) &divide; SSE around the average

R&sup2; = (10 &minus; 1.9) &divide; 10 = 0.81. The line explains 81% of the variation. A value near 1 means a very good fit. A value near 0 means the line is no better than just guessing the average.

Why SSE depends on w and b
The data points are fixed facts. The only things we can change are w and b. So the error depends only on w and b: E = f(w, b). Plot E for every pair (w, b) and you get a bowl shape. The best line is at the bottom of the bowl.

🌍 Analogy: a bowl and a marble. Every spot on the bowl is one choice of (w, b). The height at that spot is the error. We want the marble to roll to the bottom.

Check yourself 1
Errors are 3 and &minus;4. SSE? Answer: 9 + 16 = 25.

Check yourself 2
SSE around the average is 20 and SSE around the line is 5. R&sup2;? Answer: (20 &minus; 5) &divide; 20 = 0.75, so 75%.

## Tab 5: Gradient descent

Gradient descent: rolling down the bowl
⚡ At a glance
🧠 Idea: Start with a guess. Check the slope. Take a small step downhill. Repeat.
🧪 Example: w = 0, slope = &minus;6, learning rate 0.1. New w = 0 &minus; 0.1 × (&minus;6) = 0.6.
✅ Remember: New w = old w &minus; &eta; × slope. A big &eta; overshoots. A small &eta; is slow.

🎬 StatQuest: gradient descent, step by step
StatQuest explains it by fitting just the intercept of a line.
- Start with a random guess for the intercept, for example 0.
- Find the slope (gradient) of the error curve at that point. Say it is &minus;190.
- Step size = slope × learning rate. With a learning rate of 0.1: &minus;190 × 0.1 = &minus;19.
- New intercept = old intercept &minus; step size = 0 &minus; (&minus;19) = 19.
- Repeat. The slope gets smaller as we near the bottom, so the steps shrink. After 13 steps the intercept settles at about 95. We stop when the steps are tiny (or after a maximum number of steps).

We cannot try every (w, b). Instead we start somewhere and keep stepping downhill on the error bowl until we reach the bottom.

🌍 Analogy: walking down a hill in thick fog. You cannot see the bottom, but you can feel which way the ground slopes under your feet. You step that way, then feel again. After many steps you reach the valley.

The steps

- Start with a random guess for w (and b).
- Find the slope of the error at this point. The slope says which direction is uphill.
- Take a step in the opposite direction (downhill).
- Repeat until the steps are very small.

new w = old w &minus; &eta; × slope

&eta; (the learning rate) is a small number you choose. Step size = &eta; × slope.

Worked example with one number
Let the error be E(w) = (w &minus; 3)&sup2;. This is a bowl whose bottom is at w = 3. Its slope is 2 × (w &minus; 3). Take &eta; = 0.1 and start at w = 0.

Step | w now | Slope = 2(w &minus; 3) | Step = 0.1 × slope | New w = w &minus; step
1 | 0 | &minus;6 | &minus;0.6 | 0.6
2 | 0.6 | &minus;4.8 | &minus;0.48 | 1.08
3 | 1.08 | &minus;3.84 | &minus;0.384 | 1.464
4 | 1.464 | &minus;3.072 | &minus;0.3072 | 1.7712

- The slope is negative, so the bowl goes down to the right. Subtracting a negative step makes w bigger, moving toward 3.
- The slope gets smaller as we near the bottom (&minus;6, &minus;4.8, &minus;3.84...), so the steps shrink on their own. At the very bottom the slope is 0.
- The error also falls: 9, 5.76, 3.69, 2.36, 1.51.

The learning rate matters
Just right (&eta; = 0.1)
Steady steps toward 3.
Too big (&eta; = 1.1)
w goes 0, 6.6, &minus;1.32, 8.18... It jumps past the bottom and gets worse each time.
Too small (&eta; = 0.001)
The first step is only 0.006. It would need thousands of steps.

Check the too-big case: w = 0, slope &minus;6, step = 1.1 × (&minus;6) = &minus;6.6, so w = 6.6. Next slope = 2(6.6 &minus; 3) = 7.2, step = 7.92, w = 6.6 &minus; 7.92 = &minus;1.32. Next slope = 2(&minus;1.32 &minus; 3) = &minus;8.64, step = &minus;9.504, w = &minus;1.32 + 9.504 = 8.184.

🌍 Analogy: too big = running down the hill and flying across to the other side. Too small = shuffling forward one millimetre at a time.

Gradient descent on a real line
For linear regression the error E depends on both w and b, so we find two slopes and update both:

- slope for b = &minus;2 × &Sigma; (y &minus; ŷ)
- slope for w = &minus;2 × &Sigma; x (y &minus; ŷ)

(The &minus;2 comes from calculus. Just know the pattern.)

Example: data (1, 2), (2, 4), (3, 6). Start w = 0, b = 0, &eta; = 0.01.

- Predictions are all 0. Errors y &minus; ŷ = 2, 4, 6. SSE = 4 + 16 + 36 = 56.
- Slope for b = &minus;2 × (2 + 4 + 6) = &minus;24.
- Slope for w = &minus;2 × (1×2 + 2×4 + 3×6) = &minus;2 × 28 = &minus;56.
- New b = 0 &minus; 0.01 × (&minus;24) = 0.24. New w = 0 &minus; 0.01 × (&minus;56) = 0.56.
- New predictions: x = 1: 0.56 + 0.24 = 0.80. x = 2: 1.12 + 0.24 = 1.36. x = 3: 1.68 + 0.24 = 1.92.
- New errors: 1.2, 2.64, 4.08. New SSE = 1.44 + 6.97 + 16.65 = 25.06.

One step cut the error from 56 to 25.06. The best line is ŷ = 2x, which has SSE = 0. Many more steps would get there.

Check yourself 1
w = 5, slope = 4, learning rate 0.1. New w? Answer: 5 &minus; 0.1 × 4 = 4.6.

Check yourself 2
What happens if the learning rate is too big? Answer: The steps overshoot the bottom and the error can bounce around or get worse.

## Tab 6: Underfit and overfit

Underfitting and overfitting
⚡ At a glance
🧠 Idea: A model can be too simple (underfit) or too wiggly (overfit). We want the middle.
🧪 Example: A straight line on S-shaped data misses badly. A zig-zag through every dot memorises noise.
✅ Remember: Underfit = high bias. Overfit = high variance. Good = balanced.

"All models are wrong. Some are useful." Our goal is a useful model: one that works well on new data.

🌍 Analogy: studying for an exam. Studying only the chapter titles is underfitting: too shallow. Memorising last year's paper word for word is overfitting: you fail when the questions change. Understanding the ideas is the sweet spot.

 | Underfitting | Good fit | Overfitting
Also called | High bias | Balanced | High variance
Model | Too simple (a straight line for an S-shaped pattern) | Follows the broad pattern | Too flexible (a zig-zag touching every dot)
Training error | High | Low | Almost zero
Testing error | High | Low | High

- Bias means the model holds a rigid, wrong assumption, such as "the pattern must be a straight line", and ignores what the data shows.
- Variance means that if you trained on a slightly different sample, the curve would change a lot.

The bias-variance problem is finding the right model complexity. A more complex model lowers bias but raises variance. A simpler model does the opposite.

Example diagnosis: Model 1 has training error 12 and testing error 13. Both are high, so it is underfitting. Model 2 has training error 1 and testing error 15. The big gap says it is overfitting.

Check yourself 1
Training error 0.5, testing error 9. Diagnosis? Answer: Overfitting (high variance).

Check yourself 2
Which has high bias: a straight line fitted to a curve, or a zig-zag through every dot? Answer: The straight line.

## Tab 7: Logistic regression

Logistic regression: predicting categories
⚡ At a glance
🧠 Idea: Despite its name, it classifies. It turns z = w x + b into a probability between 0 and 1.
🧪 Example: Hours studied 5 gives z = 1.5, probability 0.82, so predict Pass.
✅ Remember: The sigmoid squashes any number into 0 to 1. Probability ≥ 0.5 means class 1.

🎬 StatQuest: Logistic Regression
The video predicts whether a mouse is obese from its weight. Instead of fitting a straight line, logistic regression fits an S-shaped curve that goes from 0 to 1. The curve tells you the probability that a mouse is obese for its weight: a light mouse has only a small probability, a heavy mouse a high one. It is usually used for classification: if the probability is more than 50%, we classify the mouse as obese. It can also use other kinds of data, such as genotype, to classify. And instead of least squares, it picks the best curve using maximum likelihood (explained below).

Logistic regression predicts the chance that an input belongs to a class, such as Pass or Fail, Spam or Not spam, Obese or Not obese. The name says "regression", but it is a classification method.

Why not just use a straight line?

- A straight line goes on forever. It can give &minus;1.5 or +3.2, but a probability must stay between 0 and 1.
- One extreme data point far to the side can tilt the whole line and change which points are classified correctly.

The sigmoid function
Step 1: compute the weighted sum, like linear regression: z = w × x + b. Step 2: pass z through the sigmoid:

ŷ = &sigma;(z) = 1 / (1 + e&minus;z)

z | e&minus;z | &sigma;(z) = 1 / (1 + e&minus;z) | Meaning
&minus;5 | 148.4 | 1 / 149.4 = 0.0067 | almost 0%
&minus;2 | 7.389 | 1 / 8.389 = 0.119 | 12%
0 | 1 | 1 / 2 = 0.5 | 50%
2 | 0.135 | 1 / 1.135 = 0.881 | 88%
5 | 0.0067 | 1 / 1.0067 = 0.993 | almost 100%

Big positive z gives a probability near 1. Big negative z gives near 0. z = 0 gives exactly 0.5. The curve is a smooth S shape that never leaves the range 0 to 1.

From probability to a decision
predict 1 if ŷ ≥ 0.5, predict 0 if ŷ < 0.5

0.5 is the usual threshold. A spam probability of 0.82 means spam (1). A probability of 0.15 means not spam (0). The place where z = 0 (probability exactly 0.5) is the decision boundary. Data on one side is Class 1 and on the other side is Class 0.

Worked example: pass or fail
Data (hours, result): (2, 0), (1, 0), (5, 1), (3, 0), (6, 1). Suppose training gave w = 1 and b = &minus;3.5. So z = x &minus; 3.5.

Hours x | z = x &minus; 3.5 | &sigma;(z) | Predicted class | Actual
1 | &minus;2.5 | 0.076 | 0 | 0
2 | &minus;1.5 | 0.182 | 0 | 0
3 | &minus;0.5 | 0.378 | 0 | 0
5 | 1.5 | 0.818 | 1 | 1
6 | 2.5 | 0.924 | 1 | 1

All 5 are correct. The decision boundary is at z = 0, which means x = 3.5 hours. For a new student with 4 hours: z = 4 &minus; 3.5 = 0.5, &sigma;(0.5) = 1 / (1 + 0.6065) = 0.6225. That is above 0.5, so predict Pass (1).

How does the model find w and b?
The same way as before: score every choice with an error, then use gradient descent to lower it. One way to score is the SSE with the sigmoid output, E = &Sigma; (y &minus; &sigma;(...))&sup2;. Using the same 5 students:

Hours x | Actual y | Choice 1: w = 1, b = &minus;3.5, prediction | &epsilon;&sup2; for choice 1 | Choice 2: w = 0.2, b = 0, prediction | &epsilon;&sup2; for choice 2

2 | 0 | 0.182 | 0.033 | 0.599 | 0.358

1 | 0 | 0.076 | 0.006 | 0.550 | 0.302

5 | 1 | 0.818 | 0.033 | 0.731 | 0.072

3 | 0 | 0.378 | 0.143 | 0.646 | 0.417

6 | 1 | 0.924 | 0.006 | 0.769 | 0.054

Total error E (SSE) | 0.221 |  | 1.204

Choice 1 has a much smaller total error (0.221 against 1.204), so it is the better choice. Gradient descent starts from a poor guess like choice 2 and takes small downhill steps until it reaches something like choice 1.

The StatQuest way to score: maximum likelihood
Another way to pick the best S-curve asks: "How likely is the data we actually saw?" For each obese mouse, the likelihood is the height of the curve at its weight (the probability the curve gives for obese). For each non-obese mouse, the likelihood is 1 minus that height. Multiply all the likelihoods together. The curve with the biggest product is the best.

Example: 3 mice: obese, not obese, obese.

- Curve A gives 0.9, 0.2, 0.7. Likelihood = 0.9 × (1 &minus; 0.2) × 0.7 = 0.9 × 0.8 × 0.7 = 0.504.
- Curve B gives 0.6, 0.5, 0.5. Likelihood = 0.6 × 0.5 × 0.5 = 0.15.

Curve A makes the data much more likely, so it is the better curve.

More inputs and the hyperplane
With several inputs, z = w0 + w1 x1 + w2 x2 + ... (using the x0 = 1 trick). Compare two models:

- Model A (linear regression): ŷ = w1 x1 + w2 x2 + w0
- Model B (logistic regression): ŷ = 1 / (1 + e&minus;(w1 x1 + w2 x2 + w0))

Model B is Model A pushed through a sigmoid. The decision boundary is called a hyperplane: a point when there is 1 feature, a line for 2 features, a flat plane for 3 features.

Linear vs logistic
 | Linear regression | Logistic regression
Task | Regression (a number) | Classification (a category)
Output | Any number | A probability from 0 to 1
Equation | ŷ = w x + b | ŷ = 1 / (1 + e&minus;(w x + b))
How the best fit is found | Least squares (smallest SSE) | Maximum likelihood (or a small error)
Example | House price | Is this email spam?

Check yourself 1
With w = 1 and b = &minus;3.5, what class for 3 hours? Answer: z = &minus;0.5, &sigma;(z) = 0.378, which is below 0.5, so class 0 (Fail).

Check yourself 2
Curve X has likelihood 0.4 and curve Y has 0.1 for the same data. Which is better? Answer: Curve X, because it makes the data more likely.

## Tab 8: Words list

Hard words in one place
⚡ At a glance
🧠 Idea: A quick reference for the difficult words in this lesson.
🧪 Example: Residual = the gap between a real value and the prediction.
✅ Remember: Come back here whenever a word is unclear.

Word | Plain meaning

Regression | Predicting a number

Classification | Predicting a category

Weight, bias | The slope of the line / where the line starts

Residual, error | The gap between a real value and its prediction

SSE | Sum of squared errors: the total error of a line

Least squares | Choosing the line with the smallest SSE

R&sup2; | How much of the variation the line explains (0 to 1)

Gradient descent | Taking small downhill steps on the error to find the best weights

Learning rate | How big each step is

Slope (gradient) | How steep the error curve is at one spot

Sigmoid | An S-shaped function that squashes any number into 0 to 1

Threshold | The cut-off for deciding a class, usually 0.5

Decision boundary / hyperplane | The place that separates the classes

Maximum likelihood | Choosing the curve that makes the observed data most likely

Bias, variance | Too simple a model / a model that changes a lot with the data

---

# lesson07_neural_networks.html  (Lesson 7: Neural Networks | AI Notes)


## Tab 1: The big idea

The big idea: a squiggle-fitting machine
⚡ At a glance
🧠 Idea: A neural network is a team of tiny calculators that together can fit a curvy "squiggle" to data.
🧪 Example: A drug works at a medium dose but not at a low or high dose. A straight line cannot fit that. A neural network can.
✅ Remember: Input layer, hidden layer(s), output layer. Weights and biases are the numbers it learns.

🎬 StatQuest: "Neural Networks Pt. 1: Inside the Black Box"
Josh Starmer says that a neural network is just a "big fancy squiggle-fitting machine". Give it some data and it fits a squiggle to it. People call neural networks "black boxes", but the video opens the box and shows there is nothing mysterious inside: just weights, biases and curved lines (activation functions) added together. The video uses a drug-dose example, which is the one used in this lesson.

The problem a straight line cannot solve
A drug is tested at three doses:

Dose | Effective? | Value
Low | No | 0
Medium | Yes | 1
High | No (too much) | 0

The pattern goes 0, then 1, then 0. It rises and then falls, like a hill. A straight line (linear regression, Lesson 6) can only go up or down, so it cannot follow a hill. We need something that can bend.

🌍 Analogy: bending wire. A straight ruler cannot trace a hill. But if you have a few pieces of bendy wire, you can stretch, flip and join them to make almost any shape. A neural network does this with curved lines. Each tiny calculator (a neuron) makes one bendy wire. The network joins them into a squiggle.

The parts, in plain words

- Neuron (node): one tiny calculator. It takes numbers in and gives one number out.
- Layer: a row of neurons. Input layer receives the data. Hidden layer sits in the middle (hidden because we do not directly see its values). Output layer gives the answer.
- Weight (w): a number that multiplies an input. A big weight means that input matters more.
- Bias (b): a number added afterwards. It shifts the result up or down.
- Activation function: a curved line that bends the number a neuron produces. This is what lets the network make curves.

Check yourself 1
Why can't a straight line fit the drug data 0, 1, 0? Answer: The pattern rises and then falls, but a straight line can only go in one direction.

Check yourself 2
What is a hidden layer? Answer: A layer of neurons between the input and output layers.

## Tab 2: Inside a neuron

Inside one neuron: two steps
⚡ At a glance
🧠 Idea: Step 1: weight the input and add the bias. Step 2: pass the result through an activation function.
🧪 Example: Inputs 2 and 3, weights 0.5 and &minus;1, bias 1 give z = &minus;1.
✅ Remember: z = &Sigma; w x + b, then a = f(z).

Every neuron does the same two things, one after the other: combine, then bend.

🌍 Analogy: deciding whether to go to a party. You ask your friends. Each friend's opinion (input) counts more or less for you (weight). You add up the opinions and add your own mood (bias). That total is z. Then you decide how excited to feel (activation).

Step 1: the weighted sum
z = w1 x1 + w2 x2 + ... + b

With just one input it is simply z = w × x + b, the same line formula as Lesson 6.

Step 2: the activation function
a = f(z)

The activation function bends z into the neuron's output a.

Worked example
Inputs x1 = 2 and x2 = 3. Weights w1 = 0.5 and w2 = &minus;1. Bias b = 1.

z = (0.5 × 2) + (&minus;1 × 3) + 1 = 1 &minus; 3 + 1 = &minus;1.

Activation | Output f(&minus;1)
Linear f(z) = z | &minus;1
Sigmoid | 1 / (1 + e1) = 1 / 3.718 = 0.269
Tanh | &minus;0.762
ReLU max(0, z) | 0
SoftPlus ln(1 + ez) | ln(1 + 0.368) = 0.313

The same z gives different outputs. The activation function you choose changes what the neuron does.

Real brain cells inspired this
Real neuron part | What it does | Artificial version

Dendrites | Receive signals from nearby cells | Inputs (x)

Synapse strength | How strong a connection is. It can grow or shrink with experience. | Weights (w)

Cell body | Collects all the incoming charges | The sum (&Sigma;)

Axon hillock | Checks if the total passes a threshold (about &minus;55 mV) | Activation function and bias

Axon | Sends a spike to the next cells | The output

Warm mug vs hot stove: a warm mug sends weak signals that barely reach the threshold, so the neuron fires slowly. A hot stove sends strong signals far past the threshold, so it fires at full strength and you pull your hand away. A real neuron fires fully or not at all (the all-or-none law). Activation functions are a smoother maths version of that rule.

Check yourself 1
x = (1, 4), w = (2, &minus;0.5), b = 0.5. What is z? Answer: 2 &minus; 2 + 0.5 = 0.5.

Check yourself 2
In an artificial neuron, what plays the role of synapse strength? Answer: The weights.

## Tab 3: Building the squiggle

Building the squiggle, step by step
⚡ At a glance
🧠 Idea: Two hidden neurons each make a curve. We scale the curves, add them and add a bias to get the squiggle.
🧪 Example: Dose 0 gives about 0, dose 0.5 gives about 1, dose 1 gives about 0.
✅ Remember: Input → weight and bias → activation → scale by weight → add → add bias.

🎬 The StatQuest network
The video's network has one input (the dose), two hidden nodes and one output. Each hidden node uses the same curved activation function, SoftPlus, but each has different weights and biases, so each makes a differently shaped curve. The network stretches and flips those curves and adds them together to make a squiggle that fits the data.

The SoftPlus curve
SoftPlus is f(x) = ln(1 + ex). It is a smooth curve that is almost 0 for negative x and then curves up into a rising line. Examples: f(&minus;5) &asymp; 0.007, f(0) = 0.693, f(2.14) = 2.25.

The numbers (the dose has been scaled to run from 0 to 1)
Connection | Weight | Bias
Input to hidden node 1 | &minus;34.4 | 2.14
Input to hidden node 2 | &minus;2.52 | 1.29
Hidden node 1 to output | &minus;1.3 |
Hidden node 2 to output | 2.28 |
Final bias on the output |  | &minus;0.58

Predict for dose = 0

- Hidden node 1: x = &minus;34.4 × 0 + 2.14 = 2.14. SoftPlus gives 2.25.
- Hidden node 2: x = &minus;2.52 × 0 + 1.29 = 1.29. SoftPlus gives 1.53.
- Scale the curves: 2.25 × (&minus;1.3) = &minus;2.93. And 1.53 × 2.28 = 3.49.
- Add them and the final bias: &minus;2.93 + 3.49 &minus; 0.58 = &minus;0.01, which is about 0. Not effective, as the data says.

Predict for dose = 0.5

- Node 1: x = &minus;34.4 × 0.5 + 2.14 = &minus;15.06. SoftPlus is almost 0.
- Node 2: x = &minus;2.52 × 0.5 + 1.29 = 0.03. SoftPlus gives 0.71.
- Scale: 0 × (&minus;1.3) = 0. And 0.71 × 2.28 = 1.61.
- Add the final bias: 0 + 1.61 &minus; 0.58 = 1.03, about 1. Effective, as the data says.

The whole squiggle
Dose | Node 1 curve (after SoftPlus) | Node 2 curve (after SoftPlus) | Output = &minus;1.3 × node 1 + 2.28 × node 2 &minus; 0.58

0 | 2.25 | 1.53 | &minus;0.01

0.25 | 0.00 | 1.08 | 1.87

0.5 | 0.00 | 0.71 | 1.03

0.75 | 0.00 | 0.44 | 0.42

1 | 0.00 | 0.26 | 0.00

The output starts near 0, rises above 1, then falls back to 0 at dose 1. It makes a hill, which is exactly the squiggle the data needs. At the three data doses (0, 0.5, 1) the network gives about 0, 1, 0.

Why it works

- Node 1 makes a curve that is high at the start and drops quickly to 0. Its weight &minus;1.3 flips it upside down.
- Node 2 makes a gentle falling curve. Its weight 2.28 stretches it taller.
- Adding the flipped, stretched curves, plus the bias that shifts everything, gives a hill.

🌍 Analogy: building a hill from bendy wires. One wire is stretched and flipped, another is stretched. Lay them together, slide them up or down with the bias, and you have a hill.

The hidden layer here has two nodes. A bigger network with more nodes can make a more detailed squiggle. The weights and biases are the numbers that training finds. Training is explained in the "How a network learns" tab.

Check yourself 1
In the network above, what is the output at dose 1? Answer: Node 1 &asymp; 0, node 2 &asymp; 0.26, so 0 + 2.28 × 0.26 &minus; 0.58 = 0.01, about 0.

Check yourself 2
What does the weight &minus;1.3 do to node 1's curve? Answer: It scales it and flips it upside down.

## Tab 4: Activation functions

Activation functions
⚡ At a glance
🧠 Idea: An activation function bends z into the neuron's output and lets the network learn curves.
🧪 Example: For z = 2: linear 2, sigmoid 0.88, tanh 0.96, ReLU 2.
✅ Remember: Output layer: linear for regression, sigmoid for yes/no. Hidden layers: usually ReLU (or SoftPlus).

Why we need them: without one, layers collapse
Say layer 1 is z1 = 2x + 1 and layer 2 is z2 = 3 × z1 &minus; 2. Put layer 1 into layer 2: z2 = 3(2x + 1) &minus; 2 = 6x + 3 &minus; 2 = 6x + 1. Two layers became one straight line. Check with x = 2: layer 1 gives 5, layer 2 gives 3 × 5 &minus; 2 = 13, and 6 × 2 + 1 = 13. A network made only of straight-line steps is still just a straight line, however deep. An activation function bends the signal and stops this. (This is why the drug network needs SoftPlus.)

The functions
Name | Formula | Output range | Shape

Linear | f(z) = z | &minus;&infin; to +&infin; | Straight line

Sigmoid | f(z) = 1 / (1 + e&minus;z) | 0 to 1 | S-shape

Tanh | f(z) = (ez &minus; e&minus;z) / (ez + e&minus;z) | &minus;1 to 1 | S-shape through (0, 0)

ReLU | f(z) = max(0, z) | 0 to +&infin; | Flat then a rising line

SoftPlus | f(z) = ln(1 + ez) | 0 to +&infin; | A smooth version of ReLU

z | Linear | Sigmoid | Tanh | ReLU
&minus;2 | &minus;2 | 0.119 | &minus;0.964 | 0
0 | 0 | 0.5 | 0 | 0
2 | 2 | 0.881 | 0.964 | 2

1. Linear: f(z) = z
What goes in comes out. Use: the output layer for regression (house price, temperature). Limit: in hidden layers it makes the layers collapse into one line.

2. Sigmoid
Squashes any number into 0 to 1. Big positive z gives near 1. Big negative z gives near 0. z = 0 gives exactly 0.5. Use: the output layer for yes/no classification, because the output is a probability (0.88 means 88% chance).

Limit 1: vanishing gradient. At very large or very small z the curve is almost flat. The slope of the sigmoid is &sigma;(1 &minus; &sigma;). At z = 0 the slope is 0.5 × 0.5 = 0.25. At z = 2 it is 0.881 × 0.119 = 0.105. At z = 5 it is 0.993 × 0.007 = 0.0066. When the slope is near 0, gradient descent takes tiny steps, so the early layers almost stop learning.

Limit 2: not zero-centred. All outputs are positive, so the weight updates lean the same way and zig-zag.

3. Tanh
A scaled, shifted sigmoid with range &minus;1 to +1, crossing (0, 0). Advantage: outputs are centred around zero, which balances the updates. Limit: it also flattens at the extremes, so the vanishing gradient problem remains.

4. ReLU (Rectified Linear Unit)
A one-way valve: it blocks negatives and lets positives pass. If z ≤ 0 the output is 0. If z > 0 the output is z. It makes a bent line, and bent lines can be added up to build squiggles too (StatQuest's "ReLU in Action" uses this idea).

- Cheap: it only needs an "is it above 0?" check.
- No flat part for positives: the slope is exactly 1, so gradients do not vanish.
- Sparse: negatives become 0, so many neurons stay quiet.
- Limit, dying ReLU: if a neuron's input is always negative, it always outputs 0 with slope 0 and stops learning for good.

5. SoftPlus
A smooth version of ReLU (the one used in the drug network). It has no sharp corner, which makes the slope easier to work with.

Where to use which
Function | Zero-centred? | Vanishing gradient? | Typical use
Linear | Yes (if the input is) | No | Output layer, regression
Sigmoid | No | Yes, at the extremes | Output layer, yes/no
Tanh | Yes | Yes, at the extremes | Hidden layers (older style)
ReLU / SoftPlus | No | None for z > 0 (ReLU freezes if z ≤ 0) | Hidden layers (most common today)

Check yourself 1
ReLU(&minus;3) and ReLU(4.5)? Answer: 0 and 4.5.

Check yourself 2
Which activation suits the output of a yes/no classifier? Answer: Sigmoid, because its output is a probability from 0 to 1.

## Tab 5: How a network learns

How a network learns
⚡ At a glance
🧠 Idea: Guess, measure the error, find which weights caused it, nudge them, repeat.
🧪 Example: A bias of 0 gives error 1.04. After one nudge (&minus;0.35) the error is 0.17.
✅ Remember: Forward pass, loss, backpropagation, update. One epoch = the whole data once.

🎬 StatQuest: "Neural Networks Pt. 2: Backpropagation Main Ideas"
Backpropagation uses the chain rule to find the slope of the error for every weight and bias, and then uses gradient descent to nudge them. The video starts with the simplest case: optimize only the last bias, b3, and keep every other number fixed. The same steps then work for every other parameter. That is the example below.

🌍 Analogy: practising with past papers. You attempt a paper (forward pass). You get your marks (loss). You work out which misunderstanding caused each lost mark (backpropagation). You study those parts again (update the weights). Doing the whole pile of papers once is one epoch.

The 5 steps

- Start with a guess for the weights and biases.
- Forward pass: send the data through to get predictions.
- Loss: measure the error. We use the sum of squared residuals (SSR), like SSE in Lesson 6.
- Backpropagation: find the slope of the loss for each weight and bias.
- Gradient descent: new value = old value &minus; learning rate × slope.

Backpropagation finds the slopes. Gradient descent uses them to update the values.

The chain rule, in plain words
If A changes B, and B changes C, then how much A changes C = (how much A changes B) × (how much B changes C). Example: 1 hour of work earns 10 dollars. 1 dollar buys 3 sweets. So 1 hour buys 10 × 3 = 30 sweets.

Worked example: optimizing the last bias b3
Use the drug network. The data: dose 0 → 0, dose 0.5 → 1, dose 1 → 0. Keep every weight and bias fixed except the final bias b3. Before adding b3, the three predictions are 0.569, 1.615 and 0.585.

The slope. The loss SSR depends on the predictions, and each prediction depends on b3 (adding b3 raises it one-for-one). By the chain rule: slope = &Sigma; &minus;2 × (observed &minus; predicted) × 1.

Start with b3 = 0 and learning rate 0.1:

- Predictions: 0.569, 1.615, 0.585. Residuals (observed &minus; predicted): &minus;0.569, &minus;0.615, &minus;0.585.
- SSR = 0.324 + 0.378 + 0.342 = 1.04.
- Slope = &minus;2 × (&minus;0.569 &minus; 0.615 &minus; 0.585) = &minus;2 × (&minus;1.769) = 3.54.
- Step size = 0.1 × 3.54 = 0.354. New b3 = 0 &minus; 0.354 = &minus;0.354.

Round | b3 | SSR | Slope | New b3
1 | 0 | 1.044 | 3.537 | &minus;0.354
2 | &minus;0.354 | 0.168 | 1.415 | &minus;0.495
3 | &minus;0.495 | 0.028 | 0.566 | &minus;0.552
4 | &minus;0.552 | 0.005 | 0.226 | &minus;0.574
5 | &minus;0.574 | 0.002 | 0.091 | &minus;0.584

The error falls from 1.04 to almost 0, and the slope shrinks toward 0 as b3 settles near &minus;0.58, the value used in the network above. We stop when the steps are tiny.

Epoch
One epoch = one complete pass of the whole training set through the network, forward and backward. With 1,000 samples, seeing all 1,000 once is 1 epoch. Training for 20 epochs is 20 full passes. Why many epochs? One pass is not enough to learn everything, just as you read a chapter several times to remember it.

Worked example: one learning step on one neuron
One neuron with a sigmoid, inputs x1 = 1 and x2 = 1, and the bias input x0 = 1. Target y = 1. All weights start at 0. Learning rate &eta; = 1. Error E = (y &minus; ŷ)&sup2;.

- Forward pass: z = 0 + 0 + 0 = 0, so ŷ = &sigma;(0) = 0.5.
- Loss: (1 &minus; 0.5)&sup2; = 0.25.
- Slope for each weight = &minus;2 (y &minus; ŷ) × ŷ (1 &minus; ŷ) × x. These three parts are the chain rule: how the error depends on ŷ, the slope of the sigmoid, and how the weight affects z. Here: &minus;2 × 0.5 × 0.25 × 1 = &minus;0.25.
- Update: new w = 0 &minus; 1 × (&minus;0.25) = 0.25 for every weight.
- Check: new z = 0.75, so ŷ = &sigma;(0.75) = 0.679. It moved from 0.5 toward the target 1.

Some books write the weight change as &Delta;w = &eta; × (slope of the error) with the minus sign hidden inside the slope. To go downhill the step must be minus the slope, as in Lesson 6. Either way, the weights always move to lower the error.

Check yourself 1
Slope 2, learning rate 0.1, b3 = 1. New b3? Answer: 1 &minus; 0.1 × 2 = 0.8.

Check yourself 2
What does backpropagation compute? Answer: The slope of the loss for every weight and bias, using the chain rule. Gradient descent then uses these slopes.

## Tab 6: AND, XOR and layers

Logic gates: why we need hidden layers
⚡ At a glance
🧠 Idea: A single neuron can learn AND but cannot learn XOR. XOR needs a hidden layer.
🧪 Example: AND gives 1 only for (1, 1). XOR gives 1 when exactly one input is 1.
✅ Remember: AND is linearly separable. XOR is not.

A logic gate takes inputs of 0 or 1 and gives an output of 0 or 1. We can train a neuron using the input and output rows of a gate.

The AND gate
x1 | x2 | AND
0 | 0 | 0
0 | 1 | 0
1 | 0 | 0
1 | 1 | 1

The neuron computes z = w0 + w1 x1 + w2 x2 and then ŷ = f(z). Training adjusts the weights until the outputs match, using the error E = &Sigma; (y &minus; ŷ)&sup2; and gradient descent. Suppose training ends with w0 = &minus;6, w1 = 4, w2 = 4:

x1 | x2 | z = &minus;6 + 4 x1 + 4 x2 | &sigma;(z) | Rounded
0 | 0 | &minus;6 | 0.0025 | 0
0 | 1 | &minus;2 | 0.119 | 0
1 | 0 | &minus;2 | 0.119 | 0
1 | 1 | 2 | 0.881 | 1

All four match AND. Why one neuron can do AND: the class 0 points (0,0), (0,1), (1,0) and the class 1 point (1,1) can be split by one straight line. So AND is linearly separable.

The XOR gate
x1 | x2 | XOR
0 | 0 | 0
0 | 1 | 1
1 | 0 | 1
1 | 1 | 0

XOR means "exactly one of the two is 1". Class 1 points: (0,1) and (1,0). Class 0 points: (0,0) and (1,1). Draw the four corners of a square. The two class 1 points sit on one diagonal and the two class 0 points on the other. No single straight line can put both class 1 points on one side and both class 0 points on the other. So XOR is not linearly separable, and a single neuron (or basic logistic regression) cannot solve it. It is a famous problem in AI history. A network that does solve XOR gives outputs like 0.03, 0.97, 0.96 and 0.04 for the four rows, which round to 0, 1, 1, 0.

🌍 Analogy: try to separate two chess-board colours with one straight ruler. It cannot be done. You need two cuts.

How a hidden layer solves XOR
XOR = (x1 OR x2) AND NOT (x1 AND x2). So use 2 hidden neurons, one for OR and one for AND, and an output neuron that says "OR is on and AND is off". Example weights:

- Hidden 1 (OR): a1 = &sigma;(20 x1 + 20 x2 &minus; 10)
- Hidden 2 (AND): a2 = &sigma;(20 x1 + 20 x2 &minus; 30)
- Output: &sigma;(20 a1 &minus; 20 a2 &minus; 10)

x1 | x2 | a1 (OR) | a2 (AND) | Output z = 20 a1 &minus; 20 a2 &minus; 10 | Output
0 | 0 | &asymp;0 | &asymp;0 | &minus;10 | &asymp;0
0 | 1 | &asymp;1 | &asymp;0 | 10 | &asymp;1
1 | 0 | &asymp;1 | &asymp;0 | 10 | &asymp;1
1 | 1 | &asymp;1 | &asymp;1 | &minus;10 | &asymp;0

The outputs are 0, 1, 1, 0, which is XOR. Check one row: for (1, 1), a1 = &sigma;(30) &asymp; 1 and a2 = &sigma;(10) &asymp; 1, so z = 20 &minus; 20 &minus; 10 = &minus;10 and the output is &sigma;(&minus;10) &asymp; 0. Each hidden neuron draws one straight boundary. The output neuron combines the two boundaries into a shape no single line can make. This is why adding more neurons becomes necessary.

Check yourself 1
What is XOR of (1, 0)? Answer: 1, because exactly one input is 1.

Check yourself 2
Why can't one neuron solve XOR? Answer: XOR is not linearly separable: no single straight line splits the classes.

## Tab 7: Hidden layers and MLP

Hidden layers and the Multi-Layer Perceptron (MLP)
⚡ At a glance
🧠 Idea: An MLP has an input layer, at least one hidden layer and an output layer.
🧪 Example: 2 inputs, 3 hidden neurons, 1 output: 9 weights and 4 biases.
✅ Remember: Each hidden neuron makes its own boundary. Activation functions add non-linear behaviour.

A hidden layer is a middle layer between the input and output layers. An MLP is a neural network with an input layer, at least one hidden layer and an output layer. The drug network (1 input, 2 hidden nodes, 1 output) is a small MLP.

Take 2 inputs (x1, x2), 3 hidden neurons (giving a1, a2, a3) and one output neuron. The output is:

z = a1 w7 + a2 w8 + a3 w9 + bias, then ŷ = 1 / (1 + e&minus;z)

Counting the weights

- Input to hidden: 2 inputs × 3 hidden neurons = 6 weights (w1 to w6).
- Hidden to output: 3 × 1 = 3 weights (w7 to w9).
- Total weights = 9. Biases: 3 for the hidden neurons + 1 for the output = 4. So 13 numbers are trained.

Worked forward pass
Input x = (1, 2). Use ReLU in the hidden layer, no hidden biases. Hidden weights (for x1, x2): neuron 1 = (0.5, &minus;1), neuron 2 = (1, 1), neuron 3 = (&minus;0.5, 0.5). Output weights = (1, 0.5, 2), output bias = &minus;1, with a sigmoid output.

- Hidden 1: z = 0.5 × 1 + (&minus;1) × 2 = &minus;1.5. ReLU gives 0.
- Hidden 2: z = 1 × 1 + 1 × 2 = 3. ReLU gives 3.
- Hidden 3: z = &minus;0.5 × 1 + 0.5 × 2 = 0.5. ReLU gives 0.5.
- Output: z = 0 × 1 + 3 × 0.5 + 0.5 × 2 &minus; 1 = 1.5.
- ŷ = &sigma;(1.5) = 1 / (1 + 0.223) = 0.818: about an 82% chance of class 1.

What each hidden neuron does

- One neuron gives one straight (linear) boundary. Hidden neuron 1 makes boundary 1. Hidden neuron 2 makes boundary 2. The output neuron combines them.
- Hidden layers let a network solve XOR and fit squiggles.
- The activation functions add non-linear behaviour. Without them, all the layers would collapse into one straight line.
- Neural networks work well with both numerical data (like prices) and categorical data (like Pass or Fail).

Simple models cannot fit every dataset
Data shaped like a bump cannot be followed by a straight line or a simple S-curve. Underfitting: the model is too simple to capture the pattern. Overfitting: the model is so complex that it memorises the training data, including its noise. So we add enough neurons to capture the pattern, but not so many that it memorises (see Lessons 5 and 6).

Check yourself 1
2 inputs, 4 hidden neurons, 1 output. How many weights? Answer: 2 × 4 + 4 × 1 = 12.

Check yourself 2
What does a hidden neuron contribute? Answer: Its own boundary or curve, which the output layer combines with the others.

## Tab 8: Words list

Hard words in one place
⚡ At a glance
🧠 Idea: A quick reference for the difficult words in this lesson.
🧪 Example: Epoch = one full pass of the training data.
✅ Remember: Come back here whenever a word is unclear.

Word | Plain meaning

Neuron (node) | One tiny calculator that takes numbers in and gives one out

Input, hidden, output layer | Front door / middle rooms / exit of the network

Weight, bias | A multiplier on an input / a number added afterwards

Aggregation | Adding up the weighted inputs plus the bias

Activation function | A curved line that bends the sum into the neuron's output

Forward pass | Sending data from input to output to get a prediction

Loss | A score of how wrong the predictions are (SSR or SSE)

Backpropagation | Working backward to find each weight's share of the error

Chain rule | If A changes B and B changes C, multiply the two changes to get how A changes C

Epoch | One full pass of the whole training data

Linearly separable | Two groups that one straight line can split

Vanishing gradient | The slope is almost 0, so learning stops

MLP | Multi-Layer Perceptron: input, at least one hidden, output layer

---

# lesson08_sequences_and_memory.html  (Lesson 8: Sequences and Memory | AI Notes)


## Tab 1: Start here

Why do some problems need memory?
⚡ At a glance
🧠 Idea: Some answers depend on what came before. A model for these problems needs memory.
🧪 Example: To predict tomorrow's sales you must look at the last few days, not just one number.
✅ Remember: RNN = a network with a loop that remembers. LSTM = an RNN with a better memory.

A normal neural network looks at one input and gives one answer. It forgets everything afterwards. That is a problem when the order of things matters.

Three everyday stories

- Sales: If sales went 300, 310, 320 in the last three days, tomorrow will probably be about 330. One number alone cannot show the trend.
- Sentences: "I grew up in France, so I speak fluent ___." You need the word "France" from the start to guess "French".
- Stock prices: A company may have 10 days of price history, another 30 days. A model must work with any length.

All of these are sequences: a list of items where the order matters. Models that handle sequences need memory.

🌍 Analogy: watching a film. You cannot understand the ending if you only see the last second. You remember what happened before. A sequence model does the same: it keeps a short summary of everything it has seen so far.

The words you will meet (in plain English)
Word | Meaning

Sequence | Items in an order, like days or words

Time series | Numbers recorded over time, like daily sales

Lag | An earlier value used to help predict a later one

RNN | Recurrent Neural Network: a network with a loop that feeds its own result back in

Hidden state | The RNN's running summary of what it has seen

Unrolling | Drawing the loop as a row of copies, one for each time step

Gradient | The slope that tells gradient descent which way, and how far, to move a weight

LSTM | Long Short-Term Memory: an RNN with a long-term memory lane and gates

Gate | A control that lets a percentage of something pass through

What we will learn, in order

- How to turn a list of numbers into a table a model can learn from.
- How an RNN uses a loop to remember.
- Why a simple RNN struggles with long sequences.
- How an LSTM fixes that, one stage at a time.

## Tab 2: Sequence table

Turning a list of numbers into a table
⚡ At a glance
🧠 Idea: Slide a small window along the list. The window values are inputs. The next value is the answer.
🧪 Example: 25, 28, 23, 31, 26 gives (25, 28) → 23, (28, 23) → 31, (23, 31) → 26.
✅ Remember: Train on the past, test on the future. Never shuffle time.

Before using memory networks, here is the simplest way to forecast: make a normal table from the list, using earlier values as inputs.

Step 1: the list
Sales on days 1 to 5: 25, 28, 23, 31, 26. We want day 6.

Step 2: slide a window of 2
Take the first two numbers (25, 28) as inputs. The number right after them, 23, is the answer. Move the window one step. Repeat.

Two days ago (lag 2) | Yesterday (lag 1) | Answer (today)
25 | 28 | 23
28 | 23 | 31
23 | 31 | 26
31 | 26 | ? (day 6)

The first three rows have answers, so they form an ordinary supervised dataset. The last row has no answer yet. It is the question we want the model to answer: the inputs are the latest two values, (31, 26).

A simple guess for day 6 is the average of the last two values: (31 + 26) &divide; 2 = 28.5. A trained model would learn a better rule from the rows.

Step 3: test fairly

- With 100 days of data, train on days 1 to 80 and test on days 81 to 100.
- Never shuffle the days. If day 90 is in the training set while you test on day 50, the model has seen the future. This is called data leakage, and it makes the test score look better than it really is.

🌍 Analogy: you cannot practise with tomorrow's newspaper to predict today's news.

The limit of this table method
The window has a fixed size. If the answer depends on something 50 days back, a window of 2 will never see it. Memory networks solve this.

Check yourself 1
From 10, 12, 11, 15 with a window of 2, write the rows. Answer: (10, 12) → 11 and (12, 11) → 15. To forecast the next value, use (11, 15).

Check yourself 2
Why is shuffling bad for time series? Answer: The model would train on later days and be tested on earlier days, so it has seen the future. That is data leakage.

## Tab 3: RNN: the loop

The recurrent neural network (RNN)
⚡ At a glance
🧠 Idea: An RNN is a small network with a loop. Each step uses the new input and the result of the previous step.
🧪 Example: New value = ReLU(1 × input + 0.5 × previous value). Inputs 0.5, 1, 0.5 give 0.5, 1.25, 1.125.
✅ Remember: The same weights are used at every step, so one network handles a sequence of any length.

🎬 The StatQuest way: stock prices in StatLand
An RNN is like the networks you already know: it has weights, biases, layers and activation functions. The big difference is that it also has a feedback loop. Although it takes only one input value at a time, the loop lets it use a whole sequence, such as stock prices collected over time. To see how, we run yesterday's and today's price through it to predict tomorrow's price.

The problem a normal network cannot solve
A normal network has a fixed number of inputs, for example exactly 3. But one company has 10 days of prices and another has 30. We would need a different network for every length. An RNN avoids this.

How the loop works

- Look at today's input and the result remembered from the previous step.
- Combine them using weights, add a bias, and apply an activation function.
- The result is both the output of this step and the memory for the next step. It goes round the loop.

new memory = f( win × input + wloop × old memory + b )

🌍 Analogy: a running total on a calculator. Each day you add today's number to what is already on the screen. The screen is the memory. You do not need to remember all the earlier days. They are already folded into the screen.

Worked example
Scale each stock price so Low = 0, Medium = 0.5, High = 1. Suppose the prices on three days are 0.5, 1, 0.5. Use win = 1, wloop = 0.5, b = 0, and the activation ReLU (keeps positives, turns negatives into 0). Start with memory 0.

Day | Input | Calculation | New memory

1 | 0.5 | 1 × 0.5 + 0.5 × 0 = 0.5 | 0.5

2 | 1.0 | 1 × 1.0 + 0.5 × 0.5 = 1.25 | 1.25

3 | 0.5 | 1 × 0.5 + 0.5 × 1.25 = 1.125 | 1.125

The final memory, 1.125, is built from all three days. Day 1's value still has an effect: it was carried through the loop.

Unrolling
It is hard to follow a loop. So we unroll it: make a copy of the network for each input and join the copies in a row.

Day 1
input 0.5
➜Day 2
input 1.0
➜Day 3
input 0.5
➜Prediction

Important: all the copies share the same weights and biases. Whether you unroll 3 times or 30 times, the number of weights to train stays the same. That is how one network handles a sequence of any length.

Check yourself 1
Using the same weights, inputs 1 then 0, start 0. What are the two memories? Answer: Day 1: 1 × 1 + 0.5 × 0 = 1. Day 2: 1 × 0 + 0.5 × 1 = 0.5. Even with input 0, the memory is 0.5, because it remembers day 1.

Check yourself 2
If a sequence has 30 days, do we need 30 sets of weights? Answer: No. The unrolled copies all share one set of weights and biases.

## Tab 4: Why RNNs struggle

The big problem: exploding and vanishing gradients
⚡ At a glance
🧠 Idea: The loop multiplies by the same weight at every step. Over many steps the result becomes huge or tiny.
🧪 Example: Weight 2 over 50 steps gives about 1.1 million billion. Weight 0.5 over 50 steps gives almost 0.
✅ Remember: Weight above 1 explodes. Weight below 1 vanishes. Training breaks either way.

🎬 The StatQuest way: the Vanishing / Exploding Gradient Problem
Although the name starts with "vanishing", it is easier to see how a gradient can explode first. Then we look at how it can vanish. The cause is the same: the unrolled network uses the loop's weight again and again.

Step 1: the loop weight is used many times
When we unroll the loop, each copy passes its memory to the next copy through the loop weight w. So a value from the first step is multiplied by w once for each step it travels. After n steps it has been multiplied by w, n times, which is wn.

Step 2: see what happens with different weights
Loop weight w | After 5 steps | After 50 steps | What happens

2 | 32 | 1,125,899,906,842,624 (about 1015) | Explodes

1.5 | 7.6 | 637,621,500 | Explodes

1 | 1 | 1 | Stays the same

0.9 | 0.59 | 0.005 | Fades

0.5 | 0.03 | 0.0000000000000009 (about 10&minus;15) | Vanishes

Step 3: why it breaks training
Training uses gradient descent. The size of each step is learning rate × slope (gradient). The gradient for the loop weight contains the same wn.

- Exploding: with a slope of 1015 and a learning rate of 0.01, the step is about 1013. The weight is thrown far away every time, so it never settles. Training is unstable.
- Vanishing: with a slope of 10&minus;15, the step is about 10&minus;17. The weight barely moves, so the network does not learn from things that happened long ago.

🌍 Analogy: the whisper line. A message is passed along 50 people. If each one repeats it twice as loudly, the last person hears a deafening roar (exploding). If each one repeats it half as loudly, the last person hears nothing (vanishing). Either way the message is lost.

What this means in real life
In "I grew up in France, so I speak fluent ___", the word "France" is many steps back. With a vanishing gradient the network cannot learn the link between "France" and "French". Simple RNNs remember only a few steps back.

The fix is a popular design called Long Short-Term Memory (LSTM), in the next two tabs.

Check yourself 1
Loop weight 0.5, 10 steps. What is the multiplier? Answer: 0.510 = 0.00098, about 0.001, so the signal from 10 steps ago has almost vanished.

Check yourself 2
Why does an exploding gradient make training unstable? Answer: The step size is learning rate × gradient. A gigantic gradient makes a gigantic step, so the weight jumps around and never settles.

## Tab 5: LSTM: two memories

LSTM: a better memory
⚡ At a glance
🧠 Idea: An LSTM keeps two memories: a long-term lane and a short-term memory. Gates decide what to keep.
🧪 Example: A gate of 0.68 means "keep 68% of the old long-term memory".
✅ Remember: Sigmoid makes percentages (0 to 1). Tanh makes potential memories (&minus;1 to 1).

🎬 The StatQuest way: LSTM, one stage at a time
An LSTM fixes the problem of simple RNNs by using two paths: one for long-term memory and one for short-term memory. The long-term memory path does not go through a weight, so it does not blow up or fade the same way. The LSTM then works in three stages: (1) decide the percent of the long-term memory to remember, (2) update the long-term memory, (3) update the short-term memory.

An LSTM is an RNN with a protected "memory lane" (the cell state, which is the long-term memory) and the usual short-term memory (the hidden state). Gates control what goes in and out.

🌍 Analogy: a notebook and your working memory. The notebook (long-term memory) holds important facts for a long time. Your working memory (short-term memory) holds what you are thinking about right now. Each day you decide how much of the notebook to keep, what to write in it, and what to say aloud.

Two tools: sigmoid and tanh
An LSTM uses two squashing functions you know from Lesson 7. Each has a special job.

z | Sigmoid(z) | Tanh(z)
&minus;4 | 0.018 | &minus;0.999
&minus;2 | 0.119 | &minus;0.964
0 | 0.5 | 0
2 | 0.881 | 0.964
4 | 0.982 | 0.999

- Sigmoid turns any number into a value between 0 and 1. We read that as a percentage: 0 = none, 1 = all, 0.68 = 68%. This is the "gate" job: how much to let through.
- Tanh turns any number into a value between &minus;1 and 1. We use it to create a potential memory: something that could be added (positive) or subtracted (negative).

The two memories
Long-term memory (cell state)
The lane that runs along the whole sequence. It has no weights on it. We only multiply it by a percentage and add to it.
Short-term memory (hidden state)
The working output at each step. It is created by weights, and it is also the LSTM's output.

Check yourself 1
Which function gives a percentage, sigmoid or tanh? Answer: Sigmoid, because its output is between 0 and 1.

Check yourself 2
What does a gate of 0.25 on the long-term memory mean? Answer: Keep 25% of the old long-term memory and forget 75%.

## Tab 6: LSTM step by step

The three stages of an LSTM, with real numbers
⚡ At a glance
🧠 Idea: Stage 1: keep a percent of the old memory. Stage 2: add new memory. Stage 3: make the new short-term memory.
🧪 Example: Long-term memory 2.0 becomes 1.36 (keep 68%), then 1.92 (after adding 0.56).
✅ Remember: Forget gate = stage 1, input gate = stage 2, output gate = stage 3.

Setup for our example: previous long-term memory = 2.0, previous short-term memory = 0.5, and the new input = 1.0.

Every gate looks at the new input and the previous short-term memory, multiplies them by weights, adds a bias, and squashes the answer (sigmoid for percentages, tanh for potential memories). (The weights below are chosen to keep the numbers easy. In a real LSTM they are learned.)

Stage 1: what percent of the long-term memory do we keep? (forget gate)

- Weighted sum: z = 0.5 × 0.5 (short-term) + 1 × 1.0 (input) &minus; 0.5 (bias) = 0.25 + 1 &minus; 0.5 = 0.75.
- Sigmoid: &sigma;(0.75) = 0.679, so keep about 68%.
- New long-term memory so far: 2.0 × 0.679 = 1.358.

Stage 2: add new information (input gate)

- Potential memory (tanh): z = 1 × 0.5 + 1 × 1.0 = 1.5, and tanh(1.5) = 0.905.
- Percent to add (sigmoid): z = 1 × 0.5 + 1 × 1.0 &minus; 1 = 0.5, and &sigma;(0.5) = 0.623.
- Amount added: 0.905 × 0.623 = 0.563.
- Updated long-term memory: 1.358 + 0.563 = 1.922.

Stage 3: make the new short-term memory (output gate)

- Potential short-term memory (tanh of the updated long-term memory): tanh(1.922) = 0.958.
- Percent to output (sigmoid): z = 1 × 0.5 + 1 × 1.0 &minus; 0.5 = 1.0, and &sigma;(1.0) = 0.731.
- New short-term memory: 0.958 × 0.731 = 0.700. This is also the output of this step.

 | Before | After
Long-term memory | 2.0 | 1.922
Short-term memory | 0.5 | 0.700

Then the new pair (1.922, 0.700) goes into the next time step, and the three stages repeat.

🌍 Analogy: a daily diary routine. Stage 1: tear out the pages you no longer need (keep 68%). Stage 2: write today's new idea, but only as much as seems important (62%). Stage 3: decide what part of the diary to say aloud right now (73%).

Why this fixes exploding and vanishing

- The long-term lane is changed only by multiplying with a percentage and by adding. It does not pass through the loop weight again and again.
- If the forget gate is close to 1 (keep everything), the old memory travels almost unchanged. Multiplying by about 1 over 50 steps stays about 1, instead of becoming 10&minus;15.
- The same weights and biases are used for every time step, so the number of weights does not grow with the sequence length, just like the RNN.

So an LSTM can handle longer sequences without the gradient problems of a simple RNN. It is not magic: it still needs careful training and can still forget.

Check yourself 1
Long-term memory 3, forget gate 0.5, potential memory 0.8, add percent 0.5. New long-term memory? Answer: 3 × 0.5 = 1.5. Added: 0.8 × 0.5 = 0.4. Total: 1.5 + 0.4 = 1.9.

Check yourself 2
Which stage creates the new short-term memory? Answer: Stage 3 (the output gate): tanh of the long-term memory, times a sigmoid percentage.

---

# lesson09_fuzzy_logic.html  (Lesson 9: Fuzzy Logic | AI Notes)


## Tab 1: Why fuzzy?

Why do we need "fuzzy" logic?
⚡ At a glance
🧠 Idea: Normal logic says true or false. Fuzzy logic allows "partly true", with a degree from 0 to 1.
🧪 Example: 27&deg;C can be 0.6 "warm" and 0.2 "hot" at the same time.
✅ Remember: A fuzzy degree is NOT a probability. It says how much something belongs to a category.

Many everyday ideas are not sharp: warm, tall, fast, cheap. Fuzzy logic is a way to let a computer handle these soft ideas.

Start with a story: the sharp edge
Imagine a fan that turns on when the temperature is at least 30&deg;C. At 29.9&deg;C the fan is off. At 30&deg;C it is on. A tiny change of 0.1&deg;C flips the decision completely. Real life does not feel like that. A temperature slowly becomes warmer, then hotter.

🌍 Analogy: a light switch vs a dimmer. A normal (crisp) rule is a light switch: only ON or OFF. A fuzzy rule is a dimmer: it can be a little on, half on, or mostly on.

Crisp logic and crisp sets

- A proposition is a statement that is true or false, like "the heater is on". The logic operators AND, OR and NOT combine statements. "Cold AND occupied" is true only if both parts are true.
- A crisp set has membership of exactly 0 or 1. "Temperature at least 30&deg;C": 29.9 is outside (0), 30 is inside (1).

Fuzzy sets
A fuzzy set gives every value a degree of membership between 0 and 1, written &mu;(x). The function that gives the degree is the membership function.

- Example: &mu;warm(27) = 0.7 means "27&deg;C belongs to the set 'warm' to degree 0.7".
- Sets can overlap. 27&deg;C can be partly warm and partly hot at the same time.
- You must say which values are being described, for example "temperatures from 0 to 50&deg;C" (the universe of discourse).

Do not confuse: a degree of 0.7 for "warm" does not mean "a 70% chance that it is warm". It means the chosen "warm" curve gives 0.7 at that temperature. The temperature itself is known exactly. Probability is about uncertainty. A fuzzy degree is about how much something fits a soft category.

Linguistic variables and hedges
A linguistic variable is a variable whose values are words. Example: temperature with labels cold, warm, hot. A hedge such as "very" changes a set. A common rule is &mu;very A(x) = &mu;A(x)&sup2;. If &mu;warm = 0.6, then "very warm" = 0.6 × 0.6 = 0.36. (Always state the rule you use.)

Check yourself 1
A crisp set allows which membership values? Answer: Only 0 or 1.

Check yourself 2
&mu;warm(28) = 0.7. Is there a 70% chance that 28&deg;C is warm? Answer: No. It means the chosen "warm" curve gives degree 0.7 at 28&deg;C. It is not a probability.

## Tab 2: Membership functions

Membership functions: the shape of a word
⚡ At a glance
🧠 Idea: A membership function is a curve that says how much each value fits a word like "warm".
🧪 Example: Triangle (20, 25, 30): at 23&deg;C the degree is (23 &minus; 20) &divide; (25 &minus; 20) = 0.6.
✅ Remember: Triangle: up to the peak, then down. Trapezoid has a flat top. Shoulder stays high at one end.

We draw the word "warm" as a shape. The height of the shape at a temperature is how "warm" that temperature is.

1. Triangular function
Pick three ordered points a < b < c. The degree rises in a straight line from 0 at a to 1 at b (the peak), then falls to 0 at c. Outside a to c the degree is 0.

Example: "warm" with (a, b, c) = (20, 25, 30)&deg;C.

Temperature | Calculation | &mu;warm
20 | start of the triangle | 0
23 | (23 &minus; 20) &divide; (25 &minus; 20) = 3 &divide; 5 | 0.6
25 | the peak | 1
27 | (30 &minus; 27) &divide; (30 &minus; 25) = 3 &divide; 5 | 0.6
28 | (30 &minus; 28) &divide; 5 = 2 &divide; 5 | 0.4
30 | end of the triangle | 0

Left side formula: (x &minus; a) &divide; (b &minus; a). Right side formula: (c &minus; x) &divide; (c &minus; b). Always say the units (&deg;C) and the domain.

2. Trapezoidal function
Four ordered points a ≤ b ≤ c ≤ d. The degree rises from a to b, stays at 1 from b to c, then falls from c to d.

Example: (a, b, c, d) = (20, 25, 30, 35). At 22: (22 &minus; 20) &divide; 5 = 0.4. At 28: it is between 25 and 30, so 1. At 33: (35 &minus; 33) &divide; 5 = 0.4.

3. Shoulder functions
A left shoulder or right shoulder keeps a flat high region toward one end. Example: "hot" rises from 0 at 25&deg;C to 1 at 30&deg;C and stays 1 for everything hotter. At 28: (28 &minus; 25) &divide; 5 = 0.6.

4. Gaussian (bell) function
A smooth bell centred at m with spread &sigma; > 0.

&mu;(x) = exp( &minus;(x &minus; m)&sup2; &divide; (2 &sigma;&sup2;) )

Example: m = 25, &sigma; = 3, x = 28. (28 &minus; 25)&sup2; = 9. 2 × 3&sup2; = 18. So &mu; = exp(&minus;9 &divide; 18) = exp(&minus;0.5) = 0.607.

5. Singleton
A singleton has a non-zero degree at one chosen point and 0 everywhere else. It is useful for representing a single output value.

🌍 Analogy: shapes of a tent. A triangle is a pointed tent. A trapezoid is a tent with a flat roof. A shoulder is a ramp that ends in a long flat platform. A Gaussian is a smooth hill.

Check yourself 1
Triangle (20, 25, 30). Degree at 25? Answer: 1, because 25 is the peak.

Check yourself 2
Triangle (10, 20, 30). Degree at 15? Answer: (15 &minus; 10) &divide; (20 &minus; 10) = 0.5.

## Tab 3: Fuzzy AND, OR, NOT

Combining fuzzy statements: AND, OR, NOT
⚡ At a glance
🧠 Idea: AND takes the smaller degree, OR takes the larger, NOT is 1 minus the degree.
🧪 Example: warm = 0.6, humid = 0.8. AND = 0.6, OR = 0.8, NOT warm = 0.4.
✅ Remember: min for AND, max for OR, 1 &minus; x for NOT.

In normal logic, AND, OR and NOT work on true and false. In fuzzy logic they work on numbers between 0 and 1. The most common choice (Zadeh's operators) is:

Operation | Rule | Meaning
AND (intersection) | min(&mu;A, &mu;B) | Both must be true, so we take the smaller degree
OR (union) | max(&mu;A, &mu;B) | Either is enough, so we take the larger degree
NOT (complement) | 1 &minus; &mu;A | The opposite degree

🌍 Analogy: a chain and a rope. AND is like a chain: it is only as strong as its weakest link (the minimum). OR is like two ropes: the stronger one holds (the maximum).

Worked example
At some input, "warm" has degree 0.6 and "humid" has degree 0.8.

- warm AND humid = min(0.6, 0.8) = 0.6
- warm OR humid = max(0.6, 0.8) = 0.8
- NOT warm = 1 &minus; 0.6 = 0.4

Other families of fuzzy operators exist (for example products instead of min), so always say which one you use.

Fuzzy rules
A fuzzy rule has an antecedent (the IF part) and a consequent (the THEN part).

Example rule: IF temperature is hot AND humidity is high THEN fan speed is fast.

The antecedent's degree is its firing strength. If "hot" = 0.7 and "humidity high" = 0.9, then the strength is min(0.7, 0.9) = 0.7. The rule fires at 0.7. If the strength is 0, the rule does not contribute.

Not every rule of normal logic carries over unchanged to fuzzy logic. For example, in normal logic "A OR NOT A" is always true. In fuzzy logic, with A = 0.6: max(0.6, 0.4) = 0.6, which is not 1.

Check yourself 1
A = 0.3 and B = 0.9. A AND B, A OR B and NOT A? Answer: 0.3, 0.9 and 0.7.

Check yourself 2
In "IF hot THEN fast", which part is the antecedent? Answer: "hot", the IF part.

## Tab 4: Expert systems

Expert systems and fuzzy systems
⚡ At a glance
🧠 Idea: An expert system stores an expert's rules. A fuzzy system lets rules apply partially.
🧪 Example: Crisp: IF temp ≥ 30 THEN fan on. Fuzzy: warm contributes a little, hot contributes a lot.
✅ Remember: They are not opposites. A system can be both.

Expert system
An expert system stores knowledge from a field, usually as IF-THEN rules, and uses an inference engine to reach conclusions or advice. The stored rules are the knowledge base.

Crisp rule example: IF temperature ≥ 30&deg;C THEN switch the fan on. It has a hard boundary.

Fuzzy system
A fuzzy system uses fuzzy sets, membership functions and fuzzy inference, so overlapping terms such as "warm" and "hot" can each contribute partially.

 | Crisp expert system | Fuzzy system
Categories | Sharp: in or out | Soft: a degree from 0 to 1
Rule firing | Fires or does not | Fires partly, several rules at once
Strength | Readable rules, traceable decisions | Readable rules, traceable decisions
Limit | Someone must write, check and maintain the rules | Same, plus the curves must be designed and tested

- "Expert system" describes the purpose or structure (a knowledge base plus an inference engine).
- "Fuzzy logic" describes a way to represent and combine soft values.
- A fuzzy rule system whose rules come from human experts can be both.
- Neither learns new facts on its own unless learning is added.

🌍 Analogy: a crisp expert system is a strict teacher with a pass mark of 50: 49 is a fail, 50 is a pass. A fuzzy system is a teacher who says "mostly good, a bit weak on this part".

Check yourself 1
What are the two parts of a traditional expert system? Answer: A knowledge base (the rules) and an inference engine.

Check yourself 2
Can a fuzzy rule system also be an expert system? Answer: Yes, if experts provide the rules.

## Tab 5: Fuzzification and rules

Fuzzification and the rule base
⚡ At a glance
🧠 Idea: Turn a measured number into degrees (fuzzify), then see which rules fire.
🧪 Example: 28&deg;C is 0.4 warm and 0.6 hot, so both the "warm" rule and the "hot" rule fire.
✅ Remember: Measure, fuzzify, infer, defuzzify.

A fuzzy controller follows four steps, like a small factory line.

1. Measure
crisp input
➜2. Fuzzify
degrees
➜3. Infer
rules
➜4. Defuzzify
crisp action

Step 1 and 2: measure and fuzzify
Fuzzification means: take a measured (crisp) value and evaluate every relevant membership function. Our example curves:

- Warm: triangle (20, 25, 30)&deg;C.
- Hot: right shoulder: 0 at 25&deg;C, rising to 1 at 30&deg;C, and 1 above.

The sensor reads 28&deg;C. Then warm = (30 &minus; 28) &divide; 5 = 0.4 and hot = (28 &minus; 25) &divide; 5 = 0.6.

The rule base
A rule base is a list of IF-THEN rules, often written with help from experts. Example for an air conditioner:

- IF temperature is cold THEN cooling is low.
- IF temperature is warm THEN cooling is medium.
- IF temperature is hot THEN cooling is high.

At 28&deg;C, "warm" is 0.4 and "hot" is 0.6, so two rules fire together: medium at strength 0.4 and high at strength 0.6. The rule for "cold" has strength 0, so it does not contribute.

Rules with two inputs
A rule can use two inputs: IF temperature is hot AND temperature is rising fast THEN cooling is high. If "hot" = 0.6 and "rising fast" = 0.7, the strength is min(0.6, 0.7) = 0.6.

Designing a rule base: a checklist

- Define the input ranges and curves.
- Check that the rules cover every case (no gaps).
- Define the output categories.
- Check sensible behaviour at the extremes.
- Test against real cases: experts can write rules, but the numbers still need testing.

Check yourself 1
With triangle (20, 25, 30), what is "warm" at 22? Answer: (22 &minus; 20) &divide; 5 = 0.4.

Check yourself 2
"Hot" = 0.5 and "rising fast" = 0.8, rule uses AND (min). Strength? Answer: 0.5.

## Tab 6: Mamdani inference

Mamdani inference: rule strength, clipping and combining
⚡ At a glance
🧠 Idea: Each rule's strength cuts (clips) its output curve. Then all clipped curves are combined.
🧪 Example: A curve of height 0.9 clipped at strength 0.4 becomes 0.4. Combining 0.4 and 0.5 by max gives 0.5.
✅ Remember: Clip with min, combine with max.

Mamdani inference is the classic way to turn rule strengths into a fuzzy output. It has three small steps.

Step 1: antecedent
Evaluate each rule's IF part. AND uses min, OR uses max. A rule with strength 0 does not contribute.

Step 2: implication (clipping)
The THEN part is a fuzzy output set, such as "medium cooling". We clip its curve at the rule's strength &alpha;:

&mu;rule(y) = min(&alpha;, &mu;consequent(y))

(Another method, product implication, scales the curve instead of cutting it, so results can differ. Always state which one you use.)

🌍 Analogy: a ceiling over a hill. The output curve is a hill. The rule strength is a ceiling. Anything of the hill above the ceiling is chopped off.

Step 3: aggregation
After every rule has produced a clipped curve, combine them into one output curve. The common choice is the pointwise maximum: &mu;combined(y) = max of the clipped curves at each y. (Sum or probabilistic-sum are other options.)

Worked point
"Medium cooling" fires at 0.4. "High cooling" fires at 0.6. At one output value y, the original curves are 0.9 (medium) and 0.5 (high).

- Clipped medium = min(0.4, 0.9) = 0.4.
- Clipped high = min(0.6, 0.5) = 0.5.
- Combined (max) = max(0.4, 0.5) = 0.5 at this y.

Repeat at every output value y to build the whole combined curve.

Check yourself 1
A rule fires at 0.3. Its output curve is 0.8 at some y. What is the clipped value? Answer: min(0.3, 0.8) = 0.3.

Check yourself 2
Clipped values 0.2 and 0.5 combined by max? Answer: 0.5.

## Tab 7: Defuzzification, Sugeno

Defuzzification: from a fuzzy curve to one number
⚡ At a glance
🧠 Idea: The controller needs one crisp number, like a fan speed. The centroid is the balance point of the output curve.
🧪 Example: Memberships 0.2, 0.5, 0.3 at speeds 20, 50, 80 give a centroid of 53.
✅ Remember: Centroid = &Sigma; y·&mu; &divide; &Sigma; &mu;. Sugeno uses constants and a weighted average.

The combined output is a fuzzy curve, but a fan needs a single speed. Defuzzification converts the curve into one number.

The centroid (centre of gravity)
The centroid is the balance point of the curve, like the point where you could balance a cardboard cut-out of the shape on a finger. For samples yi with degrees &mu;(yi):

output = &Sigma; yi &mu;(yi) &divide; &Sigma; &mu;(yi)

Example: degrees 0.2, 0.5, 0.3 at speeds 20, 50, 80.

- Top: 20 × 0.2 + 50 × 0.5 + 80 × 0.3 = 4 + 25 + 24 = 53.
- Bottom: 0.2 + 0.5 + 0.3 = 1.0.
- Output = 53 &divide; 1.0 = 53.

It is a weighted average: the speeds with bigger degrees pull the answer toward them. (The bottom total must be above 0.)

Other methods
The maxima methods pick from the points where the combined curve is highest: the first, middle, last or mean of those points. Different methods can give different answers, especially when the curve has two peaks.

Sugeno inference (a simpler cousin)
In zero-order Sugeno, the THEN part is a constant number (such as "fan speed = 30") instead of a fuzzy curve. The outputs are combined by a weighted average using the firing strengths &alpha;:

output = &Sigma; &alpha;i zi &divide; &Sigma; &alpha;i

Example: rule 1 (medium) outputs z = 50 with strength 0.4. Rule 2 (high) outputs z = 80 with strength 0.6. Output = (0.4 × 50 + 0.6 × 80) &divide; (0.4 + 0.6) = (20 + 48) &divide; 1.0 = 68.

 | Mamdani | Sugeno
THEN part | A fuzzy set (a curve) | A constant, or a function of the inputs
Steps | Clip, aggregate, then defuzzify | Weighted average of the constants
Strength | Easy to explain with words like "medium" | Convenient for optimization and numeric control

When no rule fires: every strength is 0, so the bottom of the formula is 0 and the answer cannot be calculated. A safe design needs a fallback rule or better coverage.

Check yourself 1
Degrees 0.5 and 0.5 at speeds 40 and 60. Centroid? Answer: (40 × 0.5 + 60 × 0.5) &divide; 1.0 = 50.

Check yourself 2
Sugeno: z = 20 with strength 0.5 and z = 60 with strength 0.5. Output? Answer: (10 + 30) &divide; 1.0 = 40.

## Tab 8: A full controller

A full fuzzy controller from sensor to fan
⚡ At a glance
🧠 Idea: Follow one reading all the way: fuzzify, fire the rules, clip, combine, defuzzify.
🧪 Example: A 28&deg;C reading gives a fan speed of about 73 (Mamdani) or 68 (Sugeno).
✅ Remember: The exact output needs the output curves. Always test the edges and "no rule fires" cases.

We design a small air-conditioner fan controller and trace one reading, 28&deg;C, from sensor to fan speed (0 to 100).

The design

- Inputs: Warm = triangle (20, 25, 30)&deg;C. Hot = 0 at 25&deg;C, rising to 1 at 30&deg;C, then 1.
- Outputs (fan speed, 0 to 100): Medium = triangle (30, 50, 70). High = 0 at 50, rising to 1 at 80, then 1.
- Rule 1: IF warm THEN fan is medium. Rule 2: IF hot THEN fan is high.

Step 1: fuzzify 28&deg;C
Warm = (30 &minus; 28) &divide; 5 = 0.4. Hot = (28 &minus; 25) &divide; 5 = 0.6.

Step 2: fire the rules
Rule 1 fires at strength 0.4. Rule 2 fires at strength 0.6. Both fire.

Step 3: clip and combine (Mamdani)
We sample the fan speed every 10 units. Clip "medium" at 0.4 and "high" at 0.6, then take the maximum:

Speed y | Medium at y | High at y | Clipped medium | Clipped high | Combined (max)

0 to 30 | 0 | 0 | 0 | 0 | 0

40 | 0.5 | 0 | 0.4 | 0 | 0.4

50 | 1.0 | 0 | 0.4 | 0 | 0.4

60 | 0.5 | 0.33 | 0.4 | 0.33 | 0.4

70 | 0 | 0.67 | 0 | 0.6 | 0.6

80 | 0 | 1.0 | 0 | 0.6 | 0.6

90 | 0 | 1.0 | 0 | 0.6 | 0.6

100 | 0 | 1.0 | 0 | 0.6 | 0.6

Step 4: defuzzify (centroid)

- Top: 40 × 0.4 + 50 × 0.4 + 60 × 0.4 + 70 × 0.6 + 80 × 0.6 + 90 × 0.6 + 100 × 0.6 = 16 + 20 + 24 + 42 + 48 + 54 + 60 = 264.
- Bottom: 0.4 × 3 + 0.6 × 4 = 1.2 + 2.4 = 3.6.
- Fan speed = 264 &divide; 3.6 = 73.3.

The fan runs at about 73, between medium (50) and high (80), closer to high because "hot" (0.6) is stronger than "warm" (0.4).

The same reading with Sugeno
If medium = 50 and high = 80 as constants: (0.4 × 50 + 0.6 × 80) &divide; (0.4 + 0.6) = 68.

Where fuzzy systems are used, and their limits

- Uses: climate control, decision support, and labelling things with soft categories.
- A fuzzy system is understandable, but it does not learn the right rules or curves from data by itself.
- Validate it: test boundary readings, contradictory rules, units, sensor errors, cases where no rule fires, and whether the final output is safe and useful.
- Remember: fuzzy degree is not the same as measurement uncertainty.

Check yourself 1
At 27&deg;C with the warm triangle (20, 25, 30), what is warm? Answer: (30 &minus; 27) &divide; 5 = 0.6.

Check yourself 2
Why can't Mamdani give a fan speed without the output curves? Answer: The centroid is calculated from the combined output curve, so the curves must be defined.

## Tab 9: Words list

Hard words in one place
⚡ At a glance
🧠 Idea: A quick reference for the words in this lesson.
🧪 Example: Fuzzification = turning a measured number into degrees.
✅ Remember: Come back here whenever a word is unclear.

Word | Plain meaning

Crisp set | Membership is only 0 or 1

Fuzzy set | Membership is a degree from 0 to 1

Membership function &mu;(x) | A curve giving the degree for each value

Universe of discourse | The range of values we are describing

Linguistic variable | A variable whose values are words, like cold, warm, hot

Hedge | A word like "very" that changes a set (for example squaring the degree)

Antecedent, consequent | The IF part / the THEN part of a rule

Firing strength | The degree to which a rule's IF part is true

Fuzzification | Turning a crisp number into membership degrees

Rule base | The list of IF-THEN rules

Inference | Using the rules to reach an output

Aggregation | Combining the outputs of all rules (often by max)

Defuzzification | Turning the fuzzy output into one crisp number

Centroid | The balance point of a curve

Mamdani, Sugeno | Two inference styles: fuzzy-set outputs / constant outputs

---

# lesson10_images_and_cnns.html  (Lesson 10: Images and Convolutional Neural Networks | AI Notes)


## Tab 1: Images as numbers

How a computer sees a picture
⚡ At a glance
🧠 Idea: A picture is a grid of numbers. Each number is a pixel.
🧪 Example: A 128×128 colour photo is 128 × 128 × 3 numbers.
✅ Remember: Colour image = 3 channels (red, green, blue). Grayscale = 1 channel.

A computer does not see a cat. It sees a grid of numbers. A pixel is one number that says how bright (or what colour) one tiny square of the picture is.

Channels

- A grayscale image has one channel: one number per pixel, from dark (0) to bright.
- A colour RGB image has three channels: red, green and blue. Each pixel has three numbers.
- A 128×128 RGB image is stored as a 128 × 128 × 3 array of numbers (width × height × channels; the order can differ between software libraries). That is 49,152 numbers.

🌍 Analogy: a mosaic. A picture is a wall of tiny coloured tiles. Each tile is a pixel. Your computer only knows the colour code of each tile, not the picture they make together.

A tiny example: the letter X on a 6×6 grid
1 means a dark pixel and 0 means a blank pixel.

1 | 0 | 0 | 0 | 0 | 1
0 | 1 | 0 | 0 | 1 | 0
0 | 0 | 1 | 1 | 0 | 0
0 | 0 | 1 | 1 | 0 | 0
0 | 1 | 0 | 0 | 1 | 0
1 | 0 | 0 | 0 | 0 | 1

You can see the X in the 1s. We will use this image in the next tabs.

Three jobs a computer can do with images
Task | The answer is... | Example
Classification | One label for the whole image | "This is a cat"
Object detection | Labels and boxes (locations) for several objects | "A dog here, a car there"
Image generation | New pixels | Colouring a black-and-white photo

Preparing images

- Resize all images to the same size (resizing can lose detail).
- Normalize the numbers in the same way for training and testing images.
- Keep each image's labels, boxes and train/test split matched up.

Check yourself 1
How many numbers are in a 10×10 RGB image? Answer: 10 × 10 × 3 = 300.

Check yourself 2
Which task gives a box and a label for each object? Answer: Object detection.

## Tab 2: Why not a normal network?

Why a normal (dense) network is a poor fit for images
⚡ At a glance
🧠 Idea: A dense network needs millions of weights for a photo and ignores which pixels are neighbours.
🧪 Example: 49,152 inputs × 100 hidden units = 4,915,200 weights.
✅ Remember: A CNN reuses a small filter everywhere, so it needs far fewer weights.

🎬 StatQuest: "Neural Networks Part 8: Image Classification with Convolutional Neural Networks (CNNs)"
The video starts with image classification using a normal neural network and shows the trouble: every pixel needs its own input node, so big images need a huge number of weights. A normal network also does not use the fact that neighbouring pixels are related, and it is upset by small shifts of the picture. Then it gives the main ideas of a CNN: (1) reduce the number of input nodes using a filter, (2) take advantage of the correlation between neighbouring pixels, and (3) tolerate small shifts in the image. The video walks through creating a feature map with a filter, pooling, using the pooled values as input for a neural network, and classifying an image of the letter "X" (and a shifted X).

Problem 1: far too many weights
Flatten a 128×128 RGB image into one long list: 49,152 numbers. Connect each to just 100 hidden neurons:

49,152 × 100 = 4,915,200 weights

(plus 100 biases). That is almost five million numbers to train, for only one layer.

Problem 2: the layout is lost
When we flatten the picture into one long list, the network no longer knows which pixels were neighbours. But nearby pixels form meaningful patterns such as edges and corners.

🌍 Analogy: a jigsaw puzzle in a heap. If you pour all pieces into a bag and list them one by one, you lose how they fit together. A CNN looks at small patches of the picture, so it keeps the neighbourhoods.

The CNN idea

- Filter (kernel): a small grid of numbers (for example 3×3) that slides across the image.
- Shared weights: the same filter numbers are used at every position, so the number of weights does not grow with the image size.
- Feature map: the grid of results made by the filter. It shows where the filter's pattern was found.
- Receptive field: each value in a feature map depends only on a small local patch.

Count: one 3×3 filter on an RGB image has 3 × 3 × 3 = 27 weights plus 1 bias, however big the image is. Compare with 4,915,200 for the dense layer.

Stacking several convolution layers lets later layers combine small patterns (edges) into bigger ones (shapes, then objects).

Shifts
Because the same filter scans every position, a shifted pattern produces a shifted response in the feature map. This is called translation equivariance. With pooling, a CNN becomes more tolerant to small shifts. But it is not automatic for every shift or rotation, so training and design still matter.

Check yourself 1
How many weights does a 3×3 filter on a 1-channel (grayscale) image have? Answer: 3 × 3 = 9 (plus 1 bias).

Check yourself 2
Why does a filter need so few weights? Answer: The same small set of weights is reused at every position of the image.

## Tab 3: Filters and feature maps

The convolution: sliding a filter
⚡ At a glance
🧠 Idea: Place a filter on a patch, multiply matching numbers, add them up. That is one feature-map value.
🧪 Example: Patch [1,0;2,1] with filter [1,0;0,1] gives 1×1 + 0×0 + 2×0 + 1×1 = 2.
✅ Remember: Output size = floor((N + 2P &minus; K) &divide; S) + 1 for each side.

A convolution slides a small filter over an image. At each position it multiplies the filter with the patch underneath, entry by entry, and adds the results. The result goes into a feature map.

🌍 Analogy: a stencil and a torch. Hold a small stencil over part of a picture and ask "how well does this part match my stencil?". Slide the stencil across the whole picture. The scores form a new picture: the feature map.

Worked example: one patch
Image (3×3):

1 | 0 | 2
2 | 1 | 0
0 | 1 | 1

Filter (2×2): rows [1, 0] and [0, 1]. Stride 1, no padding, bias 0.

- Upper-left patch is [1, 0; 2, 1]. Multiply with the filter: 1×1 + 0×0 + 2×0 + 1×1 = 2.
- Slide one step right: patch [0, 2; 1, 0]. 0×1 + 2×0 + 1×0 + 0×1 = 0.
- Slide down to the left: patch [2, 1; 0, 1]. 2×1 + 1×0 + 0×0 + 1×1 = 3.
- Slide right: patch [1, 0; 1, 1]. 1×1 + 0×0 + 1×0 + 1×1 = 2.

The feature map is [2, 0; 3, 2]. (In deep learning the "convolution" usually does not flip the filter. Strictly that is called cross-correlation. Because the filter numbers are learned, the name does not matter for training.)

Stride and padding

- Stride (S): how many pixels the filter moves each step. Stride 1 moves one pixel. Stride 2 moves two.
- Padding (P): extra border pixels (usually 0) added around the image so the edge pixels get used and the output stays larger.

output size = floor( (N + 2P &minus; K) &divide; S ) + 1

N = input size, K = filter size, P = padding, S = stride, for each side. (floor means round down.)

- 3×3 input, 2×2 filter, S = 1, P = 0: floor((3 + 0 &minus; 2) &divide; 1) + 1 = 2. So the output is 2×2.
- 5×5 input, 3×3 filter, S = 2, P = 1: floor((5 + 2 &minus; 3) &divide; 2) + 1 = floor(2) + 1 = 3. So the output is 3×3.

Channels and counting weights

- Each filter spans all the input channels and makes one output channel (one feature map).
- Eight filters make eight feature maps.
- Weights = kernel height × kernel width × input channels × output channels, plus one bias per output channel. Example: eight 3×3 filters on an RGB image = 3 × 3 × 3 × 8 = 216 weights + 8 biases = 224 numbers.

Check yourself 1
Output size for a 7×7 input, 3×3 filter, stride 1, padding 0? Answer: floor((7 &minus; 3) &divide; 1) + 1 = 5, so 5×5.

Check yourself 2
Patch [2, 1; 0, 3] and filter [1, 0; 0, 1]. Result? Answer: 2×1 + 1×0 + 0×0 + 3×1 = 5.

## Tab 4: A tiny CNN, start to end

A tiny CNN: recognising the letter X
⚡ At a glance
🧠 Idea: Filter, ReLU, pool, then feed the numbers to a small network.
🧪 Example: The X image gives pooled values 3, 0, 0, 3 for the "\" filter and 0, 3, 3, 0 for the "/" filter.
✅ Remember: Image → feature maps → ReLU → pooling → flatten → classifier.

We take the 6×6 X from the first tab and run it through two filters, ReLU and max pooling. This is the same journey the StatQuest video follows for the letter "X".

Image
6×6
➜Filter
feature map 4×4
➜ReLU
➜Max pool
2×2
➜Flatten
4 numbers
➜Classifier

Filter 1: a "\" diagonal detector
Filter (3×3): [1, &minus;1, &minus;1], [&minus;1, 1, &minus;1], [&minus;1, &minus;1, 1]. It scores high when the patch has 1s on the "\" diagonal and 0s elsewhere. Slide it over the 6×6 image (stride 1, no padding), giving a 4×4 feature map (floor((6 &minus; 3) &divide; 1) + 1 = 4):

3 | &minus;1 | &minus;3 | &minus;1
&minus;1 | 1 | &minus;3 | &minus;3
&minus;3 | &minus;3 | 1 | &minus;1
&minus;1 | &minus;3 | &minus;1 | 3

Check the top-left value: the patch is [1, 0, 0; 0, 1, 0; 0, 0, 1]. The diagonal gives 1+1+1 = 3. The six other cells are 0, so they add 0. Total = 3. The big values (3) sit at the two ends of the "\" stroke of the X.

ReLU
Replace every negative number by 0:

3 | 0 | 0 | 0
0 | 1 | 0 | 0
0 | 0 | 1 | 0
0 | 0 | 0 | 3

Max pooling (2×2 windows, no overlap)
Keep the largest value in each 2×2 window:

- Top-left window [3, 0; 0, 1] gives 3. Top-right [0, 0; 0, 0] gives 0.
- Bottom-left [0, 0; 0, 0] gives 0. Bottom-right [1, 0; 0, 3] gives 3.

Pooled map: [3, 0; 0, 3].

Filter 2: a "/" diagonal detector
With the mirror filter [&minus;1, &minus;1, 1], [&minus;1, 1, &minus;1], [1, &minus;1, &minus;1], the same steps give a pooled map of [0, 3; 3, 0].

Flatten and classify
Join the pooled values into one list: [3, 0, 0, 3, 0, 3, 3, 0]. These 8 numbers go to a small normal neural network as inputs. The network learned that an X has high values for both diagonals. We reduced 36 pixels to 8 numbers, and we kept the useful information.

🌍 Analogy: a detective with two magnifying glasses. One glass looks for "\" strokes and one for "/" strokes. The detective reports only the strongest sign of each in each part of the picture. Both strokes present in the right places means "X".

Why pooling helps with small shifts
Say a strong response of 3 moves by one cell, but stays inside the same 2×2 window: [3, 0; 0, 0] becomes [0, 3; 0, 0]. Max pooling gives 3 in both cases. So the pooled result does not change for small shifts inside a window. A bigger shift can move the response into another window, so tolerance is partial.

Check yourself 1
Max pooling of [1, 4; 2, 3]? Answer: 4.

Check yourself 2
A 6×6 image goes through a 3×3 filter, stride 1, no padding, then 2×2 pooling. What is the final size? Answer: 4×4 after the filter, then 2×2 after pooling.

## Tab 5: ReLU, pooling, the head

ReLU, pooling and the classifier head
⚡ At a glance
🧠 Idea: After each convolution: ReLU, optional pooling. At the end a classifier turns the features into labels.
🧪 Example: Pooling [1,3;2,0] gives 3. Softmax turns scores into probabilities that add up to 1.
✅ Remember: The filters are learned by backpropagation, not hand-written.

ReLU after a convolution
ReLU(z) = max(0, z): negatives become 0 and positives stay. It adds the bend (non-linearity) that lets a network learn complicated patterns. A feature map after ReLU shows where a filter responded strongly.

Max pooling
Take the largest value in each local window. Example 4×4 feature map and 2×2 windows:

1 | 3 | 0 | 2
2 | 0 | 1 | 1
4 | 1 | 2 | 3
0 | 2 | 5 | 1

Top-left [1, 3; 2, 0] gives 3. Top-right [0, 2; 1, 1] gives 2. Bottom-left [4, 1; 0, 2] gives 4. Bottom-right [2, 3; 5, 1] gives 5. The pooled map is [3, 2; 4, 5].

- Pooling reduces the size (4×4 became 2×2) and makes the result less sensitive to small shifts.
- But it throws away some detail.
- A pooling window has no weights to learn.

The classifier head
A simple CNN repeats convolution, then ReLU, then (optional) pooling several times. Then it uses flattening (or global pooling) and one or more dense layers to produce a score for each class.

For classes that exclude each other (cat, dog or bird), softmax turns the scores into probabilities that add up to 1. Example: scores 2, 1, 0 give e2 = 7.39, e1 = 2.72, e0 = 1. The total is 11.11. The probabilities are 7.39 &divide; 11.11 = 0.665, 2.72 &divide; 11.11 = 0.245 and 1 &divide; 11.11 = 0.090.

How a CNN learns

- Predict a label for a training image (forward pass).
- Compare with the true label and calculate the loss.
- Use backpropagation to find the slopes (Lesson 7).
- Update all the weights together: the filter numbers and the classifier weights.

The filters are learned from examples. Nobody types in a "cat detector". The early filters often find edges. Later layers combine them into shapes.

Check yourself 1
ReLU(&minus;2) and ReLU(5)? Answer: 0 and 5.

Check yourself 2
What do softmax outputs add up to? Answer: 1.

## Tab 6: Colourizing photos (U-Net)

Colourizing a grayscale photo with a U-Net
⚡ At a glance
🧠 Idea: Give the network the lightness of a photo. It predicts the colour channels.
🧪 Example: Input L is 1×128×128. Output a and b is 2×128×128.
✅ Remember: The colours are plausible guesses, not guaranteed true colours.

A project example: take old black-and-white photos and predict plausible colours using a CNN with an encoder and a decoder (a U-Net).

The Lab colour space
Instead of red, green and blue, Lab splits a colour into three channels:

- L: lightness (this is the grayscale picture).
- a and b: two channels that carry the colour information.

Colourizing becomes: input L, predict a and b. Then put L, a and b back together and convert to RGB.

The steps

- Resize the RGB training images to 128×128. Convert RGB to Lab.
- Input = L, shape 1×128×128. Target = a and b, shape 2×128×128 (channels first, as in PyTorch).
- Train: predict a and b, calculate the mean squared error against the true a and b, update the weights. Track training and validation scores over 15 to 20 epochs. Keep an evaluation set aside if you can.
- Use it: take the L channel of a grayscale photo, predict a and b, combine with L, convert Lab back to RGB, and show the grayscale input and the final colour output.

The Lab scaling and normalization used in training must be the same when rebuilding the colour image.

The U-Net shape

- Encoder: convolutions that squeeze the image into smaller, more abstract feature maps.
- Decoder: layers that make the maps bigger again until they return to the original size.
- Skip connections: shortcuts that pass detailed (high-resolution) encoder features straight to the matching decoder stage. They help bring back edges and fine detail.

🌍 Analogy: summarising and redrawing. The encoder squeezes a picture into a short summary. The decoder redraws it from the summary. The skip connections are sticky notes with fine details that are handed straight to the decoder so it does not forget them.

An honest limit
One grayscale photo can match several plausible colour versions (a jacket could be red or blue). The network learns plausible colours, not the true historical colours. Mean squared error also tends to average uncertain colours, so results can look muted.

Check yourself 1
In Lab colourization, which channel is the input? Answer: L (lightness).

Check yourself 2
What do skip connections do in a U-Net? Answer: They pass high-resolution encoder features to the decoder to recover fine detail.

## Tab 7: Words list

Hard words in one place
⚡ At a glance
🧠 Idea: A quick reference for the words in this lesson.
🧪 Example: Stride = how many pixels the filter moves each step.
✅ Remember: Come back here whenever a word is unclear.

Word | Plain meaning

Pixel | One number for one tiny square of the picture

Channel | One layer of numbers in an image (grayscale 1, RGB 3)

CNN | Convolutional Neural Network: a network that uses filters on images

Filter (kernel) | A small grid of numbers that slides over the image

Convolution | Multiplying a filter by a patch and adding the results

Feature map | The grid of filter results

Stride | How many pixels the filter moves each step

Padding | Extra border pixels added around the image

Receptive field | The local patch a feature-map value depends on

Pooling | Shrinking a feature map, for example by keeping the maximum of each window

Flatten | Turning a grid into one long list

Softmax | Turns scores into probabilities that add up to 1

Lab | A colour system: L is lightness, a and b carry colour

Encoder, decoder | Squeezing an image down / rebuilding it to full size

Skip connection | A shortcut that passes detail from the encoder to the decoder

---

# lesson11_explainable_ai_and_ethics.html  (Lesson 11: Explainable AI and Ethics | AI Notes)


## Tab 1: The black-box problem

The black-box problem
⚡ At a glance
🧠 Idea: Many powerful AI models give very good answers but cannot say why.
🧪 Example: A bank's AI rejects your loan and nobody can tell you the reason.
✅ Remember: Explainable AI (XAI) = methods that let humans understand why a model decided something.

A black box is a machine where you can see what goes in and what comes out, but not what happens inside. Many modern ML models work like this.

Start with a story
Imagine you apply for a student loan. Within seconds the bank's AI says "Rejected". You ask why. The bank says: "The computer decided." Nobody can tell you which fact about you caused the rejection: your income, your address, your age, or something else. You cannot fix the problem, you cannot check whether the decision was fair, and the bank cannot check either.

🌍 Analogy: two doctors. Doctor A says "Take this medicine, trust me." Doctor B says "Your blood test shows low iron, and that causes your tiredness, so take this medicine." Both may be right, but you can only check and trust Doctor B. A black-box AI is Doctor A.

Why does this happen?
Modern machine learning often puts predictive performance first and transparency second. Complex models (like deep neural networks) reach outstanding accuracy, but their decision logic is spread across millions of numbers (weights and biases). No human can read millions of numbers and see a reason.

Why it matters most when the stakes are high
Area | What can go wrong if the model cannot be explained
Medical diagnosis | A wrong or unexplained result can risk a patient's life.
Credit scoring | People can lose money or opportunities, with no way to challenge.
Autonomous driving | After an accident, who is legally responsible, and why did the car do it?

Interpretability (also called explainability) means how well a human can understand why a model made its decisions.

Check yourself 1
Why is a deep neural network called a "black box"? Answer: Its decision logic is hidden inside millions of parameters, so we can see inputs and outputs but not the reasoning.

Check yourself 2
Name two areas where unexplainable AI is risky. Answer: For example medical diagnosis, credit scoring and autonomous driving.

## Tab 2: Goals of XAI

Why we want explanations: three goals
⚡ At a glance
🧠 Idea: XAI helps us trust a model, debug it, and check that it is fair.
🧪 Example: A photo model that says "wolf" because of snow in the picture, not because of the animal.
✅ Remember: Trust, Debugging, Fairness and auditing.

01 TRUST
Check that predictions rely on real, sensible reasons and not on accidental patterns (spurious correlations).
02 DEBUGGING
Find where, how and why the model makes mistakes, especially on unusual cases.
03 FAIRNESS & AUDITING
Make sure decisions do not discriminate on protected attributes such as gender, race or religion.

Goal 1: Trust, and the spurious correlation trap
A spurious correlation is a pattern that exists in the data by accident but has nothing to do with the real cause.

🌍 Analogy. Ice-cream sales and sunburn both rise in summer. If a model learns "ice cream sales cause sunburn" it has found a spurious correlation. The real cause is the hot sunny weather.

A famous AI example: researchers trained a model to tell huskies from wolves. In the training photos, the wolves were almost always standing on snow. The model got high accuracy, but an explanation method showed it was mostly looking at the snow, not the animal. The model was right for the wrong reason, and it would fail on a husky in the snow. Without an explanation nobody would have noticed.

Goal 2: Debugging
If a medical model fails on older patients, an explanation can show which feature is misleading it. You can then fix the data or the model, like a mechanic who opens the bonnet instead of guessing.

Goal 3: Fairness and auditing
Auditing means checking from the outside, like an inspector. If an explanation shows that a hiring model gives a big weight to gender, or to a feature that stands in for gender (such as a name), the model is unfair and must be fixed. A well-known reported case: an experimental company recruiting tool learned from past hiring data and began to mark down CVs that contained signs of being female. The company stopped using it.

Check yourself 1
What is a spurious correlation? Answer: A pattern that appears in the data by accident and is not the real cause.

Check yourself 2
Which XAI goal asks "does the model discriminate?" Answer: Fairness and auditing.

## Tab 3: Accuracy vs clarity

The accuracy versus interpretability trade-off
⚡ At a glance
🧠 Idea: The simplest models are the easiest to understand. The most powerful ones are the hardest.
🧪 Example: A decision tree is easy to read. A transformer has billions of weights.
✅ Remember: Glass-box = clear. Ensemble = in between. Deep learning = most powerful, least clear.

Often you have to choose: a model you can understand, or a model that is a bit more accurate.

Model type | Examples | Interpretability | Predictive power

Glass-box (intrinsic) | Linear regression, decision trees, logistic regression | Very high | Moderate

Ensemble models | Random forest, XGBoost, LightGBM | Moderate | High

Deep learning | Convolutional networks, transformers | Low | Very high

What do these words mean?

- Glass-box model: you can see right through it. The model itself is the explanation. This is called intrinsic interpretability.
- Ensemble model: a team of many small models whose answers are combined. A random forest is many decision trees that vote. XGBoost and LightGBM build trees one after another, each fixing the mistakes of the earlier ones. One tree is easy to read, but a hundred trees voting are not.
- Deep learning: neural networks with many layers (Lessons 7 and 10). Powerful, but unreadable.

🌍 Analogy: recipes. A simple recipe card (glass-box) tells you every step. A famous restaurant's dish made by ten chefs with secret steps (ensemble) is harder to follow. A dish made by a robot using millions of micro-adjustments (deep learning) tastes amazing but nobody can write down the recipe.

The solution: explain the hard ones afterwards
If we need a powerful black-box model, we can use post-hoc explanation methods ("post-hoc" means "after the fact"). Three important ones in this lesson are permutation feature importance, LIME and SHAP.

Check yourself 1
Which model type is the most interpretable? Answer: Glass-box models such as linear regression and decision trees.

Check yourself 2
What is a random forest? Answer: Many decision trees whose votes are combined. It is an ensemble model.

## Tab 4: Glass-box models

Glass-box models: explanation built in
⚡ At a glance
🧠 Idea: In linear models the coefficients are the explanation. In trees the IF-THEN rules are the explanation.
🧪 Example: Price = 10 + 5 × bedrooms + 0.2 × area. One more bedroom adds 5.
✅ Remember: Simple models explain themselves.

1. Linear and logistic regression
Each feature has a coefficient (a weight, from Lesson 6). The coefficient tells you the expected change in the answer for each one-unit increase in that feature, while the others stay the same.

Example: house price in lakhs = 10 + 5 × bedrooms + 0.2 × area (m&sup2;).

- A house with 3 bedrooms and 100 m&sup2;: 10 + 5×3 + 0.2×100 = 10 + 15 + 20 = 45.
- Add one bedroom (4 bedrooms, same area): 10 + 20 + 20 = 50. So one more bedroom adds 5.
- Add 10 m&sup2;: it adds 0.2 × 10 = 2.

We can read the whole explanation straight from the formula. For logistic regression a positive coefficient pushes the probability of the class up, and a negative coefficient pushes it down.

2. Decision trees
A decision tree is a set of IF-THEN rules that match how people think. Loan example:

IF income ≥ 50,000:
   IF debt < 20,000  -> APPROVE
   ELSE               -> REJECT
ELSE (income < 50,000) -> REJECT

A person with income 60,000 and debt 25,000 is rejected. The explanation is the exact path: "income is at least 50,000, but debt is not below 20,000."

Limits: a very large tree with hundreds of rules is no longer easy to read. And glass-box models may be less accurate on complex problems such as images.

Check yourself 1
Price = 10 + 5 × bedrooms + 0.2 × area. What price for 2 bedrooms and 50 m&sup2;? Answer: 10 + 10 + 10 = 30.

Check yourself 2
Using the loan tree, is income 70,000 with debt 10,000 approved? Answer: Yes. Income is at least 50,000 and debt is below 20,000.

## Tab 5: Global vs local

Two scopes of explanation: global and local
⚡ At a glance
🧠 Idea: Global explains the whole model. Local explains one single decision.
🧪 Example: Global: "Income matters most overall." Local: "Why was THIS person rejected?"
✅ Remember: Global = the big picture. Local = one case.

🌍 Global interpretability
Understanding the overall logic of the model across the entire dataset.
Key question: "Which features drive predictions overall?"

🔬 Local interpretability
Explaining why the model made a specific decision for one individual data point.
Key question: "Why was this specific loan application rejected?"

🌍 Analogy: a school. Global: "In this school, study time and attendance are what mostly decide results." Local: "Why did Nimal fail?" Maybe for Nimal the biggest reason was missed attendance.

Why both are needed

- Global helps engineers and auditors check the model's general behaviour, such as whether gender plays a big role overall.
- Local helps the affected person, and the person making the decision. It is the kind of explanation a rejected applicant needs ("what could I change?").

The three methods in the next tabs: Permutation importance is mainly global. LIME is local. SHAP can be used for both.

Check yourself 1
"Which features matter most overall?" Global or local? Answer: Global.

Check yourself 2
"Why was Kamal's application rejected?" Global or local? Answer: Local.

## Tab 6: Permutation importance

Permutation feature importance
⚡ At a glance
🧠 Idea: Shuffle one feature's values. If the model gets much worse, that feature was important.
🧪 Example: Shuffling "hours studied" drops accuracy from 90% to 62%. Shuffling "shoe size" changes nothing.
✅ Remember: Importance = the drop in performance after shuffling.

Permutation importance measures how much a model's performance decreases when one feature's values are randomly shuffled.

🌍 Analogy: removing a team member. If a football team plays much worse when one player is removed, that player was important. If the team plays the same, that player did little.

The steps

- Measure the model's score on test data (for example accuracy = 90%).
- Take one feature column and shuffle its values randomly among the rows. This breaks the link between that feature and the answer.
- Measure the score again.
- Importance = original score &minus; new score.
- Repeat for every feature and rank them.

Worked example
A model predicts pass or fail from three features. Baseline accuracy = 90%.

Feature shuffled | Accuracy after shuffling | Drop (importance) | Meaning
Hours studied | 62% | 90 &minus; 62 = 28 | High impact: the model relied heavily on it
Attendance | 80% | 90 &minus; 80 = 10 | Some impact
Shoe size | 90% | 90 &minus; 90 = 0 | Low impact: the model ignored it

- High impact: shuffling breaks the accuracy, so the model relied heavily on that feature.
- Low impact: performance stays unchanged, so the feature was largely ignored.

Good to know

- It works with any model, because it only needs inputs and predictions.
- It is a global method. It does not explain one individual decision.
- If two features carry the same information (such as height in cm and height in inches), shuffling one may show little drop because the other covers for it. So correlated features can hide their importance.
- It tells you that a feature matters, not how (higher or lower values).

Check yourself 1
Baseline accuracy 85%. After shuffling feature X it is 85%. How important is X? Answer: Not important: the drop is 0.

Check yourself 2
Baseline 90%. Shuffling A gives 70% and shuffling B gives 85%. Which is more important? Answer: A (a drop of 20, against 5 for B).

## Tab 7: LIME

LIME: explaining one prediction with a simple local model
⚡ At a glance
🧠 Idea: Zoom in on one prediction. Near that point the complex model looks nearly flat, so a straight line explains it.
🧪 Example: For f(x) = x&sup2; near x = 3, the local slope is about 6.
✅ Remember: LIME = Local Interpretable Model-agnostic Explanations.

LIME builds a simple, interpretable model (such as linear regression) that copies the complex model's behaviour only in the neighbourhood of one prediction.

What the name means

- Local: it explains one prediction, near one point.
- Interpretable: the explaining model is simple enough to read.
- Model-agnostic: it works with any model, since it only needs to ask the model for predictions.

🌍 Geometric analogy: a winding map. A hilly landscape has curves everywhere. But if you zoom in very close to one spot, the ground looks flat. LIME draws a straight line across that small flat patch. The line is only valid there.

The steps

- Pick the prediction you want to explain.
- Create many slightly changed copies of the input (nearby points).
- Ask the complex model what it predicts for each copy.
- Give more weight to the copies that are closer to the original.
- Fit a simple model (like a straight line) to those predictions.
- Read the simple model's coefficients. That is the explanation.

A tiny worked example
Pretend the "complex model" is f(x) = x&sup2;, a curve. We want to explain the prediction at x = 3 (f = 9). Take two nearby points:

Nearby x | Model output x&sup2;
2.9 | 8.41
3.0 | 9.00
3.1 | 9.61

The straight line through the nearby points has slope (9.61 &minus; 8.41) &divide; (3.1 &minus; 2.9) = 1.20 &divide; 0.2 = 6. So the local explanation is: "Near x = 3, each +1 in x raises the output by about 6." But look at x = 0: the real curve is flat there (slope 0). So the explanation is correct only locally.

A real-style example
For one rejected loan, LIME might report the local effects:

Feature of this applicant | Effect on "approve" in this neighbourhood
Debt is high | &minus;0.30 (pushes toward rejection)
Income is medium | +0.10 (pushes toward approval)
Age = 24 | +0.02 (almost nothing)

(Illustrative numbers.) The applicant sees that high debt caused the rejection.

Limits

- It explains only one point, not the whole model.
- Because the nearby copies are random, the explanation can change a little from run to run.
- The simple line is an approximation, not the model itself.

Check yourself 1
Why does LIME use a straight line? Answer: Near one point a complicated curved surface looks almost flat, so a line is a good local copy.

Check yourself 2
Does a LIME explanation describe the whole model? Answer: No. It is valid only near the one prediction it explains.

## Tab 8: SHAP

SHAP: sharing the credit fairly
⚡ At a glance
🧠 Idea: SHAP shares a prediction fairly among the features, like sharing a team prize among players.
🧪 Example: Baseline 50, prediction 90. Income gets +25, Debt gets +15, and 25 + 15 = 40 = 90 &minus; 50.
✅ Remember: Additivity: contributions add up to prediction minus baseline.

SHAP uses Shapley values from cooperative game theory to measure how much each feature contributed to a prediction.

🌍 Game analogy. A team wins a cash prize. The prediction is the prize. The players are the features. How much did each player deserve? Some players only help when others are present. SHAP calculates each player's fair share by checking every possible group (coalition) of players, with and without that player.

The baseline
The baseline is the average prediction of the model when we know nothing about this person (here: 50). SHAP explains how the features move the prediction away from the baseline to the actual prediction (here: 90).

A worked example with two features
A loan model gives a score. We know these predictions when only some features are revealed:

Known features | Model's score
None (baseline) | 50
Income only | 70
Debt only | 60
Income and Debt | 90

To find Income's fair share, look at every order in which the features could be added, and see how much Income adds each time:

- Income first, then Debt: Income adds 70 &minus; 50 = 20.
- Debt first, then Income: Income adds 90 &minus; 60 = 30.
- Average = (20 + 30) &divide; 2 = 25. This is Income's SHAP value.

Debt's share in the same way:

- Debt first: 60 &minus; 50 = 10. Debt after Income: 90 &minus; 70 = 20. Average = (10 + 20) &divide; 2 = 15.

Check: 25 + 15 = 40, and the prediction minus the baseline is 90 &minus; 50 = 40. The shares add up exactly.

Three features
With a third feature, Age, the same method checks all 6 orders. In one made-up model the results are: Income +25, Debt +15, Age +2. Their sum is 42, which equals 92 &minus; 50 (the prediction 92 minus the baseline 50).

Two key properties (the "axioms")
1. Consistency
If a model changes so that a feature's contribution increases or stays the same, its SHAP value will not decrease.
2. Additivity
The sum of the feature contributions equals the difference between the actual prediction and the average baseline prediction.

Consistency example. Change the model so that Income alone now scores 80 and Income with Debt scores 100. Income's contributions are now 30 and 40, so its SHAP value is 35. It went up from 25 and did not decrease. Debt's contributions (10 and 20) did not change, so it stays 15.

Cost
With n features there are 2n possible coalitions: 8 for 3 features, 1,024 for 10, and 1,048,576 for 20. So for big models SHAP uses clever shortcuts and approximations.

Using SHAP

- Local: the SHAP values for one person ("Income +25, Debt +15") explain that person's decision.
- Global: average the sizes of the SHAP values over many people to see which features matter most overall.
- Contributions can be negative, which means the feature pushed the score down.

Check yourself 1
Baseline 40, prediction 75, two features. A has SHAP +20. What is B's SHAP value? Answer: The total is 75 &minus; 40 = 35, so B = 35 &minus; 20 = 15.

Check yourself 2
How many coalitions for 4 features? Answer: 24 = 16.

## Tab 9: Choosing a method

Comparing the methods and their limits
⚡ At a glance
🧠 Idea: Each method answers a different question. Pick the one that matches yours.
🧪 Example: Overall ranking: permutation. One rejected loan: LIME or SHAP.
✅ Remember: Explanations help judgement. They do not replace it.

Method | Scope | Main idea | Strength | Weakness

Glass-box model | Both | The model itself is readable | Exact and simple | Less powerful on complex data

Permutation importance | Global | Shuffle a feature and see the score drop | Simple, works with any model | Weak with correlated features

LIME | Local | A simple model near one point | Easy to read, any model | Approximate, can vary run to run

SHAP | Local and global | Fair sharing by Shapley values | Additive and consistent | Costly for many features

Warnings every learner should know

- An explanation is not the same as a cause. "Income mattered to the model" does not mean income causes loan repayment.
- Explanations can be wrong or misleading, because they are approximations.
- Explaining a bad model does not make it good. It only shows what the model does, including bad habits.
- Show the explanation to the right audience. A doctor, a regulator and a patient need different levels of detail.

🌍 Analogy: X-ray vs treatment. An X-ray shows what is inside, but it does not cure anything. XAI shows what the model is doing, but people must still decide what to do about it.

Check yourself 1
Which method do you use to explain why one applicant was rejected? Answer: A local method: LIME or SHAP.

Check yourself 2
Does a SHAP explanation prove that a feature causes the outcome? Answer: No. It shows what the model used, not what causes things in the real world.

## Tab 10: Ethical foundations

Ethical foundations of using (Gen)AI
⚡ At a glance
🧠 Idea: Nine principles for using AI responsibly in study and research.
🧪 Example: You use AI to check your grammar, you say so, and you take responsibility for every word.
✅ Remember: Integrity, Originality, Transparency, Accountability, Compliance, Security, Intellectual property, Fairness and bias, Human oversight.

Generative AI (like chatbots) is powerful. Ethics means choosing to use it in a way that is honest, fair, safe and responsible. The nine foundations below are written for proposals, theses, publications and presentations.

Principle | What it means | Student example

1. Integrity | Uphold academic honesty. Never use AI to misrepresent authorship or fabricate information. | Do not hand in an AI-written report as your own. Do not include references the AI invented (AI can make up convincing but fake sources).

2. Originality | AI must support, not replace, human intellect. Core scholarly output must reflect your own knowledge and critical analysis. | Use AI to improve grammar or explain a concept. The ideas, analysis and conclusions must be yours.

3. Transparency | Clearly acknowledge and document all AI tool use. | Add a note: "I used [tool] to [purpose]. I reviewed and edited the output."

4. Accountability | You remain fully responsible for outputs and conclusions. AI does not reduce your responsibility. | If the AI gives a wrong number and you copy it, the mistake is yours.

5. Compliance | Follow legal, regulatory and institutional rules, including data protection laws and ethics approvals. | If your research uses surveys about people, get ethics approval and follow data-protection rules first.

6. Security | Protect data confidentiality and intellectual property. Be careful with third-party platforms. | Do not paste private data, unpublished results or personal details into a public AI tool.

7. Intellectual property | Respect other people's IP rights, and make sure the tool's licence terms fit your institution's policy. | Do not copy copyrighted text from AI output without checking. Read what the tool's terms say about your inputs.

8. Fairness and bias | Critically evaluate outputs to spot algorithmic bias and prevent unfair or discriminatory outcomes. | If AI ranks job applicants or describes people with stereotypes, question it. It learned from biased data.

9. Human oversight | Keep meaningful human judgement in all activities. Final decisions are made by qualified people. | A teacher, not a chatbot, decides the final grade.

How explainable AI connects to ethics

- Transparency and accountability: you can only be accountable if you can explain how a result came about.
- Fairness: explanations (like SHAP) can reveal if a model leans on a protected attribute.
- Human oversight: a human can only supervise a decision they can understand.

🌍 Analogy: a calculator in an exam. A calculator helps you, but you still must know what you are calculating, tell the examiner if you used one, and own your answer.

Check yourself 1
An AI gives you a reference that looks real. Which principle says to check it? Answer: Integrity (and accountability): never include fabricated information, and you are responsible for what you submit.

Check yourself 2
Why should you not paste private research data into a public chatbot? Answer: Security: it may leak confidential data or intellectual property.

## Tab 11: The EU AI Act

The EU AI Act explained in plain English
⚡ At a glance
🧠 Idea: The EU AI Act is a law that sorts AI systems by how risky they are and sets rules for each level.
🧪 Example: A spam filter is minimal risk. A tool that scores job applicants is high risk. Social scoring is banned.
✅ Remember: Four risk levels plus a special part for general-purpose AI. Fines up to &euro;35 million or 7%.

The Artificial Intelligence Act is Regulation (EU) 2024/1689. It is the European Union's law for AI, and the first big law of its kind. It entered into force on 1 August 2024 and its rules start in stages.

🌍 Analogy: traffic and safety rules. A bicycle needs few rules. A car needs a licence and tests. A plane needs very strict checks. The AI Act works the same way: the riskier the AI, the stricter the rules.

The four risk levels
Level | What it means | Examples

Unacceptable risk | Banned outright | Social scoring; manipulative AI that exploits people's weaknesses; untargeted scraping of face images; emotion recognition in workplaces and schools (with narrow exceptions); real-time remote biometric identification in public places for police (with narrow exceptions)

High risk | Allowed, but with strict duties | AI used in hiring, education and exams, credit scoring, essential services, law enforcement, migration and border control, justice, critical infrastructure and some safety parts of products

Limited risk | Transparency duties | Chatbots (must say you are talking to AI); AI-generated or manipulated images, audio and video such as deepfakes (must be labelled)

Minimal risk | No specific duties | Spam filters, AI in video games

What high-risk systems must do

- Risk management across the whole life of the system.
- Data governance: training data must be relevant and examined for bias.
- Technical documentation that shows how the system works.
- Record-keeping: automatic logs of events.
- Transparency: clear instructions and information for the people who use it.
- Human oversight: people must be able to monitor and step in.
- Accuracy, robustness and cybersecurity.

Notice how much this overlaps with explainable AI: documentation, logs, transparency and human oversight all depend on being able to understand what a system does.

General-purpose AI (GPAI) models
These are very flexible models, such as large language models. Their providers must keep technical documentation, give information to those who build on the model, put a copyright policy in place and publish a summary of the training content. Models with systemic risk (the Act presumes this for training above 1025 operations) have extra duties: evaluations, adversarial testing, reporting serious incidents and strong cybersecurity. A voluntary Code of Practice was published in July 2025 to help providers show compliance.

Who enforces it, and the fines
A European AI Office and national authorities supervise it. The maximum fines are:

Breach | Fine up to
Prohibited practices | &euro;35 million or 7% of worldwide yearly turnover (the higher one)
Most other duties (such as high-risk and transparency rules) | &euro;15 million or 3%
Giving false information to authorities | &euro;7.5 million or 1%

The timeline (it has been changing)

- 1 Aug 2024: the Act enters into force.
- 2 Feb 2025: bans and the AI literacy duty apply.
- 2 Aug 2025: rules for general-purpose AI models and governance apply.
- 2 Aug 2026: general application, including transparency duties for things like chatbots and AI-generated content.
- The strictest rules for high-risk systems were first planned for 2026, but recent summaries say an EU amendment (the "Digital Omnibus") has postponed them to 2 Dec 2027 (the listed use areas) and 2 Aug 2028 (AI in regulated products). It also adds new bans, such as AI that creates non-consensual intimate images. Check the official text for exact dates before you quote them in your report.

Check yourself 1
Which risk level are social scoring systems in? Answer: Unacceptable risk. They are banned.

Check yourself 2
Does the AI Act ban all chatbots? Answer: No. Chatbots are limited risk: they must tell users that they are AI, not be banned.

## Tab 12: Assignment guide

How to approach your 5-page report
⚡ At a glance
🧠 Idea: Plan the report around three questions: what are the concerns, how are they addressed, what else is needed.
🧪 Example: Concern: biased hiring AI. Addressed by: data governance and human oversight rules. Gap: who checks small companies?
✅ Remember: Write it in your own words and acknowledge any AI help.

The task: read the EU AI Act (Regulation (EU) 2024/1689) and prepare a 5-page report on three things: (1) key concerns raised, (2) how the concerns are addressed, (3) what additional guardrails or regulations will be required and why.

This tab helps you understand and plan. The report itself must be your own work, written in your own words, with any AI help acknowledged. That is the integrity and transparency principle from the ethics tab.

A suggested page plan
Part | About | Pages
Introduction | What the Act is and why it exists | 0.5
1. Key concerns | The risks the law responds to | 1.5
2. How they are addressed | The rules and mechanisms | 1.5
3. Additional guardrails | Your reasoned view of gaps and needs | 1.25
Conclusion and references | Summary and sources | 0.25

Part 1: the concerns, and where to look
Think about harms that AI can cause. The Act addresses concerns such as:

- Bias and discrimination (hiring, credit, education).
- Opacity ("black boxes") and lack of accountability.
- Safety and reliability (health, transport, infrastructure).
- Manipulation and mass surveillance (subliminal techniques, social scoring, face scraping).
- Loss of human control.
- Misinformation and deepfakes.
- Copyright and the use of training data.
- Systemic risks of very powerful general-purpose models.

Part 2: concern to response, a map you can check against the text
Concern | How the Act responds

Bias and discrimination | Data and data-governance requirements for high-risk systems (Article 10); bans on some practices

Black-box decisions | Technical documentation (Article 11), logging (Article 12), information for deployers (Article 13)

Loss of human control | Human oversight (Article 14)

Safety and reliability | Risk management (Article 9); accuracy, robustness and cybersecurity (Article 15)

Manipulation and surveillance | Prohibited practices (Article 5)

Deepfakes and AI interaction | Transparency duties (Article 50)

Training data, copyright and powerful models | General-purpose AI rules (Articles 53 to 55)

Enforcement | AI Office, national authorities and fines (Article 99)

Open the real regulation and find each article yourself. Read the exact words, then explain them in your own words. Article numbers are good evidence in a report.

Part 3: questions to help you form your own view
Use these to find gaps. Then argue why each extra guardrail is needed, with reasons.

- Who checks that rules are really followed, and does that body have enough staff and technical skill?
- The Act asks for transparency and documentation. Is there a clear standard for what a "good enough" explanation is?
- If a high-risk system harms someone, how easily can the person get an explanation and a remedy?
- How can the rules keep up with fast-changing technology and new kinds of models?
- What about harms to jobs, the environment (energy use) and the information space?
- What happens with AI made outside the EU, or in countries with no AI law? What would your own country need?
- Do small companies and universities have the means to comply?

Quality checklist

- Each concern is tied to a specific part of the Act.
- Each claim has an article number or a reliable source.
- Dates are checked against the official text (they have been changing).
- Part 3 gives reasons, not only a wish list.
- An acknowledgement of any AI tool use is included.

Check yourself 1
Which article covers human oversight? Answer: Article 14.

Check yourself 2
Why should you open the real Act and not only a summary? Answer: To read the exact wording, give correct article numbers and check dates that may have changed.

## Tab 13: Words list

Hard words in one place
⚡ At a glance
🧠 Idea: A quick reference for the words in this lesson.
🧪 Example: Post-hoc = explaining after the model is already built.
✅ Remember: Come back here whenever a word is unclear.

Word | Plain meaning

Black box | A model whose inside logic cannot be understood

XAI | Explainable AI: methods to understand why a model decided something

Interpretability | How well a human can understand a model's decisions

Glass-box (intrinsic) | A model that explains itself, like a decision tree

Ensemble | Many small models combined (random forest, XGBoost)

Post-hoc | Explaining after the model is built

Global / local | Explaining the whole model / explaining one prediction

Spurious correlation | An accidental pattern that is not the real cause

Permutation importance | The drop in score when a feature is shuffled

LIME | A simple local model that explains one prediction

SHAP / Shapley value | A fair share of a prediction for each feature, from game theory

Baseline | The model's average prediction with no information

Coalition | A group of features (or players) considered together

Additivity, consistency | SHAP shares add up to prediction minus baseline / a feature that matters more never gets less credit

Accountability | Being responsible for the results

Algorithmic bias | Unfair results caused by biased data or design

Regulation | A legal rule that must be followed

High-risk AI | AI in sensitive areas that must meet strict duties under the EU AI Act

GPAI | General-purpose AI model, such as a large language model

---

# lesson12_reinforcement_learning_basics.html  (Lesson 12: Reinforcement Learning Basics | AI Notes)


## Tab 1: The big idea

The big idea: learning by trial and reward
⚡ At a glance
🧠 Idea: An agent learns what to do by trying actions and getting rewards or penalties.
🧪 Example: A dog sits and gets a treat. A game character falls in lava and loses points.
✅ Remember: No answer sheet. Only feedback after the action.

Reinforcement learning (RL) is a type of machine learning where an agent learns by interacting with an environment and receiving feedback as rewards (+) or penalties (&minus;).

🌍 Analogy: training a puppy. You do not give the puppy a book of rules. You ask it to sit. If it sits, you give a treat (reward). If it jumps on the sofa, you say "no" (penalty). After many tries, the puppy learns which actions lead to treats.

How RL is different from the other types
Type | What the machine gets | Picture

Supervised | Examples with the correct answers | A teacher with an answer sheet

Unsupervised | Data with no answers | Sorting buttons into groups

Reinforcement | Only a reward or penalty after it acts | Learning to ride a bike by trying and falling

In RL nobody tells the agent the right action. It must discover good actions by trying them, and a good action may only pay off later (like a chess move that wins the game 30 moves later).

Real examples

- Robots: Boston Dynamics builds robots (some walk on four legs like dogs). Robots can use RL ideas to learn suitable movements through interaction and feedback.
- Games: programs learn to play by playing millions of games and getting a reward for winning.
- Driving and control: learning to steer, brake and plan a route.
- Chatbots: reward signals from human feedback are used to make answers more helpful and human-like.

Check yourself 1
In RL, what does the agent get instead of the correct answers? Answer: A reward or penalty after it acts.

Check yourself 2
Why is RL harder than supervised learning? Answer: Nobody tells the agent the right action, and rewards may come much later.

## Tab 2: The RL loop

The RL loop and its vocabulary
⚡ At a glance
🧠 Idea: The agent sees a state, picks an action, and the environment gives a new state and a reward. Repeat.
🧪 Example: &pi;(s1, lift leg) = 0.7: in state s1 the policy lifts the leg with probability 0.7.
✅ Remember: State, action, reward, policy.

Agent
chooses an action
➜ action ➜Environment
reacts
➜ new state + reward ➜Agent
learns, acts again

The words, with a robot example
Word | Symbol | Meaning | Robot example

Agent |  | The learner that acts | The robot

Environment |  | Everything the agent interacts with | The floor, steps, obstacles

State | s | The current situation | Standing in front of a step

Action | a | What the agent does | Lift the leg, turn, or wait

Reward | r | The feedback number after an action | +1 for climbing, &minus;1 for falling

Policy | &pi; | The rule for choosing actions | "In front of a step, usually lift the leg"

Episode |  | One full try from start to end | One walk across the room

The policy formula: &pi;(s, a) = p
Read it as: "In state s, the policy &pi; picks action a with probability p." Example: in state s1 (in front of a step), &pi;(s1, lift leg) = 0.7, &pi;(s1, turn) = 0.2, &pi;(s1, wait) = 0.1. The probabilities add up to 1 (0.7 + 0.2 + 0.1 = 1.0), because the robot must pick something.

Learning means changing these probabilities so that actions that earn rewards become more likely.

A tiny world to keep in mind
A corridor with three squares: A (start), B, and C (the goal, which gives a reward of +10). From A the robot can only go right (to B). From B it can go left (to A) or right (to C). The best policy is "always go right". We will use this tiny world in the next tabs.

Check yourself 1
What is a policy? Answer: The rule the agent uses to choose actions in each state.

Check yourself 2
Can a policy for one state have probabilities 0.5, 0.4 and 0.3? Answer: No. They must add up to 1, and these add up to 1.2.

## Tab 3: Reward and return

Reward, return and the discount factor
⚡ At a glance
🧠 Idea: The agent wants the biggest total reward over time, and rewards that come sooner count a bit more.
🧪 Example: Rewards 0, 0, 10 with &gamma; = 0.9 give a return of 0.81 × 10 = 8.1.
✅ Remember: Return G = r1 + &gamma; r2 + &gamma;&sup2; r3 + ...

A single reward is not the goal. The goal is the total reward over a whole episode, called the return.

Why total reward?
A chess move that wins a piece now may lose the game later. A move that gives no reward now may set up a win. The agent must look at the big picture.

The discount factor &gamma; (gamma)
A reward now is usually worth more than the same reward later (it is uncertain, and time passes). We multiply later rewards by a number &gamma; between 0 and 1.

G = r1 + &gamma; r2 + &gamma;&sup2; r3 + ...

Example: the corridor gives rewards 0, 0, then +10 on reaching C (three steps).

- With &gamma; = 0.9: G = 0 + 0.9 × 0 + 0.81 × 10 = 8.1.
- With &gamma; = 0.5: G = 0 + 0.5 × 0 + 0.25 × 10 = 2.5.
- With &gamma; close to 1, the agent is patient. With &gamma; close to 0, it only cares about rewards right now.

🌍 Analogy: money in the bank. 100 rupees today is worth more to you than 100 rupees in a year. The discount factor says how much less.

Value: the expected return
The value of a state is the return the agent can expect from that state if it follows its policy. In the corridor, B is one step from the goal, so under "always go right" its value is 10. A is two steps away, so its value is 0.9 × 10 = 9. States nearer the reward have higher value.

Check yourself 1
Rewards 0, 5 with &gamma; = 0.8. What is the return? Answer: 0 + 0.8 × 5 = 4.

Check yourself 2
If &gamma; is close to 0, what does the agent care about? Answer: Mostly the reward right now.

## Tab 4: Explore or exploit

Exploration versus exploitation
⚡ At a glance
🧠 Idea: The agent must balance trying new things (explore) and using what it already knows (exploit).
🧪 Example: &epsilon;-greedy with &epsilon; = 0.3 and 3 actions picks the best one with probability 0.8.
✅ Remember: Too much exploiting misses better options. Too much exploring wastes time.

Should the agent exploit (repeat the action that has worked best so far) or explore (try something different that might be even better)?

🌍 Analogy: choosing where to eat. You have a favourite restaurant (exploit). But a new restaurant down the street might be even better (explore). If you only ever go to your favourite, you will never find out.

The &epsilon;-greedy rule
With a small probability &epsilon; (epsilon) the agent explores by choosing a random action. Otherwise (probability 1 &minus; &epsilon;) it picks the action it currently thinks is best.

Example: 3 actions and &epsilon; = 0.3.

- The random exploration is shared among all 3 actions: 0.3 &divide; 3 = 0.1 each.
- The best-known action: (1 &minus; 0.3) + 0.1 = 0.7 + 0.1 = 0.8.
- Each other action: 0.1.
- Check: 0.8 + 0.1 + 0.1 = 1.0.

A common plan is to start with a large &epsilon; (lots of exploring) and make it smaller as the agent learns.

Check yourself 1
&epsilon; = 0.1 with 2 actions. Probability of the best action? Answer: 0.9 + 0.05 = 0.95.

Check yourself 2
What goes wrong if the agent never explores? Answer: It may stay stuck with a mediocre action and never discover a better one.

## Tab 5: Q-learning

Q-learning: learning the value of each action
⚡ At a glance
🧠 Idea: Keep a score Q(state, action) for every choice and improve it after every step.
🧪 Example: Q(B, right) goes 0, 5, 7.5, 8.75 toward the true value 10.
✅ Remember: New Q = old Q + &alpha; × (reward + &gamma; × best next Q &minus; old Q).

Q-learning learns a table of Q-values. Q(s, a) is how good it is to take action a in state s (the expected return). The agent then picks the action with the highest Q.

The update rule
Q(s, a) ← Q(s, a) + &alpha; [ r + &gamma; × max Q(s', a') &minus; Q(s, a) ]

- &alpha; (alpha) is the learning rate: how big a step to take.
- r is the reward just received.
- &gamma; is the discount factor.
- max Q(s', a') is the best Q-value in the next state s'.
- The part in brackets is the error: "what I just saw" minus "what I expected". We move Q a fraction &alpha; of the way toward what we saw.

Worked example in the corridor (A, B, goal C)
&alpha; = 0.5 and &gamma; = 0.9. All Q-values start at 0. The agent walks A → B → C each episode. Reaching C gives +10 and ends the episode.

Episode 1.

- A → B (reward 0): Q(A, right) = 0 + 0.5 × [0 + 0.9 × 0 &minus; 0] = 0.
- B → C (reward 10): Q(B, right) = 0 + 0.5 × [10 + 0 &minus; 0] = 5.

Episode 2.

- A → B: Q(A, right) = 0 + 0.5 × [0 + 0.9 × 5 &minus; 0] = 0.5 × 4.5 = 2.25.
- B → C: Q(B, right) = 5 + 0.5 × [10 &minus; 5] = 5 + 2.5 = 7.5.

After episode | Q(B, right) | Q(A, right)
1 | 5 | 0
2 | 7.5 | 2.25
3 | 8.75 | 4.5
4 | 9.375 | 6.19
5 | 9.69 | 7.31
True values | 10 | 9

The reward information spreads backward: first B learns it is good (it is next to the goal), then A learns that moving toward B is good. The numbers keep climbing toward the true values 10 and 9. Because Q(B, right) is bigger than Q(B, left), the agent will choose "right".

🌍 Analogy: a rumour spreading backward. The treasure is found at C. B hears "C is great" first. Then A hears from B. Each step passes the good news one square further back.

Check yourself 1
Q(B, right) = 5, &alpha; = 0.5, reward 10 and the episode ends. New Q(B, right)? Answer: 5 + 0.5 × (10 &minus; 5) = 7.5.

Check yourself 2
Why does A's Q-value rise only after B's? Answer: A's update uses the best Q-value of the next state (B), which is 0 until B learns about the goal.

## Tab 6: Policy gradients

Policy gradients: learning with a neural network (the StatQuest way)
⚡ At a glance
🧠 Idea: A neural network picks actions. We make a guess, get a reward, and use the reward to push the network's parameter up or down.
🧪 Example: Derivative 0.5 × reward 1.0 = 0.5. With learning rate 1.0 the step size is 0.5.
✅ Remember: Multiply the derivative by the reward. A negative reward reverses the direction.

🎬 StatQuest: "Reinforcement Learning with Neural Networks: Essential Concepts"
The video reviews backpropagation, then shows why standard backpropagation falls short in reinforcement learning: we do not know the correct answer to compute the error. The fix, called policy gradients: take a guess to calculate the derivative, then use a reward to update that derivative, and finally update the parameter with the updated derivative. It explains this with a story about choosing which fries restaurant to go to, depending on how hungry you are.

The problem with ordinary backpropagation
Backpropagation (Lesson 7) needs the correct answer to work out the error and the slopes. In RL we usually do not know the correct action. We only find out later whether the action was good or bad, through a reward. So we need a way to learn from rewards.

The fries story
A small neural network decides where to go for fries: Norm's or Squatch's. Its input is your hunger level (0 = not hungry, 1 = very hungry). Its outputs are two probabilities, P(go to Norm's) and P(go to Squatch's), which add up to 1. Squatch's gives a small portion and Norm's a big one. If you are not hungry, the small portion is the right choice.

Step by step (hunger = 0.0)

- Use the network to decide. At hunger 0.0 the network outputs P(Norm's) = 0.5 and P(Squatch's) = 0.5. A random number picks the restaurant. The random number is 0.2, which falls in the first half (0 to 0.5), so we go to Squatch's.
- Make a guess: assume going to Squatch's was the right choice. The ideal probabilities would then be P(Squatch's) = 1.0 and P(Norm's) = 0.0.
- Calculate the derivative from the difference between the ideal (1.0) and the actual (0.5) probability for Squatch's. For the bias being trained, this gives a derivative of 0.5.
- Find the reward from the environment. We order fries at Squatch's and get a small portion. Because we are not hungry, a small portion is good. So the guess was correct and the reward = +1.0. (If we had received a large portion, the guess would have been wrong and the reward would be &minus;1.0.)
- Update the derivative with the reward: 0.5 × 1.0 = 0.5.
- Update the parameter with gradient descent. With a learning rate of 1.0, step size = 1.0 × 0.5 = 0.5.

What the reward does

- A positive reward keeps the derivative's direction. The update makes the guessed action more likely.
- A negative reward flips the sign. The update pushes the other way and makes the guessed action less likely.
- The size of the reward changes the size of the step. The video also looks at alternative rewards, such as other numbers instead of +1 and &minus;1.

Step | Value in the example
Network output at hunger 0 | P(Norm's) = 0.5, P(Squatch's) = 0.5
Random number and choice | 0.2, so Squatch's
Derivative | 0.5
Reward | +1.0 (small portion when not hungry)
Updated derivative | 0.5 × 1.0 = 0.5
Step size (learning rate 1.0) | 0.5

🌍 Analogy: a coach's whistle. You try a move. The coach cannot tell you the perfect move, but gives a thumbs up (+1) or thumbs down (&minus;1). A thumbs up makes you repeat it more. A thumbs down makes you do it less.

The summary of the policy gradient process

- Use the neural network to make a decision.
- Get the actual reward from the environment.
- Multiply the derivative by the reward.
- Apply gradient descent with the updated derivative.

Check yourself 1
Derivative 0.5, reward &minus;1.0, learning rate 1.0. What is the updated derivative and step size? Answer: 0.5 × (&minus;1.0) = &minus;0.5, and the step size is 1.0 × (&minus;0.5) = &minus;0.5, so the update goes the opposite way.

Check yourself 2
Why do policy gradients need a guess? Answer: We do not know the correct answer in advance, so we guess one, and the reward tells us whether to trust the guess.

## Tab 7: Uses and problems

Where RL is used, and what can go wrong
⚡ At a glance
🧠 Idea: RL works well for games, robots and control. The reward must be designed carefully.
🧪 Example: A cleaning robot rewarded for "no dirt visible" learns to hide the dirt.
✅ Remember: The agent does exactly what the reward asks, not what you meant.

Uses

- Games: winning board and video games by self-play.
- Robotics: learning to walk, grasp and balance (for example, legged robots).
- Self-driving and control: steering, braking and energy management.
- Recommendation and operations: choosing what to show or how to schedule, learning from user responses.
- Language models: human-feedback rewards help to make chatbot answers more helpful and human-like.

Problems to know

- Reward hacking: the agent finds a cheat that earns reward without doing what you wanted. Example: a robot rewarded for "no dirt visible" hides dirt under a rug. So the reward must match the real goal.
- Lots of trial and error: RL can need millions of tries. That is easy in a game and risky or costly for a real robot or car.
- Safe exploration: random actions in the real world can cause harm, so exploration must be limited.
- Delayed reward: it is hard to tell which of many earlier actions deserves the credit (the credit assignment problem).
- Explainability: a learned policy may be hard to explain (see the explainable AI lesson).

🌍 Analogy: a genie. The agent is like a genie that gives exactly what you wished for, not what you meant. Wish carefully.

Putting it together
Idea | What it does
Reward and return | Define what is good, now and over time
Discount &gamma; | Weights near rewards more than far ones
Explore and exploit | Balance trying new things and using what works
Q-learning | Learns a score for every state-action pair
Policy gradients | A neural network learns the policy directly, using rewards to scale its updates

Check yourself 1
What is reward hacking? Answer: The agent earns reward by a cheat instead of doing the intended task.

Check yourself 2
Why is real-world RL risky? Answer: It needs lots of trial and error, and random exploring can cause harm or cost.

## Tab 8: Words list

Hard words in one place
⚡ At a glance
🧠 Idea: A quick reference for the words in this lesson.
🧪 Example: Episode = one full try from start to end.
✅ Remember: Come back here whenever a word is unclear.

Word | Plain meaning

Agent | The learner that takes actions

Environment | Everything the agent interacts with

State (s), action (a) | The situation / what the agent does

Reward (r) | The feedback number after an action

Policy (&pi;) | The rule for choosing actions, often probabilities

Episode | One full try from start to end

Return (G) | The total (discounted) reward over time

Discount factor (&gamma;) | How much later rewards are worth compared with now

Value | The expected return from a state

Q-value | The expected return of taking a particular action in a particular state

Exploration / exploitation | Trying new actions / using the best known action

&epsilon;-greedy | Explore with probability &epsilon;, otherwise exploit

Learning rate (&alpha;) | How big each update step is

Policy gradient | Updating a policy network by multiplying its derivative by the reward

Reward hacking | Earning reward by a cheat instead of the intended task