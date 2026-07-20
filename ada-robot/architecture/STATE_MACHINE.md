# Runtime State Machine

## Top-level states

- `IDLE`
- `ATTRACT`
- `LISTENING`
- `UNDERSTANDING`
- `RESPONDING`
- `PLANNING_ACTION`
- `EXECUTING_ACTION`
- `VERIFYING`
- `RECOVERING`
- `ESCALATING`
- `PAUSED_BY_HUMAN`
- `EMERGENCY_STOP`
- `DEGRADED_MODE`

## Key transitions

- IDLE -> LISTENING: wake word, touch, direct address or approved proximity trigger
- LISTENING -> UNDERSTANDING: end-of-turn detected
- UNDERSTANDING -> RESPONDING: information-only request
- UNDERSTANDING -> PLANNING_ACTION: physical/service action requested
- PLANNING_ACTION -> EXECUTING_ACTION: validated action
- EXECUTING_ACTION -> VERIFYING: executor reports completion candidate
- VERIFYING -> RESPONDING: postcondition verified
- VERIFYING -> RECOVERING: postcondition failed
- RECOVERING -> EXECUTING_ACTION: bounded retry/replan
- RECOVERING -> ESCALATING: retry budget exhausted
- ANY -> PAUSED_BY_HUMAN: staff override
- ANY -> EMERGENCY_STOP: emergency input
- ANY -> DEGRADED_MODE: critical dependency unavailable

## Interrupt policy

Priority:
1. emergency stop
2. staff override
3. collision/safety event
4. navigation cancellation
5. active customer's correction
6. new customer speech
7. background face/proximity events
