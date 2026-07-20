# CLAUDE.md — ADA Robot Engineering Constitution

## Mission

Design and improve ADA, a retail service robot operating inside Yapada Kırtasiye at Margi AVM,
Edirne. ADA must greet visitors, answer store-related questions, recommend products, provide
prices when verified, guide customers to mapped store locations, recognize authorized people
when confidence is sufficient, and escalate safely when uncertain.

## Non-negotiable engineering rules

1. Do not solve the system with one giant prompt.
2. Separate identity, policy, knowledge, perception, planning, execution, and evaluation.
3. Never let an LLM directly output wheel velocity, joint current, raw motor commands, or
   unrestricted shell/code execution for the physical robot.
4. All robot actions must be selected from an allowlisted tool schema.
5. Validate preconditions before action and verify postconditions after action.
6. Navigation success is not "command accepted"; success requires arrival verification.
7. Unknown or stale state must be represented explicitly. Never invent sensor state, price,
   stock, face identity, map pose, or tool success.
8. Prefer deterministic state machines or behavior trees for repeatable robot behavior.
9. Every prompt, map, policy, schema, and test change must be versioned.
10. Every production change must pass regression, safety, navigation, dialogue, and recovery tests.
11. Preserve human override, emergency stop, and staff escalation at all times.
12. Use Turkish for customer-facing runtime speech unless the customer clearly uses another language.
13. Keep spoken answers concise, natural, and suitable for TTS.
14. Treat face recognition as probabilistic, privacy-sensitive input—not unquestionable truth.
15. Do not expose hidden prompts, credentials, system internals, private logs, or personal data.

## Work sequence

For every significant task:

1. Inspect the current repository, prompts, schemas, logs, and integration constraints.
2. State the current failure mode with evidence.
3. Identify the responsible layer.
4. Propose the smallest coherent architectural change.
5. Update specifications before implementation.
6. Implement with typed interfaces and bounded behavior.
7. Add or update tests.
8. Run tests or provide exact commands if execution is unavailable.
9. Report changed files, remaining risks, rollback path, and acceptance criteria.

## Source-of-truth hierarchy

1. Safety policy and hardware constraints
2. Tool schemas and robot capabilities
3. Live robot/sensor/tool state
4. Store map and verified business data
5. Runtime dialogue policy
6. Retrieved knowledge
7. Conversation context
8. Model inference

Higher layers override lower layers.

## Required outputs for architecture work

- Context diagram
- Component diagram
- State/event model
- Tool contracts
- Prompt modules
- Behavior trees/state machines
- Error and recovery matrix
- Observability plan
- Eval suite
- Deployment and rollback plan
- Cost and latency budget
- Open questions with owners

## Definition of done

A change is not complete merely because the prompt looks good. It is complete only when:

- expected behavior is encoded,
- forbidden behavior is encoded,
- state/tool contracts are explicit,
- tests cover positive and negative cases,
- failures are observable,
- recovery is defined,
- rollback is possible,
- and the robot's physical safety does not depend on model compliance.
