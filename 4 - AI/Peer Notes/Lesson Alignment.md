# AI course: lesson alignment (plan vs materials vs peer notes)

Purpose: single reference mapping every lesson of INTE 22303 to the lecture plan, the lecturer's own materials and each set of peer notes, so any agent can find all sources for a lesson. Lesson numbers below are the **study-guide numbers** (`4 - AI/Study Guides/`), which follow the order of the lecture plan (`Lecture Materials/00 - Lesson Plan.png`). The lecturer's own file numbers (01, 05, 07, 09, 10, 11) are session numbers and do NOT match the plan weeks, so they are listed separately.

## Lecture plan (from the image)

| Week | Date | Topic |
|---|---|---|
| 1 | 22-Jun | Introduction |
| 2 | 29-Jun | Holiday |
| 3 | 6-Jul | Prompt Engineering |
| 4 | 13-Jul | Intelligent Agents |
| 5 | 20-Jul | State Space Search |
| 6 | 27-Jul | Heuristic Search |
| 7 | 3-Aug | Discriminative AI and Machine Learning |
| 8 | 10-Aug | Artificial Neural Networks |
| 9 | 17-Aug | Deep Neural Networks |
| 10 | 24-Aug | Generative AI and Transformers |
| 11 | 31-Aug | Generating Images and Diffusion Models |
| 12 | 7-Sep | Reinforcement Learning |
| 13 | 14-Sep | Genetic Algorithms |
| 14 | 21-Sep | Swarm Intelligence |
| 15 | 28-Sep | Fuzzy Logic Systems |

Assessment (Geethma AI 1, p.1): Paper 70 %, Assignments 30 %.

## Mapping

| Guide # | Topic (plan week) | Lecturer materials | Peer Made Notes 1 (HTML, 12 lessons) | Yasiru (typed, 7) | Geethma (handwritten, 7) |
|---|---|---|---|---|---|
| 1 | Introduction (wk 1) | `01 - Reading Material - AI Kitchen Guide.pdf` (partly) | L1 | 1 | AI 1 |
| 2 | Prompt Engineering (wk 3) | Kitchen Guide (prompt/context/harness/loop) | L2 | 2 | AI 2 |
| 3 | Intelligent Agents (wk 4) | `07 - Introduction to Google ADK.pdf`; `Assignments & Labs/02 N8N`, `07 ADK Lab`, `08 ADK Assignment`; `Web Resources & Videos/02 - Building AI Agents.md` | L1 tab "AI agents" | n/a | AI 1 (sense/act, embodied) |
| 4 | State Space Search + Heuristic Search (wk 5-6) | `Videos/04 ... Uniform Cost / A Star` (+ `.md` in Web Resources) | L3 | 3 | AI 3 |
| 5 | Discriminative AI and Machine Learning (wk 7) | none | L5, L6 | 5, 6 | AI 4 (pp. 8-12), AI 5, AI 6 |
| 6 | Artificial Neural Networks (wk 8) | none | L7 | 7 | AI 6 (p.3-4), AI 7 |
| 7 | Deep Neural Networks (wk 9) | `09 - Convolutional Neural Networks (CNN).pdf/.pptx`; `Assignments & Labs/09 CNN` | L10 (CNN tabs), L8 (RNN/LSTM) | n/a | n/a |
| 8 | Generative AI and Transformers (wk 10) | none | L8 (sequences, RNN, LSTM) | n/a | AI 1 p.5 (generative vs discriminative) |
| 9 | Generating Images and Diffusion (wk 11) | none | L10 tab 6 (U-Net colourising) | n/a | n/a |
| 10 | Reinforcement Learning (wk 12) | none | L12 | n/a | AI 4 p.11-12, AI 5 p.1-2 |
| 11 | Genetic Algorithms (wk 13) | `05 - Genetic Algorithms.pdf/.pptx` | L4 | 4 | AI 4 (pp. 1-7) |
| 12 | Swarm Intelligence (wk 14) | none found | none (2 passing mentions) | none | listed in outline only |
| 13 | Fuzzy Logic Systems (wk 15) | `10 - Fuzzy Logic Systems.pdf/.pptx` | L9 | n/a | n/a |
| 14 | Explainable AI and Ethics (taught as session 11; not on the plan image) | `11 - Explainability and Ethics - XAI Core Theory.pdf/.pptx`; `Assignments & Labs/11 - Explainability Assignment/EU Case Analysis Assignment.md` | L11 | n/a | n/a |

Notes
- The peer notes' own lesson numbers (L1-L12) differ from the guide numbers above; use this table to translate.
- **Swarm Intelligence has no source material** in the folder (no slides, no peer notes). Guide 12 is a placeholder until material is added.
- Other assignments/labs (Dengue week self-learning, DPL Kottawa industry visit, CNN notebook) are listed in the subject file browser; they are not exam theory.

## Source files and conversions (for agents)

| Source | Converted file |
|---|---|
| `Peer Notes/Notes- Yasiru/*.pdf` (typed) | `Peer Notes/Notes - Yasiru (converted).md` |
| `Peer Notes/Notes - Geethma/AI 1-7.pdf` (handwritten) | `Peer Notes/Notes - Geethma (transcribed).md` |
| `Peer Notes/Peer Made Notes 1/lesson*.html` (JS tabs) | `Peer Notes/Peer Made Notes 1 (converted).md` |
| `Peer Notes/Notes- Yasiru/WhatsApp Image ... .jpeg` | an unrelated screenshot of a mobile app ("Discover Events"); not course notes; ignored |

Known issues found while aligning: Geethma's GA example gives roulette shares (1 %, 17 %, 33 %, 49 %) that do not match the fitness values (exact: 0.6 %, 7.7 %, 40.4 %, 51.2 %); the study guide uses the exact numbers.
