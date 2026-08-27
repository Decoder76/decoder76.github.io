---
layout: page
title: "Deep Sequence NLP Classifier"
subtitle: "Context-aware text classification via Bidirectional LSTM"
date: 2026-04-18
category: "NLP & Deep Learning"
tech_stack: ["Python", "PyTorch", "NLTK", "Scikit-Learn"]
github_url: "[https://github.com/Decoder76/nlp-rnn-lstm-project](https://github.com/Decoder76/nlp-rnn-lstm-project)"
featured: true
---

**Pipeline Flow**

```mermaid
flowchart LR
    Raw([Raw Text]) --> Prep[Tokenizer & Padder]
    Prep --> Emb[Dense Embedding]
    Emb --> BiLSTM[Bi-LSTM Core]
    BiLSTM --> Drop[Dropout & Dense]
    Drop --> Out([Class Prediction])
```

**Key Highlights**
* **Bidirectional Context**: Dual hidden states preserving forward and backward semantic signals.
* **Gradient Stability**: Gradient clipping and AdamW optimization eliminating vanishing gradients.
* **Tensor Batching**: Memory-mapped PyTorch DataLoaders accelerating epoch convergence.

**Performance Metrics**

| Metric | Standard RNN | Bi-LSTM Pipeline |
| :--- | :--- | :--- |
| **Macro F1-Score** | 76.2% | **91.4%** |
| **Epoch Time** | 4.2 min | **2.7 min** |
| **Loss Convergence** | 24 Epochs | **12 Epochs** |
