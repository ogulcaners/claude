# Failure Mode Matrix

| Failure | Likely layer | Detection | Immediate behavior | Durable fix |
|---|---|---|---|---|
| Robot promises to move but stays still | tool/integration | no navigation action/result | admit inability, call staff | typed nav adapter |
| Goes to wrong shelf | map/destination resolver | destination/pose mismatch | cancel, clarify | canonical ids + map tests |
| Never says "Geldik" | postcondition/dialogue event | arrival event not connected | neutral completion after verification | arrival event contract |
| Says "Geldik" too early | prompt/executor contract | goal accepted but pose not reached | suppress phrase | postcondition gate |
| Repeats greeting | session/debounce | repeated encounter event | suppress | encounter state |
| Wrong named greeting | face recognition | low/unstable confidence | neutral greeting | threshold + track confirmation |
| Wrong time greeting | dynamic context | time/prompt mismatch | deterministic greeting service | remove time inference from LLM |
| Hallucinates price | data/RAG | no verified source id | staff confirmation | structured price tool |
| Long irrelevant answer | dialogue policy | intent/topic classifier | short redirect | topic rail + token cap |
| Cost spike | orchestration | token/tool-loop telemetry | route smaller model, cap loops | gateway/budgets/caching |
| Silent tool failure | observability | missing result/timeout | truthful failure speech | standardized result codes |
| Prompt patch breaks another rule | release process | regression delta | rollback | modular prompts + eval CI |
