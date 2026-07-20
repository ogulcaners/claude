---
name: ada-voice-dialogue
description: Use for ADA microphone, ASR, VAD, turn-taking, TTS, interruption, greeting, conversation session, latency, or spoken-response design.
---

# ADA Voice and Dialogue Skill

- Support barge-in: customer speech cancels current TTS.
- Do not respond to partial ASR unless explicitly designed.
- Deduplicate repeated transcripts.
- Keep customer speech concise and natural.
- Use time-appropriate Turkish greetings:
  - 06:00-11:59 Günaydın
  - 12:00-17:59 İyi günler
  - 18:00-21:59 İyi akşamlar
  - 22:00-05:59 Merhaba
- Do not repeat a greeting in the same active encounter.
- On low ASR confidence, ask one short clarification.
- Distinguish silence, no-speech, low-confidence speech and service failure.
