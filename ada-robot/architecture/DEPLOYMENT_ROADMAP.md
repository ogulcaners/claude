# Phased Deployment Roadmap

## Phase 0 — Evidence and inventory
- export all current prompts and versions,
- collect failure logs,
- document Akınrobotics APIs/tools,
- obtain map and destination coordinates,
- document face recognition outputs and thresholds,
- record model/provider/cost configuration.

## Phase 1 — Prompt modularization
- create system kernel and separate policy/capability modules,
- add typed output schema,
- remove duplicated and conflicting rules,
- build regression tests.

## Phase 2 — Tool contracts and state
- define robot state schema,
- wrap all actions in allowlisted adapters,
- add precondition/postcondition checks,
- standardize result/error codes.

## Phase 3 — Navigation closed loop
- canonical destination ids,
- localization and map checks,
- arrival verification,
- bounded recovery and staff escalation,
- navigation replay tests.

## Phase 4 — Voice and face reliability
- interruption handling,
- TTS cancellation,
- confidence-aware face greeting,
- duplicate greeting suppression,
- privacy policy.

## Phase 5 — RAG and memory
- structured catalog lookup,
- semantic product/FAQ retrieval,
- source metadata and freshness,
- tiered memory with retention.

## Phase 6 — Observability and release gate
- tracing,
- token/cost dashboards,
- prompt version comparison,
- promptfoo CI,
- canary rollout and rollback.

## Phase 7 — Optimization
- model routing,
- caching,
- latency tuning,
- local fallback components,
- continuous failure-mining into eval cases.
