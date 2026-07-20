---
name: ada-navigation
description: Use for ADA map destinations, ROS2/Nav2 or vendor navigation integration, customer escort behavior, arrival verification, obstacle recovery, localization, or route failures.
---

# ADA Navigation Skill

## Architecture
Use named destinations and a deterministic navigation adapter.

## Required preconditions
- current map version known,
- destination id exists,
- localization confidence above threshold,
- navigation service healthy,
- no emergency/override,
- sensor freshness valid.

## Required execution behavior
- send an allowlisted `navigate_to_destination` action,
- monitor progress,
- allow cancellation,
- enforce timeout,
- verify arrival by result and pose tolerance,
- speak "Geldik." only after verified arrival,
- use bounded recovery,
- escalate after recovery budget.

Never let the LLM invent coordinates or report arrival from intention alone.
