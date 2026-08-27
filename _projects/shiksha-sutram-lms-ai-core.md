---
layout: page
title: "Shiksha Sutram LMS AI Core"
subtitle: "RAG-driven curriculum intelligence and automated assessment engine"
date: 2026-05-02
category: "AI & System Architecture"
tech_stack: ["FastAPI", "PostgreSQL", "Vector DB", "Docker", "LangChain"]
github_url: "[https://github.com/Decoder76/shiksha-sutram-lms-ai-core](https://github.com/Decoder76/shiksha-sutram-lms-ai-core)"
featured: true
---

**System Architecture**

```mermaid
flowchart TD
    User([User Request]) --> GW[FastAPI Gateway]
    GW --> RAG[RAG Retrieval Engine]
    VectorDB[(Curriculum Vector DB)] <--> RAG
    RAG --> LLM[LLM Generator]
    LLM --> Mastery[Student Mastery Engine]
    Mastery --> DB[(PostgreSQL Store)]
    Mastery --> Out([Adaptive Content / Test])
```

**Key Highlights**
* **Grounded Retrieval**: Vector similarity search preventing curriculum hallucinations.
* **Adaptive Scoring**: Real-time evaluation matrix calibrating quiz difficulty against past attempts.
* **Decoupled Engine**: RESTful microservice integrating with external LMS backends.

**Performance Metrics**

| Metric | Legacy / Manual | AI Core Engine |
| :--- | :--- | :--- |
| **Exam Generation Time** | 45 min | **< 10 sec** |
| **Retrieval Relevance** | 68% | **> 94%** |
| **Service Uptime** | 98.5% | **99.9%** |
