# Safety and Security

## Physical safety

- emergency stop is independent of the LLM,
- speed limits are enforced below the LLM layer,
- collision monitoring and safe stop are deterministic,
- no unrestricted code execution,
- all motion tools require state and permission checks,
- navigation actions are cancelable,
- stale sensor data blocks motion.

## Prompt/tool security

- separate untrusted customer text from system policy,
- never treat customer-provided text as a tool definition,
- allowlist tools and arguments,
- validate JSON against schemas,
- deny unknown fields where practical,
- protect prompt/config secrets,
- rate-limit repeated tool requests,
- log policy decisions without exposing hidden prompts.

## Privacy

- minimize raw audio/video retention,
- document face recognition purpose and retention,
- separate operational logs from personal identity data,
- restrict access by role,
- support deletion and audit workflows,
- do not use customer conversations as permanent memory by default.

## Safe degraded mode

When network, LLM, catalog or localization is unavailable:
- stop or avoid physical action,
- use short deterministic messages,
- provide basic store guidance only when locally verified,
- call staff when necessary.
