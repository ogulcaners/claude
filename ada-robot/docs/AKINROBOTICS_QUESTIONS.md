# Questions for Akınrobotics AI / Robotics Team

## Navigation
1. Which navigation stack and ROS/ROS2 distribution does Mini Ada 3 use?
2. Is there a supported named-goal API or only raw coordinates?
3. What are the exact goal status/result codes?
4. How is arrival determined?
5. Is current pose and localization confidence exposed?
6. Can navigation be cancelled immediately?
7. Which recovery behaviors are implemented?
8. Are map versions and coordinate frames exposed?
9. Can obstacle/costmap events be read?
10. Can we test in simulation or replay recorded routes?

## LLM/tool integration
11. What exact function/tool calling format is supported?
12. Does the platform validate JSON schemas?
13. Can system, developer and dynamic context be separated?
14. Can prompt modules be versioned independently?
15. Are model/tool traces accessible to the customer?
16. Are token counts, cache hits, latency and provider errors exposed?
17. Can a gateway such as LiteLLM be placed between the robot and providers?
18. Are streaming and cancellation supported?

## Voice
19. Which ASR, VAD, turn-end and TTS components are used?
20. Can TTS be interrupted by customer speech?
21. Is echo cancellation available?
22. Are ASR confidence and partial/final transcript flags exposed?

## Face recognition
23. What are detection, tracking and identity confidence outputs?
24. Can thresholds and temporal confirmation be configured?
25. Is duplicate greeting suppression available?
26. Where is face data stored, and what are retention/access controls?

## Safety and operations
27. Which safety functions are independent of AI?
28. Is there a remote pause/override and hardware e-stop?
29. How are prompt/model updates rolled back?
30. Can we access structured logs and replay incidents?
31. What parts of the stack are vendor-supported versus customer-customizable?
