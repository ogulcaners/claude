# Observability, Cost and Latency

## Trace every turn

Required fields:
- trace id
- session id
- timestamp
- prompt version
- model/provider
- input/output token count
- cached tokens if available
- latency by stage
- ASR confidence
- intent
- retrieved source ids
- proposed tool calls
- validator decision
- tool result
- navigation result
- recovery attempts
- final speech
- error/reason code

## Dashboards

- p50/p95 voice-to-first-audio latency
- tool success rate
- navigation success and recovery rate
- false/uncertain face greeting rate
- unsupported/guessed answer rate
- staff escalation rate
- token and provider cost
- prompt version comparison
- top failure reasons

## Cost controls

- use a small/fast model for classification and routing,
- use deterministic lookup for price/SKU,
- use the larger model only for complex recommendation/dialogue,
- cache stable system modules and store knowledge where supported,
- summarize long sessions,
- cap tool loops and model retries,
- route providers through a gateway if vendor independence is needed.

## Reference tools

- Langfuse: traces, prompt management, evaluation and debugging
- LiteLLM: model gateway, routing, budgets and provider abstraction
- promptfoo: offline prompt/model comparison and red teaming
