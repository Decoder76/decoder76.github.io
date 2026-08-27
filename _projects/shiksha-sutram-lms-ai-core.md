---
layout: page
title: "Shiksha Sutram LMS AI Core"
subtitle: "Intelligent content recommendation and adaptive learning assessment engine for LMS platforms"
date: 2026-05-02
category: "System Architecture & AI"
tech_stack: ["Python", "FastAPI", "PostgreSQL", "Docker", "LangChain", "Vector DB"]
github_url: "https://github.com/Decoder76/shiksha-sutram-lms-ai-core"
live_url: ""
featured: true
---

**System Architecture**

```mermaid
flowchart TD
    User([Student / Educator]) --> GW[FastAPI Gateway]
    GW --> RAG[RAG Engine]
    VectorDB[(Curriculum Vector DB)] <--> RAG
    RAG --> LLM[LLM Generator]
    LLM --> Eval[Mastery Engine]
    Eval --> DB[(PostgreSQL Store)]
    Eval --> Out([Adaptive Content / Test])
