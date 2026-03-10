\# Architecture Overview



User Query

↓

Planner (LLM)

↓

Generator (LLM)

↓

Validator (Rule-Based)

↓

Executor (Database Tool)

↓

Results



Design Decisions:

\- Separate reasoning from execution

\- Deterministic validation layer

\- Safety-first approach

