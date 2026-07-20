# Data Contract Requirements

## Sensor/perception events
Every event requires:
- timestamp,
- source,
- confidence/quality,
- freshness,
- coordinate frame where relevant,
- correlation or track id,
- schema version.

## Tool result
Every tool returns:
- status: succeeded / failed / cancelled / timed_out / rejected,
- reason_code,
- started_at,
- finished_at,
- observable postconditions,
- retryable flag,
- human-readable diagnostic,
- privacy-safe customer message suggestion.

## Knowledge item
Every item includes:
- source_id,
- record_id,
- version,
- effective_from,
- effective_to if applicable,
- verification_state,
- retrieval_score where semantic,
- structured fields for price/SKU/category.

## Prompt bundle
Every assembled prompt records:
- kernel version,
- module versions,
- selected skills,
- retrieved source ids,
- model and parameters,
- output schema version.
