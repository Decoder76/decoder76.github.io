---
layout: page
title: "Autonomous Telegram AI Assistant"
subtitle: "Event-driven conversational bot integrating LLMs with session persistence and custom tool orchestration"
date: 2026-05-15
category: "AI Agents & Automation"
tech_stack: ["Python", "python-telegram-bot", "Asyncio", "Redis", "OpenAI API", "Docker"]
github_url: "https://github.com/Decoder76/telegram-ai-bot"
live_url: ""
featured: true
---

**Overview**
An asynchronous Telegram bot built to provide contextual AI assistance, query parsing, and automated task execution with stateful multi-turn memory.

---

**The Challenge**
Managing synchronous LLM calls inside conversational interfaces frequently leads to connection timeouts, dropped user messages during high traffic, and lost conversation history across client reconnects.

**System Architecture**
* **Asynchronous Event Loop**: Powered by `asyncio` to handle concurrent message updates without blocking chat threads.
* **Ephemeral Session Storage**: Redis-backed cache tracking sliding-window conversation history per user session.
* **Rate Limiting & Queueing**: Token-bucket rate limiter safeguarding against upstream API quota exhaustion.

[ Telegram Webhook ] ──> [ Async Dispatcher ] ──> [ Redis Session Context ]
│
[ Telegram User ] <───── [ Output Streamer ] <──── [ LLM Orchestrator ]

---

**Key Technical Implementations**
* **Context Window Truncation**: Built dynamic token-counting heuristics that compress past conversational turns, keeping API requests strictly within model context limits.
* **Fault-Tolerant Retry Logic**: Added exponential backoff and jitter algorithms to handle network hiccups and upstream model provider downtime gracefully.
* **Secure Environment Configuration**: Isolated API tokens, webhook secrets, and user authorization levels via structured environment variables.

---

**Key Metrics & Results**
* **Concurrent Chat Handling**: Supports up to 200 concurrent user sessions with sub-second message dispatch times.
* **Context Retention**: Successfully persists multi-turn dialogue state with zero memory leaks over long-running daemon lifecycles.
* **Zero Drop Rate**: Achieved a $100\%$ message processing reliability rate across load test simulations.
