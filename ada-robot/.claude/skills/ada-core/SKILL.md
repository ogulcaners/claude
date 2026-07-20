---
name: ada-core
description: Use for any architecture, prompt, code, policy, testing, or integration work involving ADA, the Yapada retail service robot.
---

# ADA Core Skill

Treat ADA as a safety-bounded retail service robot, not a generic chatbot.

Always:
- preserve physical safety and human override,
- separate LLM decisions from deterministic execution,
- represent uncertainty explicitly,
- use verified store data,
- keep runtime Turkish concise,
- add tests for every behavior change,
- identify whether a problem belongs to prompt, tool, integration, navigation, perception, data, or hardware.

Do not:
- create one giant prompt,
- invent robot state or tool success,
- issue raw motor commands,
- silently hide failures,
- permanently store ordinary customer conversations.
