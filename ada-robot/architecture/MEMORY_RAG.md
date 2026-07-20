# Memory and RAG Design

## Memory tiers

### Tier 0 — No memory
Transient audio buffers, raw camera frames, low-confidence face candidates.

### Tier 1 — Session memory
Current customer request, referenced products, current destination and unresolved question.
Expires after the interaction or a short inactivity timeout.

### Tier 2 — Operational memory
Non-personal robot facts such as recurring navigation failures, tool health, map version,
prompt version, recovery counts and aggregate performance.

### Tier 3 — Approved business knowledge
Product catalog, verified prices, category locations, store policies and scripted campaigns.
Versioned and auditable.

### Tier 4 — Explicitly approved person memory
Only authorized identities/roles or data with a clear operational reason and appropriate consent.

## Retrieval rules

- Filter by source, effective date, category and verification state.
- Prefer exact structured lookup for price and SKU.
- Use semantic search for descriptions, recommendations and FAQ.
- Return source ids with every retrieved item.
- Reject stale or conflicting price records and escalate to staff.
- Do not retrieve unrelated personal memory into customer sessions.

## Suggested stores

- Structured operational state: relational database or key-value store.
- Vector retrieval: Qdrant or equivalent.
- Logs/traces: observability platform with retention controls.
