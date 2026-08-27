---
layout: page
title: "Projects Showcase"
permalink: /pages/projects/
---

**Featured Engineering Work** — Production-grade systems, machine learning models, and automated RAG assistants.

---

### Featured Systems & Repositories

| Project Title | Category | Core Tech Stack | Impact / Metrics |
| :--- | :--- | :--- | :--- |
| **[Production ML Inference API](../_projects/fastapi-prediction-api.md)**[cite: 1] | Backend & ML[cite: 1] | Python, FastAPI, Docker, Redis, PyTorch[cite: 1] | **48ms** p95 latency, **1.1k RPM** throughput |
| **[Deep Sequence NLP Classifier](../_projects/nlp-rnn-lstm-project.md)**[cite: 1] | NLP & Deep Learning[cite: 1] | PyTorch, Bi-LSTM, NLTK, Scikit-Learn[cite: 1] | **91.4%** Macro F1-score |
| **[Shiksha Sutram LMS AI Core](../_projects/shiksha-sutram-lms-ai-core.md)**[cite: 1] | AI & Architecture[cite: 1] | FastAPI, Vector DB, PostgreSQL, LangChain[cite: 1] | **< 10s** exam gen, **> 94%** relevance |
| **[Autonomous Telegram AI Assistant](../_projects/telegram-ai-bot.md)**[cite: 1] | Agents & Automation[cite: 1] | Python, Asyncio, Redis, OpenAI API[cite: 1] | **200+** concurrent sessions, **100%** reliability |

---

### Dynamic Data Feeds
{% for project in site.projects %}
#### [{{ project.title }}]({{ project.url }})[cite: 1]
{{ project.overview }}

**Tech Stack:** `{{ project.stack | join: " • " }}`
{% endfor %}

{% for data_project in site.data.projects %}
#### [{{ data_project.title }}](/projects/{{ data_project.slug }}/)
{{ data_project.summary }}

**Tech Stack:** `{{ data_project.stack | join: " • " }}`
{% endfor %}
