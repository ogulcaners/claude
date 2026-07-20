# Navigation Architecture for ADA

## Root problem pattern

A language model saying "I will take you there" does not make navigation happen.
Navigation must be a tool-driven closed loop with a verified map and robot state.

## Named destination flow

1. Resolve user phrase to a canonical destination id.
2. Confirm destination exists in current map version.
3. Read localization confidence and navigation health.
4. Check whether escorting is allowed in the current safety state.
5. Start navigation using a typed tool call.
6. Announce a short start phrase.
7. Monitor progress, obstacle events, timeout and cancellation.
8. Verify arrival using navigation result plus pose tolerance.
9. Speak a completion phrase such as "Geldik."
10. If failed, run bounded recovery.
11. If still failed, explain truthfully and call staff.

## Recovery budget

Recommended maximum:
- one local retry for transient obstruction,
- one re-localization/replan attempt if supported,
- then staff escalation.

Never loop indefinitely.

## Destination naming

The LLM never invents coordinates. It chooses only a canonical `destination_id` from the map.
The navigation adapter owns coordinates and map-version compatibility.

## Customer correction

"Hayır, orası değil" cancels the current navigation goal before a new goal is accepted.
