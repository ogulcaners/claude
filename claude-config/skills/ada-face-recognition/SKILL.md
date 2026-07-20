---
name: ada-face-recognition
description: Use for ADA face detection, recognition, authorized-person greetings, confidence thresholds, duplicate greeting suppression, privacy, or recognition failures.
---

# ADA Face Recognition Skill

- Treat recognition as probabilistic evidence.
- Require multi-frame confirmation and a strict confidence threshold.
- Use a neutral greeting below threshold.
- Do not expose confidence scores to customers.
- Debounce repeated greetings.
- Separate face detection, tracking, recognition, role lookup and dialogue.
- Log false-positive/false-negative review cases with privacy controls.
- Never let face recognition alone grant dangerous privileges.
