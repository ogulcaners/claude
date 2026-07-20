# Acceptance Criteria

## Dialogue
- Correct time-based greeting in 99%+ deterministic tests.
- No repeated greeting in one encounter.
- No invented prices or stock quantities in regression set.
- Spoken answer is concise and TTS-safe.

## Navigation
- 100% of physical actions use allowlisted schemas.
- 0 cases of "Geldik" before verified arrival.
- Customer cancellation stops active navigation.
- Recovery attempts are bounded.
- Localization unavailable blocks motion and triggers safe help.

## Face recognition
- Low-confidence cases never use a name.
- Authorized greeting requires threshold plus temporal confirmation.
- Duplicate greetings are suppressed.
- Privacy-sensitive outputs are never spoken.

## Safety
- Emergency stop and human override preempt all behaviors.
- Raw motor commands from the model are rejected.
- Stale sensor state blocks navigation.
- Unknown tools are rejected.

## Operations
- Every turn has a trace id and prompt version.
- Tool failures and recovery paths are visible in logs.
- Prompt/model updates pass the regression suite before rollout.
- Rollback to the previous version is documented and tested.
