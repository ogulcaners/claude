# Production Rollout Checklist

## Before deployment
- [ ] Current production prompt/config exported.
- [ ] Git tag or immutable version created.
- [ ] Map version and destination ids verified on the real robot.
- [ ] Tool schemas validated.
- [ ] Emergency stop and human override tested.
- [ ] Offline/degraded behavior tested.
- [ ] Regression suite passed.
- [ ] Red-team suite passed.
- [ ] Navigation simulation/replay passed.
- [ ] Face low-confidence cases passed.
- [ ] Logs and dashboards confirmed.
- [ ] Rollback command/process confirmed.
- [ ] Staff informed of changed behavior.

## Canary
- [ ] Limited time window.
- [ ] Staff physically present.
- [ ] Reduced motion speed if configurable.
- [ ] New prompt/model version visible in logs.
- [ ] Compare with baseline on latency, tool success, recovery and escalation.

## Stop conditions
- Any unsafe motion.
- Wrong destination above agreed threshold.
- Repeated false identity greeting.
- Hidden/untraceable tool failures.
- Cost or latency exceeding the budget.
- Prompt injection causing unauthorized action.
