# Uncertainly Yours
[![View App](https://img.shields.io/badge/🧠%20Launch-App-green?style=for-the-badge)](https://uncertainly-yours.streamlit.app/)

**Uncertainly Yours** is a playful yet powerful tool for transforming your gut feelings into calibrated probability estimates. This app uses zero-shot natural language classification to map your intuition to a probability label, range, and interpretation.

---

## 🔍 What It Does

- Accepts natural language input like “It’s probably going to happen soon.”
- Uses HuggingFace’s `facebook/bart-large-mnli` to classify the tone of certainty.
- Maps your statement to a **calibrated probability label**:
  - *Remote*, *Highly Improbable*, *Improbable*, etc.
- Displays:
  - A probability **range**
  - A brief **interpretation**
  - A **bar chart** of confidence scores across all labels

---
