# Developer Handoff Prompt

Review the supplied ADA issue, logs, configuration and source files.

Return:
1. observed symptom,
2. evidence,
3. likely root cause,
4. responsible layer,
5. minimal coherent fix,
6. files/modules to change,
7. tests to add,
8. telemetry to verify,
9. rollback method,
10. vendor questions if the fix depends on Akınrobotics internals.

Do not assume a prompt change can repair a missing tool, broken map, unavailable API,
low-confidence localization, or faulty face-recognition pipeline.
