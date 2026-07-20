# ADA Incident Analysis Prompt

Analyze one robot incident from logs and replay data.

Classify:
- dialogue,
- ASR/turn-taking,
- prompt/policy,
- retrieval/data,
- face recognition,
- intent routing,
- tool validation,
- navigation/localization,
- executor,
- hardware,
- network/provider,
- observability gap.

Build a timeline using timestamps. Identify the first incorrect state transition, not merely the
final visible error. Recommend one immediate containment action and one durable corrective action.
Add a regression case that would have caught the incident before release.
