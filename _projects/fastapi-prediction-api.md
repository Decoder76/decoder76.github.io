---
layout: page
title: "Production ML Inference API"
subtitle: "High-throughput asynchronous model serving pipeline"
date: 2026-04-10
category: "Backend & ML"
tech_stack: ["Python", "FastAPI", "Docker", "Redis", "PyTorch"]
github_url: "[https://github.com/Decoder76/fastapi-prediction-api](https://github.com/Decoder76/fastapi-prediction-api)"
featured: true
---

**System Architecture**

```mermaid
flowchart LR
    Client([Client Request]) --> API[FastAPI Gateway]
    API --> Cache{Redis Cache}
    Cache -- Hit --> Resp([Instant Response])
    Cache -- Miss --> Worker[PyTorch Worker]
    Worker --> Cache
    Worker --> Resp
```

**Key Highlights**
* **Async Gateway**: Non-blocking request handling powered by FastAPI's native async event loop.
* **Inference Caching**: Redis cache layer eliminating redundant compute for repeated queries.
* **Worker Isolation**: Containerized multi-stage Docker environment isolating model execution threads.

**Performance Metrics**

| Metric | Baseline | Optimized |
| :--- | :--- | :--- |
| **p95 Latency** | 340ms | **48ms** |
| **Throughput** | 250 RPM | **1,100+ RPM** |
| **Container Size** | 1.2 GB | **580 MB** |
