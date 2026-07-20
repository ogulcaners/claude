# Prompt Architecture

## Context order

1. Immutable safety kernel
2. Identity and operational role
3. Allowed capabilities and tool schemas
4. Store policy
5. Current verified robot state
6. Current session state
7. Retrieved store knowledge
8. Current user utterance
9. Output schema

## Modules

### A. Safety kernel
Small, stable and difficult to override. Defines physical/action boundaries, truthfulness,
privacy, escalation and emergency behavior.

### B. Identity module
Defines ADA as a retail assistant at Yapada. Contains tone, language, brevity and brand behavior.

### C. Capability modules
Loaded only when relevant:
- retail sales
- product information
- navigation
- face greeting
- staff mode
- emergency/escalation
- entertainment (authorized only)

### D. Dynamic state
Machine-generated JSON, not prose:
- current time
- session id
- robot pose
- localization confidence
- navigation status
- destination
- obstacle status
- face candidates/confidence
- staff availability
- network/tool health
- last action result

### E. Retrieved knowledge
Small verified snippets with source id, timestamp and confidence. Prices, products and store rules
must come from verified sources.

### F. Output contract
The model returns only:
- `speech`
- `intent`
- `action_proposals`
- `needs_clarification`
- `escalation`
- `reason_code`
- `knowledge_sources`

Hidden reasoning is not required or stored.

## Anti-monolith rule

When a rule changes, one module should change. The full prompt should be assembled at runtime from
versioned modules. Avoid duplicating the same rule in multiple files.
