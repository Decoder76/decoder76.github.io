---
layout: page
title: "Autonomous Telegram AI Assistant"
subtitle: "Event-driven conversational assistant with sliding-window memory"
date: 2026-05-15
category: "Agents & Automation"
tech_stack: ["Python", "Asyncio", "Redis", "OpenAI API", "Docker"]
github_url: "[https://github.com/Decoder76/telegram-ai-bot](https://github.com/Decoder76/telegram-ai-bot)"
featured: true
---

**Event Flow**

```mermaid
flowchart LR
    User([Telegram User]) --> Hook[Async Webhook]
    Hook --> Session[(Redis Session Buffer)]
    Session --> Agent[LLM Orchestrator]
    Agent --> Stream[Response Streamer]
    Stream --> User
```

**Key Highlights**
* **Stateful Sessions**: Redis cache maintaining multi-turn dialogue context across user reconnections.
* **Async Dispatching**: Event-driven loop preventing UI blocking during high-volume chat spikes.
* **Rate Protection**: Sliding-window token limiter shielding upstream API rate thresholds.

**Performance Metrics**

| Metric | Target Specification |
| :--- | :--- |
| **Concurrent Sessions** | **200+ Active Users** |
| **Dispatch Latency** | **< 800ms** |
| **Message Delivery Reliability** | **100% Zero-Drop** |
