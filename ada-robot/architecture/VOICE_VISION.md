# Voice, Turn-Taking and Vision

## Voice pipeline

`Wake/activation -> VAD -> ASR -> turn-end detection -> intent/dialogue -> TTS -> echo suppression`

Requirements:
- low latency,
- barge-in support,
- TTS cancellation on customer interruption,
- duplicate ASR suppression,
- confidence and noise metadata,
- short spoken responses,
- no reading of raw JSON or technical errors.

Potential references:
- Pipecat for vendor-neutral voice/multimodal pipelines,
- LiveKit Agents as an alternative real-time framework,
- openWakeWord for a local activation phrase.

## Face recognition pipeline

1. detect face,
2. track across multiple frames,
3. quality/liveness checks if available,
4. compare against authorized gallery,
5. require confidence threshold and temporal confirmation,
6. suppress repeated greetings,
7. use neutral greeting on uncertainty,
8. never reveal confidence or private identity information to bystanders.

## Identity behavior

Recognition is a hint. If confidence is below the strict threshold:
- do not use a person's name,
- use a neutral time-appropriate greeting,
- allow staff/customer correction without arguing.
