# Uncertainly Yours
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://uncertainly-yours.streamlit.app/)

**Uncertainly Yours** is a tool for transforming your gut feelings into probability estimates. This app uses zero-shot natural language classification to map your intuition to a probability label, range, and interpretation.

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

## 📸 Results

Here are a few example forecasts generated using the app:

### AI Alignment (Prompt 1)
“With the spotlight on AI alignment and global attention on existential risk, it wouldn’t surprise me if an AI ethics researcher wins a Nobel Peace Prize in the next 2–3 years.”
![AI Alignment Prize](Screenshots/AI_Alignment.png)

### Biden (Prompt 2)
![Biden Incumbency](Screenshots/Biden.png)
 

---
