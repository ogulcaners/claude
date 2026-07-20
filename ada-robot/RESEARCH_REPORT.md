# GitHub Research Report — LLM + Robotics + Claude Architecture

Access date: 2026-07-20

## Executive recommendation

### Best repository to upload into Claude as the base robotics engineering skill set

**arpitg1304/robotics-agent-skills**
- URL: https://github.com/arpitg1304/robotics-agent-skills
- Role: Primary Claude robotics engineering knowledge layer.
- Why: Native `SKILL.md` approach, ROS1/ROS2, lifecycle/QoS, design patterns, perception,
  testing, Docker, web integration, bringup and security.
- Limitation: Navigation/Nav2 is listed as roadmap rather than an implemented skill.
- Decision: Adopt as the primary external skill package and supplement with this pack's
  `ada-navigation` and retail-specific skills.

### Best modern embodied orchestration reference

**automatika-robotics/emos**
- URL: https://github.com/automatika-robotics/emos
- Role: Reference architecture for separating intelligence, navigation and runtime orchestration.
- Useful ideas: recipes, semantic routing, event-driven cognition, lifecycle nodes, runtime fallbacks,
  point navigation, semantic mapping and `llms.txt` context for coding agents.
- Decision: Reference and prototype selected patterns; do not wholesale replace the vendor stack
  without hardware/API compatibility proof.

### Best prompt-design reference for robotics

**microsoft/PromptCraft-Robotics**
- URL: https://github.com/microsoft/PromptCraft-Robotics
- Role: Historical design patterns and prompting examples for embodied agents, spatial reasoning,
  manipulation and closed-loop navigation.
- Limitation: Example-oriented and old; not a production runtime. Direct execution patterns must not
  be copied into a customer-facing physical robot without a validator and safety supervisor.
- Decision: Reference only.

## Recommended repository stack

| Responsibility | Repository | Decision |
|---|---|---|
| Claude skill format | https://github.com/anthropics/skills | Adopt format |
| Robotics coding skills | https://github.com/arpitg1304/robotics-agent-skills | Adopt |
| Embodied orchestration | https://github.com/automatika-robotics/emos | Reference / prototype |
| Robot LLM node + dynamic tools | https://github.com/bob-ros2/bob_llm | Reference; maturity-check |
| Prompt design | https://github.com/microsoft/PromptCraft-Robotics | Reference |
| Conversational robot architecture | https://github.com/pollen-robotics/reachy_mini_conversation_app | Reference |
| Task planning + BT generation | https://github.com/ProNeverFake/kios | Research reference |
| Deterministic behavior | https://github.com/BehaviorTree/BehaviorTree.CPP | Adopt if stack permits |
| ROS2 navigation | https://github.com/ros-navigation/navigation2 | Adopt/adapter if available |
| Stateful agent memory | https://github.com/letta-ai/letta | Optional reference |
| Semantic memory/RAG | https://github.com/qdrant/qdrant | Optional production component |
| Memory MCP | https://github.com/qdrant/mcp-server-qdrant | Claude development memory option |
| Guardrails | https://github.com/NVIDIA-NeMo/Guardrails | Evaluate / integrate selectively |
| Prompt eval + red team | https://github.com/promptfoo/promptfoo | Adopt |
| LLM observability | https://github.com/langfuse/langfuse | Adopt or replicate minimum features |
| Model gateway/cost routing | https://github.com/BerriAI/litellm | Evaluate / adopt |
| Voice pipeline | https://github.com/pipecat-ai/pipecat | Strong candidate |
| Realtime voice alternative | https://github.com/livekit/agents | Alternative |
| Wake word | https://github.com/dscripka/openWakeWord | Optional local component |
| Research index | https://github.com/GT-RIPL/Awesome-LLM-Robotics | Research source |

## Selection principles

Do not create a dependency collection. Every repo must own one clearly bounded responsibility.
Use mature deterministic robotics software below the LLM layer. Use the LLM for language
understanding, product dialogue, intent routing and bounded task planning—not for raw motion control.

## Proposed dependency tiers

### Tier 0 — Required concepts
- Claude Agent Skills format
- modular prompts
- typed tool calls
- deterministic execution
- test/eval harness
- structured logs

### Tier 1 — Strong implementation candidates
- robotics-agent-skills
- Nav2 / vendor navigation adapter
- BehaviorTree.CPP or an equivalent deterministic state-machine engine
- promptfoo
- Langfuse or equivalent tracing

### Tier 2 — Conditional
- Pipecat or LiveKit for voice
- LiteLLM for provider routing and cost controls
- Qdrant for store knowledge and semantic retrieval
- NeMo Guardrails for programmable topic/tool/output rails

### Tier 3 — Research references
- EMOS
- PromptCraft-Robotics
- KIOS
- Reachy Mini conversation app
- bob_llm

## What not to do

- Do not paste several repositories into one runtime without architecture.
- Do not let an LLM dynamically discover unrestricted robot commands.
- Do not store every conversation in permanent memory.
- Do not equate face recognition with confirmed identity.
- Do not retry navigation forever.
- Do not hide failures behind friendly speech.
- Do not release a new prompt without replayable evals.
