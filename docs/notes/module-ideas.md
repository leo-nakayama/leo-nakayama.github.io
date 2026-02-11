# Here are some idas of DSL modules.


```text

You are an AI that produces a structured Observation Report. 
Load the following Mental DSL modules and use only the operators that are explicitly requested. 
Do not provide chain-of-thought; return the report in the specified format.

---
name: AristotleFourCauses
type: module
axioms:
  - id: M
    name: MaterialCause
    description: "Resources, materials, raw data, inventory, constraints (material side)"
  - id: F
    name: FormalCause
    description: "Form, structure, design, blueprint, rules"
  - id: E
    name: EfficientCause
    description: "Agent, process, instruments, operators (who/how)"
  - id: T
    name: FinalCause
    description: "Purpose, value, KPI, telos (why/for what end)"
operators:
  - id: O_decompose
    signature: "O_decompose(data)"
    description: "Tag each fact as M/F/E/T"
  - id: O_rebalance
    signature: "O_rebalance(target)"
    description: "Shift emphasis among M/F/E/T to meet target"
  - id: O_tracechain
    signature: "O_tracechain()"
    description: "Map M->F->E->T dependencies and bottlenecks"
  - id: O_agent_network
    signature: "O_agent_network()"
    description: "Map EfficientCause actors and handoffs"
tensions:
  - "Mechanism (E/M) ↔ Purpose (T)"
  - "Structure (F) ↔ Flow (E)"
invariants:
  - "Any improvement must not degrade FinalCause (T) beyond agreed guardrails"
---

---
name: TradeoffLens
type: module
description: "A module specialized in detecting trade-offs. Fits well with 'Dynamics' and 'Otsu' series."
axioms:
  - id: T1
    description: "Every design entails trade-offs"
  - id: T2
    description: "Optimality is context-dependent"
  - id: T3
    description: "Multiple measures can coexist simultaneously"
operators:
  - id: O_surfaceAxes
    signature: "O_surfaceAxes(data)"
    description: "Extract evaluation axes (up to 5)"
  - id: O_mapFrontier
    signature: "O_mapFrontier(data)"
    description: "List hypotheses of Pareto frontier"
  - id: O_shiftKnob
    signature: "O_shiftKnob(axis, +|-)"
    description: "Conduct sensitivity analysis by axis unit"
invariants:
  - id: I1
    description: "Effects must always update the 4 quadrants (Accuracy/Speed/Exploration/Safety)"
  - id: I2
    description: "If KPI is undefined, must call [AristotleFourCauses.O_telos_check]"

...

### OBSERVATION REQUEST ##########################################
[Module] = AristotleFourCauses,TradeoffLens
[Function] = Deduction # Deduction or Induction (or both)
[Data] = <|DATA|>
[Ops] = ..use all operators of each module

Return the report in English.
Before executing this DSL request, you (ChatGPT) need to:
 - check if this Observation Request is stable, or makes sense.
 - suggest any recomended auxiliary tags
##################################################################

### REPORT FORMAT
[ObservationReport]
- [Module] Which axioms/operators were activated
- [Function] Deduction / Induction (rules applied or generalized)
- [InputData] What data was used (summary)
- [Transformations] Which operators were applied and where
- [DetectedPatterns] 3–5 bullets
- [Effects]
    * Accuracy: ↑/→/↓ (+ one sentence)
    * Speed: ↑/→/↓ (+ one sentence)
    * Exploration: ↑/→/↓ (+ one sentence)
    * Safety/Robustness: ↑/→/↓ (+ one sentence)
- [Trade-offs] bullet list
- [Micro-Playbook] 3–6 verb-first action steps
- [Limits] boundaries, open questions, and next tests
- [Language] English / Japanese
- [AuxiliaryTags] <list of auxiliary tags, if any>
### INSTRUCTIONS
- Use the exact format above.
- Use bullet points where indicated.
- Use arrows (↑/→/↓) to indicate changes in effects.
- Keep each section concise and focused.


```