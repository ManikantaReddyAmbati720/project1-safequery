\# SafeQuery – AI SQL Database Query Agent



\## Domain

Database Agent



\## Project Description

SafeQuery is an AI-powered SQL Database Query Agent that converts natural language queries into safe and validated SQL statements.



The system follows a structured pipeline:



User → Planner → Generator → Validator → Executor → Results



The goal is to improve database accessibility while enforcing strict safety controls.



---



\## How to Run the Demo



1\. Install Python (3.10+)

2\. Install dependencies:

&nbsp;  pip install -r requirements.txt

3\. Run:

&nbsp;  python demo.py



---



\## Security Features



\- SELECT-only enforcement

\- Blocks DROP, DELETE, ALTER, TRUNCATE, CREATE

\- Prevents stacked queries

\- Schema validation

\- No secrets committed (.env not uploaded)



---



\## Repository Structure



\- src/ – core agent components

\- prompts/ – prompt templates

\- docs/ – architecture documentation

\- tests/ – validation test cases

\- demo.py – runnable end-to-end example

