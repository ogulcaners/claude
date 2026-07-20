# Target System Architecture

```mermaid
flowchart LR
    MIC[Microphone] --> ING[Input Gateway]
    CAM[Camera / Face Events] --> ING
    UI[Touch / Staff UI] --> ING
    ING --> NORM[Perception Normalizer]
    NORM --> SES[Session Manager]
    NORM --> WS[World-State Store]

    SES --> IR[Intent Router]
    IR --> POL[Policy & Guardrail Engine]
    POL --> KB[Verified Store Knowledge / RAG]
    POL --> DP[Dialogue Planner]
    POL --> TP[Task Planner]

    KB --> DP
    WS --> DP
    WS --> TP

    TP --> AV[Action Validator]
    AV --> BT[Deterministic Executor / Behavior Tree]
    BT --> NAV[Navigation Adapter]
    BT --> EXP[Speech & Expression Adapter]
    BT --> ESC[Human Escalation]

    NAV --> WS
    EXP --> WS
    ESC --> WS

    SES --> MEM[Memory Manager]
    WS --> OBS[Observability / Replay]
    DP --> OBS
    TP --> OBS
    BT --> OBS
    MEM --> OBS

    OBS --> EVAL[Offline Evals / Release Gate]
```

## Hard boundary

The LLM side ends at:
- structured dialogue plan,
- structured intent,
- structured high-level action proposal.

The deterministic side owns:
- capability permission,
- state freshness checks,
- map destination validation,
- collision avoidance,
- path execution,
- timeout/cancel,
- emergency stop,
- arrival verification,
- recovery and escalation.

## Runtime loop

1. Receive timestamped input.
2. Normalize and reject stale/low-quality inputs.
3. Update world state.
4. Determine active session and interrupt policy.
5. Route intent.
6. Apply policy.
7. Retrieve verified business information if needed.
8. Produce compact dialogue and/or action proposal.
9. Validate action against state, capability, policy and safety.
10. Execute deterministically.
11. Verify completion.
12. Recover or escalate.
13. Speak the truthful outcome.
14. Record a trace with prompt/config versions.
